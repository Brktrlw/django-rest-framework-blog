from rest_framework import serializers
from NOTIFICATIONAPP.models import ModelNotification

class SerializerNotificationList(serializers.ModelSerializer):
    class Meta:
        model  = ModelNotification
        fields = ("NotificationText",)










