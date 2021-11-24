from django.shortcuts import render
from . import  models



def index(req):
    contatos = models.Contato.objects.all()
    return render(req, 'contatos/index.html', {
        'contatos': contatos
    })


def ver_contato(req, id):
    contato = models.Contato.objects.get(id=id)
    return render(req, 'contatos/ver_contato.html', {
        'contato': contato
    })