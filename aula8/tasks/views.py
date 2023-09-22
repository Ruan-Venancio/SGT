from django.shortcuts import render

# Create your views here.

tasks = ["primeiro", "segundo", "terceiro"]

def index(request):
    return render(request, 'tasks/index.html', {
        "tasks":tasks
    })