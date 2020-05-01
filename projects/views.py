from django.shortcuts import render

from .models import *

def dashboard(request):

    project_list = Project.objects.all()

    context = {
        'project_list': project_list,
    }

    return render(request, 'projects/dashboard.html', context)
