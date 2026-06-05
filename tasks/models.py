from django.conf import settings
from django.db import models


class Task(models.Model):
    """
    Modelo que representa uma tarefa.
    Cada tarefa tem um título, descrição,
    status de conclusão e data de que foi criada.
    """
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    responsible = models.ForeignKey(
        # Referencia ao user do django
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        # Permite acessar: user.tasks.all()
        related_name='tasks',
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title
