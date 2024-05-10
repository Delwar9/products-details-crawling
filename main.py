import time
from selenium import webdriver
from web_pages.men_page import MenPage
page_number_to_crawl = 2
def start_crawling():
    start_time = time.time()

    print("Starting crawling at: ", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(start_time)))
    with webdriver.Chrome() as driver:
        men_page = MenPage(driver)
        men_page.get_products(page_number_to_crawl)

    elapsed_time = time.time() - start_time
    print(f"Crawling runtime: {time.strftime('%H:%M:%S', time.gmtime(elapsed_time))}")


if __name__ == '__main__':
    start_crawling()
