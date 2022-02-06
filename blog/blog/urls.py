
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/post/",include("POSTAPP.api.urls",namespace="post")),
    path("api/comment/",include("COMMENTAPP.api.urls",namespace="comment")),
    path("api/user/",include("USERAPP.api.urls",namespace="account")),
    path("api/favorites/",include("FAVORITES.api.urls",namespace="favorites")),
    path("api/postlikes/",include("LIKESAPP.api.urls",namespace="postlikes")),
    path("api/commentlikes/",include("COMMENTLIKES.api.urls",namespace="commentlikes")),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path("api/notification/",include("NOTIFICATIONAPP.api.urls"),name="notification")

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)