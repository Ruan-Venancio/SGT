from django.urls import path
from . import views

urlpatterns = [
	path("abacate", views.index, name="index")
]
