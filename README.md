# scrapy_MeiZiTu、Python3.7、Pycharm
#----------------------------------#
#在MySpider中：
    def content_2(self, response):
        # 得到每张图片的url
        item = Scrapy1Item()
        html_3 = response.text
        img_url = re.findall(r'''img src="(.*?)"''',html_3)
        item['img_url'] = img_url[0]
        yield item
        '''img_url是一个列表，如果传入item['img_url]会报错，需要使用img_url[0]取出url'''
#---------------------------------#
#在setting中：
DEFAULT_REQUEST_HEADERS = {
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
  'Accept-Language': 'en',
  'referer': 'https://www.mzitu.com/',
  'user-agent': 'Mozillar/5.0',
}
'''该网站（www.meizitu.com）需要提交referer信息，否则无法下载'''
#---------------------------------#
#在setting中:
ITEM_PIPELINES = {
   'Scrapy_1.pipelines.Scrapy1Pipeline': 100,
   'Scrapy_1.ImgPipelines.ImgPipeline': 1,
}
'''由于加入了ImgPipelines.py，需要在setting中更新加入'''
#---------------------------------#
#在setting中:
DOWNLOAD_DELAY = 0.2
'''加入DOWNLOAD_DELAY限制爬取时间，否则会报错 514'''
#---------------------------------#


