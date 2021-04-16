from django.urls import path, include
from rest_framework.authtoken import views as authtoken_views 
from api.accounts import views
urlpatterns = [
	path('user-record/', views.UserRecordView.as_view(), name='users'),
	path('api-auth-token/', authtoken_views.obtain_auth_token, name='api-auth-token'),
	path('register/', views.RegisterView.as_view(), name='register')

]