# scrapy
- python 기반의 web scrawling library

scrapy 를 이용한 웹 크롤링 실행

1. 모듈 scrapy를 설치한다.
    > pip install scrapy
2. powershell을 통해 프로젝트 시작 
    > scrapy startproject [프로젝트이름]
3. 생성된 파일 내부의 spiders 폴더에 들어간다.
    > cd [프로젝트이름]
    > cd spiders
4. gensprider를 사용해 bot 생성
    > scrapy genspider [domain주소("https://"부분은빼고)]
5. 생성된 mybots.py에 스크랩 할 함수를 생성해준다.
    > 예시
        def parse(self, response):
            titles = response.xpath('//*[@id="old_content"]/table/tbody/tr/td[2]/a[1]/text()').extract()
            ratings = response.xpath('//*[@id="old_content"]/table/tbody/tr/td[2]/div/em/text()').extract()
            authors = response.xpath('//*[@id="old_content"]/table/tbody/tr/td[3]/a/text()').extract()
            cdates = response.xpath('//*[@id="old_content"]/table/tbody/tr/td[3]/text()').extract()
            
            items = []
            for idx in range(len(titles)):
                item = MoviescraperItem()
                item['title'] = titles[idx]
                item['rating'] = ratings[idx]
                item['author'] = authors[idx]
                item['cdate'] = cdates[idx]
                items.append(item)
            return items
6. settings.py를 설정하여 스크랩 데이터의 타입과 위치 파일 명 등을 지정가능
    > 예시
    FEED_FORMAT = 'csv'
    FEED_URI = 'my_news.csv'

7. 프로젝트 실행
    > scrapy crawl