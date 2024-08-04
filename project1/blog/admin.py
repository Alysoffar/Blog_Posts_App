from django.contrib import admin # type: ignore
from .models import Post
# Register your models here.
admin.site.register(Post)