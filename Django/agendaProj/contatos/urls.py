from django.urls import  path
from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path("busca/", views.busca, name='busca'),
    path("<int:id>", views.ver_contato, name='ver_contato'),
]