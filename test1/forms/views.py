from django.shortcuts import render

def index(request):
    if request.method == "GET":
        nome = "Ninguém"
        idade = 0
        return render(request, 'forms/index.html', {
            'nome': nome
        })
    elif request.method == "POST":
        nome = request.POST.get('nome')
        idade = request.POST.get('idade')

        return render (request, 'forms/index.html', {
            'nome':nome,
            'idade':idade
        })
