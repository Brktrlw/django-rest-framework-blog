from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model  = User
        fields =  ('id','first_name','last_name',)


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True),
    class Meta:
        model  = User
        fields =('id','username','password')

    def validate(self, attrs):
        pass

    def create(self, validated_data):
        pass





