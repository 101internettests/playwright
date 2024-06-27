from playwright.sync_api import Page, expect
from pages.main_page import check_header, search_tariffs, one_click_form, tariffs_block, blue_form
from pages.main_page import check_footer, blue_form_second, search_tariffs_second
from pages.main_site_pages.abakan_page import review, check_tags, check_header_abakan


def test_main_page(page: Page):
    page.goto('https://101internet.ru/abakan')
    check_header(page)
    check_footer(page)
    review(page)
    one_click_form(page)
    blue_form(page)
    search_tariffs(page)
    check_header_abakan(page)
    expect(page.locator('//h1[contains(text(), "Подключить интернет")]')).to_contain_text('Подключить интернет')
    expect(page.locator('(//div[contains(text(), "Введите адрес и сравните тарифы всех провайдеров в своём доме – подключайтесь с гарантией 90 дней!")])[1]')).to_be_visible()
    expect(page.locator('(//a[@datatest="providers_provider_alltariff_button"])[1]')).to_have_text('Показать все')
    expect(page.locator('//div[@datatest="main_raitingprovider_button"]')).to_have_text('Рейтинг провайдеров')
    expect(page.locator('//div[@datatest="main_comparetariff_button"]')).to_have_text('Выгодные пакеты интернета3 в 1')
    expect(page.locator('//div[@class="col-sm-6 col-lg-4"]')).to_contain_text('получили нашу помощь в выборе интернета за  15 лет')
    expect(page.locator('//div[@class="onlyNotMd onlyNotSm onlyNotXs col-lg-4"]')).to_contain_text('Бесплатная консультация')
    expect(page.locator('(//h2[contains(text(), "Наши партнеры в Абакане")])[2]')).to_contain_text('Наши партнеры в Абакане ')
    expect(page.locator('(//div[@class="row"])[7]')).to_be_visible()
    expect(page.locator('//div[@class="row"]//div[@class="col-12 col-sm-6 col-md-4 col-lg-3"]').nth(4))
    expect(page.locator('(//h2)[9]')).to_be_visible()
    expect(page.locator('(//div[contains(text(), "Все")])[1]')).to_be_visible()
    expect(page.locator('//div[@datatest="main_inflat_button"]')).to_contain_text('ИнтернетВ квартиру')
    expect(page.locator('//div[@datatest="main_inhouse_button"]')).to_contain_text('ИнтернетНа дачу')
    expect(page.locator('//div[@datatest="main_inoffice_button"]')).to_contain_text('ИнтернетВ офис')


def test_tohome(page: Page):
    page.goto('https://101internet.ru/abakan/orders/tohome')
    check_header(page)
    check_footer(page)
    one_click_form(page)
    blue_form(page)
    search_tariffs(page)
    check_header_abakan(page)
    expect(page.locator('(//span[contains(text(), "Подключить интернет")])[1]')).to_be_visible()
    expect(page.locator('//span[contains(text(), "поиск по адресу")]')).to_be_visible()
    expect(page.locator('//h1[contains(text(), "Провайдеры интернета по адресу в Абакане")]')).to_be_visible()
    expect(page.locator('//ul[@style]')).to_be_visible()
    expect(page.locator('(//h2)[1]')).to_be_visible()
    expect(page.locator('(//h2)[2]')).to_be_visible()
    for i in range(4, 7):
        expect(page.locator(f'(//h2)[{i}]')).to_be_visible()


def test_providers(page: Page):
    page.goto('https://101internet.ru/abakan/providers')
    check_header(page)
    check_footer(page)
    search_tariffs_second(page)
    blue_form(page)
    blue_form_second(page)
    check_header_abakan(page)
    expect(page.locator('(//span[contains(text(), "Подключить интернет")])[1]')).to_be_visible()
    expect(page.locator('//span[contains(text(), "Провайдеры Абакана")]')).to_be_visible()
    expect(page.locator('(//h2)[2]')).to_be_visible()
    expect(page.locator('(//h2)[3]')).to_be_visible()
    expect(page.locator('(//a[@datatest="top_provider_block"])[1]')).to_be_visible()
    for i in range(1, 19):
        expect(page.locator(f'(//div[@datatest="providers_provider_button"])[{i}]')).to_be_visible()
    for i in range(5, 7):
        expect(page.locator(f'(//h2)[{i}]')).to_be_visible()
    expect(page.locator('(//ol[@align="left"])[1]')).to_be_visible()


def test_rating(page: Page):
    page.goto('https://101internet.ru/abakan/rating')
    check_header(page)
    check_footer(page)
    search_tariffs_second(page)
    check_header_abakan(page)
    expect(page.locator('(//span[contains(text(), "Подключить интернет")])[1]')).to_be_visible()
    expect(page.locator('//span[contains(text(), "Рейтинг провайдеров")]')).to_be_visible()
    expect(page.locator('//div[contains(text(), "Период")]')).to_be_visible()
    expect(page.locator('//div[contains(text(), "Интернет")]')).to_be_visible()
    expect(page.locator('//input[@datatest="raiting_input_filter_period"]')).to_be_visible()
    expect(page.locator('//input[@datatest="raiting_input_filter_internet_type"]')).to_be_visible()
    expect(page.locator('(//div[@itemprop="offers"])[1]')).to_be_visible()
    expect(page.locator('(//h2)[1]')).to_be_visible()
    expect(page.locator('(//h2)[2]')).to_be_visible()


def test_rates(page: Page):
    page.goto('https://101internet.ru/abakan/rates')
    check_header(page)
    check_footer(page)
    check_tags(page)
    check_header_abakan(page)
    expect(page.locator('(//span[contains(text(), "Подключить интернет")])[1]')).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Тарифы на интернет")])[1]')).to_be_visible()
    expect(page.locator('(//h1)[1]')).to_be_visible()
    expect(page.locator('(//p[@align="left"])[1]')).to_be_visible()
    expect(page.locator('(//a[@aria-current="page"])[4]')).to_be_visible()
    for i in range(1, 4):
        expect(page.locator(f'(//div[@datatest="providers_provider_button"])[{i}]')).to_be_visible()
    for i in range(2, 5):
        expect(page.locator(f'(//h2)[{i}]')).to_be_visible()
    expect(page.locator('(//a[@datatest="top_provider_block"])[1]')).to_be_visible()
    for i in range(1, 10):
        expect(page.locator(f'(//h3[@itemprop="name"])[{i}]')).to_be_visible()
    expect(page.locator('(//h3[@itemprop="name"])[1]')).to_be_visible()


