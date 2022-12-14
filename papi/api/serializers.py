from rest_framework import serializers
from .models import Task

class TaskSerializador(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ('nombre', 'prioridad', 'completado_en', 'creado_en')
    
