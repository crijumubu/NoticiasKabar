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

    url = 'https://www.eltiempo.com'
    page = requests.get(url)

    soup = BeautifulSoup(page.content, 'html.parser')
    
    # Obtencion de los articulos que se encuentran dentro del panel principal del portal
    
    articles = soup.find('section', class_='col2').find_all('article')
    
    # Definicion del diccionario que contiene los enlaces de las respectivas noticias junto con su categoria
    
    global newsLinkDictionary
    
    # Extraccion de la categoria junto con el enlace de la noticias y definicion de la fuente de la noticia
    
    try:

        extractNewsInitialInformation(url, articles)

    except:

        pass
    
    source = 'El tiempo'

    # Recorrido o barrido de cada una de las noticias que se encontraron en el panel principal 
    
    for newsLink in newsLinkDictionary:
        
        try:

            # Acceso a la categoria de la noticias a traves de la llave del diccionario
            
            category = newsLinkDictionary[newsLink]

            # Extraccion del titulo, descripcion e imagen de la noticia
            
            title, description, image = extractInformation(url, newsLink)
            
            # Insercion de la noticia a la lista de las noticias
            
            listNews.append(ns.news(category, title, description, image, source, newsLink))

        except:

            continue
        
    return listNews

# Metodo el cual extrae el enlace y la categoria de las noticias 

def extractNewsInitialInformation(url, articles):
    
    # Recorrido o barrido de cada uno de los articulos que se extrajeron del panel principal
    
    for article in articles:
        
        # Definicion de variables
        
        articleLink = ''
        articleCategory = ''
        
        # Extraccion de la categoria y el enlace de la noticia
        
        articleCategory = article.find('div', class_='category-published').a.text
        articleLink = url + article.h2.a['href']
        #articleLink = url + article.h3.a['href']
        
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
    
    articlesContainer = soup.find('article', class_='content_grid articulo article default')
    
    # Obtencion del titulo, descripcion e imagen de la noticia
    
    title = articlesContainer.h1.text
    description = articlesContainer.h2.text
    image = articlesContainer.img['src']
    
    if (image == '/images/1x1.png'):
        image = articlesContainer.picture.source['data-original']
        
    image = url + image
    
    # Retorno del titulo, descripcion e imagen de la noticia
    
    return title, description, image