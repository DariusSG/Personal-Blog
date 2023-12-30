from django.contrib import admin
from django.contrib.admin import ModelAdmin

from ProjectWeb.blog.models import *


# Register your models here.


@admin.register(Post)
class PostAdmin(ModelAdmin):
    pass


@admin.register(Tag)
class TagAdmin(ModelAdmin):
    pass
