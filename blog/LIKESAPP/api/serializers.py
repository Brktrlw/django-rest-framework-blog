
from rest_framework import serializers
from LIKESAPP.models import LikesDislikesModel
class LikesSerializer(serializers.ModelSerializer):

    Username = serializers.SerializerMethodField(method_name="get_Username")

    def get_Username(self,obj):
        return obj.user.username

    class Meta:
        model  = LikesDislikesModel
        fields = ("Username",)

class DislikesSerializer(serializers.ModelSerializer):

    Username = serializers.SerializerMethodField(method_name="get_Username")

    def get_Username(self,obj):
        return obj.user.username

    class Meta:
        model  = LikesDislikesModel
        fields = ("Username",)

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = LikesDislikesModel
        fields = ("Post","user")

    def validate(self, attrs):
        _isLike = LikesDislikesModel.objects.filter(user=attrs["user"],isLike=1,Post=attrs["Post"]).exists()
        if _isLike:
            raise serializers.ValidationError("Bu kullanıcı zaten bu gönderiyi beğenmiş")
        return attrs


