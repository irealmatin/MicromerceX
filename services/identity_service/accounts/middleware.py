from django.http import HttpResponseForbidden
from django.contrib.gis.geoip2 import GeoIP2

class BlockIPMiddleware:
    """Middleware to block requests from specific countries based on IP address."""

    def __init__(self, get_response):
        self.get_response = get_response
        self.geoip = GeoIP2()

    def __call__(self, request):
        """Process each incoming request.
        
        Args:
            request: HttpRequest object.
            
        Returns:
            HttpResponse: Forbidden response if IP is from blocked country,
                         otherwise passes request to next middleware.
        """
        ip = self.get_client_ip(request)
        try:
            country = self.geoip.country(ip)['country_code']
            if country == 'IL':
                return HttpResponseForbidden("Access denied from your country.")
        except Exception:
            pass  # optional:default is allow access
        return self.get_response(request)

    def get_client_ip(self, request):
        """Extract client IP address from request.
        
        Args:
            request: HttpRequest object.
            
        Returns:
            str: Client IP address, prioritizing X-Forwarded-For header.
        """
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            return x_forwarded_for.split(',')[0].strip()
        return request.META.get('REMOTE_ADDR')
