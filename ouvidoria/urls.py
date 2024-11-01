from django.urls import path
from . import views

urlpatterns = [
    path('helloWorld/', views.helloWorld),
    path('', views.form_manifestacao, name='form_manifestacao'),
    path('yourName/<str:name>', views.yourName, name='yourName')
]
