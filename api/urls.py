from django.urls import path, include
from api.views import ConsumptionView
urlpatterns = [
    path('consumption/', ConsumptionView.as_view(),
         name='consumption-view')
]
