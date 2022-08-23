from bs4 import BeautifulSoup
import requests

website = 'https://www.eltiempo.com/'
result = requests.get(website)
html = result.content

soup = BeautifulSoup(html, 'lxml') #Contenido HTML

articles = soup.find_all('article',class_= 'image-left')

listTitle=list()
i=0

for article in articles:


    # Para obtener la dirección de las imagenes toca extraer el data-original porque algunos src de imágenes eran 'imagen1x1' y presentaba problemas

    figure = article.find('figure',class_='image-container')
    a = figure.find('a',class_='image page-link')
    source = a.find('source').attrs.get("data-original",None) #Dirección imagen
    print(source)

    #Descargar las imágenes, revisar qué imagen se selecciona y aplicar filtro para repetidas
    '''
    img = requests.get('https://www.eltiempo.com'+source)
    i += 1
    nameImg = 'noticia'+str(i)+'.jpg'
    with open(nameImg,'wb') as imagen:
        imagen.write(img.content)
    '''
