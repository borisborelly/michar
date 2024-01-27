import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class TestAgendaclick:
    def setup_method(self, method):
        self.driver = webdriver.Firefox()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def wait_for_window(self, timeout=2):
        time.sleep(round(timeout / 1000))
        wh_now = self.driver.window_handles
        wh_then = self.vars["window_handles"]
        if len(wh_now) > len(wh_then):
            return set(wh_now).difference(set(wh_then)).pop()

    def test_agendaclick(self):
        self.driver.get(
            "https://longbeach.legistar.com/MeetingDetail.aspx?From=RSS&ID=1133618&GUID=E5F162A4-32CE-4992-B72F-E20E428C56BA"
        )
        self.driver.set_window_size(1174, 778)
        self.vars["window_handles"] = self.driver.window_handles
        self.driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_hypAgenda").click()
        self.vars["win5013"] = self.wait_for_window(2000)
        self.driver.switch_to.window(self.vars["win5013"])
