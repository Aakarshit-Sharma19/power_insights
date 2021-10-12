from django.urls import path, include
from api.views import ConsumptionView, verify_token
urlpatterns = [
    path('consumption/', ConsumptionView.as_view(),
         name='consumption-view'),
    path('verify_token/', verify_token, name='verify-token')
]
