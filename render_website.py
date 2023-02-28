import json
import jinja2

from jinja2 import Environment, FileSystemLoader, select_autoescape
from http.server import HTTPServer, SimpleHTTPRequestHandler

if __name__ == '__main__':
    with open(r"D:\Bootstrap\Downloads\books.json", "r") as books:
        books_info = json.load(books)

    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html'])
    )

    template = env.get_template("template.html")
    rendered_page = template.render(books=books_info)

    with open("index.html", "w", encoding='utf8') as file:
        file.write(rendered_page)

    server = HTTPServer(('0.0.0.0',8000), SimpleHTTPRequestHandler)
    server.serve_forever()





