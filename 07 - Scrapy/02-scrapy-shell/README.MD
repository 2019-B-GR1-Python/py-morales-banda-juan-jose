# Scrapy
## Scrapy instalacion


Ejecutar dentro de `Anaconda Prompt`.
```
$ pip install scrapy
```

## Comando generales

Muestra `las caracteristicas` para  poder hacer Web Scraping o Web Crawling de dicho computador
```
$ scrapy bench
```

Visualizar las `configuraciones extra`
```
$ scrapy settings
```

Visualizamos la `version` de Scrapy
```
$ scrapy version
```
### Scrapy view `url`

La pagina esta identica a su version web y si se puede hacer web scrapy
```
$ scrapy view https://www.pluralsight.com/authors
```

No se ve el contenido porque hay algunos servidores de antemano que redireccionan al lugar con el contenido verdadero.
```
$ scrapy view https://srienlinea.sri.gob.ec/sri-en-linea/inicio/NAT
```

### scrapy shell `url`

Permite `interactuar con la respuesta` del scrapy mediante un `shell`
```
$ scrapy shell http://quotes.toscrape.com/
$ response.css('title')
$ response.css('title').extract()
$ response.css('title::text').extract()
$ response.css('.author').extract()
$ response.css('.author::text').extract()
$ type(response.css('.author'))
$ response.css('.author::text')[0]
$ response.css('.author::text').extract_first()
$ response.css('span.text').extract()
$ response.css('span.text::text').extract()
$ response.css('div.tags > a.tag::text').extract()
$ response.css('.quote > span > a::attr(href)')
$ response.css('.row > div > div:nth-child(2) > .text::text').extract()
```

###  response xpath

```
$ response.xpath('/html/head/title').extract()
$ response.xpath('/html/body/div/div[2]/div[2]/h2').extract()
$ response.xpath('/html/body/div/div[2]/div[2]/h2/text()').extract()
$ response.xpath("//div[@class='quote']").extract_first()
$ response.xpath("//div[@class='quote']/span[@class='text']").extract_first()
$ response.xpath("//div[@class='quote']/span[@class='text']/text()").extract_first()
$ response.xpath("//div[@class='quote']/span/a/@href").extract_first()
```

### scrapy starproject 'nombre_proyecto'

```
$ scrapy startproject arania_basica

```












