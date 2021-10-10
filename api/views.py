from typing import Dict
from rest_framework.generics import (ListAPIView)
from rest_framework.permissions import IsAuthenticated
from django.db.models import F, Sum
from api.models import Record
from api.serializers import ConsumptionRecordSerializer
from api.exceptions import DateNotProvided
from django.contrib.auth import get_user_model


# Create your views here.
User = get_user_model()


class ConsumptionView(ListAPIView):
    serializer_class = ConsumptionRecordSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        '''
        For any params only day is optional but month and year are not
        '''
        params = self.request.GET
        month = params.get('month', None)
        year = params.get('year', None)
        day = params.get('day', None)
        get_total = params.get('get_total', None) == 'true'
        filters: Dict = {
            'user_id': self.request.user.pk
        }

        if not month or not year:
            raise DateNotProvided
        if year:
            filters['datetime__year'] = int(year)
        if month:
            filters['datetime__month'] = int(month)
        if day:
            filters['datetime__day'] = int(day)
            return Record.objects.filter(
                **filters
            ).order_by('datetime')

        return Record.objects.filter(
            **filters
        ).values(
            date=F('datetime__date')
        ).annotate(
            Sum('consumption')
        ).order_by(
            'datetime__date')
