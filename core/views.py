from django.shortcuts import render,redirect
from core.models import Evento

# Create your views here.
def index(request):
    return redirect ('/agenda/')

def lista_eventos(request):
    #resque.user verifica quem é o usuário
    #usuario = request.user
    evento = Evento.objects.all()
    dados = {'eventos':evento}
    return render(request, 'agenda.html', dados)