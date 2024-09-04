from django.urls import path
from .views import URLCreateView, URLRedirectView

urlpatterns = [
    path('create_url/', URLCreateView.as_view(), name='create_url'),
    path('<str:short_code>/', URLRedirectView.as_view(), name='redirect_url'),
]