# Importacion de bibliotecas y paquetes necesarios para el correcto funcionamiento del spyder

from bs4 import BeautifulSoup
import requests
import news as ns

# Lista de objetos de la clase noticias

listNews = list()

# Obtencion de la informacion relacionadas a las noticias junto con la creacion y almacenamientno de los objetos de la clase noticias en la lista

def extractMain():
    
    # Definicion y preparacion del enlace a consultar

    url = 'https://www.eltiempo.com'
    page = requests.get(url)

    soup = BeautifulSoup(page.content, 'html.parser')

    articlesContainer = soup.find_all('article', class_='image-left')
    
    # Recorrido o barrido de cada uno de los articulos que se encuentran en el panel principal
    
    contadorNoticias = 1
    
    for article in articlesContainer:
        
        articleDetails = article.find('div', class_ ='article-details')
        
        # Obtencion del enlace de la noticia
        
        link = url + articleDetails.h3.find('a', class_='multimediatag page-link')['href']
        
        # Verificacion de que se encuentre una imagen y una descripcion, por el contrario se omite la noticia
        
        try:

            description = extractSpecific(link)[0]
            image = url + extractSpecific(link)[1]
            
        except:
            
            continue
        
        # Obtencion de la categoria y el titulo de la noticia
        
        category = articleDetails.find('div', class_ ='category-published').a.text
        title = articleDetails.h3.find('a', class_='title page-link').text
        
        # Insercion de la noticia a la lista de noticias
        
        listNews.append(ns.news(link, category, title, description, image))
        
        # Impresion por consola de la noticia
        
        print(f'NOTICIA {contadorNoticias}\n\n{listNews[contadorNoticias-1].toString()}\n')
        
        contadorNoticias += 1

def extractSpecific(url):
    
    # Preparacion del enlace a consultar
    
    page = requests.get(url)

    soup = BeautifulSoup(page.content, 'html.parser')
    
    # Obtencion de la descripcion y la imagen de la noticia
    
    articlesContainer = soup.find('div', class_='main-container')
    
    description = articlesContainer.find('div', 'middle-content').h2.text
    
    imagePictureContainer = articlesContainer.find('section', class_='intro articulos').picture
    image = imagePictureContainer.img['src']
    
    if (image == '/images/1x1.png' or image == ''):
        image = imagePictureContainer.source['data-original']
    
    # Retorno de la descripcion y la imagen
    
    return description, image

# Ejecucion del spyder

extractMain()