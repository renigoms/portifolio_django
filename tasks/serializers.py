from rest_framework import serializers
from tasks.models import Task

class TaskSerializer(serializers.ModelSerializer):
    """
    Serializer para o modelo Tarefa.
    ModelSerializer gerar automaticamente os campos
    com base no modelo, iniciando validação.
    """
    responsible = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Task

        fields = ['id', 'title', 'description', 'completed', 'created_at', 'responsible']

        read_only_fields = ['id', 'created_at' ,'responsible']
        

