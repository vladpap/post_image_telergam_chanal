# Скрипт отправки фото в телеграм канал
Отправляет фото или директорию через заданное время.
Вспомогательные скрипты закачки фотографий NASA .


## Установка

Python3 должен быть уже установлен.
Используйте `pip` (или `pip3`, если есть конфликт с Python2) для установки зависимостей
```
pip install -r requirements.txt
```
* в переменную окружения `NASA_API_KEY` записать API ключ NASA
* в переменную окружения `TOKEN_BOT_TELEGRAM` записать TOKEN бота телеграм
* в переменную окружения `CHAT_ID_TELEGRAM` записать ID или имя телеграм канала ключ NASA
* в переменную окружения `TIME_OF_POST` записать время (в секундах) между постами

Все фотографии храняться в директории `images/`.

Рекомендуется использовать среду окружения [venv](https://docs.python.org/3/library/venv.html) для изоляции проекта.


## Использование
### Скрипт fetch_spacex_images
```console
$ python fetch_spacex_images.py

$ python fetch_spacex_images.py [id_launch]
```
Скачивает последние фотографии запуска ракет компании Илона Маска или по заданному id.


### Скрипт fetch_nasa_photos
```console
$ python fetch_nasa_photos.py

$ python fetch_nasa_photos.py [count_images]
```
Скачивает 30 фотографии из [Astronomy Picture of the Day](https://api.nasa.gov/) или заданное количество.


### Скрипт fetch_epic_photo
```console
$ python fetch_epic_photo.py
```
Скачивает случайную фотографию земли [Earth Polychromatic Imaging Camera](https://api.nasa.gov/) запуска ракет компании Илона Маска или по заданному id.


### Скрипт fetch_images
```console
$ python fetch_images.py
```
Запускает 3 скрипта (fetch_spacex_images, fetch_nasa_photos, fetch_epic_photo).


### Скрипт send_photo_telegram
```console
$ python send_photo_telegram.py

$ python3 send_photo_telegram.py images/nasa_apod_25.jpg
```
Публикует в случайном порядке все фотографии из директории `images/` раз в заданный промежуток времени (переменная окружения `TIME_OF_POST`).
Если вдруг все фото из директории опубликованы – он просто начинает публиковать их заново.

При заданном аргументе загружает только указанную фотографию.


## Цель проекта

Код написан в образовательных целях на онлайн-курсу для веб-разработчиков [dvmn.org](https://dvmn.org/)