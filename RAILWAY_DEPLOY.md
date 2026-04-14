# Railway Deployment Guide

Railway — отличная альтернатива Vercel для Django-приложений.

## Шаги развертывания:

1. **Создайте аккаунт на Railway** (railway.app)

2. **Подключите GitHub:**
   - В Railway нажмите "New Project"
   - Выберите "Deploy from GitHub repo"
   - Авторизуйтесь и выберите `Dryzenix/railway-site`

3. **Настройка переменных окружения:**
   В Railway добавьте:
   - `SECRET_KEY`: `your-unique-secret-key`
   - `DEBUG`: `False`
   - `ALLOWED_HOSTS`: `railway-site-production.up.railway.app`
   - `RAILWAY_START_COMMAND`: `./start.sh`

4. **Railway автоматически создаст PostgreSQL базу данных**

5. **Deploy:**
   Railway автоматически развернет при push на GitHub.

## Преимущества Railway:
- Полная поддержка Django
- PostgreSQL база данных
- Автоматическое масштабирование
- Бесплатный тариф до определенных лимитов

## URL после развертывания:
Railway предоставит URL типа: `https://railway-site-production.up.railway.app/`

Админка: `https://railway-site-production.up.railway.app/admin/`

## Локальная проверка:
```bash
pip install dj-database-url psycopg2-binary
python manage.py migrate
python manage.py runserver
```
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