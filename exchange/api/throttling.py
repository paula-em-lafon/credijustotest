from rest_framework.throttling import SimpleRateThrottle
from rest_framework_api_key.models import APIKey


class UserRateThrottle(SimpleRateThrottle):
    """
    Limits the rate of API calls that may be made by a given user.
    The user id will be used as a unique cache key if the user is
    authenticated.  For anonymous requests, the IP address of the request will
    be used.
    """
    scope = 'apikey'

    def get_cache_key(self, request, view):
        api_key = APIKey()
        boolean = api_key.is_valid(request.META['HTTP_AUTHORIZATION'].split()[1])
        if boolean:
            ident = request.META['HTTP_AUTHORIZATION'].split()[1]
        else:
            ident = self.get_ident(request)

        return self.cache_format % {
            'scope': self.scope,
            'ident': ident
        }
