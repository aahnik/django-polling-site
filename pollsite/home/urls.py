from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('opensource/', views.opnsrc, name='opensource')
]
