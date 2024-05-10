import requests
from bs4 import BeautifulSoup
import json
import os


class WebCrawler:
    def __init__(self, base_url='https://shop.adidas.jp/item/', gender='mens', limit=120):
        self.base_url = base_url
        self.gender = gender
        self.limit = limit
        self.pages = []

    def fetch_page(self, page_number):
        url = f'{self.base_url}?gender={self.gender}&limit={self.limit}&page={page_number}'
        try:
            response = requests.get(url)
            if response.status_code == 200:
                html_content = response.text
                file_path = f'adidas_page_{page_number}.html'
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(html_content)
                print(f"Webpage saved successfully as {file_path}")
                return file_path
            else:
                print(f"Failed to retrieve webpage for page {page_number}. Status code: {response.status_code}")
                return None
        except requests.exceptions.RequestException as e:
            print(f"Error occurred while fetching page {page_number}: {e}")
            return None

    def extract_products_links(self, html_content, output_file):
        soup = BeautifulSoup(html_content, 'html.parser')
        script_tag = soup.find('script', id='__NEXT_DATA__')
        if script_tag:
            script_content = script_tag.string
            start_index = script_content.find('{')
            end_index = script_content.rfind('}') + 1
            if start_index != -1 and end_index != -1:
                json_data = script_content[start_index:end_index]
                try:
                    data = json.loads(json_data)
                    articles = data['props']['pageProps']['apis']['plpInitialProps']['productListApi']['articles']
                    with open(output_file, 'w', encoding='utf-8') as f:
                        for article in articles:
                            f.write(f"https://shop.adidas.jp/products/{article}/\n")
                    print(f"Product links extracted and saved to {output_file}")
                except json.JSONDecodeError as e:
                    print(f"Error decoding JSON data: {e}")
        else:
            print("Unable to find '__NEXT_DATA__' script tag in the HTML content.")

    def combine_files(self):
        output_file = "../product_urls.txt"
        input_files = [file for file in os.listdir() if
                       file.startswith('adidas_page_') and file.endswith('_products.txt')]
        with open(output_file, 'w', encoding='utf-8') as output:
            for input_file in input_files:
                with open(input_file, 'r', encoding='utf-8') as input:
                    output.write(input.read())
        print(f"All {len(input_files)} product files have been combined into '{output_file}'.")

    def cleanup_files(self):
        # Delete all html and product link files except 'combined_products.txt'
        for filename in os.listdir():
            if filename.startswith('adidas_page_') and (
                    filename.endswith('.html') or filename.endswith('_products.txt')):
                if filename != 'combined_products.txt':
                    os.remove(filename)
                    print(f"Deleted file: {filename}")

    def crawl_pages(self, num_pages):
        for page_number in range(1, num_pages + 1):
            page_file = self.fetch_page(page_number)
            if page_file:
                self.pages.append(page_file)
                self.extract_products_links(open(page_file, 'r', encoding='utf-8').read(),
                                            f'adidas_page_{page_number}_products.txt')


def product_urls_finders(page_number):
    crawl_page_count = page_number
    crawler = WebCrawler()
    crawler.crawl_pages(crawl_page_count)
    crawler.combine_files()
    crawler.cleanup_files()

    # read the product urls from the combined file
    with open('../product_urls.txt', 'r') as file:
        product_urls = file.readlines()
    print(f"Total product URLs found: {len(product_urls)}")
    return product_urls
