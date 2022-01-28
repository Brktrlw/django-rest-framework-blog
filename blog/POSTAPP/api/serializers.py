from rest_framework import serializers
from POSTAPP.models import PostModel
from datetime import datetime
class PostSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="post:postDetail", lookup_field="Slug")
    CreatedDate  = serializers.SerializerMethodField(method_name="get_CreatedDate")
    ModifiedDate = serializers.SerializerMethodField(method_name="get_ModifiedDate")

    def get_CreatedDate(self,obj):
        tarih = datetime.strftime(obj.CreatedDate, '%m/%d/%Y, %H:%M:%S')
        return str(tarih)

    def get_ModifiedDate(self,obj):
        tarih = datetime.strftime(obj.ModifiedDate, '%m/%d/%Y, %H:%M:%S')
        return str(tarih)


    AuthorName      = serializers.CharField(source="Author.username")
    class Meta:
        model=PostModel
        fields=[
            "AuthorName","Title","Content",'Draft','CreatedDate','ModifiedDate','Image','url'
        ]