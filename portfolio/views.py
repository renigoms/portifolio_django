from django.contrib import messages
from django.db.models import QuerySet
from django.http import HttpResponse
from django.shortcuts import render

from core.models import Profile
from portfolio.form import ContactForm
from portfolio.models import Certificate, Project


# Create your views here.
def home(request):
    profile: Profile|None = Profile.objects.all().first()
    certificates: QuerySet[Certificate] = Certificate.objects.all()
    return render(request, 'portfolio/home.html', {'profile': profile, 'certificates': certificates})

def projetos(request):
    projects: QuerySet[Project] = Project.objects.all()
    return render(request, 'portfolio/projetos.html',
                  {'projects': projects, 'ProjectType': Project.ProjectTypeChoice})

def contato(request):
    form = ContactForm(request.POST or None)
    if str(request.method) == 'POST':
        if form.is_valid():
            form.send_email()
            # Isso é o que vai fazer o {% bootstrap_messages %} funcionar
            messages.success(request, 'E-mail enviado com sucesso!')
            # form = ContactForm(request.POST or None)
            form = ContactForm()
        else:
            messages.error(request, 'Erro ao enviar a mensagem!')
    return render(request,
                  'portfolio/contato.html',
                  {'form': form})
