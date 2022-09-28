from gc import callbacks
from subprocess import call
from urllib.parse import urljoin
import scrapy
urlPrueba = 'http://www.publimetro.co/'

class NoticiasSpider(scrapy.Spider):
    name = 'news'
    allowed_domains = ['www.publimetro.co']
    start_urls = ['http://www.publimetro.co/']

    def parse(self, response):
        for link in response.css('h2.primary-font__PrimaryFontStyles-o56yd5-0.ctbcAa.sm-promo-headline a::attr(href)'):
            if(link.get().find('https') == -1):
                url = urljoin(urlPrueba,link.get())
                yield response.follow(link.get(),callback=self.parse_categories)

    def parse_categories(self, response):
        general = response.css('div.container.layout-section')
        noticia = general.css('div.col-sm-xl-12.layout-section.wrap-bottom.promo1')
        if (noticia.css('a.primary-font__PrimaryFontStyles-o56yd5-0.ctbcAa.overline.overline--link::text').get()!="Publimetro TV"):
            yield{
                'Title' : noticia.css('h1.primary-font__PrimaryFontStyles-o56yd5-0.ctbcAa.headline::text').get(),
                'Descripcion' : noticia.css('h2.primary-font__PrimaryFontStyles-o56yd5-0.ctbcAa.h4-primary.sub-headline::text').get(),
                'Category' : noticia.css('a.primary-font__PrimaryFontStyles-o56yd5-0.ctbcAa.overline.overline--link::text').get(),
                'Image' : general.css('img::attr(src)').get(),
                'Url' : response.url,
                'Fuente' : 'Publimetro'
            }
