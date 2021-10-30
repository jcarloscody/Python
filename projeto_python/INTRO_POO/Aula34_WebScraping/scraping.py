"""
INSTALAÇÃO DE MODULOS

pip install requests       OU    //o request vai fazer a requisição, vai baixar o html,
pipenv install requests

pipenv install beautifulsoup4      //vai permitir que a gente manipule o html
"""

import requests
from bs4 import BeautifulSoup

url = 'https://pt.stackoverflow.com/questions/tagged/python'
response = requests.get(url)   #aqui o requests está pegando a url, porém ele tbm faz post
html = BeautifulSoup(response.text, 'html.parser')

for pergunta in html.select('.question-summary'):
    titulo = pergunta.select_one('.question-hyperlink')
    data = pergunta.select_one('.relativetime')
    votos = pergunta.select_one('.vote-count-post')

    print(data.text, titulo.text, votos.text, sep='\t')
