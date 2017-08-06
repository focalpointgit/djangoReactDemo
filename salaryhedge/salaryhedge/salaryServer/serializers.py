from django.contrib.auth.models import User, Group
from rest_framework import serializers
from models import Address, Asset

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url','username', 'email','groups')

class AddressSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Address
        fields = ('street_number','street_name','street_type','city','state','zip_code','latitude','longitude')
