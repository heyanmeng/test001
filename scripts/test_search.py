import os,sys
sys.path.append(os.getcwd())
import pytest
from base.base_driver import init_driver
from page.search_page import SearchPage
from base.base_yml import yml_data_with_file


def data_with_key(key):
    return yml_data_with_file("search_data")[key]


class TestSearch:

    def setup(self):
        self.driver = init_driver()
        self.search_page = SearchPage(self.driver)

    @pytest.mark.parametrize("content", data_with_key("test_search"))
    def test_search(self, content):
        self.search_page.click_search()
        self.search_page.input_content(content)
        self.search_page.click_back()

    @pytest.mark.parametrize("content", data_with_key("test_search1"))
    def test_search1(self, content):
        self.search_page.click_search()
        self.search_page.input_content(content)
        self.search_page.click_back()