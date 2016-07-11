# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from universo.items import UniversoItem


class UniversoCrawlerSpider(CrawlSpider):
    name = 'universo_crawler'
    allowed_domains = ['eluniverso.com']
    start_urls = ['http://www.eluniverso.com/tema/asesinatos']

    rules = (
        Rule(LinkExtractor(allow=r'asesinatos\?page=[0-9]'),callback='parse_item', follow=True),
        Rule(LinkExtractor(allow=r'/noticias/'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        #node-nota-5664144
        #div[@class="content clearfix"]/article/header/time/span[@class="date"]
        #questions = response.xpath('//article[@id="node-nota-5664144"]')
        #questions = response.xpath('//div[@id="node-nota-full-group-etiquetado-2"]/div[@class="field field-name-field-location field-type-taxonomy-term-reference field-label-hidden"]/div[@class="field-items"]/div[@class="field-item even"]')
        #questions = response.xpath('//div[@class="resumen"]/header/h2')
        #questions2 = response.xpath('')
        questions = response.xpath('//div[@id="region-content"]/div/div[@id="block-system-main"]/div/div[@class="content clearfix"]/article')

        for question in questions:
            item = UniversoItem()
            #div[@id="node-nota-full-group-etiquetado-2"]
            #item['location'] = question.xpath('a/@href').extract()[0]
            #item['location'] = question.xpath('div[@class="content clearfix"]//div[@id="node-nota-full-group-etiquetado-2"/div[@class="field field-name-field-location field-type-taxonomy-term-reference field-label-hidden"]/div[@class="field-items"]/div[@class="field-item even"]/a/text()').extract()[0]
            #item['date'] = question.xpath('a/text()').extract()[0]
            #item['date'] = question.xpath('header/time/span[@class="date"]/span/text()').extract()[0]
            item['date'] = question.xpath('header/time/span[@class="date"]/span/text()').extract()
            #div[@id="node-nota-full-group-etiquetado-2"/div[@class="field field-name-field-location field-type-taxonomy-term-reference field-label-hidden"]/div[@class="field-items"]/div[@class="field-item even"]/a/text()
            item['location'] = question.xpath('div[@class="content clearfix"]/div[@class="tags-lea-ademas"]/div[@class="field field-name-field-location field-type-taxonomy-term-reference field-label-hidden"]/div/div/a/text()').extract()
            print '+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
            #.//div[@id='region-content']/div/div[@id='block-system-main']/div/div[@class='content clearfix']/article/header/time/span[@class='date']/span/text()
            print question.xpath('header/time/span[@class="date"]/span/text()').extract()
            print question.xpath('div[@class="content clearfix"]/div[@class="tags-lea-ademas"]/div[@class="field field-name-field-location field-type-taxonomy-term-reference field-label-hidden"]/div/div/a/text()').extract()
            print '+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
            yield item

#response.xpath(".//article[@class='node node-nota node-published node-not-promoted node-not-sticky author-redaccion odd clearfix']/header/div[@class='content clearfix']/div[@id='node-nota-full-group-etiquetado-2']/div[@class='field field-name-field-location field-type-taxonomy-term-reference field-label-hidden']/div/div/a/text()")
#response.xpath(".//article[@id='node-nota-5664144']/div[@class='content clearfix']//div[@id='node-nota-full-group-etiquetado-2']/div[@class='field field-name-field-location field-type-taxonomy-term-reference field-label-hidden']/div[@class='field-items']/div[@class='field-item even']/a/text()")
#article/div[@class='content clearfix']/div[@class='tags-lea-ademas']/div[@class='field field-name-field-location field-type-taxonomy-term-reference field-label-hidden']/div/div/a/text()
#response.xpath(".//article[@id='node-nota-5664144']/header/time/span[@class='date']/span/text()")


#//*[@id="node-nota-full-group-etiquetado-2"]/div[2]/div/div/a