import string
import random
from django.db import models
from config import Expiration_Date
from datetime import timedelta, datetime
from django.utils import timezone

class URLMapping(models.Model):
    original_url = models.URLField(max_length=2048)
    short_code = models.CharField(max_length=6, unique=True)
    expiration_date = models.DateTimeField(null=False, default=datetime.now() + timedelta(days=int(Expiration_Date.EXPIRATION_DATE)))

    def save(self, *args, **kwargs):
        if not self.short_code:
            self.short_code = self.generate_short_code() 
        super().save(*args, **kwargs)

    def generate_short_code(self, length=6):
        characters = string.ascii_letters + string.digits 
        while True:
            short_code = ''.join(random.choices(characters, k=length))
            if not URLMapping.objects.filter(short_code=short_code).exists():
                break
        return short_code