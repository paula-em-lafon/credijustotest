from rest_framework import serializers
from .models import BdmExch,DofExch, FixerExch

class BdmExchSerializer(serializers.ModelSerializer):
    value = serializers.DecimalField(source="exch", decimal_places=4,max_digits= 30)
    last_updated = serializers.DateTimeField(source="time")
    class Meta:
        model = BdmExch
        fields = ('last_updated', 'value')

class DofExchSerializer(serializers.ModelSerializer):
    value = serializers.DecimalField(source="exch", decimal_places=4, max_digits= 30)
    last_updated = serializers.DateTimeField(source="time")
    class Meta:
        model = DofExch
        fields = ('last_updated', 'value')

class FixerExchSerializer(serializers.ModelSerializer):
    value = serializers.DecimalField(source="exch", decimal_places=4,max_digits= 30)
    last_updated = serializers.DateTimeField(source="time")
    class Meta:
        model = FixerExch
        fields = ('last_updated', 'value')

class ExchangeSerializer(serializers.Serializer):
    Diario_Oficial_de_la_Federacion = DofExchSerializer(read_only=True)
    Banco_de_Mexico = BdmExchSerializer(read_only=True)
    Fixer= FixerExchSerializer(read_only=True)
