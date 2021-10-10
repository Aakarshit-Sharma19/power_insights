from rest_framework.exceptions import APIException
from rest_framework import status


class DateNotProvided(APIException):
    status = status.HTTP_400_BAD_REQUEST
    default_code = 'date_not_provided'
    default_detail = 'proper date for the request is not provided'
