from rest_framework import serializers
from .models import *


class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = [
                'id',
                'name',
                'address',
                'latitude',
                'longitude',
                'category',
                'parking',
                'dis_parking',
                'big_parking',
                'wheelchair',
                'toilet',
                'braille',
                'audio'

                ]

class PlaceDetailSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = [
                'name',
                'address',
                'category',
                'parking',
                'dis_parking',
                'big_parking',
                'wheelchair',
                'toilet',
                'braille',
                'audio'
        ]
        

class MySerializers(serializers.ModelSerializer):
    class Meta:
        model = My
        fields = ["author", "latitude",'longitude']