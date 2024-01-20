import rich_click as click
import michar.api.util as util
from typing import List
from michar.cli.app.michar import gooza
import requests
from bs4 import BeautifulSoup, Tag
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

from selenium.webdriver.chrome.service import Service as BraveService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.os_manager import ChromeType



url_option : click.Option = click.option("-U", "--url", required=False, default="https://longbeach.legistar.com/calendar.aspx", type=str, help="website to crawl for data")

@gooza.command()
@url_option
def crawl(url: str):
    """
    crawl websites for data
    """
    log = util.get_logger()
    log.info(f"crawling {url}")

    #page = requests.get(url)

    driver = webdriver.Firefox()
    #driver = webdriver.Chrome(service=BraveService(ChromeDriverManager(chrome_type=ChromeType.BRAVE).install()))

    # Navigate to the .aspx page
    log.info(driver)
    driver.get(url)
    try:
        # Wait for the dynamic content to load (adjust the timeout as needed)
        # https://longbeach.legistar.com/calendar.aspx
        # TODO figure out how to crawl this javascript crap
        element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, 'ctl00_ContentPlaceHolder1_divGrid'))
        )

        # Extract data from the dynamic element
        dynamic_content = driver.find_element(By.ID, 'your_dynamic_element_id').text
        print(dynamic_content)

    finally:
        # Close the browser window
        driver.quit()

    








    # soup = BeautifulSoup(page.content, "html.parser")
    # log.debug(soup)

    # data: Tag = soup.find(id="ctl00_ContentPlaceHolder1_gridCalendar")
    # log.info(data.prettify())

    # master_table: Tag = data.find(class_='rgMasterTable')
    # print("AAA")
    # log.info(master_table)

    # entries: List[Tag] = master_table.find_all('tr')
    # log.info("SDSSSAAS")
    # log.info(entries)

    # rows: List[Tag] = entries.find_all('tr')
    # for row in rows:
    #     # Extract data from each cell in the row
    #     cells = row.find_all(['th', 'td'])
    #     row_data = [cell.text.strip() for cell in cells]
        
    #     # Process or print the row data
    #     print(row_data)
