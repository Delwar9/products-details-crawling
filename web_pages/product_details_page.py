from selenium.webdriver.common.by import By
from utils.utils import Utils

class ProductDetailsPage:
    def __init__(self, driver):
        self.driver = driver

    IMAGE_BASE_URL: str = "https://shop.adidas.jp"
    FOOTER_CLOSE_BUTTON: tuple[str, str] = (By.XPATH, "//button[@class='footerstickyClosebutton']")
    RETURN_BUTTON: tuple[str, str] = (By.XPATH, "//a[@class='breadcrumbListItemLink backLink']")
    BREADCRUMB_TEXTS: tuple[str, str] = (By.XPATH, "//li[contains(@class,'breadcrumbListItem breadcrumbLink')]/a")
    CATEGORY_TEXT: tuple[str, str] = (By.XPATH, "//span[contains(@class,'categoryName')]")
    PRODUCT_NUMBER_TEXT: tuple[str, str] = (By.XPATH, "//li[contains(@class,'articleId')]/span")
    PRODUCT_NAME_TEXT: tuple[str, str] = (By.XPATH, "//h1[@class='itemTitle test-itemTitle']")
    PRICING_TEXT: tuple[str, str] = (By.XPATH, "//span[@class='price-value test-price-value']")
    AVAILABLE_SIZE_TEXT: tuple[str, str] = (By.XPATH, "//li[contains(@class,'sizeSelectorListItem')]/button")
    SENSE_OF_THE_SIZE_TEXTS: tuple[str, str] = (By.XPATH, "//div[contains(@class,'sizeFitBar')]/div[contains(@class,'label')]/span")
    IMAGE_LINKS: tuple[str, str] = (By.XPATH, "//div[contains(@class,'article_image') and @role='img']/img")
    PRODUCT_SUBTITLE_TEXT: tuple[str, str] = (By.XPATH, "//h4[contains(@class,'subheading')]")
    PRODUCT_COMMENT_ITEM_TEXT: tuple[str, str] = (By.XPATH, "//div[contains(@class,'commentItem')]")
    PRODUCT_FEATURE_TEXTS: tuple[str, str] = (By.XPATH, "//li[contains(@class,'articleFeaturesItem')]")
    TABLE_FIRST_COLUMN_TEXTS: tuple[str, str] = (By.XPATH, "//table[@class='sizeChartTable']/thead/tr/th")
    TABLE_ALL_ROW_TEXTS: tuple[str, str] = (By.XPATH, "//table[@class='sizeChartTable']/tbody/tr/td")
    REVIEW_STAR_TEXTS: tuple[str, str] = (By.XPATH, "//div[@class='BVRRRatingNormalImage']/img")
    REVIEW_TITLE_TEXTS: tuple[str, str] = (By.XPATH, "//span[contains(@class,'ReviewTitle')]")
    REVIEW_DATE_TEXTS: tuple[str, str] = (By.XPATH, "//span[contains(@class,'ReviewDate')]")
    REVIEW_DESCRIPTION_TEXTS: tuple[str, str] = (By.XPATH, "//span[contains(@class,'ReviewText')]")
    REVIEW_NICKNAME_TEXTS: tuple[str, str] = (By.XPATH, "//span[contains(@class,'Nickname')]")

    def get_formatted_data(self):
        utils = Utils()

        breadcrumb_elements = utils.find_elements_or_none(self.driver, self.BREADCRUMB_TEXTS)
        category_element = utils.find_element_or_none(self.driver, self.CATEGORY_TEXT)
        product_name_element = utils.find_element_or_none(self.driver, self.PRODUCT_NAME_TEXT)
        if product_name_element is not None:
            utils.scroll_to_element(self.driver, product_name_element)
        pricing_element = utils.find_element_or_none(self.driver, self.PRICING_TEXT)
        available_size_elements = utils.find_elements_or_none(self.driver, self.AVAILABLE_SIZE_TEXT)
        sense_of_the_size_elements = utils.find_elements_or_none(self.driver, self.SENSE_OF_THE_SIZE_TEXTS)
        image_link_elements = utils.find_elements_or_none(self.driver, self.IMAGE_LINKS)
        product_number_element = utils.find_element_or_none(self.driver, self.PRODUCT_NUMBER_TEXT)
        product_title_element = utils.find_element_or_none(self.driver, self.PRODUCT_SUBTITLE_TEXT)
        product_generation_description_element = utils.find_element_or_none(self.driver, self.PRODUCT_COMMENT_ITEM_TEXT)
        product_itemization_generation_description_elements = utils.find_elements_or_none(self.driver, self.PRODUCT_FEATURE_TEXTS)
        utils.scroll_to_percentage(self.driver, 30)
        table_first_column_text_elements = utils.find_elements_or_none(self.driver, self.TABLE_FIRST_COLUMN_TEXTS)
        table_all_row_text_elements = utils.find_elements_or_none(self.driver, self.TABLE_ALL_ROW_TEXTS)
        review_star_elements = utils.find_elements_or_none(self.driver, self.REVIEW_STAR_TEXTS)
        review_title_elements = utils.find_elements_or_none(self.driver, self.REVIEW_TITLE_TEXTS)
        review_date_elements = utils.find_elements_or_none(self.driver, self.REVIEW_DATE_TEXTS)
        review_description_elements = utils.find_elements_or_none(self.driver, self.REVIEW_DESCRIPTION_TEXTS)
        review_nickname_elements = utils.find_elements_or_none(self.driver, self.REVIEW_NICKNAME_TEXTS)

        coordinated_product = {
            "coordinated_product_name": product_name_element.text.strip() if product_name_element is not None else None,
            "pricing": pricing_element.text.strip() if pricing_element is not None else None,
            "product_number": product_number_element.text.strip() if product_number_element is not None else None,
            "category": category_element.text.strip() if category_element is not None else None,
            "image_urls": [image_link_element.get_attribute("src") for image_link_element in image_link_elements] if image_link_elements is not None else None,
            "product_page_url": self.driver.current_url,
            "available_sizes": [size.text.strip() for size in available_size_elements] if available_size_elements is not None else None,
            "sense_of_the_sizes": [sense.text.strip() for sense in sense_of_the_size_elements] if sense_of_the_size_elements is not None else None,
            "breadcrumbs": [breadcrumb.text.strip() for breadcrumb in breadcrumb_elements] if breadcrumb_elements is not None else None,
            "product_title": product_title_element.text.strip() if product_title_element is not None else None,
            "product_generation_description": product_generation_description_element.text.strip() if product_generation_description_element is not None else None,
            "product_itemization_generation_descriptions": [feature.text.strip() for feature in product_itemization_generation_description_elements] if product_itemization_generation_description_elements is not None else None,
            "table_first_column_contents": [cell_content.text.strip() for cell_content in table_first_column_text_elements] if table_first_column_text_elements is not None else None,
            "table_all_row_contents": [cell_content.text.strip() for cell_content in table_all_row_text_elements] if table_all_row_text_elements is not None else None,
            "review_stars": [star.get_attribute("title") for star in review_star_elements] if review_star_elements is not None else None,
            "review_titles": [title.text.strip() for title in review_title_elements] if review_title_elements is not None else None,
            "review_dates": [date.text.strip() for date in review_date_elements] if review_date_elements is not None else None,
            "review_descriptions": [description.text.strip() for description in review_description_elements] if review_description_elements is not None else None,
            "review_nicknames": [nickname.text.strip() for nickname in review_nickname_elements] if review_nickname_elements is not None else None,
        }

        return coordinated_product
