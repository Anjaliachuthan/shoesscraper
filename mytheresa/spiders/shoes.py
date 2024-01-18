import scrapy

class ShoeSpider(scrapy.Spider):
    name = "shoe"
    allowed_domains = ["www.mytheresa.com"]
    start_urls = ["https://www.mytheresa.com/int/en/men/shoes?rdr_src=mag"]

    def start_requests(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        yield scrapy.Request(url=self.start_urls[0], headers=headers, callback=self.parse)
    
    



    def parse(self, response):
        self.log(f"Visited: {response.url}")

        for pro in response.css('div.item.item--sale'):
            sizes = pro.css('div.item__sizes span.item__sizes__size::text').getall()
            

            yield {
                'image_urls': pro.css('img::attr(src)').extract_first(), 
                'brand': pro.css('div.item__info__header__designer::text').get(),
                'product_name': pro.css('div.item__info__name a::text').extract_first(),
                'discount': pro.css("div.pricing__info span::text").get(),
                'sizes': sizes,
                'Listing_prices': pro.css('span.pricing__prices__original span.pricing__prices__price::text').getall()[1],
                'offer_price':response.css('span.pricing__prices__discount span.pricing__prices__price::text').getall()[1],
                'breadcrumb': pro.css('div.breadcrumb a::text').getall(),
                
                

            }

    #     next_page = response.css('div.pagination__itemcontainer a::attr(href)').get()
    #     if next_page is not None:
    #         next_page_url= 'https://www.mytheresa.com/' + next_page
    # yield response.follow(next_page_url,callback=self.parse)

