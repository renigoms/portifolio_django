from django.db import models
from stdimage import StdImageField


# Create your models here.
class Profile(models.Model):
    name = models.CharField('Nome', max_length=100, blank=False, null=False)
    email = models.EmailField('E-mail', max_length=100, blank=False, null=False)
    description = models.CharField("Sobre Mim", max_length=255, blank=False, null=False)
    course = models.CharField('Curso', max_length=100, blank=False, null=False)
    linken = models.CharField('Linken', max_length=100, blank=False, null=False)
    git = models.CharField('Git', max_length=100, blank=False, null=False)
    image_profile_url = StdImageField('Foto de Perfil', upload_to='images/profile/', variations={'thumb': (128, 128)})
    period = models.CharField('Periodo', max_length=100, blank=False, null=False)