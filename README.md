# Homework 57 — Issue Tracker

## Установка и запуск (Windows CMD)

```cmd
cd C:\Users\tukuv\Desktop\homework_57\source
py -m venv venv
venv\Scripts\activate
py -m pip install -r ..\requirements.txt
py manage.py migrate
py manage.py loaddata initial_data
py manage.py runserver
```

Откройте http://127.0.0.1:8000/

## Админ-панель

Адрес: http://127.0.0.1:8000/admin/

Тестовый суперпользователь из фикстуры:
- Логин: `admin57`
- Пароль: `Admin57!ChangeMe`

Это учебные данные. После первого входа смените пароль.

## Этапы задания

- Этап 1: модели задач, статусов и типов; миграции; админка; фикстура.
- Этап 2: CRUD на `TemplateView`/`View`, формы Django, `ModelChoiceField`; состояние до перехода на M2M сохранено в миграциях.
- Этап 3: типы задачи переведены на `ManyToManyField`; CRUD использует `ModelMultipleChoiceField` и `CheckboxSelectMultiple`.
- Бонус по миграции: миграции `0002`–`0005` создают новое поле, переносят данные и удаляют старое поле в отдельных шагах.

## Git

В архиве сохранена история из пяти осмысленных коммитов на английском языке.
