from rest_framework import serializers
from POSTAPP.models import PostModel

class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model=PostModel
        fields=[
            "Title","Content",'Draft','CreatedDate','ModifiedDate','Image','Slug'
        ]
