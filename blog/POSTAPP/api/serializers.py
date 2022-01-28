from rest_framework import serializers
from POSTAPP.models import PostModel
from datetime import datetime
class PostSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name="post:postDetail",
        lookup_field="Slug"
    )

    AuthorName      = serializers.CharField(source="Author.username")
    #olusturmaTarihi = serializers.SerializerMethodField(method_name="createdDateMethod")
    class Meta:
        model=PostModel
        fields=[
            "AuthorName","Title","Content",'Draft','CreatedDate','ModifiedDate','Image','url',
        ]
    def createdDateMethod(self,obj):
        zaman=datetime.strptime()