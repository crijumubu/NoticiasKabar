# Definicion de la clase relacionada a las noticias

class news():

    category = ''
    title = ''
    description = ''
    image = ''
    source = ''
    link = ''

    def __init__(self, category, title, description, image, source, link):
        self.category = category
        self.title = title
        self.description = description
        self.image = image
        self.source = source
        self.link = link


    def toString(self):
        return 'Categoria: ' + self.category + '\nTitulo: ' + self.title + '\nDescripcion: ' + self.description + '\nImagen: ' + self.image + '\nFuente: ' + self.source + '\nEnlace: ' + self.link