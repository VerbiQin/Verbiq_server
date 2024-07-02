from rest_framework import serializers
from .models import TextNote,CommentReplay,Comment

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = TextNote
        fields = ['id', 'content', 'created_at']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'note', 'content', 'created_at']

class CommentReplaySerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentReplay
        fields = ['id', 'comment', 'content', 'created_at']