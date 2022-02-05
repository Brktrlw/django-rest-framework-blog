from rest_framework import serializers
from COMMENTLIKES.models import CommentLikesModel

class CommentLikesListSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField(method_name="get_username")
    def get_username(self,obj):
        return obj.user.username
    class Meta:
        model  = CommentLikesModel
        fields = ("username",)