from django.contrib import admin

from core.models import Profile


# Register your models here.

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'description', 'period', 'course', 'linken', 'git', 'image_profile_url']