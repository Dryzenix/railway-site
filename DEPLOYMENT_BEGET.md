# Инструкция по развертыванию на Beget

## 1. Подготовка проекта
✅ Проект готов к развертыванию.

## 2. Загрузка на Beget

### Шаг 1: Создание Python-приложения
1. В панели Beget найди раздел **Python**
2. Выбери версию Python 3.10 или выше
3. Введи имя приложения: `bezbreda`
4. Выбери свой домен
5. Нажми **Создать**

### Шаг 2: Загрузка файлов
1. Перейди в **Менеджер файлов**
2. Найди папку приложения (обычно `public_html/bezbreda/`)
3. Удали стандартные файлы Beget
4. Загрузи архив проекта и распакуй его
5. Убедись, что `manage.py` в корне папки

### Шаг 3: Настройка WSGI
- Файл `passenger_wsgi.py` уже создан и готов к использованию
- Beget обычно автоматически его находит

### Шаг 4: Установка зависимостей
В разделе **Python → Управление модулями (Pip)** установи:
- `django`

### Шаг 5: Миграции и статика
Используя **Терминал** в панели Beget:

```bash
cd ~/bezbreda/public_html/bezbreda
source .venv/bin/activate  # Активация виртуального окружения
python manage.py migrate
python manage.py collectstatic --noinput
python manage.py createsuperuser  # Создай администратора
```

## Важно!
- **DEBUG = False** — уже установлено в settings.py
- При ошибках на сайте проверь логи в панели Beget
- Убедись, что база данных (db.sqlite3) находится в корне проекта
- Статика должна быть в папке `static/`

## Файлы проекта
```
bezbreda/
├── manage.py              # Главный скрипт Django
├── passenger_wsgi.py      # Для запуска на хостинге
├── requirements.txt       # Зависимости
├── bezbreda/
│   ├── settings.py        # Настройки (DEBUG=False)
│   ├── urls.py
│   ├── wsgi.py
│   └── __init__.py
├── agency/                # Приложение
│   ├── models.py
│   ├── views.py
│   ├── admin.py
│   └── ...
├── templates/
│   └── index.html         # 3D-сайт с Three.js
└── static/
    └── css/
        └── style.css
```

## Контакты для поддержки Beget
- Сайт: beget.com
- Служба поддержки работает 24/7
