from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404, redirect
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import URLMapping
from .serializers import URLMappingSerializer
from .handler import validate_url
from config import SERVER_HOST


class URLCreateView(APIView):
    def post(self, request, *args, **kwargs):
        try:
            validate_url(request.data.get("original_url"))
            serializer = URLMappingSerializer(data=request.data)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response({"short_url": '', 'expiration_date': '', "success": False, "reason": f"{e}"})

class URLRedirectView(APIView):
    def get(self, request, short_code, *args, **kwargs):
        url_mapping = get_object_or_404(URLMapping, short_url=f'{SERVER_HOST.HOST}/redirection/{short_code}/')
        return redirect(url_mapping.original_url)
