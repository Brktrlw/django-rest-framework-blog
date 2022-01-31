from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from FAVORITES.models import FavoritesModel

class FavoritesListCreateAPISerializer(ModelSerializer):

    class Meta:
        model  = FavoritesModel
        fields = ('user','Post')

    def validate(self, attrs):
        #Eğer favorilerinde zaten varsa ve yine favorilerine eklemeye çalışıyorsa uyarı verir
        queryset = FavoritesModel.objects.filter(Post=attrs["Post"],user= attrs["user"])
        if queryset.exists():
            raise serializers.ValidationError("Zaten kayıtlı")
        return attrs