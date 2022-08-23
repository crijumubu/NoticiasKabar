# Definicion de la clase relacionada a las noticias

class news():

    category = ''
    title = ''
    description = ''
    image = ''
    link = ''

    def __init__(self, link, category, title, description='', image=''):
        self.link = link
        self.category = category
        self.title = title
        self.description = description
        self.image = image

    def toString(self):
        return 'Categoria: ' + self.category + '\nTitulo: ' + self.title + '\nDescripcion: ' + self.description + '\nImagen: ' + str(self.image) + '\nEnlace: ' + self.link