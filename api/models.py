from django.db import models

class TextNote(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

