import scrapy

class JobSpider(scrapy.Spider):
    name = 'job'
    headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'Connection': 'keep-alive',
            'Cache-Control': 'max-age=0',
            'Cookie': 'JSESSIONID=ABAAABAAADEAAFI5F082310E3212713B7E8A6B8B4C50B92; SEARCH_ID=065fcf8222d049fca1d0b9bfdb891e4e; user_trace_token=20180827143708-8c727295-97a8-42dc-b96d-e02a511670b2; _ga=GA1.2.357646922.1535351830; _gat=1; _gid=GA1.2.116543037.1535351830; LGSID=20180827143709-9fb38811-a9c3-11e8-b24b-5254005c3644; PRE_UTM=; PRE_HOST=; PRE_SITE=; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Fzhaopin%2F1%2F; LGUID=20180827143709-9fb389ed-a9c3-11e8-b24b-5254005c3644; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1535075423; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1535351830; LGRID=20180827143720-a5ef602e-a9c3-11e8-b24b-5254005c3644',                                                                        }

    
    def start_requests(self):
         urls = ['https://www.zhipin.com/c101010100/?page={haha}&ka=page-{haha}'.format(haha=i) for i in range(1, 9)]
         for url in urls:
             yield scrapy.Request(url=url, callback=self.parse, headers=self.headers)
    
    def parse(self,response):
        for i in response.css('div.job-primary'):
            yield {
                    'name' :i.css('div.job-title::text').extract_first(),
                    'salary_low':i.css('span::text').extract_first().split('-')[0],
                    'salary_high':i.css('span::text').extract_first().split('-')[1],
                    'location':i.css('p::text').extract()[0],
                    'experience_requirement':i.css('p::text').extract()[1],
                    'degree_requirement':i.css('p::text').extract()[2]

                    }
