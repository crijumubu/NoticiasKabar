# Importacion de bibliotecas y paquetes necesarios para el correcto funcionamiento del spyder

from bs4 import BeautifulSoup
import requests
import news as ns

# Lista de objetos de la clase noticias

listNews = list()

# Diccionario de noticias el cual contiene los enlaces y la categoria de la misma

newsLinkDictionary = dict()

# Obtencion de la informacion relacionadas a las noticias junto con la creacion y almacenamientno de los objetos de la clase noticias en la lista

def extractMain():
    
    # Definicion y preparacion del enlace a consultar

    url = 'https://www.eltiempo.com'
    page = requests.get(url)

    soup = BeautifulSoup(page.content, 'html.parser')
    
    # Obtencion de los articulos que se encuentran dentro del panel principal del portal
    
    articles = soup.find('section', class_='col2').find_all('article')
    
    # Definicion del diccionario que contiene los enlaces de las respectivas noticias junto con su categoria
    
    global newsLinkDictionary
    
    # Extraccion de la categoria junto con el enlace de la noticias
    
    extractNewsInitialInformation(url, articles)
    
    # Recorrido o barrido de cada una de las noticias que se encontraron en el panel principal 
    
    contadorNoticias = 1
    
    for newsLink in newsLinkDictionary:
        
        # Acceso a la categoria de la noticias a traves de la llave del diccionario
        
        category = newsLinkDictionary[newsLink]
        
        # Extraccion del titulo, descripcion e imagen de la noticia
        
        title, description, image = extractInformation(url, newsLink)
        
        # Insercion de la noticia a la lista de las noticias
        
        listNews.append(ns.news(newsLink, category, title, description, image))
        
        # Impresion por consola de la noticia
        
        print(f'NOTICIA {contadorNoticias}\n\n{listNews[contadorNoticias-1].toString()}\n')
        
        contadorNoticias += 1

def extractNewsInitialInformation(url, articles):
    
    # Recorrido o barrido de cada uno de los articulos que se extrajeron del panel principal
    
    for article in articles:
        
        # Definicion de variables
        
        articleLink = ''
        articleCategory = ''
        
        # Extraccion de la categoria y el enlace de la noticia
        
        try:
            
            articleCategory = article.find('div', class_='category-published').a.text
            articleLink = url + article.h2.a['href']
            
        except:
            
            articleLink = url + article.h3.a['href']
        
        # Insercion del enlace de la noticia junto con la categoria de la misma al diccionario definido
        
        newsLinkDictionary[articleLink] = articleCategory
        
def extractInformation(url, newsLink):
    
    # Definicion de variables
    
    title = ''
    image = ''
    description = ''
    
    # Preparacion del enlace a consultar
    
    page = requests.get(newsLink)

    soup = BeautifulSoup(page.content, 'html.parser')
    
    # Obtencion del div que contiene la informacion que se desea extraer
    
    articlesContainer = soup.find('div', class_='main-container').article
    
    # Obtencion del titulo, descripcion e imagen de la noticia
    
    try:
    
        title = articlesContainer.h1.text
        description = articlesContainer.h2.text
        image = articlesContainer.img['src']
        
        if (image == '/images/1x1.png'):
            image = articlesContainer.picture.source['data-original']
            
        image = url + image
        
    except:
        
        pass
    
    # Retorno del titulo, descripcion e imagen de la noticia
    
    return title, description, image

# Ejecucion del spyder

extractMain()