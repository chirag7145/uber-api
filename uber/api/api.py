from tastypie.resources import ModelResource
from api.models import User, Driver
from tastypie import fields
from tastypie.api import Api
from tastypie.authentication import ApiKeyAuthentication
from tastypie.authorization import DjangoAuthorization
from tastypie.exceptions import InvalidFilterError
import datetime

class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'

class DriverResource(ModelResource):
    class Meta:
        queryset = Driver.objects.all()
        resource_name = 'driver'

UserApi_api = Api(api_name='UserApi')
UserApi_api.register(UserResource())
DriverApi_api = Api(api_name='DriverApi')
DriverApi_api.register(DriverResource())
