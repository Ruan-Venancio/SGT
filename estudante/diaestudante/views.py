from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
	return HttpResponse("Hello, world!")
	
def index2(request):
	return HttpResponse("Olá Ruan")
	
def andre(request):
	return HttpResponse("tu é gay")
