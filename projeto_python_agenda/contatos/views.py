from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import contato
from django.core.paginator import Paginator
from django.db.models import Q, Value
from django.db.models.functions import Concat


def index(request):
    contatos = contato.objects.order_by('-id')
    paginador = Paginator(contatos, 20)

    page = request.GET.get('p')
    contatos = paginador.get_page(page)

    return render(request, 'contatos/index.html',{
        'contatos':contatos
    })

def ver_contato(request, contato_id):
    """try:
        contato1 = contato.objects.get(id=contato_id)
        return render(request, 'contatos/ver_contato.html',{
            'contato1':contato1
        })
    except contato.DoesNotExist as e:
        raise Http404()"""

    #contato1 = contato.objects.get(id=contato_id)
    contato1 = get_object_or_404(contato, id=contato_id)

    if not contato1.mostrar:
        raise  Http404()

    return render(request, 'contatos/ver_contato.html', {
        'contato1': contato1
    })



def busca (request):
    termo = request.GET.get('termo')
    if termo is None or not termo:
        raise Http404

    campos = Concat('nome', Value(' '),'sobrenome')

    contatos = contato.objects.annotate(
        nome_completo=campos).filter(
        Q(nome_completo__icontains=termo) | Q(telefone__icontains=termo)
    )

    """contatos = contato.objects.order_by('-id').filter(
        Q(nome__icontains=termo) | Q(sobrenome__icontains = termo),
        mostrar=True
    )"""
    paginador = Paginator(contatos, 20)

    page = request.GET.get('p')
    contatos = paginador.get_page(page)

    return render(request, 'contatos/busca.html', {
        'contatos': contatos
    })