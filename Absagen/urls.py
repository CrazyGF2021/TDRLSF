from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.Absagen_user, name='Absagen_list'),
]