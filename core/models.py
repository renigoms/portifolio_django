from django.conf import settings
from django.db import models
from stdimage import StdImageField


# Create your models here.
class Profile(models.Model):

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        related_name='profile',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    image_profile_url = StdImageField('Foto de Perfil', upload_to='images/profile/', variations={'thumb': (128, 128)}, blank=True, null=True)
    name = models.CharField('Nome', max_length=100, blank=False, null=False)
    email = models.EmailField('E-mail', max_length=100, blank=False, null=False)
    description = models.CharField("Sobre Mim", max_length=255, blank=True, null=True)
    course = models.CharField('Curso', max_length=100, blank=False, null=False)
    period = models.CharField('Periodo', max_length=100, blank=False, null=False)
    linkend = models.URLField('Linkend', max_length=100, blank=True, null=True)
    git = models.URLField('Git', max_length=100, blank=True, null=True)

    class Meta:
        verbose_name = 'Perfil Pessoal'
        verbose_name_plural = 'Perfis Pessois'

    def __str__(self):
        return self.name