import pytest
from playwright.sync_api import Page, expect


@pytest.fixture()
def header(page: Page):
    expect(page.locator('(//a[@aria-label="/ryazan"] )[2]')).to_be_visible()
    expect(page.locator('(//div[@itemscope])[1]')).to_be_visible()
    expect(page.locator('(//a[@href="tel:+78003023276"])[1]')).to_be_visible()
    expect(page.locator('(// span[contains(text(), "Рязань")])[1]')).to_be_visible()
    expect(page.locator('(//a[contains(text(), "Поиск по адресу")])[1]')).to_be_visible()
    expect(page.locator('(//a[contains(text(), "провайдеры")])[1]')).to_be_visible()
    expect(page.locator('(//a[contains(text(), "рейтинг")])[1]')).to_be_visible()
    expect(page.locator('(//a[contains(text(), "Тарифы")])[1]')).to_be_visible()
    expect(page.locator('(//a[contains(text(), "Интернет в офис")])[1]')).to_be_visible()
    expect(page.locator('(// span[contains(text(), "Рязань")])[1]')).to_be_visible()

@pytest.fixture()
def search_tariffs(page: Page):
    expect(page.locator('(//span[contains(text(), "Введите улицу")])[1]')).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Дом")])[1]')).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Тип подключения")])[1]')).to_be_visible()
    expect(page.locator('(//button[contains(text(), "найти")])[1]')).to_be_visible()


@pytest.fixture()
def one_click_form(page: Page):
    expect(page.locator('//div[@id="OneClickForm"]')).to_be_visible()


@pytest.fixture()
def tariffs_block(page: Page):



@pytest.fixture()
def blue_form(page: Page):
    expect(page.locator('//div[@datatest="providers_find_adress"]')).to_be_visible()
    expect(page.locator(
        '//div[@datatest="providers_find_adress"]//span[contains(text(), "Введите улицу")]')).to_be_visible()
    expect(page.locator('//div[@datatest="providers_find_adress"]//span[contains(text(), "Дом")]')).to_be_visible()
    expect(page.locator('//div[@datatest="providers_find_adress"]//div[contains(text(), "Проверить")]')).to_be_visible()

@pytest.fixture()
def review(page: Page):



@pytest.fixture()
def tags(page: Page):


@pytest.fixture()
def seo_questions(page: Page):

@pytest.fixture()
def footer(page: Page):
    expect(page.locator('//footer')).to_be_visible()
    expect(page.locator(
        '//span[contains(text(), "© 2008-2024 «101 Интернет» — поиск провайдеров по адресу")]')).to_contain_text(
        '© 2008-2024 «101 Интернет» — поиск провайдеров по адресу')
    expect(page.get_by_role("link", name="https://vk.com/ru101internet"))
    expect(page.get_by_role('link', name='https://www.odnoklassniki.ru/group/51961592610882'))
    expect(page.get_by_role('link', name='yan-dzen'))
    expect(page.locator('//section')).to_be_visible()