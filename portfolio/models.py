from django.db import models

# Create your models here.
class Certificate(models.Model):
    description = models.CharField('Descrição', max_length=255, blank=False, null=False)

class Project(models.Model):
    class ProjectTypeChoice(models.TextChoices):
        PERSONAL = 'PESSOAL', 'Pessoal'
        SUBJECT = 'DISCIPLINA', 'Disciplina'

    project_type = models.CharField('Tipo',
                                    choices=ProjectTypeChoice,
                                    default=ProjectTypeChoice.PERSONAL,
                                    max_length=10)
    name = models.CharField('Nome', max_length=100, blank=False, null=False)
    description = models.CharField('Descrição', max_length=255, blank=False, null=False)
    git = models.CharField('Git', max_length=100, blank=False, null=False)



