# Установка

## Установка python

Мы используем `python 3.13.x`

### Debian-подобные системы

Скопируй в консоль:

```sh
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt-get update
sudo apt-get install python3.13
sudo apt-get install python3-pip
sudo apt-get install python3.13-venv
```

### Windows

Скачай `python 3.13` [отсюда](https://www.python.org/downloads/) и установи его

Зайди в переменные среды windows`

## Создание виртуальной среды

В корне репозитория, запусти команду

На Unix:

```sh
python3.13 -m venv .venv
.venv/scripts/activate
```

На windows

```cmd
"C:\Program Files\Python313\python.exe" -m venv .venv
```

> [!TIP]
> Если python 3.13 у тебя не в `C:\Program Files\Python313`, то пиши другой путь к `exe` файлу.
> Например, `C:\Users\lesar\AppData\Local\Programs\Python313` при установке только данному пользователю

> [!TIP]
> В `vs code` в консоли перед строкой ввода должен появиться текст `(.venv)`,
> а при открытии файла `src/main.py` справа снизу появится кнопка `3.13 ('.venv': venv)`.
> Если там другая версия питона, нажми на нее и выбери ту, где написано `venv`

## Установка библиотек

Просто запусти команду из корня репозитория

```sh
pip install -r requirements.txt
```

## .env файл

1. Скопируй `example.env` в `.env`

2. Замени `token_123` на свой токен бота

## Запуск бота

В корне репозитория запусти команду

```sh
python3 src/main.py
```
