# Importacion de bibliotecas y paquetes necesarios para el correcto funcionamiento del spyder

from bs4 import BeautifulSoup
import requests
import news as ns

# Definicion y preparacion del enlace a consultar

url = 'https://www.eltiempo.com/'
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

articlesContainer = soup.find_all('article', class_='image-left')

# Lista de objetos de la clase noticias

listNews = list()

# Obtencion de la informacion relacionadas a las noticias junto con la creacion y almacenamientno de los objetos de la clase noticias en la lista

for article in articlesContainer:

    articleDetails = article.find('div', class_ ='article-details')

    category = articleDetails.find('div', class_ ='category-published').a.text
    title = articleDetails.h3.find('a', class_='title page-link').text
    link = url + articleDetails.h3.find('a', class_='multimediatag page-link')['href']
    description = ''

    # Si no encuentra una descripcion para la noticias procede a agregarla a la lista asi sin descripcion

    try:
        description = articleDetails.find('div', class_ ='epigraph-container').a.text
    except:
        pass
    
    # Por el momento se agrega a la lista sin una imagen

    listNews.append(ns.news(category, title, description, link))

# Visualizacion de las noticias obtenidas

cont = 1
for obj in listNews:
    print(f'Noticia {cont}\n{obj.toString()}\n')
    cont += 1