from icrawler.builtin import BingImageCrawler

//we are building cats image detection that's why we put cat here
//if you want some other images then put that name in classes list
classes=['cats images']
number=100
//here root directory is find your root directory there u will find
//new file name data in which all images are saved.
for c in classes:
    bing_crawler=BingImageCrawler(storage={'root_dir':f'p/{c.replace(" ",".")}'})
    bing_crawler.crawl(keyword=c,filters=None,max_num=number,offset=0)