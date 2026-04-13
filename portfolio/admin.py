from django.contrib import admin

from portfolio.models import Project, Certificate


# Register your models here.
@admin.register(Project)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'project_type', 'git']

@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ['description']