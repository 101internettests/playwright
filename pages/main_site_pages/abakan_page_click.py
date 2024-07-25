import pytest
from playwright.sync_api import Page, expect


def check_header_abakan(page: Page):
    page.goto('https://101internet.ru/abakan')
    page.locator('[(//a[@datatest="main_internet_button"])[1]]').click()
    page.get_by_role("link", name="Подключить интернет").click()
    page.get_by_role("link", name="провайдеры").click()
    page.get_by_role("link", name="Подключить интернет").click()
    page.get_by_role("link", name="рейтинг", exact=True).click()
    page.get_by_role("link", name="Подключить интернет").click()
    page.get_by_role("link", name="Тарифы").click()
    page.get_by_role("link", name="Подключить интернет").click()
    page.get_by_role("link", name="Интернет в офис").click()





