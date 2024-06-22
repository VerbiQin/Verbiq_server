from rest_framework import serializers
from .models import TextNote

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = TextNote
        fields = ['id', 'content', 'created_at']
