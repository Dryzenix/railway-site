# Railway Deployment Guide

Railway — отличная альтернатива Vercel для Django-приложений.

## Шаги развертывания:

1. **Создайте аккаунт на Railway** (railway.app)

2. **Подключите GitHub:**
   - В Railway нажмите "New Project"
   - Выберите "Deploy from GitHub repo"
   - Авторизуйтесь и выберите `Dryzenix/site`

3. **Настройка переменных окружения:**
   В Railway добавьте:
   - `SECRET_KEY`: `your-secret-key-here`
   - `DEBUG`: `False`
   - `ALLOWED_HOSTS`: `*`

4. **База данных:**
   Railway автоматически создаст PostgreSQL базу данных.
   Добавьте переменную:
   - `DATABASE_URL`: (Railway предоставит автоматически)

5. **Обновите settings.py для Railway:**

```python
import dj_database_url
import os

DATABASES = {
    'default': dj_database_url.config(
        default='sqlite:///db.sqlite3',
        conn_max_age=600,
        conn_health_checks=True,
    )
}
```

6. **Deploy:**
   Railway автоматически развернет при push на GitHub.

## Преимущества Railway:
- Полная поддержка Django
- PostgreSQL база данных
- Автоматическое масштабирование
- Бесплатный тариф до определенных лимитов

## URL после развертывания:
Railway предоставит URL типа: `https://site-production.up.railway.app/`

Админка: `https://site-production.up.railway.app/admin/`

## Локальная проверка:
```bash
pip install dj-database-url psycopg2-binary
python manage.py migrate
python manage.py runserver
```