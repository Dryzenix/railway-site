from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from agency.views import index

def health(request):
    return HttpResponse("OK", status=200)

urlpatterns = [
    path('health/', health, name='health'),
    path('admin/', admin.site.urls),
    path('', index, name='index'),
]