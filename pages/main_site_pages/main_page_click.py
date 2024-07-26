import pytest
from playwright.sync_api import Page, expect
from time import sleep


def check_header(page: Page):
    page.locator('(//a[@datatest="main_internet_button"])[1]').click()
    page.get_by_role("link", name="Подключить интернет").click()
    page.get_by_role("link", name="провайдеры", exact=True).click()
    page.get_by_role("link", name="Подключить интернет").click()
    page.get_by_role("link", name="рейтинг", exact=True).click()
    page.get_by_role("link", name="Подключить интернет").click()
    page.get_by_role("link", name="Тарифы", exact=True).click()
    page.get_by_role("link", name="Подключить интернет").click()
    page.locator('(//a[contains(text(), "Интернет в офис")])[1]').click()


def check_footer(page: Page):
    page.get_by_role("link", name="О нас").click()
    page.get_by_role("link", name="Подключить интернет").click()
    page.get_by_role("link", name="Оплата и гарантии").click()
    page.get_by_role("link", name="Подключить интернет").click()
    page.locator('//a[contains(text(), "Сотрудничество")]').click()
    page.goBack()
    page.get_by_role("link", name="Документы").click()
    page.get_by_role("contentinfo").locator("li").filter(has_text="Политика обработки персональных данных").click()
    page.get_by_role("link", name="Карта сайта").click()


def check_footer_career(page: Page):
    page.goto('https://101internet.ru/abakan')
    page.get_by_role("link", name="Карьера").click()


def check_footer_blog(page: Page):
    page.goto('https://101internet.ru/abakan')
    page.get_by_role("link", name="Блог").click()


def check_footer_rewievs(page: Page):
    page.goto('https://101internet.ru/abakan')
    page.get_by_role("link", name="Отзывы о компании").click()


