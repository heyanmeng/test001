import os,sys

from selenium.webdriver.common.by import By

sys.path.append(os.getcwd())
from base.base_action import BaseAction


class SearchPage(BaseAction):

    search_button = By.ID, "com.android.settings:id/search"
    input_text_view = By.ID, "android:id/search_src_text"
    back_button = By.CLASS_NAME, "android.widget.ImageButton"

    def __init__(self, driver):
        super().__init__(driver)

    def click_search(self):
        self.click(self.search_button)

    def input_content(self,text):
        self.input_text(self.input_text_view, text)

    def click_back(self):
        self.click(self.back_button)

    # self.search_page.click_search()
    # self.search_page.input_content()
    # self.search_page.click_back()