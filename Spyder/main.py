# Importacion de los spyder especificos para cada portal de noticias

import eltiempo as et
import portafolio as pt

# Definicion del metodo principal

def main():
    
    # Definicion de la lista que contendra las noticias de todos los portales
    
    listNews = []
    
    # Extraccion de noticias para el portal del tiempo
    
    listNews = et.extractMain() + pt.extractMain()

    # Recorrido o barrido de cada una de las noticias que se encontraron de los diferentes portales definidos
    
    contadorNoticias = 1
    
    for news in listNews:
        
        # Impresion por consola de la noticia
        
        print(f'NOTICIA {contadorNoticias}\n\n{listNews[contadorNoticias-1].toString()}\n')
        
        contadorNoticias += 1

# Llamado a la accion del metodo principal     

main()