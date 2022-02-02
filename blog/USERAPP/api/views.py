from django.contrib.auth import update_session_auth_hash
from rest_framework import status
from rest_framework.generics import RetrieveUpdateAPIView,get_object_or_404,CreateAPIView
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from rest_framework.response import Response

from .permissions import isauthenticated
from .throttles import RegisterThrottle
from .serializers import UserSerializer, ChangePasswordSerializer, RegisterSerializer
from rest_framework.views import APIView

class ProfileAPIView(RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated,]
    serializer_class   = UserSerializer
    queryset           = User.objects.all()

    def get_object(self):
        queryset = self.get_queryset()
        obj      = get_object_or_404(queryset,id=self.request.user.id)
        return obj

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

class UpdatePasswordAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def put(self,request,*args,**kwargs):
        self.KULLANICI = self.request.user
        data={
            "old_password":request.data["old_password"],
            "new_password":request.data["new_password"]
        }
        serializer = ChangePasswordSerializer(data=data)
        if serializer.is_valid():
            old_password = serializer.data.get("old_password")
            if not self.KULLANICI.check_password(old_password):
                return Response({"old_password":"wrong_password"},status=status.HTTP_400_BAD_REQUEST)
            self.KULLANICI.set_password(serializer.data.get("new_password"))
            self.KULLANICI.save()
            update_session_auth_hash(request,self.KULLANICI)
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class CreateUserAPIView(CreateAPIView):
    model = User.objects.all()
    #throttle_classes = [RegisterThrottle]
    permission_classes = [isauthenticated]
    serializer_class = RegisterSerializer