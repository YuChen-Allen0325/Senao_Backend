import pytz
import logging.config
from .models import URLMapping
from .serializers import URLMappingSerializer
from .handler import validate_url
from datetime import datetime
from django.shortcuts import redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .throttling import IPRateThrottle

log = logging.getLogger(__name__)

class URLCreateView(APIView):
    throttle_classes = [IPRateThrottle]   ## rate limiting   5/min in same IP

    def post(self, request, *args, **kwargs):
        try:
            original_url = request.data.get("original_url")

            if original_url is None:
                return Response({"short_url": '', 'expiration_date': '', "success": False, "reason": "original_url is required"}, status=status.HTTP_400_BAD_REQUEST)

            if type(original_url) != str:
                return Response({"short_url": '', 'expiration_date': '', "success": False, "reason": "original_url must be a string"}, status=status.HTTP_400_BAD_REQUEST)

            validate_url(original_url)
            serializer = URLMappingSerializer(data=request.data)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)

        except Exception as e:
            log.error(f"{e} in URLCreateView")
            return Response({"short_url": '', 'expiration_date': '', "success": False, "reason": f"{e}"}, status=status.HTTP_400_BAD_REQUEST)

class URLRedirectView(APIView):
    def get(self, request, short_code, *args, **kwargs):

        timezone = pytz.timezone('UTC')
        datetime_now_with_tz = datetime.now(timezone)

        try:
            url_mapping_data = URLMapping.objects.get(short_code=short_code)
        except URLMapping.DoesNotExist:
            log.error("URL not found in URLRedirectView")
            return Response({"error": "URL not found"}, status=status.HTTP_404_NOT_FOUND)
        
        if url_mapping_data.expiration_date < datetime_now_with_tz:
            return Response({"error": "URL expired"}, status=status.HTTP_410_GONE)

        return redirect(url_mapping_data.original_url)
