from rest_framework.generics import ListAPIView
from  rest_framework.permissions import IsAuthenticated
from NOTIFICATIONAPP.models import ModelNotification
from .serializers import SerializerNotificationList


class NotificationListAPIView(ListAPIView):
    permission_classes =[IsAuthenticated]
    serializer_class = SerializerNotificationList

    def get_queryset(self):
        return ModelNotification.objects.filter(user=self.request.user)


