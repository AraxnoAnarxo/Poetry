# Poetry

Веб-сайт “MetaPoet”

Основная тема: применение инструментов backend-рарзаботки для освещения творчества поэта в сети Интернет.

Стек технологий:
- Язык программирования Python
- Фреймворк Django
- СУБД Postgresql
- модуль озвучивания текста gtts
- модуль морфологического анализа текста Pymorphy2
- модуль API Django REST framework
- Frontend - визуальное оформление: CSS-стили, html-страницы, js-скрипты. Реализована кнопка переключения цветовых тем (светлый/темный режим). На главной странице использован js-скрипт архимедовой спирали.

Карта сайта: 
- - Главная страница - "home" - название сайта, имя автора стихов
- - - Стихи - все стихотворения
- - - - Словарь - разбивка слов стиха по частям речи
- - - - - Один стих - анимация набора текста
- - - - Аудио - генерация аудио стиха
- - - - Изменить - изменить стих  (для admin)
- - - - Удалить - удалить стих (для admin)
- - - Содержание - поиск по названию или по первой строке;
- - - Аналитика - сервис, подсчитывающий кол-во слов всего, кол-во уникальных слов, топ-100 слов, топ-100 по частям речи - через форму checkbox (сущ, прил, глагол)
- - API - "API" - скачать все стихи автора, все теги
- - TOKEN - генерация токена для API, обновление токена (для зарегистрированного пользователя)
- - ADD - добавить стихотворение (для admin)
- - Auth - войти.
- - Register - зарегистрироваться.
- - Exit - выйти.

Схема сайта по ссылке:
<p align="center">
  <img src="https://raw.githubusercontent.com/tahoeivanova/diploma/master/Screen%20Shot%202020-06-04%20at%2017.17.01.png
" width="350" title="hover text">
</p>


https://github.com/tahoeivanova/diploma/blob/master/Screen%20Shot%202020-06-04%20at%2017.17.01.png?raw=true

Размещение проекта в сети Интернет:

- Web https://tranquil-refuge-12390.herokuapp.com/
- Docker-образ https://hub.docker.com/repository/docker/tahoeivanova/metapoet
- Docker-compose https://github.com/tahoeivanova/Poetry/blob/master/poetry/docker-compose.yml
- Git https://github.com/tahoeivanova/Poetry
