from django.urls import path

from core import views

app_name = 'core'

urlpatterns = [
    path('api/perfil/', views.ProfileDetail.as_view(), name='perfil-api'),
]