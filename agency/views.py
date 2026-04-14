from django.shortcuts import render
from django.http import HttpResponse
from .models import Project
import traceback
import logging

logger = logging.getLogger(__name__)

def index(request):
    try:
        logger.info("Starting index view")
        projects = Project.objects.all()
        logger.info(f"Retrieved {len(projects)} projects")
        return render(request, 'index.html', {'projects': projects})
    except Exception as e:
        logger.error(f"Error in index view: {e}")
        traceback.print_exc()
        return HttpResponse(f"Error: {str(e)}", status=500)