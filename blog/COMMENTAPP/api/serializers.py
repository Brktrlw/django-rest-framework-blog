from rest_framework.serializers import ModelSerializer
from COMMENTAPP.models import CommentModel
from rest_framework import serializers
class CommentCreateSerializer(ModelSerializer):
    class Meta:
        model=CommentModel
        exclude=["CreatedDate",]
    def validate(self, attrs):
        if attrs["Parent"]:
            if attrs["Parent"].Post != attrs["Post"]:
                raise serializers.ValidationError("Bir şey yanlış")
        return attrs

class CommentListSerializers(ModelSerializer):
    class Meta:
        model=CommentModel
        fields='__all__'
