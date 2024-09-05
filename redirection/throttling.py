from rest_framework.throttling import BaseThrottle
from django.core.cache import cache
import time

class IPRateThrottle(BaseThrottle):
    def __init__(self):
        self.rate = 5
        self.cache_timeout = 60

    def allow_request(self, request, view):
        client_ip = request.META.get('REMOTE_ADDR')
        if not client_ip:
            return True
        
        cache_key = f'throttle_ip_{client_ip}'
        request_times = cache.get(cache_key, [])

        now = time.time()
        request_times = [t for t in request_times if now - t < self.cache_timeout]

        if len(request_times) >= self.rate:
            return False
        
        request_times.append(now)
        cache.set(cache_key, request_times, timeout=self.cache_timeout)

        return True

    def wait(self):
        return self.cache_timeout
