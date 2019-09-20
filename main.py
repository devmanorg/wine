from jinja2 import Environment, FileSystemLoader, select_autoescape
from http.server import HTTPServer, SimpleHTTPRequestHandler


env = Environment(
    loader=FileSystemLoader(''),
    autoescape=select_autoescape(['html', 'xml'])
)

template = env.get_template('index.html')

html = template.render()

with open('index.html', 'w') as file:
    file.write(html)


server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
server.serve_forever()
