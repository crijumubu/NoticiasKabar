import scrapy
from urllib.parse import urljoin

class newsSpider(scrapy.Spider):
    
    name = 'news'
    
    start_urls = ['https://www.eltiempo.com/', 'https://www.portafolio.co/', 'https://www.elnuevosiglo.com.co/']
    
    def parse(self, response):

        originalUrl = response.url

        if (originalUrl == 'https://www.eltiempo.com/'):

            for productsLink in response.xpath("//a[@class='title page-link']"):

                url = urljoin(response.url, productsLink.attrib['href'])
                
                yield scrapy.Request(url, callback=self.parseElTiempo)

        elif (originalUrl == 'https://www.portafolio.co/'):

            for productsLink in response.xpath("//a[@class='page-link']"):

                url = urljoin(response.url, productsLink.xpath('.//@href').get())

                yield scrapy.Request(url, callback=self.parseElPortafolio)
            
        elif (originalUrl == 'https://www.elnuevosiglo.com.co/'):

            for productsLink in response.xpath("//div['text-node']/a"):

                url = urljoin(response.url, productsLink.xpath('.//@href').get())

                if (originalUrl in url and not 'seccion' in url):
                    
                    yield scrapy.Request(url, callback=self.parseElNuevoSiglo)
                
    def parseElTiempo(self, response):

        try:

            imgDir = ''

            for image in response.xpath('//img/@src').extract():

                if '/files' in image:
                    imgDir = image

            title = response.xpath("//h1[@class='titulo ']/text()").get()
            description = response.xpath("//h2[@class='article-epigraph ']/text()").get()

            if (title == None):

                title = response.xpath("//h1[@class='titulo']/text()").get()

            if (description == None):

                description = response.xpath("//h2[@class='article-epigraph']/text()").get()

            yield {
                'Title' : title,
                'Descripcion' : description,
                'Category' : response.xpath("//span[@class='span-following']/text()").get(),
                'Image' : response.url + imgDir,
                'Url' : response.url,
                'Fuente' : 'El tiempo'
            }

        except:

            yield scrapy.Request(callback=self.emptyYield)

    def parseElPortafolio(self, response):

        try:

            imgDir = ''

            for image in response.xpath('//img/@src').extract():

                if '/files' in image and '.jpeg' in image:
                    imgDir = image

            title = response.xpath("//h1[@class='title tiemposBold8 titularUnderBlanco']/text()").get()
            description = response.xpath("//p[@class='epigraph regular_lead1']/text()").get()

            if (title == None):

                title = response.xpath("//h1[@class='title tiemposBold8 titularUnderBlanco ']/text()").get()

            if (description == None):

                description = response.xpath("//p[@class='epigraph regular_lead1 ']/text()").get()

            yield {
                'Title' : title,
                'Descripcion' : description,
                'Category' : " ".join(response.xpath("//a[@class='logoSection']/text()").get().split()),
                'Image' : response.url + imgDir,
                'Url' : response.url,
                'Fuente' : 'Portafolio'
            }

        except:

            yield scrapy.Request(callback=self.emptyYield)
    
    def parseElNuevoSiglo(self, response):

        try:

            yield {
                'Title' : response.xpath("//span[@class='field field--name-title field--type-string field--label-hidden']/text()").get(),
                'Descripcion' : response.xpath("//div[@class='clearfix text-formatted field field--name-body field--type-text-with-summary field--label-hidden field__item']/p/strong/text()").get(),
                'Category' : response.xpath("//div[@class='container']/h3/text()").get(),
                'Image' : response.xpath("//div[@class='multimedia']/img/@src").get().replace('//',''),
                'Url' : response.url,
                'Fuente' : 'El nuevo siglo'
            }

        except:

            yield scrapy.Request(callback=self.emptyYield)

    def emptyYield(self):

        return {

            'Title' : '',
            'Descripcion' : '',
            'Category' : '',
            'Image' : '',
            'Url' : '',
            'Fuente' : '',
        }