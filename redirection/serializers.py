from rest_framework import serializers
from .models import URLMapping
from config import SERVER_HOST

class URLMappingSerializer(serializers.ModelSerializer):
    class Meta:
        model = URLMapping
        fields = ['original_url', 'short_code', 'expiration_date']
        read_only_fields = ['short_code', 'expiration_date']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        short_code = data.get('short_code')
        
        filtered_data = {
            'short_url': f'{SERVER_HOST.HOST}/redirection/{short_code}/',
            'expiration_date': data.get('expiration_date'),
            'success': True,
            'reason': ''
        }
        
        return filtered_data
