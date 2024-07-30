import pytest
import allure
from playwright.sync_api import Page, expect
from pages.main_site_pages.main_page_click import check_header, check_footer, check_footer_rewievs, check_footer_blog, \
    check_footer_career, check_top_footer, check_maim_page
from pages.main_site_pages.abakan_page_click import check_maim_page_top_providers, check_linking, check_faq


@allure.step("Проверка хедера и футера в Абакане")
def test_main_page(page: Page):
    page.goto('https://101internet.ru/abakan')
    check_header(page)
    check_top_footer(page)
    check_footer(page)
    check_footer_rewievs(page)
    check_footer_blog(page)
    check_footer_career(page)


@allure.step("Проверка главной страницы в Абакане")
def test_maim_page_abakan(page: Page):
    page.goto('https://101internet.ru/abakan')
    check_maim_page(page)
    check_maim_page_top_providers(page)
    check_linking(page)
    check_faq(page)
