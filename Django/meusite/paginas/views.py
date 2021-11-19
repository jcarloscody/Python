from django.shortcuts import render

def index(req):
    return render(req, 'paginas/index.html')


def sobre(req):
    return render(req, 'paginas/sobre.html')