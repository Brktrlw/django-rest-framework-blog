
from rest_framework import serializers
from LIKESAPP.models import PostLikesModel

class LikesDetailSerializer(serializers.ModelSerializer):
    Username = serializers.SerializerMethodField(method_name="get_Username")
    def get_Username(self,obj):
        return obj.user.username
    class Meta:
        model  = PostLikesModel
        fields = ("Username",)

class LikeCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostLikesModel
        fields = ("user",)





