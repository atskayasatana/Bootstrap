import bottle
import json
import jinja2
import livereload


from jinja2 import Environment, FileSystemLoader, select_autoescape
from http.server import HTTPServer, SimpleHTTPRequestHandler
from livereload import Server, shell
from more_itertools import chunked


def on_reload():

    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html'])
    )

    template = env.get_template("template.html")
    rendered_page = template.render(books=list(chunked(books_info, 50)))

    with open("index.html", "w", encoding='utf8') as file:
        file.write(rendered_page)


if __name__ == '__main__':

    with open(r"D:\Bootstrap\Downloads\books.json", "r") as books:
        books_info = json.load(books)

    on_reload()
    print(len(books_info))
    b1 = list(chunked(books_info, 50))
    print(len(b1[0]))

    server = Server()
    server.watch('template.html', on_reload)
    server.serve(root='.')




