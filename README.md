## Project Description

This project aims to retrieve product details data from a dynamic e-commerce website through web crawling techniques. Given the dynamic nature of the site, the approach adopted involves converting it into a static representation by locally storing HTML files. The Beautiful Soup Python library is utilized for parsing HTML documents extracted from the locally saved files, enabling extraction of specific product URLs.

Each HTML page typically contains a substantial number of product URLs, with approximately 120 URLs per page. For the purpose of this project, two pages are selected for crawling, resulting in a total of 240 product details page URLs. Following extraction, the URLs are consolidated into a single text file for further processing.

Subsequently, Selenium WebDriver is employed to systematically navigate through each product URL link and retrieve the requisite data as per project requirements. This approach ensures robustness in handling the dynamic nature of the e-commerce website and facilitates efficient data extraction for subsequent analysis or application. 

**Key Technologies Used:**
- Beautiful Soup
- Selenium WebDriver
- Python

### Install Requirements:

```bash
pip install -r requirements.txt
```
### Run Project

```bash
python main.py
```

Thank you for reading. If you face any problem, kindly contact me via email at: delwar.hosen95@gmail.com
