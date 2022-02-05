
from rest_framework import serializers
from LIKESAPP.models import LikesDislikesModel
class LikesDislikeDetailSerializer(serializers.ModelSerializer):

    Username = serializers.SerializerMethodField(method_name="get_Username")

    def get_Username(self,obj):
        return obj.user.username

    class Meta:
        model  = LikesDislikesModel
        fields = ("Username",)

class LikeCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = LikesDislikesModel
        fields = ("Post","user")

class LikesDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model  = LikesDislikesModel
        fields = ("Post","user")




