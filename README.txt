ИНСТРУКЦИЯ ПО ЗАПУСКУ (bez.breda):
----------------------------------
1. Установите зависимости: 
   pip install -r requirements.txt

2. Подготовьте базу данных:
   python manage.py migrate

3. Создайте аккаунт администратора:
   python manage.py createsuperuser
   (используйте его для входа в http://127.0.0.1:8000/admin)

4. Запустите сервер:
   python manage.py runserver

5. Откройте сайт:
   http://127.0.0.1:8000/

Чтобы проекты появились на главной, зайдите в админку и добавьте их в разделе Agency -> Projects.