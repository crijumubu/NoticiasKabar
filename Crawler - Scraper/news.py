# Definicion de la clase relacionada a las noticias

class news():

    title = ''
    description = ''
    category = ''
    link = ''

    def __init__(self, category, title, description, link):
        self.category = category
        self.title = title
        self.description = description
        self.link = link

    def toString(self):
        return 'Categoria: ' + self.category + '. Titulo: ' + self.title + '. Descripcion: ' + self.description + ' Enlace: ' + self.link