import pytest
from playwright.sync_api import Page, expect


def header(page: Page):
    expect(page.locator('(//a[@aria-label="/kolpino"])[2]')).to_be_visible()
    expect(page.locator('(// span[contains(text(), "Колпино")])[1]')).to_be_visible()
    expect(page.locator('//div[@id="HeaderMenu"]')).to_be_visible()
    expect(page.locator('(// a[@ aria-label="call"])[1]')).to_contain_text('БЕСПЛАТНАЯ КОНСУЛЬТАЦИЯ')
    expect(page.locator('(// div[@ datatest="main_button_enter"])[1]')).to_be_visible()
    expect(page.locator('(//a[contains(text(), "Поиск по адресу")])[1]')).to_be_visible()
    expect(page.locator('(//a[contains(text(), "провайдеры")])[1]')).to_be_visible()
    expect(page.locator('(//a[contains(text(), "рейтинг")])[1]')).to_be_visible()
    expect(page.locator('(//a[contains(text(), "Тарифы")])[1]')).to_be_visible()
    expect(page.locator('(//a[contains(text(), "Интернет в офис")])[1]')).to_be_visible()


def search_tariffs(page: Page):
    expect(page.locator('(//span[contains(text(), "Введите улицу")])[1]')).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Дом")])[1]')).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Тип подключения")])[1]')).to_be_visible()
    expect(page.locator('(//button[contains(text(), "показать тарифы")])[1]')).to_be_visible()


def one_click_form(page: Page):
    expect(page.locator('//div[@id="OneClickForm"]')).to_be_visible()


def tariffs_block(page: Page):
    expect(page.locator('//div[@data-test="countRates"]')).to_be_visible()


def blue_form(page: Page):
    expect(page.locator('//div[@datatest="providers_find_adress"]')).to_be_visible()
    expect(page.locator('//div[@datatest="providers_find_adress"]//span[contains(text(), "Введите улицу")]')).to_be_visible()
    expect(page.locator('//div[@datatest="providers_find_adress"]//span[contains(text(), "Дом")]')).to_be_visible()
    expect(page.locator('//div[@datatest="providers_find_adress"]//div[contains(text(), "Проверить")]')).to_be_visible()


def rewiew(page: Page):
    expect(
        page.locator('(//a[@datatest="main_allreviews_button"][contains(text(), "оставить отзыв")])[1]')).to_have_text(
        'оставить отзыв')
    expect(page.locator('(//a[@datatest="main_allreviews_button"][contains(text(), "все отзывы")])[1]')).to_have_text(
        'все отзывы')


def tags(page: Page):
    expect(page.locator('(//a[@href="/kolpino/rates/internet-i-mobilnaya-svyaz"])[1]')).to_be_visible()
    expect(page.locator('(//a[@href="/kolpino/rates/internet-tv-mobile"])[1]')).to_be_visible()
    expect(page.locator('(//a[@href="/kolpino/rates/domashnij-internet"])[1]')).to_be_visible()
    expect(page.locator('(//a[@href="/kolpino/rates/internet-i-tv"])[1]')).to_be_visible()
    expect(page.locator('(//a[@href="/kolpino/rates/nedorogoj-domashnij-internet"])[1]')).to_be_visible()
    expect(page.locator('(//a[@href="/kolpino/rates/internet-100-mbit"])[1]')).to_be_visible()
    expect(page.locator('(//a[@href="/kolpino/rates/internet-300-mbit"])[1]')).to_be_visible()
    expect(page.locator('(//a[@href="/kolpino/rates/internet-500-mbit"])[1]')).to_be_visible()
    expect(page.locator('(//a[@href="/kolpino/rates/online-kinoteatr"])[1]')).to_be_visible()


def footer(page: Page):
    expect(page.locator('//section')).to_be_visible()
    expect(page.locator('//footer')).to_be_visible()
    expect(page.locator(
        '//span[contains(text(), "© 2008-2024 «Питер Онлайн» — поиск провайдеров по адресу")]')).to_contain_text(
        '© 2008-2024 «Питер Онлайн» — поиск провайдеров по адресу')
    expect(page.get_by_role("link", name="https://vk.com/ru101internet"))
    expect(page.get_by_role('link', name='https://www.odnoklassniki.ru/group/51961592610882'))
    expect(page.get_by_role('link', name='yan-dzen'))




def sorting(page: Page):
    expect(page.locator('(//div[contains(text(), "ПРОВАЙДЕР")])[1]')).to_be_visible()
    expect(page.locator('//div[contains(text(), "Сортировка")]')).to_be_visible()
    expect(page.locator('//input[@name="select_providers"]')).to_be_visible()
    expect(page.locator('//input[@name="sort_providers"]')).to_be_visible()