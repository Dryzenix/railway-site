# Развертывание на Vercel

## Шаги:

1. **Создайте аккаунт на Vercel** (vercel.com) и подключите GitHub.

2. **Импортируйте репозиторий:**
   - В Vercel нажмите "New Project"
   - Выберите ваш GitHub репозиторий
   - Настройте проект:
     - **Framework Preset:** Other
     - **Root Directory:** ./
     - **Build Command:** (оставьте пустым)
     - **Output Directory:** (оставьте пустым)

3. **Environment Variables:**
   Добавьте в Vercel:
   - `SECRET_KEY`: ваш секретный ключ Django
   - `DEBUG`: false

4. **Deploy:**
   Нажмите "Deploy" — Vercel автоматически развернет сайт.

## Особенности:
- Используется in-memory SQLite база данных
- Сайт будет доступен по URL от Vercel
- Админка: `https://your-vercel-url.vercel.app/admin/`

## Локальная проверка:
```bash
pip install -r requirements.txt
python manage.py runserver
```

## Примечание:
Vercel лучше подходит для статических сайтов, но Django может работать через serverless functions. Для production рассмотрите Heroku или Railway.