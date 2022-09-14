from itertools import product
import scrapy
from urllib.parse import urljoin

class newsSpider(scrapy.Spider):
    
    name = 'news'
    start_urls = ['https://www.eltiempo.com/']
    
    def parse(self, response):

        originalUrl = response.url

        if (originalUrl == 'https://www.eltiempo.com/'):
            
            for productsLink in response.css('a.title.page-link'):

                url = urljoin(response.url, productsLink.attrib['href'])
                
                yield scrapy.Request(url, callback=self.parseElTiempo)

    def parseElTiempo(self, response):

        try:

            imgDir = ''

            for image in response.xpath('//img/@src').extract():

                if '/files' in image:
                    imgDir = image


            yield {
                'Title' : response.css('h1.titulo::text').extract(),
                'Descripcion' : response.css('h2.article-epigraph::text').extract(),
                'Category' : response.css('span.span-following::text').get(),
                'Image' : response.url + imgDir,
                'Url' : response.url,
                'Fuente' : 'EL tiempo'
            }

        except:

            yield{

                'Title' : '',
                'Descripcion' : '',
                'Category' : '',
                'Image' : '',
                'Url' : '',
                'Fuente' : '',
            }
