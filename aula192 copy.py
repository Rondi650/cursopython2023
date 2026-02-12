# + Web Scraping com Python usando requests e bs4 BeautifulSoup
# - Web Scraping é o ato de "raspar a web" buscando informações de forma
# automatizada, com determinada linguagem de programação, para uso posterior.
# - O módulo requests consegue carregar dados da Internet para dentro do seu
# código. Já o bs4.BeautifulSoup é responsável por interpretar os dados HTML
# em formato de objetos Python para facilitar a vida do desenvolvedor.
# - Doc: https://www.crummy.com/software/BeautifulSoup/bs4/doc.ptbr/
# + Instalação
# - pip install requests types-requests bs4

import os
import json
from datetime import datetime

os.system('cls')

import requests
from bs4 import BeautifulSoup

url = 'https://g1.globo.com/'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser', from_encoding='utf8')

noticias = soup.find_all('a', class_='feed-post-link')

data = datetime.now()
data_string = data.strftime('%d/%m/%Y %H:%M:%S')

lista = []
for n in noticias:
    titulo = n.get_text()
    link = n.get('href')
    hora = data_string
    lista.append({"noticia": titulo, "link": link, "hora":hora})
    
print(json.dumps(lista, ensure_ascii=False, indent=2))

with open('noticias.json','w', encoding='utf8') as file:
    json.dump(lista, file, ensure_ascii=False, indent=2)
 