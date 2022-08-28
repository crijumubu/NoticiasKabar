# Importacion de bibliotecas y paquetes necesarios para el correcto funcionamiento del spyder

from bs4 import BeautifulSoup
import requests
import news as ns

# Lista de objetos de la clase noticias

listNews = list()

# Diccionario de noticias el cual contiene los enlaces y la categoria de la misma

newsLinkDictionary = dict()

# Metodo principal el cual obtiene toda la informacion relacionada a las noticias y retorna una lista con las mismas

def extractMain():
    
    # Definicion y preparacion del enlace a consultar

    url = 'https://www.portafolio.co/'
    page = requests.get(url)

    soup = BeautifulSoup(page.content, 'html.parser')
    
    # Obtencion de los articulos que se encuentran dentro del panel principal del portal
    
    articles = soup.find('div', class_='secondary-board modules').find_all('article')
    # Definicion del diccionario que contiene los enlaces de las respectivas noticias junto con su categoria
    
    global newsLinkDictionary
    
    # Extraccion de la categoria junto con el enlace de la noticias
    
    extractNewsInitialInformation(url, articles)
    
    # Recorrido o barrido de cada una de las noticias que se encontraron en el panel principal 
    
    for newsLink in newsLinkDictionary:
        
        # Acceso a la categoria de la noticias a traves de la llave del diccionario
        
        category = newsLinkDictionary[newsLink]
        
        # Extraccion del titulo, descripcion e imagen de la noticia
        
        title, description, image = extractInformation(url, newsLink)
        
        # Insercion de la noticia a la lista de las noticias
        
        listNews.append(ns.news(newsLink, category, title, description, image))
        
    return listNews

# Metodo el cual extrae el enlace y la categoria de las noticias 

def extractNewsInitialInformation(url, articles):
    
    # Recorrido o barrido de cada uno de los articulos que se extrajeron del panel principal
    
    for article in articles:
        
        # Definicion de variables
        
        articleLink = ''
        articleCategory = ''
        
        # Extraccion de la categoria y el enlace de la noticia
        
        articleCategory = article.find('div').a.text
        articleLink = url + article.h3.a['href']

        # Insercion del enlace de la noticia junto con la categoria de la misma al diccionario definido
        
        newsLinkDictionary[articleLink] = articleCategory

# Metodo el cual extrae el titulo, la descripcion y la imagen de las noticias        

def extractInformation(url, newsLink):
    
    # Definicion de variables
    
    title = ''
    image = ''
    description = ''
    
    # Preparacion del enlace a consultar
    
    page = requests.get(newsLink)

    soup = BeautifulSoup(page.content, 'html.parser')
    
    # Obtencion del div que contiene la informacion que se desea extraer
    
    articlesContainer1 = soup.find('div', class_='content_grid_articulos')
    articlesContainer2 = soup.find('div', class_='content_grid_especiales cabezote-scroll-infinito')
    
    # Obtencion del titulo, descripcion e imagen de la noticia
    
    title = articlesContainer2.h1.text
    description = articlesContainer2.find('p',class_='epigraph regular_lead1').text
    imagediv = articlesContainer1.find('div',class_='captioned-image')
    image = imagediv.img['src']
    
    image = url + image
    # Retorno del titulo, descripcion e imagen de la noticia
    
    return title, description, image
