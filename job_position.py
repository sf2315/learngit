import scrapy
from ZhipinSpider.items import ZhipingspiderItem


class JobPositionSpider(scrapy.Spider):
    #定义该Spider的名字
    name = 'job_position'
    #定义该Spider允许爬取的域名
    allowed_domains = ['zhipin.com']
    #定义该Spider爬取的首页列表
    start_urls = ['http://zhipin.com/']

    #该方法负责提取response所包含的信息
    #response代表下载器从start_urls中的每个URL下载得到的响应
    def parse(self, response):
        #遍历页面中的所有//div[@class="job_primary"]节点
        for job_primary in response.xpath('//div[@class="job-primary"]'):
            item = ZhipinspiderItem()
            #匹配//div[@class="job-primary"]节点下的/div[@class="info-primary"]节点
            info_primary = job_primary.xpath('./div[@class="info-primary"]')
            item['title'] = info_primary.xpath('./h3/a/div[@class="job-title"]/text()').extract_first()
            item['salary'] = info_primary.xpath('./h3/a/span[@class="red"]/text()').extract_first()
            item['work_addr'] = info_primary.xpath('./p/text()').extract_first()
            item['url'] = info_primary.xpath('./h3a/@herf').extract_first()

            company_text = job_primary.xpath('./div[@class="info-company"]' + '/div[@class="company-text"]' )
            item['company'] = company_text.xpath('./h3/a/text()').extract_first()
            company_info = company_text.xpath('./p/text()').extract()
            if company_info and len(company_info) > 0:
                item['industry'] = company_text.xpath('./p/text()').extract()[0]
            if company_info and len(company_info) > 1:
                item['company_size'] = company_text.xpath('./p/text()').extract()[2]
            info_publish = job_primary.xpath('./div[@class="info-publish"]')
            item['recruiter'] = info_publish.xpath('./h3/text()').extract_first()
            item['publish_date'] = info_publish.xpath('./p/text()').extract_first()
            yield item
