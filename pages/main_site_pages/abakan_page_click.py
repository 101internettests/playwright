import pytest
import allure
from playwright.sync_api import Page, expect


@allure.step("Проверка раздела топ провайдеров в Абакане")
def check_maim_page_top_providers(page: Page):
    page.get_by_role("link", name="Тарифы провайдера Ростелеком Ростелеком").click()
    page.locator('//span[contains(text(), "Подключить интернет")]').click()
    page.get_by_role("link", name="Тарифы провайдера ТТК-Сибирь ТТК-Сибирь").click()
    page.locator('//span[contains(text(), "Подключить интернет")]').click()
    page.get_by_role("link", name="Тарифы провайдера ГК Орион ГК Орион").click()
    page.locator('//span[contains(text(), "Подключить интернет")]').click()


@allure.step("Проверка раздела топ провайдеров в Абакане на странице поиск по адресу")
def check_top_providers_to_home(page: Page):
    page.get_by_role("link", name="Тарифы провайдера Ростелеком Ростелеком").click()
    page.locator('(//a[@datatest="main_internet_button"])[1]').click()
    page.get_by_role("link", name="Тарифы провайдера ТТК-Сибирь ТТК-Сибирь").click()
    page.locator('(//a[@datatest="main_internet_button"])[1]').click()
    page.get_by_role("link", name="Тарифы провайдера ГК Орион ГК Орион").click()
    page.locator('(//a[@datatest="main_internet_button"])[1]').click()


@allure.step("Проверка раздела топ провайдеров в Абакане на странице провайдеров")
def check_top_providers_providers(page: Page):
    page.get_by_role("link", name="Тарифы провайдера Ростелеком Ростелеком").click()
    page.locator('(//a[@datatest="main_providers_button"])[1]').click()
    page.get_by_role("link", name="Тарифы провайдера ТТК-Сибирь ТТК-Сибирь").click()
    page.locator('(//a[@datatest="main_providers_button"])[1]').click()
    page.get_by_role("link", name="Тарифы провайдера ГК Орион ГК Орион").click()
    page.locator('(//a[@datatest="main_providers_button"])[1]').click()


@allure.step("Проверка перелинковки на главной странице")
def check_linking(page: Page):
    page.get_by_role("link", name="Абакан", exact=True).click()
    page.locator('//span[contains(text(), "Подключить интернет")]').click()


@allure.step("Проверка перелинковки на странице происк по адресу")
def check_linking_to_home(page: Page):
    page.get_by_role("link", name="Абакан", exact=True).click()
    page.locator('//span[contains(text(), "Карта покрытия")]').click()


@allure.step("Проверка перелинковки на странице провайдеров")
def check_linking_providers(page: Page):
    page.get_by_role("link", name="Абакан", exact=True).click()
    page.locator('(//a[@datatest="main_providers_button"])[1]').click()


@allure.step("Проверка перелинковки на странице рейтинга")
def check_linking_rating(page: Page):
    page.get_by_role("link", name="Абакан", exact=True).click()
    page.locator('(//a[@datatest="main_rating_button"])[1]').click()


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


@allure.step("Проверка раздела ЧАВО на странице поиск по адрксу в Абакане")
def check_faq_to_home(page: Page):
    page.locator('(//div[@class="container"]//span)[8]').click()
    page.locator('(//div[@class="container"]//span)[9]').click()
    page.locator('(//div[@class="container"]//span)[10]').click()
    page.locator('(//div[@class="container"]//span)[11]').click()


@allure.step("Проверка раздела ЧАВО на странице провайдеров в Абакане")
def check_faq_providers(page: Page):
    page.locator('(//div[@class="container"]//span)[8]').click()
    page.locator('(//div[@class="container"]//span)[9]').click()
    page.locator('(//div[@class="container"]//span)[10]').click()
    page.locator('(//div[@class="container"]//span)[11]').click()
    page.locator('(//div[@class="container"]//span)[12]').click()
    page.locator('(//div[@class="container"]//span)[13]').click()
    page.locator('(//div[@class="container"]//span)[14]').click()
    page.locator('(//div[@class="container"]//span)[15]').click()


@allure.step("Проверка блока с провайдерами в Абакане")
def check_providers_block(page: Page):
    for i in range(1, 19):
        page.locator(f'(//div[@datatest="providers_provider_button"])[{i}]').click()
        page.locator('(//a[@datatest="main_providers_button"])[1]').click()


@allure.step("Проверка кнопки проверить покрытие на странице провайдеры")
def check_button_coverage_providers(page: Page):
    page.locator('(//div[@data-test="providers_provider_connect_button"])[1]').click()
    expect(page.locator('(//input[@datatest="main_input_street_home_new"])[9]')).to_be_visible()
    expect(page.locator('(//input[@datatest="main_input_street_home_new"])[10]')).to_be_visible()
    page.locator('(//input[@aria-labelledby="label"])[13]').click()
    expect(page.get_by_text("В квартиру").nth(3)).to_be_visible()
    expect(page.get_by_text("В офис", exact=True).nth(2)).to_be_visible()
    page.get_by_text("На дачу").nth(3).click()
    expect(page.locator('[data-test="find_tohome_button_popup"]')).to_be_visible()
    expect(page.get_by_text(
        "Введите ваш адрес и сравните всех провайдеров своего дома в одной удобной таблице. В ней есть вся информация, необходимая для выбора провайдера: тарифы, сведения о прочих опциях, народный рейтинг провайдеров").nth(
        1)).to_be_visible()


@allure.step("Проверка кнопки проверить покрытие на странице рейтинга")
def check_button_coverage_rating(page: Page):
    page.locator('//a[@datatest="raiting_connect_button"]').click()
    expect(page.locator('(//input[@datatest="main_input_street_home_new"])[5]')).to_be_visible()
    expect(page.locator('(//input[@datatest="main_input_street_home_new"])[6]')).to_be_visible()
    page.locator('(//input[@aria-labelledby="label"])[11]').click()
    expect(page.get_by_text("В квартиру").nth(3)).to_be_visible()
    expect(page.get_by_text("В офис", exact=True).nth(2)).to_be_visible()
    page.get_by_text("На дачу").nth(3).click()
    expect(page.locator('[data-test="find_tohome_button_popup"]')).to_be_visible()
    expect(page.get_by_text(
        "Введите ваш адрес и сравните всех провайдеров своего дома в одной удобной таблице. В ней есть вся информация, необходимая для выбора провайдера: тарифы, сведения о прочих опциях, народный рейтинг провайдеров").nth(
        1)).to_be_visible()


@allure.step("Проверка блока с провайдером на странице рейтинга")
def check_block_provider_rating(page: Page):
    page.get_by_role("link", name="Ростелеком").nth(1).click()
    page.locator('(//a[@datatest="main_rating_button"])[1]').click()
    page.get_by_role("link", name="отзывов").click()
    page.locator('(//a[@datatest="main_rating_button"])[1]').click()
    page.get_by_role("link", name="Все тарифы (26)").click()
    page.locator('(//a[@datatest="main_rating_button"])[1]').click()
