# Definicion de la clase relacionada a las noticias

class news():

    category = ''
    title = ''
    description = 'Not found'
    image = 'Not found'
    link = ''

    def __init__(self, category, title, description, image, link):
        self.category = category
        self.title = title
        self.description = description
        self.image = image
        self.link = link

    def toString(self):
        return 'Categoria: ' + self.category + '\nTitulo: ' + self.title + '\nDescripcion: ' + self.description + '\nImagen: ' + str(self.image) + '\nEnlace: ' + self.link