class ZhipinspiderPipeline(object):
    def process_item(self, item, spider):
        print("工作：", item['title'] )
        print("工资：", item['salary'] )
        print("工作地点：", item['work_adr'] )
        print("详情链接：", item['url'] )

        print("公司：", item['company'] )
        print("行业：", item['industry'] )
        print("公司规模：", item['company_size'] )

        print("招聘人：", item['recruiter'] )
        print("发布日期：", item['publish_date'] )

