from django.contrib.auth.models import User
from django_countries.serializer_fields import CountryField
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from users.models import Profile


class UserSerializer(serializers.Serializer):
    email = serializers.EmailField()
    username = serializers.CharField(max_length=100)


class ProfileListSerializer(ModelSerializer):
    country = CountryField(country_dict=True)
    user = UserSerializer()

    class Meta:
        model = Profile
        fields = ['user', 'first_name', 'last_name', 'dob', 'image', 'country']
