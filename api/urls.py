
from django.urls import path
from . import views

urlpatterns = [
    path('get_all',views.index,name='index'),
    path('postnote', views.postnote, name='postnote'),
]
