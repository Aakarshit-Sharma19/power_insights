from rest_framework.generics import CreateAPIView, ListAPIView, ListCreateAPIView
from rest_framework.mixins import CreateModelMixin, ListModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.views import APIView

from api.models import Record
from api.serializers import ConsumptionRecordSerializer

# Create your views here.


class ConsumptionView(ListCreateAPIView):
    serializer_class = ConsumptionRecordSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        params = self.request.GET
        month = params['month']
        year = params['year']
        return Record.objects.filter(
            date__year=int(year),
            date__month=int(month)
        ).order_by('date')
