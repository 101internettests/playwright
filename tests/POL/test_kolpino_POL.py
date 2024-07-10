from playwright.sync_api import Page, expect
from pages.main_page import check_header, search_tariffs, one_click_form, tariffs_block, blue_form
from pages.main_page import footer_pol, blue_form_second, search_tariffs_second, sorting
from pages.POL.kolpino_page import review, check_tags, header_kolpino


def test_first_kol(page: Page):
    page.goto('https://piter-online.net/kolpino')
    check_header(page)
    footer_pol(page)
    review(page)
    one_click_form(page)
    blue_form(page)
    search_tariffs(page)
    header_kolpino(page)
    expect(page.locator('//h1[contains(text(), "Подключить домашний интернет в Колпино")]')).to_be_visible()
    expect(page.locator('(//div[contains(text(), "Подключить интернет просто – введите свой адрес, а мы поможем выбрать лучшее предложение из доступных. Даём гарантию на 90 дней и начисляем кэшбэк до 1000 рублей!")])[1]')).to_be_visible()
    expect(page.locator('//div[@datatest="main_raitingprovider_button"]')).to_have_text('Рейтинг провайдеров')
    expect(page.locator('//div[@datatest="main_comparetariff_button"]')).to_have_text('Выгодные пакеты интернета3 в 1')
    expect(page.locator('//div[@class="col-sm-6 col-lg-4"]')).to_contain_text('получили нашу помощь в выборе интернета за  15 лет')
    expect(page.locator('//div[@class="onlyNotMd onlyNotSm onlyNotXs col-lg-4"]')).to_contain_text('Бесплатная консультация')
    expect(page.locator('//div[@datatest="main_inflat_button"]')).to_contain_text('ИнтернетВ квартиру')
    expect(page.locator('//div[@datatest="main_inhouse_button"]')).to_contain_text('ИнтернетНа дачу')
    expect(page.locator('//div[@datatest="main_inoffice_button"]')).to_contain_text('ИнтернетВ офис')
    expect(page.locator('(//a[@datatest="providers_provider_alltariff_button"])[1]')).to_have_text('Показать все')
    expect(page.locator('(//div[@class="row"])[7]')).to_be_visible()
    expect(page.locator('//div[@class="row"]//div[@class="col-12 col-sm-6 col-md-4 col-lg-3"]').nth(4))
    for i in range(1, 4):
        expect(page.locator(f'(//h2)[{i}]')).to_be_visible()
    for i in range(6, 9):
        expect(page.locator(f'(//h2)[{i}]')).to_be_visible()


def test_tohome_kol(page: Page):
    page.goto('https://piter-online.net/kolpino/orders/tohome')
    check_header(page)
    footer_pol(page)
    one_click_form(page)
    blue_form(page)
    search_tariffs(page)
    header_kolpino(page)
    tariffs_block(page)
    expect(page.locator('(//span[contains(text(), "Подключить интернет")])[1]')).to_be_visible()
    expect(page.locator('//span[contains(text(), "поиск по адресу")]')).to_be_visible()
    expect(page.locator('//h1[contains(text(), "Интернет по адресу в Колпино")]')).to_be_visible()
    expect(page.locator('//div[@data-test="countRates"]')).to_be_visible()
    expect(page.locator('//div[@datatest="providers_find_adress"]')).to_be_visible()
    expect(page.locator('(//div[@itemscope])[1]')).to_be_visible()
    for i in range(1, 2):
        expect(page.locator(f'(//h2)[{i}]')).to_be_visible()
    for i in range(4, 7):
        expect(page.locator(f'(//h2)[{i}]')).to_be_visible()


def test_providers_kol(page: Page):
    page.goto('https://piter-online.net/kolpino/providers')
    check_header(page)
    footer_pol(page)
    blue_form(page)
    blue_form_second(page)
    search_tariffs_second(page)
    header_kolpino(page)
    expect(page.locator('(//span[contains(text(), "Подключить интернет")])[1]')).to_be_visible()
    expect(page.locator('//span[contains(text(), "Провайдеры Колпино")]')).to_be_visible()
    expect(page.locator('(//h2)[2]')).to_be_visible()
    expect(page.locator('(//h2)[4]')).to_be_visible()
    expect(page.locator('(//h2)[5]')).to_be_visible()
    expect(page.locator('(//a[@datatest="top_provider_block"])[1]')).to_be_visible()
    for i in range(1, 19):
        expect(page.locator(f'(//div[@datatest="providers_provider_button"])[{i}]')).to_be_visible()
    expect(page.locator('(//h2)[6]')).to_be_visible()
    expect(page.locator('(//ol[@align="left"])[1]')).to_be_visible()
    expect(page.locator('(//div[@datatest="providers_find_adress"])[1]')).to_be_visible()
    expect(page.locator('(//div[@datatest="providers_find_adress"])[2]')).to_be_visible()


def test_rating_kol(page: Page):
    page.goto('https://piter-online.net/kolpino/rating')
    check_header(page)
    footer_pol(page)
    search_tariffs_second(page)
    header_kolpino(page)
    expect(page.locator('(//span[contains(text(), "Подключить интернет")])[1]')).to_be_visible()
    expect(page.locator('//span[contains(text(), "Рейтинг провайдеров")]')).to_be_visible()
    expect(page.locator('//div[contains(text(), "Период")]')).to_be_visible()
    expect(page.locator('(//div[contains(text(), "Интернет")])[1]')).to_be_visible()
    expect(page.locator('//input[@datatest="raiting_input_filter_period"]')).to_be_visible()
    expect(page.locator('//input[@datatest="raiting_input_filter_internet_type"]')).to_be_visible()
    for i in range(1, 2):
        expect(page.locator(f'(//div[@itemprop="offers"])[{i}]')).to_be_visible()
    expect(page.locator('(//h2)[1]')).to_be_visible()
    expect(page.locator('(//h2)[2]')).to_be_visible()
    for i in range(1, 2):
        expect(page.locator('(//div[contains(text(), "К")])[6]')).to_be_visible()


def test_rates_kol(page: Page):
    page.goto('https://piter-online.net/kolpino/rates')
    check_header(page)
    footer_pol(page)
    search_tariffs(page)
    header_kolpino(page)
    sorting(page)
    expect(page.locator('(//span[contains(text(), "Подключить интернет")])[1]')).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Тарифы на интернет")])[1]')).to_be_visible()
    expect(page.locator('//h1')).to_be_visible()
    expect(page.locator('(//h2)[2]')).to_be_visible()
    for i in range(1, 4):
        expect(page.locator(f'(//div[@datatest="providers_provider_button"])[{i}]')).to_be_visible()
    expect(page.locator('(//h2)[4]')).to_be_visible()
    expect(page.locator('(//a[@datatest="top_provider_block"])[1]')).to_be_visible()
    expect(page.locator('(//h2)[1]')).to_be_visible()
    for i in range(1, 8):
        expect(page.locator(f'(//h3[@itemprop="name"])[{i}]')).to_be_visible()
    expect(page.locator('(//h3[@itemprop="name"])[1]')).to_be_visible()