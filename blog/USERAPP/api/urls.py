

from django.urls import path
from USERAPP.api.views import ProfileAPIView,UpdatePasswordAPIView,CreateUserAPIView
app_name="account"

urlpatterns = [
    path('profile/', ProfileAPIView.as_view(),name="profileUpdate"),
    path('change-password/', UpdatePasswordAPIView.as_view(), name="changePassword"),
    path('create/', CreateUserAPIView.as_view(), name="createUser"),
]
