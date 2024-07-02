from django.db import models

class TextNote(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"TextNote {self.id} created on {self.created_at}"

class Comment(models.Model):
    note = models.ForeignKey(TextNote, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    

class CommentReplay(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='replay')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

