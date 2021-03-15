from rest_framework import views, generics
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from .serializers import ExchangeSerializer
from .models import BdmExch,DofExch, FixerExch
from rest_framework.decorators import api_view
from rest_framework_api_key.permissions import HasAPIKey

from .throttling import UserRateThrottle


from django.db import models
from django.http.request import HttpRequest

from rest_framework_api_key.models import APIKey

@api_view()
def create_key_view(request):
    api_key, key = APIKey.objects.create_key(name="my-remote-service")
    return Response({"Api-Key":key})

class ExchangeView(generics.RetrieveAPIView):
    queryset = DofExch.objects.all()
    permission_classes = [HasAPIKey]
    throttle_classes = [UserRateThrottle]

    def get(self, request, *args, **kwargs):
        filters = {}
        try:
            filters['Diario_Oficial_de_la_Federacion'] = DofExch.objects.latest('id')
        except:
            filters['Diario_Oficial_de_la_Federacion'] = None
        
        try:
            filters['Banco_de_Mexico'] = BdmExch.objects.latest('id')
        except:
            filters['Banco_de_Mexico'] = None
        
        try:
            filters['Fixer'] = FixerExch.objects.latest('id')
        except:
            filters['Fixer'] = None
        
        serializer = ExchangeSerializer(filters)
        return Response (serializer.data, status=HTTP_200_OK)


