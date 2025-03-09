from rest_framework import serializers
from .models import *

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ('id', 'name')


class CharacteristicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Characteristic
        fields = ('id', 'name')


class LeagueSerializer(serializers.ModelSerializer):
    class Meta:
        model = League
        fields = ('id', 'name')

class ClubSerializer(serializers.ModelSerializer):
    characteristic_names = serializers.SerializerMethodField()
    country_details = CountrySerializer(source='country', read_only=True)
    league_details = LeagueSerializer(source='league', read_only=True)
    class Meta:
        model = Club
        fields = '__all__'

    def get_characteristic_names(self, obj):
        return [char.name for char in obj.characteristic.all()]