import scrapy

class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    start_urls = ['http://maoyan.com/board/4']

    def parse(self, response):
        title_list = response.xpath('//*[@id="app"]/div/div/div[1]/dl/dd/div/div/div[1]/p[1]/a/text()').extract()
        actor_list = response.xpath('//*[@id="app"]/div/div/div[1]/dl/dd/div/div/div[1]/p[2]/text()').extract()
        pub_time = response.xpath('//*[@id="app"]/div/div/div[1]/dl/dd/div/div/div[1]/p[3]/text()').extract()
        for a, b, c in zip(title_list, actor_list, pub_time):
            print(
                {
                    'title' : a,
                    'actor' : b.strip('\n').strip(),
                    'time' : c
                }
            )