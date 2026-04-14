from django.shortcuts import render
from django.http import HttpResponse
from .models import Project
import traceback

def index(request):
    try:
        projects = Project.objects.all()
        return render(request, 'index.html', {'projects': projects})
    except Exception as e:
        traceback.print_exc()
        return HttpResponse(f"Error: {str(e)}", status=500)