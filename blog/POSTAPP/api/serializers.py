from rest_framework import serializers
from POSTAPP.models import PostModel
from datetime import datetime

class PostSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name="post:postDetail",
        lookup_field="Slug")

    AuthorName      = serializers.CharField(source="Author.username")
    class Meta:
        model=PostModel
        fields=[
            "AuthorName","Title","Content",'Draft','CreatedDate','ModifiedDate','Image','url',
        ]