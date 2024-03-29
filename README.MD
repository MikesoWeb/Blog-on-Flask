Приветствую, друзья. Меня зовут **_Михаил Терехов_** и я начинающий **разработчик
на замечательном Python**

На данном этапе я создаю **свой блог с нуля на Python**, используя **веб-фреймворк flask**

У меня есть своя [группа ВК](https://vk.com/python_for_me), где я публикую свои мнения,
куски кода, чего достиг на данном этапе

У меня есть свой [Youtube канал ](https://www.youtube.com/channel/UCLr7DxWBT0NWZv_w4uvLJaw),
посвященный **Python**, где я создаю различные программы, 
а так же уроки по рабочему окружению и инструментарию, который используется при разработке.
В основном на канале ролики посвящены **flask**

[Блог](http://mikedoit.pythonanywhere.com/) по разработке которого ведутся данные уроки
Функционал не полный и конечно же будут вноситься правки. Можете зарегистрироваться и поюзать блог.


На ютуб канале в плейлисте 
[Flask blog (full course) / Полный курс по созданию блога на веб фреймворке flask ](https://www.youtube.com/watch?v=dAfYYhC0RFQ&list=PLq89pZIwXSou6UxWQahrfRUGYpta43md4),
я с нуля начинаю создавать блог на flask и весь плейлист посвящен разработке блога постепенно усложняя и расширяя его

    использованы модули:

        flask
        flask-admin
        flask-slugify
        flask-wtf
        flask-login
        flask-sqlalchemy
        flask-bcrypt
        python-dotenv
        email-validator
        ...


В файле requirements.txt находятся зависимости проекта. 
Установка зависимостей:
    
    pip install -r requirements.txt


Создать файл .env в корне папки blog и записать туда переменные окружения

- FLASK_ENV=development
- FLASK_APP=run.py
- SQLALCHEMY_DATABASE_URI=sqlite:///blog.db
- SQLALCHEMY_TRACK_MODIFICATIONS=True
- EMAIL_USER=YOUR_MAIL
- EMAIL_PASS=YOUR_PASS


Для запуска проекта используется файл

    run.py

Или на windows запускаем run
Или на linux запускаем run

Но тогда нужно сначлала создать базу данных с таблицами!



Михаил Терехов, 2021 год
