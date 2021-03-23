from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path(r'^user/', views.Fahrten_user,
        name='Fahrten_user'),
    path('fahrt/<int:pk>/', views.fahrten_detail, name='fahrt_detail'),
    path('absage/<int:pk>/',views.fahrten_Absage, name='fahrt_absage'),
]