
from django.urls import path
from . import views

urlpatterns = [
    
    path('get_all',views.index,name='index'),
    path('postnote', views.postnote, name='postnote'),

    path('display_comment/<int:note_id>',views.display_comment, name='display_comment'),
    path('post_comment/<int:note_id>',views.post_comment, name='post_comment'),

    path('display_comment_replay/<int:comment_id>',views.display_comment_replay, name='display_comment_replay'),
    path('post_comment_replay/<int:comment_id>', views.post_comment_replay, name='post_comment_replay'),
]
