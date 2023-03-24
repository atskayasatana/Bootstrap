import os.path
import json
import shutil

from jinja2 import Environment, FileSystemLoader, select_autoescape
from livereload import Server
from more_itertools import chunked
from pathlib import Path

PROJECT_DIRECTORY = os.getcwd()
MAX_BOOKS_CARDS_QTY_PER_PAGE = 20
JSON_FILE_PATH = os.path.join(PROJECT_DIRECTORY, 'Media', 'books.json')

def on_reload():

    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html'])
    )

    Path(os.path.join(PROJECT_DIRECTORY, 'pages')).mkdir(exist_ok=True)

    chunked_books_cards = list(chunked(books_cards, MAX_BOOKS_CARDS_QTY_PER_PAGE))

    pages_qty = len(chunked_books_cards)

    for page_num, chunk in enumerate(chunked_books_cards, 1):
        template = env.get_template('template.html')
        rendered_page = template.render(books_cards_on_page=list(chunked(chunk, (MAX_BOOKS_CARDS_QTY_PER_PAGE//2))),
                                        total_pages_qty=pages_qty,
                                        current_page_num=page_num,
                                        current_dir=Path(PROJECT_DIRECTORY))

        file_name = os.path.join('pages', f'index_{page_num}.html')
        with open(file_name, 'w', encoding='utf8') as file:
            file.write(rendered_page)

    shutil.copy('pages/index_1.html', os.path.join(PROJECT_DIRECTORY, 'index.html'))


if __name__ == '__main__':
    print(PROJECT_DIRECTORY)

    with open(JSON_FILE_PATH, 'r', encoding='CP1251') as books:
        books_cards = json.load(books)

    on_reload()
    server = Server()
    server.watch('template.html', on_reload)
    server.serve(root='.')
