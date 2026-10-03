from django.shortcuts import render
from . import models #import all tables from models. The period indicates the current app.
#from .models import Projects, Skills #import specific tables 

def projects_view(request):
    projects_list = models.Projects.objects.all().order_by('-year')
    
    context = {
        'projects': projects_list
    }
    
    return render(request, 'projects/projects.html', context)

