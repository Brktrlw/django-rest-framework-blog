from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer
from COMMENTAPP.models import CommentModel
from rest_framework import serializers
from datetime import datetime

class CommentCreateSerializer(ModelSerializer):
    class Meta:
        model=CommentModel
        exclude=["CreatedDate","Author"]

    def validate(self, attrs):
        if attrs["Parent"]:
            if attrs["Parent"].Post != attrs["Post"]:
                raise serializers.ValidationError("Bir şeyler Ters Gitti")
        return attrs

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields=('first_name','last_name','username',"id") #

class CommentListSerializers(ModelSerializer):
    CreatedDate  = serializers.SerializerMethodField()
    Author       = UserSerializer()
    Replies      = serializers.SerializerMethodField()
    ModifiedDate = serializers.SerializerMethodField()

    def get_Replies(self,obj):
        if obj.any_children:
            return CommentListSerializers(obj.children(),many=True).data

    def get_CreatedDate(self,obj):
        tarih = datetime.strftime(obj.CreatedDate, '%d/%m/%Y %H:%M:%S')
        return str(tarih)

    def get_ModifiedDate(self,obj):
        tarih = datetime.strftime(obj.ModifiedDate, '%d/%m/%Y %H:%M:%S')
        return str(tarih)

    def get_Author(self,obj):
        return obj.Author.username

    class Meta:
        model=CommentModel
        fields=("Author","CreatedDate","ModifiedDate","Post","Parent","CommentText","Replies")

class CommentUpdateSerializer(ModelSerializer):
    class Meta:
        model=CommentModel
        fields=('CommentText',)
