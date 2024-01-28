from django.contrib import admin
from petstagram.common.models import Like, PhotoComment


# Register your models here.
@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    pass


@admin.register(PhotoComment)
class PhotoCommentAdmin(admin.ModelAdmin):
    pass
