from django.urls import path
from . import views

urlpatterns = [
    path('ruan', views.hello, name='hello_ruan')
]
