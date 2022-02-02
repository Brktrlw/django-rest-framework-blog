

from django.urls import path
from USERAPP.api.views import ProfileAPIView
app_name="account"

urlpatterns = [
    path('update-user/', ProfileAPIView.as_view(),name="userUpdate"),

]
