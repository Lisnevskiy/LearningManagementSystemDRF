# LMS-система для онлайн-обучения

Этот проект представляет собой LMS (систему управления обучением), 
которая позволяет пользователям создавать 
и размещать свои полезные материалы и курсы для онлайн-обучения. 
LMS-система разработана с использованием SPA (Single Page Application) архитектуры 
и возвращает JSON-структуры в качестве результатов запросов к бэкенд-серверу.

## Установка и запуск

- Клонируйте репозиторий на вашем компьютере:
`git clone https://github.com/Lisnevskiy/MailingManagementService.git`
- Установите зависимости:
`pip install -r requirements.txt`
- Необходимые примеры переменных окружения указаны в файле [.env.sample](.env.sample)
- Выполните миграции базы данных:
`python manage.py migrate`
- Создайте суперпользователя `python manage.py create_sup_us`
- Наполение БД с помощью фикстур: `python manage.py loaddata data.json`
- Запустите докер:
`docker compose build`
`docker compose up`
