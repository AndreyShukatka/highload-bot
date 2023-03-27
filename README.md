# Ответы на вопросы задания

> Что значит `[::1]` в `ALLOWED_HOSTS`?
>> Используется для `IPv6` в качестве локального хоста. Альтернатива `127.0.0.1` в `IPv4`

> Что такое settings.MIDDLEWARE.
>> Строка, которая помогает обмену запросами

> что делает вот этот код? `'debug_toolbar.middleware.DebugToolbarMiddleware'`
>> Включает обмен запросами и информацией для `DebugToolbar`

> Что такое `bot_state`? Какие значения у него бывают? Зачем это нужно?
>> Записывает текущее положение, в котором находится пользователь.
> > Его состояния:
>> - `START`
>>- `HANDLE_AUTH`
>>- `HANDLE_SELECTIONS`
>> - `HANDLE_POLL`
>> - `HANDLE_REBUS`

> Что такое `DrawQuerySet`? Как вызвать методы оттуда?
>> Это класс модели, который создаётся за счет наследования от `models.QuerySet`, в данном коде используется как
> > менеджер
> > для классса `Draw`, выдаеёт и фильтрует следующие значения для бота:
>> - текущий розыгрыш
>> - Будущий розыгрыш
     > > Вызывается через модель `Draw`, например `Draw.objects.get_draw`

> Как работает `get_draw`?
>> Вызывается через модель `Draw`, получается текущий розыгрыш, если розыгрыш найден, то возвращает первое значение
> > розыгрыша, если нет, то возвращает будущий розыгрыш.

> Что такое `PlayerResources`?
>> Это класс в административной панели, наследующийся от `resources.ModelResource`, который необходим для подключения
> > поискового поля и выгрузки отчётов

> Что такое DrawFilter?
>> Это класс в административной панели, наследуется от `admin.SimpleListFilter`, который необходим для фильтрации по розыграшам.
>> - Текущие розыгрыши
>> - Будущие розыгрыши
>> - Прошедшие розыгрыши

# Highload Bot

Техническое задание читать [здесь](https://gist.github.com/dvmn-tasks/7e002681fd9dc0f0da5c1907b240c053).

Сценарии использования админки [здесь](https://gist.github.com/dvmn-tasks/3555fc35ba12929d564a708fa6374208).

## Переменные окружения

Все настройки, кроме отмеченных звёздочкой `*` необязательные. На localhost в отладочном режиме сайт можно запустить
почти без настроек.

\*`TELEGRAM_ACCESS_TOKEN` — токен бота;

`DEBUG` — режим отладки, по дефолту `False`

`INTERNAL_IPS` - хост для Django Debug Toolbar

`SECRET_KEY` — секретный ключ `Django`

`DATABASE_URL` — адрес базы данных. [Формат записи](https://github.com/jacobian/dj-database-url).

`ALLOWED_HOSTS` — один или несколько хостов, разделённых
запятой. [Документация](https://docs.djangoproject.com/en/3.1/ref/settings/#allowed-hosts).

`ROLLBAR_TOKEN` — токен к [rollbar.com](https://rollbar.com/).

`ROLLBAR_ENVIRONMENT` — на production-сервере выставлено в `production`.

`S3_ACCESS_KEY_ID` — переключает Django на использовать S3 хранилища медиа-файлов. В названии
настройки [Документация](https://django-storages.readthedocs.io/en/latest/backends/digital-ocean-spaces.html).

`S3_SECRET_ACCESS_KEY` — секретный ключ к хранилищу S3 (если используется)
. [Документация](https://django-storages.readthedocs.io/en/latest/backends/digital-ocean-spaces.html).

`S3_*` — множество прочих необязательных "тонких" настроек хранилища S3. См. файл settings.py.

`MAX_PUZZLES_TO_WIN` - количество ребусов, которые необходимо решить для участия в розыгрыше.

## Как установить dev-версию

Скачай репозиторий:

```sh
$ git clone https://github.com/LevelUp-developers/highload-bot.git
```

Перейжи в репозиторий, установи библиотеки и зависимости:

```sh
$ cd highload-bot
$ pip3 install -r requirements.txt
```

Накати миграцию:

```sh
$ python3 manage.py migrate
```

Запусти сервер:

```sh
$ python3 manage.py runserver
```

## Как попасть в админку

Создай нового пользователя с правами админа:

```sh
$ python3 manage.py createsuperuser
```

Запусти сервер:

```sh
$ python3 manage.py runserver
```

Перейдите по ссылке в [127.0.0.1:8000/admin](http://127.0.0.1:8000/admin).

## Как запустить Telegram-бота

Выполни команду:

```bash
$ python3 manage.py start_bot
```
