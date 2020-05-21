# Poetry

Сайт со стихотворениями Клары Емельяновой.

В качестве тестирования и отладки работы сайта в базу данных были пропарсены стихи следующих поэтов:
-Пушкин
-Лермонтов
-Ахмадулина

Общие сведения о проекте: Сайт предназначен для чтения, анализа, а также прослушивания стихов.

Цели: совместить поэзию и аналитические инструменты для анализа текста, а также озвучивание текста с помощью синтеза речи gtts.

Задачи:

+сделать удобным анализ творчества поэта:
++подсчет количества слов
++количество уникальных слов
++топ-100 слов
++словарь стихотворения
++вывод топ-100 слов по частям речи (опции: существительное, прилагательное, глагол);
+сделать удобным раздел для автора (чтобы автор мог добавлять свой материал);
+сделать интересным ознакомление пользователя с поэзией, как-то: озвучить текст стихотворений с помощью модуля синтеза речи;


Аудитория приложения: Люди, проявляющие интерес к поэзии, школьники, филологи.

Карта сайта:
- Главная страница - "Home" - название сайта, имя авторов стихов; разделы: Стихи, Содержание, Аналитика.
  - Стихотворения - "Poems" - выводит все стихотворения;
  - Содержание - "Contents" - поиск по названию, в стихах без названия (* * *) - по первой строке;
  - Аналитика - Поэтический анализатор: - "Meta" - подсчитвает кол-во слов всего, кол-во уникальных слов, топ-100 слов, топ-100 по частям речи (сущ, прил, глагол) - для выбора параметров реализован checkbox.
- Содержание - "Contents" - поиск стихов по сайту (общий);
- Стихотворение (одно):
  -Название, Текст стихотвоерния;
  -Словарь стиха.
  -Аудио
- API - "API" - все стихи автора, все теги;
- TOKEN - для зарегистрированного пользователя возможна генерация токена для API, обновление токена.
- Тест-драйв - стихи других поэтов:
  - Страница с изображением поэта: разделы: Стихи, Содержание, Аналитика.
- API Тест-драйв(список поэтов, стихи авторов)
- Добавить стихотворение - "Add poem" - для админа ( добавить: название, текст, год, первая строка, выбрать тег, выбрать поэта).
- Auth - войти.
- Register - зарегистрироваться.
- Exit - выйти.


Добавлена пагинация.

Реализована кнопка переключения цветовых тем (светлый/темный режим).

Для superuser возможно добавление, изменение и удаление стиха.


