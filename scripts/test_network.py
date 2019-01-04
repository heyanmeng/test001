import os,sys
sys.path.append(os.getcwd())
from base.base_driver import init_driver
from page.network_page import PageNetwork

class TestSettings:
    def setup(self):
        self.driver = init_driver()
        self.network_page = PageNetwork(self.driver)

    def test_mobile_network_settings_2g(self):
        # self.network_page.click_more()
        # self.network_page.click_network()
        # self.network_page.click_first_network()
        self.network_page.click_2g()

    def test_mobile_network_settings_3g(self):
        # self.network_page.click_more()
        # self.network_page.click_network()
        # self.network_page.click_first_network()
        self.network_page.click_3g()

