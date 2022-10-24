from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import sys 
sys.path.append('/home/cristian/Documents/Personal/Universidad/2.6 Sexto semestre/Proyecto integrador II/Development/Implemenation/database')
from connection import mongo

class artificalIntelligence:

    def __init__(self):

        self.connection = mongo()
        self.checkSimilarity()
        self.connection.client.close()
    
    def getNewsWithoutCategory(self):

        data = self.connection.selectEspecificByCategory('')
        return data

    def checkSimilarity(self):

        categoriesIndex = ['Deportes', 'Judicial', 'Política', 'Unidad investigativa', 'Colombia', 'Economía', 'Tecnología', 'Ciencia', 'Salud', 'Educación', 'Entretenimiento']
        
        categories = [['Deporte', 'Fútbol', 'Fitness', 'Ejercicio', 'Gol', 'Campeón', 'Vencer', 'Copa', 'Jugador', 'Clasificación', 'Cuadrangular', 'Liga'], ['Corrupción', 'Justicia' ,'Escándalo', 'Fiscalía', 'Contrato', 'Audiencia', 'Mafia', 'Ley', 'Corte', 'Proceso', 'Muerte', 'Irregularidad', 'Juez'], ['Presidente', 'Estado', 'Vicepresidente', 'Alcalde', 'Gobernador', 'Electoral', 'Director', 'Congreso', 'Reforma', 'Senado', 'Embajador', 'Ministro', 'Partido'], ['Investigación', 'Escándalo', 'Denuncia', 'Presunto', 'Estudio', 'Corrupción', 'Testigo', 'Indagación', 'Capturado', 'Proceso', 'Confesión', 'Muertos'], ['Colombia', 'Bogotá', 'Medellín', 'Cali', 'Bucaramanga', 'Barranquilla', 'Cartagena', 'Región', 'Municipio', 'Departamento', 'Caribe', 'Pacífico', 'Cundinamarca'], ['Economía', 'Finanzas', 'Banco', 'Interés', 'Peso', 'Crisis', 'Devaluación', 'Dólar', 'Petróleo', 'Tributaria', 'Inversión', 'Crédito', 'Inflación', 'Comercio', 'Ahorro', 'Precio'], ['Tecnología', 'TikTok', 'Instagram', 'Facebook', 'Twitter', 'WhatsApp', 'Meta', 'Teléfono', 'Computador', 'Google', 'iPhone', 'App'], ['Ciencia', 'Nasa', 'Científico', 'ADN', 'Extinción', 'Astrónomo', 'Luna', 'Espacial', 'Atómico', 'Astronauta', 'Telescopio', 'Descubrir'], ['Salud', 'Organo', 'Paciente', 'Obesidad', 'Sangre', 'Enfermedad', 'OMS', 'OPS', 'Brote', 'Vacuna', 'Bacteria', 'Viruela'], ['Educación', 'Becas', 'Universidad', 'Estudiar', 'Examen', 'Icetex', 'Curso', 'Libro', 'Colegio', 'Escuela', 'Enseñanza', 'Aprendizaje'], ['Entretenimiento', 'Actriz', 'Actor', 'Álbum', 'Canción', 'Película', 'Música', 'Series', 'Televisión', 'Cantante', 'Redes', 'Farándula']]

        for new in self.getNewsWithoutCategory():
            
            categoriesSimilarity = []

            title = new['Title']
            description = new['Description']

            titleTokenization = word_tokenize(title.lower())
            descriptionTokenization = word_tokenize(description.lower())

            for category in categories:
                
                categorySimilarityCont = 0
                
                for subcategory in category:

                    subcategoryTokenization = word_tokenize(subcategory.lower())

                    titleCorrelation = self.wordSimilarity(subcategoryTokenization, titleTokenization)        
                    descriptionCorrelation = self.wordSimilarity(subcategoryTokenization, descriptionTokenization)

                    if titleCorrelation > descriptionCorrelation:

                        correlation = titleCorrelation
                    else:

                        correlation = descriptionCorrelation

                    categorySimilarityCont += correlation
                
                categoriesSimilarity.append(categorySimilarityCont)

            maxCorrelation = max(categoriesSimilarity)
            category = ''

            if (maxCorrelation != 0):

                categoryIndex = categoriesSimilarity.index(maxCorrelation)
                category = categoriesIndex[categoryIndex]

            else:

                category = 'Otros'

            self.connection.updateEspecific(title, category)

    def wordSimilarity(self, phraseTokenization, newsWordTokenization):

        try:

            sw = stopwords.words('spanish') 

            l1 =[]
            l2 =[]

            phraseSet = {w for w in phraseTokenization if not w in sw}
            newsWordSet = {w for w in newsWordTokenization if not w in sw} 

            rvector = newsWordSet.union(phraseSet) 
            for w in rvector:
                if w in newsWordSet: l1.append(1)
                else: l1.append(0)
                if w in phraseSet: l2.append(1)
                else: l2.append(0)
            c = 0

            for i in range(len(rvector)):
                c+= l1[i]*l2[i]
            cosine = c / float((sum(l1)*sum(l2))**0.5)

            return cosine

        except:

            return 0

IAobject = artificalIntelligence();