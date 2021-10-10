from rest_framework import serializers

from .models import Record


class ConsumptionRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Record
        fields = ('datetime', 'consumption')

    def create(self, validated_data):
        return Record.objects.create(**validated_data, user=self.context['request'].user)
