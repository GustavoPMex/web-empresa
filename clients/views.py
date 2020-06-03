from django.shortcuts import render
from .models import inoutiProjects, clientesImg

# Create your views here.

def clientes_view(request):
    projects = inoutiProjects.objects.all()
    clientes = clientesImg.objects.all()

    list_obj = {
        'projects':projects,
        'clientes':clientes
    }

    return render(request, 'clientes/clients.html', list_obj)
