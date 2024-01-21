import logging
import rich_click as click
from typing import Optional
from rich.logging import RichHandler
from rich.traceback import install
from dataclasses import dataclass, field
from selenium import webdriver
from selenium.webdriver.remote import webdriver as webdrv
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

# from selenium.webdriver.chrome.service import Service as BraveService
# from webdriver_manager.chrome import ChromeDriverManager
# from webdriver_manager.core.os_manager import ChromeType
# from selenium.webdriver.firefox.service import Service as FirefoxService
# from webdriver_manager.firefox import GeckoDriverManager

install()

logging.basicConfig(
    level="INFO",
    format="%(message)s",
    datefmt="[%X]",
    handlers=[RichHandler(rich_tracebacks=True, tracebacks_suppress=[click])],
)


def get_logger(name: Optional[str] = "util") -> logging.Logger:
    return logging.getLogger(name)

log = get_logger()

@dataclass
class Krawl(object):
    url: str
    browser: Optional[str] = "Firefox"
    _driver: RemoteWebDriver = None

    def shutdown(self):
        self._driver.close()
    
    def get_div(self, div_id: str) -> object:
        '''
        gets data from a div name
        '''
        # try:
        # finally:
        #     # Close the browser window
        #     driver.quit()

        # Wait for the dynamic content to load (adjust the timeout as needed)
        # https://longbeach.legistar.com/calendar.aspx
        div = WebDriverWait(self._driver, 20).until(
            EC.presence_of_element_located((By.ID, div_id))
        )
        return div


    def get_element(self, element_id: str):
        '''
        gets data from a dynamic element id
        '''
        dynamic_content = self._driver.find_element(By.ID, element_id)
        return dynamic_content

@dataclass
class SeleniumKrawler(Krawl):

    def __post_init__(self):
        if self.browser == "Firefox":
                self._driver = webdriver.Firefox()
        else:
            log.error("use firefox")
        # if self.browser == "Brave":
        #     _driver = webdriver.Chrome(service=BraveService(ChromeDriverManager(chrome_type=ChromeType.BRAVE).install()))

        log.debug(f"{self._driver=} {self.url}")
        # opens the web url in browser
        self._driver.get(self.url)


            

def get_crawler(url: str, impl: str = "Selenium") -> Krawl:
    '''
    gets web crawler
    '''
    log.debug(f"crawling {url=} using {impl=}")
    if impl == "Selenium":
        krawler = SeleniumKrawler(url=url)
    else:
        log.error("add another crawler impl")
    return krawler


