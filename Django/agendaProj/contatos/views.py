from django.shortcuts import render
from django.http import Http404
from django.template import  TemplateSyntaxError


from . import  models



def index(req):
    contatos = models.Contato.objects.all()
    return render(req, 'contatos/index.html', {
        'contatos': contatos
    })


def ver_contato(req, id):
    try:
        contato = models.Contato.objects.get(id=id)
        return render(req, 'contatos/ver_contato.html', {
            'contato': contato
        })
    except models.Contato.DoesNotExist as e:
        #raise Http404()
        return render(req, "contatos/erro.html", {"erro": e})
    except TemplateSyntaxError as e:
        return render(req, "contatos/erro.html", {"erro": e})