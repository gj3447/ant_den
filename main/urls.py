from django.urls import path
from . import views

app_name = 'community'

urlpatterns = [
    path('test', views.index, name='index'),
]