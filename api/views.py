from rest_framework.generics import (ListAPIView)
from rest_framework.permissions import IsAuthenticated

from api.models import Record
from api.serializers import ConsumptionRecordSerializer


# Create your views here.


class ConsumptionView(ListAPIView):
    serializer_class = ConsumptionRecordSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        params = self.request.GET
        month = params['month']
        year = params['year']
        return Record.objects.filter(
            datetime__year=int(year),
            datetime__month=int(month)
        ).order_by('datetime')
