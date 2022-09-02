from rest_framework.serializers import ModelSerializer
from base.models import Note,Pita


class NoteSerializer(ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'


class PitaSerializer(ModelSerializer):
    class Meta:
        model = Pita
        fields = '__all__'
