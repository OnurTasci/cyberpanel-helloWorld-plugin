from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='helloWorld'),
    path('createHello', views.index, name='helloWorld_createHello'),
]
