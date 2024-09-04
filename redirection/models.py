import string
import random
from django.db import models
from config import SERVER_HOST
from datetime import datetime, timedelta

class URLMapping(models.Model):
    original_url = models.URLField()
    short_url = models.URLField(unique=True)
    expiration_date = models.DateTimeField(null=False, default=datetime.now() + timedelta(days=30))

    def save(self, *args, **kwargs):
        if not self.short_url:
            self.short_url = self.generate_short_url() 
        super().save(*args, **kwargs)

    def generate_short_url(self, length=6):
        characters = string.ascii_letters + string.digits 
        while True:
            short_code = ''.join(random.choices(characters, k=length))
            short_url = f'{SERVER_HOST.HOST}/redirection/{short_code}/'
            if not URLMapping.objects.filter(short_url=short_url).exists():
                break
        return short_url