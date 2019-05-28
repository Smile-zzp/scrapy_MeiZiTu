import scrapy
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem

class ImgPipeline(ImagesPipeline):
    #通过抓取的图片url获取一个Request用于下载
    def get_media_requests(self, item, info):
        #交给Scrapy.Requests去访问img_url
        yield scrapy.Request(item['img_url'])
    #当下载请求完成后执行该方法
    def item_completed(self, results, item, info):
        #img_path生成文件名并且存储
        img_path = [x['path'] for ok, x in results if ok]
        #判断是否成功
        if not img_path:
            raise DropItem("Item contains no images")
        #将地址存入item
        item['img_path'] = img_path
        return item
