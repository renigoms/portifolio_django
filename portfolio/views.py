from django.db.models import QuerySet
from django.shortcuts import render

from core.models import Profile
from portfolio.models import Certificate, Project


# Create your views here.
def home(request):
    profile: Profile|None = Profile.objects.all().first()
    certificates: QuerySet[Certificate] = Certificate.objects.all()
    return render(request, 'portfolio/home.html', {'profile': profile, 'certificates': certificates})

def projetos(request):
    projects: QuerySet[Project] = Project.objects.all()
    return render(request, 'portfolio/projetos.html', {'projects': projects})
