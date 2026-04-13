from django.conf.urls.static import static
from django.urls import path

from portfolio import views
from projeto_portifolio import settings

app_name = 'portfolio'
urlpatterns = [
    path('', views.home, name='home'),
    path('projetos/', views.projetos, name='projetos'),

]

