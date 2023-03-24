# Верстка с использованием библиотеки Bootstrap

Сайт со скачанными с https://tululu.org/ книгами. 

Онлайн-версия на [GitHubPages](https://atskayasatana.github.io/Bootstrap/)

![Главная страница](https://github.com/atskayasatana/Images/blob/2cfd674f0a0aa11116bb7cae8162dbbd910e1c1a/5/index.png)

Чтобы открыть текстовую версию книги нужно кликнуть на "Читать":

![Читать](https://github.com/atskayasatana/Images/blob/main/book_example.png)

## Запуск

Для запуска проекта нужен Python версии 3 и выше. В файле requirements.txt указан список библиотек, необходимых для корректной работы. После распаковки архива необходимо будет установить зависимости из данного файла.

```
pip install -r requirements.txt
```

После установки библиотек можно запустить сайт локально

```
python render_website.py

```

Сайт с книгами будет здесь: http://127.0.0.1:5500/


## Оффлайн версия

После запуска скрипта в директории проекта появится папка pages с файлами index_<номер страницы>:

![pages](https://github.com/atskayasatana/Images/blob/2cfd674f0a0aa11116bb7cae8162dbbd910e1c1a/5/pages_dir.png)

Можно открыт любой из файлов с помощью браузера (Edge, Firefox, Chrome) и попасть на одну из страниц библиотеки. 

На скрине ниже файл index_2.html:

![index_2](https://github.com/atskayasatana/Images/blob/2cfd674f0a0aa11116bb7cae8162dbbd910e1c1a/5/page_example.png)

Между страницами можно переходить с помощью "Вперед"/"Назад" или просто выбрав страницу.









