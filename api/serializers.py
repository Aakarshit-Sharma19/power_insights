from rest_framework import serializers

from .models import Record


class ConsumptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Record
        fields = ('datetime', 'consumption')

    def create(self, validated_data):
        return Record.objects.create(**validated_data, user=self.context['request'].user)


class DailyConsumptionSerializer(serializers.Serializer):
    date = serializers.DateField()
    consumption = serializers.DecimalField(
        max_digits=15, decimal_places=3)



class MonthlyConsumptionSerializer(serializers.Serializer):
    month = serializers.IntegerField(min_value=1, max_value=12)
    consumption = serializers.DecimalField(
        max_digits=15, decimal_places=3)
