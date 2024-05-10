from web_pages.product_url_crawl import product_urls_finders
from utils.utils import Utils
from web_pages.product_details_page import ProductDetailsPage


class MenPage:
    def __init__(self, driver):
        self.driver = driver

    def get_products(self, page_number):
        utils = Utils()
        product_urls = product_urls_finders(page_number)

        data = []
        for url in product_urls:
            self.driver.get(url)
            product_details_page = ProductDetailsPage(self.driver)
            data_output = product_details_page.get_formatted_data()
            data.append(data_output)
        utils.write_dict_to_csv(data, 'product_details_output.csv')
