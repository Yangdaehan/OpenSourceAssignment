from django.contrib import admin
from .models import Friend

class FriendAdmin(admin.ModelAdmin):
    search_fields = ['friend']

admin.site.register(Friend,FriendAdmin)