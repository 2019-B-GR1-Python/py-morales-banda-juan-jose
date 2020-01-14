import scrapy

class IntroSpider(scrapy.Spider):
    name = 'introduccion_spider'
    urls = ['http://books.toscrape.com/catalogue/category/books/travel_2/index.html']

    def start_requests(self):
        for url in self.urls:
            yield scrapy.Request(url=url)

    def parse(self, response):
        etiqueta_contenedora = response.css('article.product_pod')
        titulos = etiqueta_contenedora.css('h3 > a::text').extract()
        links = etiqueta_contenedora.css('div.image_container > a > img.thumbnail::attr(src)').extract()
        precios = etiqueta_contenedora.css('div.product_price > p.price_color::text').extract()
        categorias = response.css('div.side_categories > ul > li > ul > li > a::attr(href)').extract()

        pathImagenes = 'http://books.toscrape.com'
        pathCategorias = 'http://books.toscrape.com/catalogue/category/books'
        reemplazoImagenes = '../../../..'
        reemplazoCategorias = '..'
        

        def completarEnlace(path, reemplazo, array):
            for posicion in range(len(array)):
                array[posicion] = array[posicion].replace(reemplazo, path)
                #print(array[posicion])

        completarEnlace(pathImagenes, reemplazoImagenes, links)
        completarEnlace(pathCategorias, reemplazoCategorias, categorias)

        print(f"---------------CATEGORIAS---------------")
        for a in range(len(categorias)):
            print(categorias[a])
        print('\n---------------LIBROS---------------')
        
        
        pathArchivo = "./Libros.txt"
        archivo_escritura_abierto = open(pathArchivo, mode = "a")
        try:
            for a in range(len(titulos)):
                print(f"{titulos[a]}\n{links[a]}\n{precios[a]}\n") 
                archivo_escritura_abierto.writelines(f"{titulos[a]}\n{links[a]}\n{precios[a]}\n")
            archivo_escritura_abierto.close()
        except Exception as error:
            print("Error")



        
