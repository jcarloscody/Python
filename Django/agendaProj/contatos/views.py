from django.shortcuts import render, redirect
from django.http import Http404
from django.template import  TemplateSyntaxError
from django.core.paginator import Paginator
from django.db.models import Q, Value
from django.db.models.functions import  Concat
from django.contrib import messages

from . import  models




def index(req):


    #contatos = models.Contato.objects.all()
    contatos = models.Contato.objects.order_by('id').filter(
        mostrar=True
    ) #se quiser pode tirar o if do index.html

    paginator = Paginator(contatos, 1)
    page = req.GET.get('p')

    contatos = paginator.get_page(page)
    return render(req, 'contatos/index.html', {
        'contatos': contatos
    })


def ver_contato(req, id):
    try:
        contato = models.Contato.objects.get(id=id)

        if not contato.mostrar:
            return render(req, "contatos/erro.html", {"erro": "erro"})

        return render(req, 'contatos/ver_contato.html', {
            'contato': contato
        })
    except models.Contato.DoesNotExist as e:
        #raise Http404()
        return render(req, "contatos/erro.html", {"erro": e})
    except TemplateSyntaxError as e:
        return render(req, "contatos/erro.html", {"erro": e})

def busca (req):
    termo = req.GET.get('termo')

    if termo is None or not termo:
        messages.add_message(req, messages.ERROR, 'o campo deve ser preenchido')
        return redirect('index')

    campos = Concat('nome', Value(' '), 'sobrenome')

    """contatos = models.Contato.objects.order_by('id').filter(
        Q(nome__icontains = termo) | Q(sobrenome__icontains = termo),
        mostrar=True
    )"""

    contatos = models.Contato.objects.annotate(
        nome_completo = campos
    ).filter(
        Q(nome_completo__icontains = termo) | Q(telefone__icontains = termo),
        mostrar = True
    )

    paginator = Paginator(contatos, 1)
    page = req.GET.get('p')

    contatos = paginator.get_page(page)
    return render(req, 'contatos/busca.html', {
        'contatos': contatos
    })