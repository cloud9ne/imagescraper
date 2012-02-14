'''
Created on Feb 13, 2012

@author: todd
'''
from scrapy.spider import BaseSpider
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request
import urlparse

from crawler.items import Image

def is_absolute(url):
    return bool(urlparse.urlparse(url).scheme)

class ImageSpider(BaseSpider):
    name = "image"
    start_urls = [ ]
    #    "http://sonorous.net/sample.html",
    #]

    def __init__(self, name=None, **kwargs):
        BaseSpider.__init__(self,name)
        self.__dict__.update(kwargs)
        self.start_urls.append(kwargs['url'])

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        imageurls = []
        
        # add url to allo
        
        #links = hxs.select('//ul/li/a/@href').extract()
        #for l in links:
        #    print l
        # get images
        
        #for url in hxs.select('//a/@href').extract():
        #    yield Request(url, callback=self.parse)
        images = hxs.select('//img/@src').extract()
        for image in images:
            imageurl = Image()
            #urlparse.urljoin(response.url, image_relative_url.strip())
            imageurl['url'] = image
            imageurls.append(imageurl)         
        return imageurls