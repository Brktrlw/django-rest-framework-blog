from rest_framework import serializers
from POSTAPP.models import PostModel
from datetime import datetime
from COMMENTAPP.api.serializers import CommentListSerializers
from LIKESAPP.models import PostLikesModel
class PostSerializer(serializers.ModelSerializer):
    url          = serializers.HyperlinkedIdentityField(view_name="post:postDetail", lookup_field="Slug")
    CreatedDate  = serializers.SerializerMethodField(method_name="get_CreatedDate")
    ModifiedDate = serializers.SerializerMethodField(method_name="get_ModifiedDate")
    Author       = serializers.SerializerMethodField(method_name="get_Author")
    totalLikes   = serializers.SerializerMethodField(method_name="get_totalLikes")
    isLiked      = serializers.SerializerMethodField(method_name="get_isLiked")

    def get_isLiked(self,obj):
        isLiked = PostLikesModel.objects.filter(user=self.context["request"].user,Post=obj).exists()
        return isLiked

    def get_totalLikes(self,obj):
        totalLike = obj.likes.all().count()
        return totalLike

    def get_CreatedDate(self,obj):
        tarih = datetime.strftime(obj.CreatedDate, '%d/%m/%Y %H:%M:%S')
        return str(tarih)

    def get_ModifiedDate(self,obj):
        tarih = datetime.strftime(obj.ModifiedDate, '%d/%m/%Y %H:%M:%S')
        return str(tarih)

    def get_Author(self,obj):
        return obj.Author.username

    class Meta:
        model=PostModel
        fields=["Author","Title","isLiked","Content",'totalLikes','CreatedDate','ModifiedDate','Image','url']

class PostDetailSerializer(serializers.ModelSerializer):
    url          = serializers.HyperlinkedIdentityField(view_name="post:postDetail", lookup_field="Slug")
    Author       = serializers.SerializerMethodField()
    Yorumlar     = serializers.SerializerMethodField(method_name="get_Yorumlar")
    CreatedDate  = serializers.SerializerMethodField(method_name="get_CreatedDate")
    ModifiedDate = serializers.SerializerMethodField(method_name="get_ModifiedDate")
    totalLikes   = serializers.SerializerMethodField(method_name="get_totalLikes")
    isLiked      = serializers.SerializerMethodField(method_name="get_isLiked")

    def get_isLiked(self,obj):
        isLiked = PostLikesModel.objects.filter(user=self.context["request"].user,Post=obj).exists()
        return isLiked

    def get_totalLikes(self,obj):
        totalLike = obj.likes.all().count()
        return totalLike

    def get_Yorumlar(self,obj):
        yorumlar   = obj.comments.filter(Parent=None)
        serializer = CommentListSerializers(yorumlar,many=True)
        if serializer.data==[]:
            return None
        return serializer.data

    def get_CreatedDate(self, obj):
        tarih = datetime.strftime(obj.CreatedDate, '%d/%m/%Y %H:%M:%S')
        return str(tarih)

    def get_ModifiedDate(self, obj):
        tarih = datetime.strftime(obj.ModifiedDate, '%d/%m/%Y %H:%M:%S')
        return str(tarih)

    def get_Author(self,obj):
        return obj.Author.username

    class Meta:
        model = PostModel
        fields=["Author","Title","isLiked","Content","totalLikes",'CreatedDate','ModifiedDate','Image','url','Yorumlar']


class PostCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostModel
        fields = ["Title","Content",'Draft','Image']

