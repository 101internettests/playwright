import pytest
from playwright.sync_api import Page, expect
from pages.main_site_pages.main_page_click import check_header, check_footer, check_footer_rewievs, check_footer_blog, check_footer_career


def test_header_abakan(page: Page):
    page.goto('https://101internet.ru/abakan')
    check_header(page)


def test_footer_abakan(page: Page):
    page.goto('https://101internet.ru/abakan')
    check_footer(page)
    check_footer_rewievs(page)
    check_footer_blog(page)
    check_footer_career(page)
