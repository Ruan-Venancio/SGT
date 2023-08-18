from django.urls import path
from . import views

urlpatterns = [
	path("abacate", views.index, name="index"),
	path("abacaxi", views.index2, name="index2"),
	path("andre", views.andre, name="andrezinho")
]
