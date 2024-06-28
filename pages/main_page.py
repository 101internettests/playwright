import pytest
from playwright.sync_api import Page, expect


def check_header(page: Page):
    expect(page.locator("#HeaderMenu")).to_contain_text("БЕСПЛАТНАЯ КОНСУЛЬТАЦИЯ")
    expect(page.locator("#HeaderMenu").get_by_role("link", name="call")).to_be_visible()
    expect(page.locator('(//div[@ datatest="main_button_enter"])[1]')).to_be_visible()
    expect(page.locator('(//div[@itemscope])[1]')).to_be_visible()
    expect(page.locator('(// div[@ datatest="main_button_enter"])[1]')).to_be_visible()
    expect(page.locator('(//a[contains(text(), "Поиск по адресу")])[1]')).to_be_visible()
    expect(page.locator('(//a[contains(text(), "провайдеры")])[1]')).to_be_visible()
    expect(page.locator('(//a[contains(text(), "рейтинг")])[1]')).to_be_visible()
    expect(page.locator('(//a[contains(text(), "Тарифы")])[1]')).to_be_visible()
    expect(page.locator('(//a[contains(text(), "Интернет в офис")])[1]')).to_be_visible()


def search_tariffs(page: Page):
    expect(page.locator('(//span[contains(text(), "Введите улицу")])[1]')).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Дом")])[1]')).to_be_visible()
    # expect(page.locator('(//span[contains(text(), "Тип подключения")])[1]')).to_be_visible()
    expect(page.locator('(//div[contains(text(), "показать тарифы")])[1]')).to_be_visible()


def search_tariffs_second(page: Page):
    expect(page.locator('(//span[contains(text(), "Введите улицу")])[1]')).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Дом")])[1]')).to_be_visible()
    # expect(page.locator('(//span[contains(text(), "Тип подключения")])[1]')).to_be_visible()
    expect(page.locator('(//div[contains(text(), "найти")])[1]')).to_be_visible()


def one_click_form(page: Page):
    expect(page.locator('//div[@id="OneClickForm"]')).to_be_visible()


def tariffs_block(page: Page):
    expect(page.locator('//div[@data-test="countRates"]')).to_be_visible()


def blue_form(page: Page):
    expect(page.locator('(//div[@datatest="providers_find_adress"])[1]')).to_be_visible()
    expect(page.locator('(//div[@datatest="providers_find_adress"]//span[contains(text(), "Введите улицу")])[1]')).to_be_visible()
    expect(page.locator('(//div[@datatest="providers_find_adress"]//span[contains(text(), "Дом")])[1]')).to_be_visible()
    expect(page.locator('(//div[@datatest="providers_find_adress"]//div[contains(text(), "Проверить")])[1]')).to_be_visible()


def blue_form_second(page: Page):
    expect(page.locator('(//div[@datatest="providers_find_adress"])[2]')).to_be_visible()
    expect(page.locator('(//div[@datatest="providers_find_adress"]//span[contains(text(), "Введите улицу")])[2]')).to_be_visible()
    expect(page.locator('(//div[@datatest="providers_find_adress"]//span[contains(text(), "Дом")])[2]')).to_be_visible()
    expect(page.locator('(//div[@datatest="providers_find_adress"]//div[contains(text(), "Проверить")])[2]')).to_be_visible()


def check_footer(page: Page):
    expect(page.locator('//section')).to_be_visible()
    expect(page.locator('//footer')).to_be_visible()
    expect(page.locator(
        '//span[contains(text(), "© 2008-2024 «101 Интернет» — поиск провайдеров по адресу")]')).to_contain_text(
        '© 2008-2024 «101 Интернет» — поиск провайдеров по адресу')
    expect(page.get_by_role("link", name="https://vk.com/ru101internet"))
    expect(page.get_by_role('link', name='https://www.odnoklassniki.ru/group/51961592610882'))
    expect(page.get_by_role('link', name='yan-dzen'))


def footer_mol(page: Page):
    expect(page.locator('//section')).to_be_visible()
    expect(page.locator('//footer')).to_be_visible()
    expect(page.locator(
        '//span[contains(text(), "© 2008-2024 «Москва Онлайн» — поиск провайдеров по адресу")]')).to_contain_text(
        '© 2008-2024 «Москва Онлайн» — поиск провайдеров по адресу')
    expect(page.get_by_role("link", name="https://vk.com/ru101internet"))
    expect(page.get_by_role('link', name='https://www.odnoklassniki.ru/group/51961592610882'))
    expect(page.get_by_role('link', name='yan-dzen'))


def footer_pol(page: Page):
    expect(page.locator('//section')).to_be_visible()
    expect(page.locator('//footer')).to_be_visible()
    expect(page.locator(
        '//span[contains(text(), "© 2008-2024 «Питер Онлайн» — поиск провайдеров по адресу")]')).to_contain_text(
        '© 2008-2024 «Питер Онлайн» — поиск провайдеров по адресу')
    expect(page.get_by_role("link", name="https://vk.com/ru101internet"))
    expect(page.get_by_role('link', name='https://www.odnoklassniki.ru/group/51961592610882'))
    expect(page.get_by_role('link', name='yan-dzen'))


def sorting(page: Page):
    expect(page.locator('//div[contains(text(), "Сортировка")]')).to_be_visible()
    expect(page.locator('//input[@name="select_providers"]')).to_be_visible()
