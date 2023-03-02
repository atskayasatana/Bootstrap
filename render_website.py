import os.path

import bottle
import json
import jinja2
import livereload


from jinja2 import Environment, FileSystemLoader, select_autoescape
from http.server import HTTPServer, SimpleHTTPRequestHandler
from livereload import Server, shell
from more_itertools import chunked
from pathlib import Path


def on_reload():

    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html'])
    )

    current_dir = os.path.dirname(os.path.realpath(__file__))
    Path(os.path.join(current_dir, 'pages')).mkdir(exist_ok=True)

    chunked_books = list(chunked(books_info, 10))

    pages_qty = len(chunked_books)

    for i, chunk in enumerate(chunked_books, 1):
        template = env.get_template("template.html")
        rendered_page = template.render(books=chunk,
                                        total_pages_qty=pages_qty,
                                        current_page_num=i)
        file_name = os.path.join("pages", f'index_{i}.html')
        with open(file_name, "w", encoding='utf8') as file:
            file.write(rendered_page)


if __name__ == '__main__':

    with open(r"D:\Bootstrap\Downloads\books.json", "r") as books:
        books_info = json.load(books)

    on_reload()
    print(len(books_info))
    b1 = list(chunked(books_info, 10))
    print(len(b1))

    server = Server()
    server.watch('template.html', on_reload)
    server.serve(root='.')




