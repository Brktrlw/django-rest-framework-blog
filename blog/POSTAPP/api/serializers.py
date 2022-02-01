from rest_framework import serializers
from POSTAPP.models import PostModel
from datetime import datetime
from COMMENTAPP.api.serializers import CommentListSerializers

class PostSerializer(serializers.ModelSerializer):
    url          = serializers.HyperlinkedIdentityField(view_name="post:postDetail", lookup_field="Slug")
    CreatedDate  = serializers.SerializerMethodField(method_name="get_CreatedDate")
    ModifiedDate = serializers.SerializerMethodField(method_name="get_ModifiedDate")
    Author       = serializers.SerializerMethodField(method_name="get_Author")


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
        fields=["Author","Title","Content",'Draft','CreatedDate','ModifiedDate','Image','url']

class PostDetailSerializer(serializers.ModelSerializer):
    url      = serializers.HyperlinkedIdentityField(view_name="post:postDetail", lookup_field="Slug")
    Author   = serializers.SerializerMethodField()
    Yorumlar = serializers.SerializerMethodField(method_name="get_Yorumlar")

    def get_Yorumlar(self,obj):
        yorumlar   = obj.comments.all()
        serializer = CommentListSerializers(yorumlar,many=True)
        if serializer.data==[]:
            return None
        return serializer.data


    def get_Author(self,obj):
        return obj.Author.username

    class Meta:
        model = PostModel
        fields=["Author","Title","Content",'Draft','CreatedDate','ModifiedDate','Image','url','Yorumlar']

class PostCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostModel
        fields = ["Title","Content",'Draft','Image']
