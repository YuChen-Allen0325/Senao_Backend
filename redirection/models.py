import string
import random
from django.db import models

class URLMapping(models.Model):
    original_url = models.URLField()
    short_code = models.CharField(max_length=8, unique=True)

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
