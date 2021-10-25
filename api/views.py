from typing import Dict
from rest_framework.generics import (ListAPIView)
from rest_framework.response import Response, responses
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from django.db.models import F, Sum, query
from api.models import Record
from api.serializers import ConsumptionSerializer, DailyConsumptionSerializer, MonthlyConsumptionSerializer
from api.exceptions import DateNotProvided
from django.contrib.auth import get_user_model
import datetime

# Create your views here.
User = get_user_model()


class ConsumptionView(ListAPIView):
    """
    This is the consumption view
    3 scenarios for the getting the electricity consumption are allowed
    Hourly Consumption - By providing the complete date in YYYY-MM-DD format as a GET param
    Daily Consumption - By providing the month and year separately as individual GET parameters
    Monthly Consumption - By only providing the year as a GET parameter
    """

    serializer_class = ConsumptionSerializer
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            params = self.request.GET
            if not 'date' in params:
                if 'month' not in params:
                    return MonthlyConsumptionSerializer

                else:
                    return DailyConsumptionSerializer
        return super().get_serializer_class()

    def get_queryset(self):
        params = self.request.GET
        month = params.get('month', None)
        year = params.get('year', None)
        date = params.get('date', None)
        # get_total = params.get('get_total', None) == 'true'
        filters: Dict = {
            'user_id': self.request.user.pk
        }

        if not year and not date:
            raise DateNotProvided
        # Store params for query parameters
        if year:
            filters['datetime__year'] = int(year)
        if month:
            filters['datetime__month'] = int(month)
        # If date is specified, return hourly consumption data of that particular date
        if date:
            filters['datetime__date'] = date
            return Record.objects.filter(
                **filters
            ).order_by('datetime')
        # If month is specified then return daily consumption
        if month:
            return Record.objects.filter(
                **filters
            ).values(
                date=F('datetime__date'),
            ).annotate(
                consumption=Sum('consumption')
            ).order_by(
                'datetime__date')
        else:
            # In this scenario, if year is only specified return monthly consumption
            return Record.objects.filter(
                **filters
            ).values(
                month=F('datetime__month'),
            ).annotate(
                consumption=Sum('consumption')
            ).order_by(
                'datetime__month')

    def get(self, request, *args, **kwargs):
        try:
            return super().get(request, *args, **kwargs)
        except DateNotProvided as error:
            return Response({
                'message': error.detail
            }, status=error.status)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def verify_token(request):
    '''
    Verifying 
    '''
    return Response(status=status.HTTP_204_NO_CONTENT)
