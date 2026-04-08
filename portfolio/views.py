from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'portfolio/home.html')

def projetos(request):
    return render(request, 'portfolio/projetos.html')