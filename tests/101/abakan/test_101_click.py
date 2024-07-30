import pytest
import allure
from playwright.sync_api import Page, expect
from pages.main_site_pages.main_page_click import check_header, check_footer, check_footer_rewievs, check_footer_blog, \
    check_footer_career, check_top_footer, check_maim_page, check_tariff, check_tariff_to_home, check_sorting_rating
from pages.main_site_pages.abakan_page_click import check_maim_page_top_providers, check_linking, check_faq, \
    check_faq_to_home, check_linking_to_home, check_top_providers_to_home, check_top_providers_providers, \
    check_linking_providers, check_faq_providers, check_providers_block, check_button_coverage_rating, \
    check_button_coverage_providers, check_linking_rating, check_block_provider_rating


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
    check_tariff(page)


@allure.step("Проверка страницы поиск по адресу в Абакане")
def test_page_to_home_abakan(page: Page):
    page.goto('https://101internet.ru/abakan/orders/tohome')
    check_tariff_to_home(page)
    check_linking_to_home(page)
    check_faq_to_home(page)
    check_top_providers_to_home(page)


@allure.step("Проверка страницы провайдеры в Абакане")
def test_page_providers(page: Page):
    page.goto('https://101internet.ru/abakan/providers')
    check_top_providers_providers(page)
    check_linking_providers(page)
    check_providers_block(page)
    check_faq_providers(page)
    check_button_coverage_providers(page)
    expect(page.get_by_text("Проверить возможность подключения Ростелеком по адресу")).to_be_visible()


@allure.step("Проверка страницы рейтинга в Абакане")
def test_page_providers(page: Page):
    page.goto('https://101internet.ru/abakan/rating')
    check_sorting_rating(page)
    check_linking_rating(page)
    check_block_provider_rating(page)
    check_button_coverage_rating(page)
    expect(page.get_by_text("Проверить возможность подключения Ростелеком по адресу")).to_be_visible()


