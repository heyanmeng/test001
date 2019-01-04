from selenium.webdriver.common.by import By
from base.base_action import BaseAction


class PageNetwork(BaseAction):
    # 更多按钮
    more_button = By.XPATH, "text,更多"
    network_button = By.XPATH, "text,移动网络"
    first_network_button = By.XPATH, "//*[contains(@text,'首选网络类型')]"
    network_2g_button = By.XPATH, "//*[contains(@text,'2G')]"
    network_3g_button = By.XPATH, "//*[contains(@text,'3G')]"

    def __init__(self, driver):
        super().__init__(driver)
        self.click_more()
        self.click_network()
        self.click_first_network()

    def click_more(self):
        self.click(self.more_button)

    def click_network(self):
        self.click(PageNetwork.network_button)

    def click_first_network(self):
        self.click(PageNetwork.first_network_button)

    def click_2g(self):
        self.click(PageNetwork.network_2g_button)

    def click_3g(self):
        self.click(PageNetwork.network_3g_button)

# self.driver.find_element_by_xpath("//*[contains(@text,'更多')]").click()
#         self.driver.find_element_by_xpath("//*[contains(@text,'移动网络')]").click()
#         self.driver.find_element_by_xpath("//*[contains(@text,'首选网络类型')]").click()
#         self.driver.find_element_by_xpath("//*[contains(@text,'2G')]").click()