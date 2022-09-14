from itertools import product
import scrapy
from urllib.parse import urljoin

class newsSpider(scrapy.Spider):
    
    name = 'news'

    start_urls = ['https://www.eltiempo.com/', 'https://www.portafolio.co/']
    
    def parse(self, response):

        originalUrl = response.url

        if (originalUrl == 'https://www.eltiempo.com/'):

            for productsLink in response.css('a.title.page-link'):

                url = urljoin(response.url, productsLink.attrib['href'])
                
                yield scrapy.Request(url, callback=self.parseElTiempo)

        elif (originalUrl == 'https://www.portafolio.co/'):

            for productsLink in response.css('a.page-link'):

                url = urljoin(response.url, productsLink.xpath('.//@href').get())

                yield scrapy.Request(url, callback=self.parseElPortafolio)


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
    
    def emptyYield(self):

        return {

            'Title' : '',
            'Descripcion' : '',
            'Category' : '',
            'Image' : '',
            'Url' : '',
            'Fuente' : '',
        }