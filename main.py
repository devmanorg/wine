from http.server import HTTPServer, SimpleHTTPRequestHandler
import datetime
import os
from jinja2 import Environment, FileSystemLoader, select_autoescape
import pandas
from collections import defaultdict

path = os.path.abspath(os.path.dirname(__file__))
os.chdir(path)

env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html', 'xml'])
)
template = env.get_template('template.html')
year_ago = datetime.datetime.now().year-datetime.datetime(year=1920,
                                                          month=1, day=1).year


def year_to_word(year: int):
    if 21 > year_ago % 100 >= 10 or 9 >= year_ago % 100 % 10 >= 5 or year_ago % 100 % 10 == 0:
        return "лет"
    if year_ago % 100 % 10 == 1:
        return "год"
    return "года"


def excel_to_dict_wines(template) -> defaultdict:
    excel_data_df = pandas.read_excel(
        template, keep_default_na=False, na_values='', na_filter=False)
    list_to = excel_data_df.to_dict(orient="records")
    dict_out = defaultdict(list)
    for dict_drink in list_to:
        dict_out[dict_drink["Категория"]].append(dict_drink)
    return dict_out


dict_wines = excel_to_dict_wines("wine3.xlsx")


rendered_page = template.render(
    year_now=year_ago,
    word=year_to_word(year_ago),
    dict_wines=dict_wines
)

with open('index.html', 'w', encoding="utf8") as file:
    file.write(rendered_page)

server = HTTPServer(('127.0.0.1', 8000), SimpleHTTPRequestHandler)
server.serve_forever()
