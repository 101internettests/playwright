import pytest
import allure
from playwright.sync_api import Page, expect


@allure.step("Проверка раздела топ провайдеров на главной странице")
def check_maim_page_top_providers(page: Page):
    page.get_by_role("link", name="Тарифы провайдера Ростелеком Ростелеком").click()
    page.locator('//span[contains(text(), "Подключить интернет")]').click()
    page.get_by_role("link", name="Тарифы провайдера ТТК-Сибирь ТТК-Сибирь").click()
    page.locator('//span[contains(text(), "Подключить интернет")]').click()
    page.get_by_role("link", name="Тарифы провайдера ГК Орион ГК Орион").click()
    page.locator('//span[contains(text(), "Подключить интернет")]').click()


@allure.step("Проверка перелинковки на главной странице")
def check_linking(page: Page):
    page.get_by_role("link", name="Абакан", exact=True).click()
    page.locator('//span[contains(text(), "Подключить интернет")]').click()


@allure.step("Проверка раздела ЧАВО на главной странице в Абакане")
def check_faq(page: Page):
    page.locator('(//div[@class="container"]//span)[19]').click()
    page.locator('(//div[@class="container"]//span)[20]').click()
    page.locator('(//div[@class="container"]//span)[21]').click()
    page.locator('(//div[@class="container"]//span)[22]').click()
    page.locator('(//div[@class="container"]//span)[23]').click()
    page.locator('(//div[@class="container"]//span)[24]').click()
    page.locator('(//div[@class="container"]//span)[25]').click()
    page.locator('(//div[@class="container"]//span)[26]').click()
    page.locator('(//div[@class="container"]//span)[27]').click()
