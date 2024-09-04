from rest_framework import serializers
from .models import URLMapping
from datetime import datetime
import pytz

class URLMappingSerializer(serializers.ModelSerializer):
    class Meta:
        model = URLMapping
        fields = ['original_url', 'short_url', 'expiration_date']
        read_only_fields = ['short_url', 'expiration_date']

    def to_representation(self, instance):
        data = super().to_representation(instance)

        filtered_data = {
            'short_url': data.get('short_url'),
            'expiration_date': data.get('expiration_date'),
            'success': True,
            'reason': ''
        }
        
        return filtered_data
