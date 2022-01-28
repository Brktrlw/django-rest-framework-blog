from rest_framework.serializers import ModelSerializer
from COMMENTAPP.models import CommentModel

class CommentCreateSerializer(ModelSerializer):

    class Meta:
        model=CommentModel
        exclude=["CreatedDate"]