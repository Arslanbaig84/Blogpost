from django.contrib import admin
from .models import Follow

# Register your models here.
class FollowAdmin(admin.ModelAdmin):
    pass

admin.site.register(Follow, FollowAdmin)