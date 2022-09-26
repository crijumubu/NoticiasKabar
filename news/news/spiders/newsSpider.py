import json
import scrapy
from urllib.parse import urljoin

class newsSpider(scrapy.Spider):
    
    name = 'news'

    start_urls = ['https://www.eltiempo.com/', 'https://www.elespectador.com/', 'https://www.elnuevosiglo.com.co/', 'https://www.portafolio.co/']

    headersElEspectador = {
        "authority": "www.elespectador.com",
        "method": "GET",
        "path": "/pf/api/v3/content/fetch/getNotes?query=%7B%22size%22%3A10%2C%22sourceInclude%22%3A%22_id%2Cadditional_properties%2Ccanonical_url%2Ctype%2Csubtype%2Cdescription.basic%2Cheadlines.basic%2Csubheadlines.basic%2Ctaxonomy.primary_section._id%2Ctaxonomy.primary_section.name%2Ctaxonomy.primary_section.path%2Ctaxonomy.sections.name%2Ctaxonomy.tags.text%2Ctaxonomy.tags.slug%2Cfirst_publish_date%2Cdisplay_date%2Clast_updated_date%2Cpromo_items.basic%2Cpromo_items.comercial%2Cpromo_items.comercial_movil%2Cpromo_items.jw_player%2Clabel%2Ccredits.by._id%2Ccredits.by.name%2Ccredits.by.additional_properties.original%2Ccredits.by.image.url%2CcommentCount%22%2C%22uris%22%3A%5B%22%2Fdeportes%2Fmas-deportes%2Fsu-majestad-roger-federer-el-adios-que-nadie-queria-escuchar-retiro-roger-federer%2F%22%2C%22%2Fcolombia-20%2Fpaz-y-memoria%2Fpartido-comunes-propone-tratamiento-penal-especial-para-cocaleros-en-que-consiste%2F%22%2C%22%2Fdeportes%2Fseleccion-colombia%2Fjames-falcao-y-ospina-en-la-primera-convocatoria-de-nestor-lorenzo%2F%22%5D%7D&d=592&_website=el-espectador",
        "scheme": "https",
        "accept": "*/*",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "en-US,en;q=0.5",
        "cache-control": "no-cache",
        "cookie": "_fbp=fb.1.1663169652621.1297634291; _pprv=%7B%22consent%22%3A%7B%220%22%3A%7B%22mode%22%3A%22opt-in%22%7D%2C%221%22%3A%7B%22mode%22%3A%22opt-in%22%7D%2C%222%22%3A%7B%22mode%22%3A%22opt-in%22%7D%2C%223%22%3A%7B%22mode%22%3A%22opt-in%22%7D%2C%224%22%3A%7B%22mode%22%3A%22opt-in%22%7D%2C%225%22%3A%7B%22mode%22%3A%22opt-in%22%7D%2C%226%22%3A%7B%22mode%22%3A%22opt-in%22%7D%2C%227%22%3A%7B%22mode%22%3A%22opt-in%22%7D%7D%7D; _pcid=%7B%22browserId%22%3A%22l81s9pr8wnv8j55l%22%7D; __pat=-18000000; _pc_suscriptor=false; AKA_A2=A; _vfa=www%2Eelespectador%2Ecom.00000000-0000-4000-8000-a4de5f363b96.caec9331-768d-4706-b99d-dfbeb72668ad.1663169653.1663288050.1663300535.6; _vfz=www%2Eelespectador%2Ecom.00000000-0000-4000-8000-a4de5f363b96.1663300900.1.medium=direct|source=|sharer_uuid=|terms=; xbc=%7Bkpex%7D_oghGffBXJl5do0T8Rzbgh87IWXmJO4gJcbxSkAYWcYa3G8hk0pNBDNG-PsQ-_LgKFLlVFY0LDwfPzYaTSQaMM3LUuUnkKErBvPKiFIPM__RpbCqJ2Px_8YskOx6M9CbeQ-v9KK4Lby-ZBcKnFHr85VEkwX6Q0MFQH1VKUYoIyAH5qmhamz3FWzCe33_oSrw0HlhnyGxCfeScyj0A2ssy1NtJtRhFMbxEd10tGEjGwNdn2BNwlSSFldDwP0PGg6ZAgtOEr4bFbp3orHwGQ0_EUEHcsPGbKzu6_bf1leaEhVNceId9pP_K4GkqD3VNQL7hw4pu2FBjpsYrKETNA5qTTsvglcLWv29H9oz2rxZjR8sK41UF0ch3ijWJYyX3Q4wOfsw8Nizq3LQr3tWLgBsIU2TGVUjUFr42Sj9S5IUqX5HV4K9nlFj61KCNKOsg9ynGRqA-Bc8Se7mtdBE4UUY3C91YJJY3zxfSzMG6CdCG_IKfA_qi3wk-JwbWs27OtAaBUdquk1Ip4hK11YJcA8BVBJ1L-aFtrQBiB6BKN7Q78ebCSvBePsujyfJkAe9X1ETSsh4nBNs8_J6ODbmsUcSLhzb7tC-DanLAcjCOdupIq4; _vfb=www%2Eelespectador%2Ecom.00000000-0000-4000-8000-a4de5f363b96.16..1663300535.true...; __tbc=%7Bkpex%7DUxFZTuCWIQcTcd0oyV5xe1qDu50P3nIoMIslVhrWi_Y7Ndfuo1FftDKXrachWmdk; _pctx=%7Bu%7DN4IgDghg5gpgagSxgdwJIBMQC4QBsAcAzAJ4B2ATLgKwC2MMAxgC4ICuAXiADQisDOMAE59spVrlw9%2BQgMpMITfthARSAe1LcQfBExgZR43AF8gA; __pvi=%7B%22id%22%3A%22v-2022-09-15-22-55-34-316-GmjGnP2vs6dXUnju-8724897b88c269dee1388dfce601d6e7%22%2C%22domain%22%3A%22.elespectador.com%22%2C%22time%22%3A1663301286627%7D",
        "pragma": "no-cache",
        "referer": "https://www.elespectador.com/",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "sec-gpc": "1",
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
    }

    def parse(self, response):

        originalUrl = response.url

        if (originalUrl == 'https://www.eltiempo.com/'):

            for productsLink in response.xpath("//a[@class='title page-link']"):

                url = urljoin(response.url, productsLink.attrib['href'])
                
                yield scrapy.Request(url, callback=self.parseElTiempo)

        elif (originalUrl == 'https://www.elespectador.com/'):
            
            getUrls = ['https://www.elespectador.com/pf/api/v3/content/fetch/getNotes?query=%7B%22size%22%3A10%2C%22sourceInclude%22%3A%22_id%2Cadditional_properties%2Ccanonical_url%2Ctype%2Csubtype%2Cdescription.basic%2Cheadlines.basic%2Csubheadlines.basic%2Ctaxonomy.primary_section._id%2Ctaxonomy.primary_section.name%2Ctaxonomy.primary_section.path%2Ctaxonomy.sections.name%2Ctaxonomy.tags.text%2Ctaxonomy.tags.slug%2Cfirst_publish_date%2Cdisplay_date%2Clast_updated_date%2Cpromo_items.basic%2Cpromo_items.comercial%2Cpromo_items.comercial_movil%2Cpromo_items.jw_player%2Clabel%2Ccredits.by._id%2Ccredits.by.name%2Ccredits.by.additional_properties.original%2Ccredits.by.image.url%2CcommentCount%22%2C%22uris%22%3A%5B%22%2Fdeportes%2Fmas-deportes%2Fsu-majestad-roger-federer-el-adios-que-nadie-queria-escuchar-retiro-roger-federer%2F%22%2C%22%2Fcolombia-20%2Fpaz-y-memoria%2Fpartido-comunes-propone-tratamiento-penal-especial-para-cocaleros-en-que-consiste%2F%22%2C%22%2Fdeportes%2Fseleccion-colombia%2Fjames-falcao-y-ospina-en-la-primera-convocatoria-de-nestor-lorenzo%2F%22%5D%7D&d=592&_website=el-espectador','https://www.elespectador.com/pf/api/v3/content/fetch/getNotes?query=%7B%22size%22%3A10%2C%22sourceInclude%22%3A%22_id%2Cadditional_properties%2Ccanonical_url%2Ctype%2Csubtype%2Cdescription.basic%2Cheadlines.basic%2Csubheadlines.basic%2Ctaxonomy.primary_section._id%2Ctaxonomy.primary_section.name%2Ctaxonomy.primary_section.path%2Ctaxonomy.sections.name%2Ctaxonomy.tags.text%2Ctaxonomy.tags.slug%2Cfirst_publish_date%2Cdisplay_date%2Clast_updated_date%2Cpromo_items.basic%2Cpromo_items.comercial%2Cpromo_items.comercial_movil%2Cpromo_items.jw_player%2Clabel%2Ccredits.by._id%2Ccredits.by.name%2Ccredits.by.additional_properties.original%2Ccredits.by.image.url%2CcommentCount%22%2C%22uris%22%3A%5B%22%2Fmundo%2Feuropa%2Ffotos-las-cicatrices-de-la-guerra-en-izium-la-ciudad-que-ucrania-recupero-noticias-hoy-galeria%2F%22%2C%22%2Fbogota%2Fdenuncian-que-colegio-no-atendio-caso-de-bullying-que-termino-en-suicidio-de-menor-en-bogota-noticias-bogota-hoy%2F%22%2C%22%2Fpolitica%2Fno-se-requieren-bloqueos-porque-gobierno-llegara-a-regiones-con-dialogo-social-alfonso-prada%2F%22%2C%22%2Fmundo%2Famerica%2Fatentado-contra-cristina-fernandez-que-se-sabe-sobre-los-cuatro-detenidos%2F%22%2C%22%2Fmundo%2Famerica%2Fmexico-capturado-militar-responsable-en-crimen-de-los-43-estudiantes-de-ayotzinapa-noticias-hoy%2F%22%5D%7D&d=592&_website=el-espectador', 'https://www.elespectador.com/pf/api/v3/content/fetch/getNotes?query=%7B%22size%22%3A10%2C%22sourceInclude%22%3A%22_id%2Cadditional_properties%2Ccanonical_url%2Ctype%2Csubtype%2Cdescription.basic%2Cheadlines.basic%2Csubheadlines.basic%2Ctaxonomy.primary_section._id%2Ctaxonomy.primary_section.name%2Ctaxonomy.primary_section.path%2Ctaxonomy.sections.name%2Ctaxonomy.tags.text%2Ctaxonomy.tags.slug%2Cfirst_publish_date%2Cdisplay_date%2Clast_updated_date%2Cpromo_items.basic%2Cpromo_items.comercial%2Cpromo_items.comercial_movil%2Cpromo_items.jw_player%2Clabel%2Ccredits.by._id%2Ccredits.by.name%2Ccredits.by.additional_properties.original%2Ccredits.by.image.url%2CcommentCount%22%2C%22uris%22%3A%5B%22%2Fentretenimiento%2Fmusica%2Fcoldplay-una-noche-llena-de-estrellas-en-bogota%2F%22%2C%22%2Feconomia%2Fmacroeconomia%2Flos-analistas-esperan-que-la-inflacion-cierre-en-1122-para-este-ano%2F%22%2C%22%2Fcontenido-patrocinado%2Fbanco-de-bogota-entregara-boveda-de-oxigeno-con-18000-nuevos-arboles-al-amazonas%2F%22%5D%7D&d=592&_website=el-espectador','https://www.elespectador.com/pf/api/v3/content/fetch/getNotes?query=%7B%22size%22%3A10%2C%22sourceInclude%22%3A%22_id%2Cadditional_properties%2Ccanonical_url%2Ctype%2Csubtype%2Cdescription.basic%2Cheadlines.basic%2Csubheadlines.basic%2Ctaxonomy.primary_section._id%2Ctaxonomy.primary_section.name%2Ctaxonomy.primary_section.path%2Ctaxonomy.sections.name%2Ctaxonomy.tags.text%2Ctaxonomy.tags.slug%2Cfirst_publish_date%2Cdisplay_date%2Clast_updated_date%2Cpromo_items.basic%2Cpromo_items.comercial%2Cpromo_items.comercial_movil%2Cpromo_items.jw_player%2Clabel%2Ccredits.by._id%2Ccredits.by.name%2Ccredits.by.additional_properties.original%2Ccredits.by.image.url%2CcommentCount%22%2C%22uris%22%3A%5B%22%2Fpolitica%2Flos-giros-en-la-exploracion-del-gobierno-petro-por-lograr-la-paz-con-el-eln%2F%22%5D%7D&d=592&_website=el-espectador','https://www.elespectador.com/pf/api/v3/content/fetch/getNotes?query=%7B%22size%22%3A10%2C%22sourceInclude%22%3A%22_id%2Cadditional_properties%2Ccanonical_url%2Ctype%2Csubtype%2Cdescription.basic%2Cheadlines.basic%2Csubheadlines.basic%2Ctaxonomy.primary_section._id%2Ctaxonomy.primary_section.name%2Ctaxonomy.primary_section.path%2Ctaxonomy.sections.name%2Ctaxonomy.tags.text%2Ctaxonomy.tags.slug%2Cfirst_publish_date%2Cdisplay_date%2Clast_updated_date%2Cpromo_items.basic%2Cpromo_items.comercial%2Cpromo_items.comercial_movil%2Cpromo_items.jw_player%2Clabel%2Ccredits.by._id%2Ccredits.by.name%2Ccredits.by.additional_properties.original%2Ccredits.by.image.url%2CcommentCount%22%2C%22uris%22%3A%5B%22%2Fjudicial%2Fen-el-caso-nicolas-neira-la-corte-suprema-prepara-una-decision-historica%2F%22%2C%22%2Fbogota%2Fla-batalla-que-gano-la-comunidad-en-el-guavio%2F%22%2C%22%2Feconomia%2Fmacroeconomia%2Finminente-recesion-mundial%2F%22%5D%7D&d=592&_website=el-espectador','https://www.elespectador.com/pf/api/v3/content/fetch/general?query=%7B%22must%22%3A%7B%22subtype%22%3A%22editorial%22%7D%2C%22size%22%3A20%2C%22sourceInclude%22%3A%22_id%2Cadditional_properties%2Ccanonical_url%2Ctype%2Csubtype%2Cdescription.basic%2Cheadlines.basic%2Csubheadlines.basic%2Ctaxonomy.primary_section._id%2Ctaxonomy.primary_section.name%2Ctaxonomy.primary_section.path%2Ctaxonomy.sections.name%2Ctaxonomy.tags.text%2Ctaxonomy.tags.slug%2Cfirst_publish_date%2Cdisplay_date%2Clast_updated_date%2Cpromo_items.basic%2Cpromo_items.comercial%2Cpromo_items.comercial_movil%2Cpromo_items.jw_player%2Clabel%2Ccredits.by._id%2Ccredits.by.name%2Ccredits.by.additional_properties.original%2Ccredits.by.image.url%2CcommentCount%22%7D&d=592&_website=el-espectador']

            for url in getUrls:

                yield scrapy.Request(url, callback=self.parseAPIElEspectador, headers=self.headersElEspectador)

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

            if (imgDir == ''):
                
                return

            title = response.xpath("//h1[@class='titulo ']/text()").get()
            description = response.xpath("//h2[@class='article-epigraph ']/text()").get()

            if (title == None):

                title = response.xpath("//h1[@class='titulo']/text()").get()

                if (title == None):

                    title = response.xpath("//h1[@class='title']/text()").get()

                    if (title == None):

                        title = response.xpath("//h1[@class='title ']/text()").get()

            if (description == None):

                description = response.xpath("//h2[@class='article-epigraph']/text()").get()

                if (description == None):

                    description = response.xpath("//p[@class='epigraph']/text()").get()

                    if (description == None):

                        description = response.xpath("//p[@class='epigraph ']/text()").get()

            category = response.xpath("//span[@class='span-following']/text()").get()

            if (category == None):

                category = 'Opinión'

            yield {
                'Title' : title,
                'Descripcion' : description,
                'Category' : category,
                'Image' : urljoin(response.url, imgDir),
                'Url' : response.url,
                'Fuente' : 'El tiempo'
            }

        except:

            return

    def parseAPIElEspectador(self, response):

        originalUrl = self.start_urls[1]
        
        rawData = response.body
        data = json.loads(rawData)

        for news in data['content_elements']:

            newsUrl = urljoin(originalUrl, news['canonical_url'])
            
            yield scrapy.Request(newsUrl, callback=self.parseElEspectador, headers=self.headersElEspectador)

    def parseElEspectador(self, response):

        try:
            
            description = response.xpath("//div[@class='ArticleHeader-Hook']/div/text()").get()

            if (description == None):

                description = response.xpath("//div[@class='ImageArticle-Description']/text()").get()

                if (description == None):

                    return

            yield {
                'Title' : response.xpath("//h1[@class='Title ArticleHeader-Title Title_article']/text()").get(),
                'Descripcion' : description,
                'Category' : response.xpath("//span[@class='Breadcrumb-Text']/a/text()").get(),
                'Image' : response.xpath("//img[@class='ImageArticle-Image']/@src").get(),
                'Url' : response.url,
                'Fuente' : 'El espectador',
            }

        except:

            return

    def parseElPortafolio(self, response):

        try:

            imgDir = ''

            for image in response.xpath('//img/@src').extract():

                if ('article_multimedia' in image or 'main_video_image' in image) and ('.jpeg' in image or '.png' in image):

                    imgDir = image

            if (imgDir == ''):

                return

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
                'Image' : urljoin(response.url, imgDir),
                'Url' : response.url,
                'Fuente' : 'Portafolio'
            }

        except:

            return
    
    def parseElNuevoSiglo(self, response):

        try:
            
            xpath = "//div[@class='clearfix text-formatted field field--name-body field--type-text-with-summary field--label-hidden field__item']/p[1]"

            while response.xpath(xpath + '/node()') != []:

                xpath += '/node()'

            description = response.xpath(xpath).get()

            image = response.xpath("//div[@class='multimedia']/img/@src").get().replace('//','').split("?")

            yield {
                'Title' : response.xpath("//span[@class='field field--name-title field--type-string field--label-hidden']/text()").get(),
                'Descripcion' : description,
                'Category' : response.xpath("//div[@class='container']/h3/text()").get(),
                'Image' : image[0],
                'Url' : response.url,
                'Fuente' : 'El nuevo siglo'
            }

        except:

            return