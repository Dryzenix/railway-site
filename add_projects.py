import os
import sys
import django

sys.path.insert(0, os.path.dirname(__file__))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bezbreda.settings')
django.setup()

from agency.models import Project

projects = [
    {
        'title': 'Smart-Admin for Marketing Agency',
        'description': 'Разработка кастомной панели управления с автоматическим парсингом лидов и аналитикой в реальном времени.',
        'tech_stack': 'Python, Django, PostgreSQL, Redis',
        'link': ''
    },
    {
        'title': 'Scale-Up E-commerce Engine',
        'description': 'Архитектура интернет-магазина, способная выдержать до 50,000 запросов в секунду без задержек.',
        'tech_stack': 'Django REST Framework, React, Docker',
        'link': ''
    },
    {
        'title': 'Neuro-Analytic Dashboard',
        'description': 'Интеграция API искусственного интеллекта для прогнозирования конверсии на основе поведения пользователей.',
        'tech_stack': 'Python, OpenAI API, Celery',
        'link': ''
    }
]

for proj in projects:
    if not Project.objects.filter(title=proj['title']).exists():
        Project.objects.create(**proj)
        print(f"Added project: {proj['title']}")
    else:
        print(f"Project already exists: {proj['title']}")