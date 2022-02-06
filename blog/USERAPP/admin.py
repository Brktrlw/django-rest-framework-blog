from django.contrib import admin
from .models import ProfileModel
from FAVORITES.models import FavoritesModel
from LIKESAPP.models import PostLikesModel
from COMMENTLIKES.models import CommentLikesModel
from NOTIFICATIONAPP.models import ModelNotification
from POSTAPP.models import PostModel
from COMMENTAPP.models import CommentModel

admin.site.register(PostLikesModel)
admin.site.register(CommentLikesModel)
admin.site.register(ModelNotification)
admin.site.register(PostModel)
admin.site.register(CommentModel)
admin.site.register(FavoritesModel)
admin.site.register(ProfileModel)




