from rest_framework import serializers
from NOTIFICATIONAPP.models import ModelNotification

class SerializerNotificationList(serializers.ModelSerializer):
    postSlug = serializers.SerializerMethodField()
    re_user  = serializers.SerializerMethodField()

    def get_re_user(self,obj):
        return obj.re_user.username

    def get_postSlug(self,obj):
        return obj.post.Slug

    class Meta:
        model  = ModelNotification
        fields = ("NotificationText","postSlug","re_user")










