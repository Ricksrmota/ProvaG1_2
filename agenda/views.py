from django.shortcuts import render
from agenda.models import Agenda
from agenda.models import UsuarioAgenda
from django.http import HttpResponse
from rest_framework import routers, serializers, viewsets
from django.contrib.auth.models import User
from agenda.serializers import UserSerializer
from django.conf.urls import url

from rest_framework import viewsets
from django.contrib.auth.models import User
from agenda.serializers import UserSerializer
from agenda.serializers import AgendaSerializer
from agenda.serializers import UsuarioSerializer
from agenda.models import Usuario

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer

class AgendaViewSet(viewsets.ModelViewSet):
    queryset = Agenda.objects.all()
    serializer_class = AgendaSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer


	queryset = User.objects.all()
	serializer_class = UserSerializer



def listaAgenda(request):
    retorno = "<h1>Agendas</h1>"
    lista = Agenda.objects.all()
    for agenda in lista:
        retorno += '</br>Compromisso: {}</br>'.format(agenda.descricao) + '{}'.format(agenda.compromisso)
    return HttpResponse(retorno)

def listaAgendaFeriados(request):
    retorno = "<h1>Feriados</h1>"
    lista = Agenda.objects.all()
    for agenda in lista:
        if agenda.institucional == True:
            retorno += '</br>Data do Feriado: {}</br>'.format(agenda.compromisso) + '{}'.format(agenda.descricao)
    return HttpResponse(retorno)

def get_evento_byID(request,id):
    retorno = "<h1>Compromissos</h1>"
    agenda = UsuarioAgenda.objects.get(pk=id)
    retorno += '</br>Nome do Compromisso: {}</br>'.format(agenda.nome)
    return HttpResponse(retorno)

