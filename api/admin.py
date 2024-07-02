from django.contrib import admin
from .models import TextNote,CommentReplay,Comment
# Register your models here.
admin.site.register(TextNote)
admin.site.register(CommentReplay)
admin.site.register(Comment)