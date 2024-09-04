from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponseRedirect
from rest_framework import generics
from django.shortcuts import get_object_or_404, redirect
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import URLMapping
from .serializers import URLMappingSerializer


class URLCreateView(generics.CreateAPIView):
    queryset = URLMapping.objects.all()
    serializer_class = URLMappingSerializer

class URLRedirectView(APIView):
    def get(self, request, short_code, *args, **kwargs):
        url_mapping = get_object_or_404(URLMapping, short_code=short_code)
        return redirect(url_mapping.original_url)
