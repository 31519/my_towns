from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework import serializers
from productivity.models import Jobs, Advertisement, Shops, OwnBusiness, Celebrities, Hotels, Tourisms, Resell

class JobsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Jobs
        fields ='__all__'



class AdvertisementSerializers(serializers.ModelSerializer):
    class Meta:
        model = Advertisement
        fields ='__all__'



class ShopsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Shops
        fields ='__all__'


class OwnBusinessSerializers(serializers.ModelSerializer):
    class Meta:
        model = OwnBusiness
        fields ='__all__'


class CelebritiesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Celebrities
        fields ='__all__'

class HotelsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Hotels
        fields ='__all__'

class TourismsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Tourisms
        fields ='__all__'

class ResellSerializers(serializers.ModelSerializer):
    class Meta:
        model = Resell
        fields ='__all__'
