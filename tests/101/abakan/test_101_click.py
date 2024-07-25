import pytest
from playwright.sync_api import Page, expect
from pages.main_site_pages.abakan_page_click import check_header_abakan


def test_header_abakan(page: Page):
    page.goto('https://101internet.ru/abakan')
    check_header_abakan(page)