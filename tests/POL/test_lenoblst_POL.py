from playwright.sync_api import Page, expect
from pages.main_page import check_header, search_tariffs, one_click_form, tariffs_block, blue_form, check_header_operator_page
from pages.main_page import footer_pol, blue_form_second, search_tariffs_second, sorting, check_footer
from pages.POL.lenoblast_page import review, header_lenoblast


def test_first_lenoblst(page: Page):
    page.goto('https://piter-online.net/leningradskaya-oblast')
    check_header(page)
    footer_pol(page)
    review(page)
    one_click_form(page)
    blue_form(page)
    search_tariffs(page)
    header_lenoblast(page)
    expect(page.locator('//h1[contains(text(), "Подключить домашний интернет в Ленинградской области")]')).to_be_visible()
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
    expect(page.locator('(//a[@datatest="main_allreviews_button"][contains(text(), "оставить отзыв")])[1]')).to_have_text('оставить отзыв')
    expect(page.locator('(//a[@datatest="main_allreviews_button"][contains(text(), "все отзывы")])[1]')).to_have_text('все отзывы')
    expect(page.locator('//div[@class="row"]//div[@class="col-12 col-sm-6 col-md-4 col-lg-3"]').nth(4))
    for i in range(1, 4):
        expect(page.locator(f'(//h2)[{i}]')).to_be_visible()
    for i in range(6, 9):
        expect(page.locator(f'(//h2)[{i}]')).to_be_visible()


def test_tohome_lenoblst(page: Page):
    page.goto('https://piter-online.net/leningradskaya-oblast/orders/tohome')
    check_header(page)
    footer_pol(page)
    one_click_form(page)
    blue_form(page)
    search_tariffs(page)
    header_lenoblast(page)
    tariffs_block(page)
    expect(page.locator('(//span[contains(text(), "Подключить интернет")])[1]')).to_be_visible()
    expect(page.locator('//span[contains(text(), "поиск по адресу")]')).to_be_visible()
    expect(page.locator('//h1[contains(text(), "Интернет по адресу в Ленинградской области")]')).to_be_visible()
    expect(page.locator('//div[@datatest="providers_find_adress"]')).to_be_visible()
    expect(page.locator('(//div[@itemscope])[1]')).to_be_visible()
    for i in range(1, 2):
        expect(page.locator(f'(//h2)[{i}]')).to_be_visible()
    for i in range(4, 6):
        expect(page.locator(f'(//h2)[{i}]')).to_be_visible()


def test_providers_lenoblst(page: Page):
    page.goto('https://piter-online.net/leningradskaya-oblast/providers')
    check_header(page)
    footer_pol(page)
    blue_form(page)
    blue_form_second(page)
    search_tariffs_second(page)
    header_lenoblast(page)
    expect(page.locator('(//span[contains(text(), "Подключить интернет")])[1]')).to_be_visible()
    expect(page.locator('//span[contains(text(), "Провайдеры Ленинградской области")]')).to_be_visible()
    expect(page.locator('(//h2)[2]')).to_be_visible()
    expect(page.locator('(//h2)[4]')).to_be_visible()
    expect(page.locator('(//h2)[5]')).to_be_visible()
    expect(page.locator('(//a[@datatest="top_provider_block"])[1]')).to_be_visible()
    for i in range(1, 19):
        expect(page.locator(f'(//div[@datatest="providers_provider_button"])[{i}]')).to_be_visible()
    expect(page.locator('(//h2)[6]')).to_be_visible()
    expect(page.locator('(//ol[@align="left"])[1]')).to_be_visible()


def test_providers_lenoblst_second(page: Page):
    page.goto('https://piter-online.net/leningradskaya-oblast/providers/2')
    check_header(page)
    footer_pol(page)
    blue_form(page)
    blue_form_second(page)
    search_tariffs_second(page)
    header_lenoblast(page)
    expect(page.locator('//span[contains(text(), "Провайдеры Ленинградской области")]')).to_be_visible()
    expect(page.locator('(//h2)[1]')).to_be_visible()
    expect(page.locator('(//h2)[3]')).to_be_visible()
    expect(page.locator('(//a[@datatest="top_provider_block"])[1]')).to_be_visible()
    for i in range(1, 30):
        expect(page.locator(f'(//div[@datatest="providers_provider_button"])[{i}]')).to_be_visible()
    expect(page.locator('(//h2)[4]')).to_be_visible()
    expect(page.locator('(//div[@datatest="providers_find_adress"])[1]')).to_be_visible()
    expect(page.locator('(//div[@datatest="providers_find_adress"])[2]')).to_be_visible()


def test_rating_lenoblst(page: Page):
    page.goto('https://piter-online.net/leningradskaya-oblast/rating')
    check_header(page)
    footer_pol(page)
    search_tariffs_second(page)
    header_lenoblast(page)
    expect(page.locator('(//span[contains(text(), "Подключить интернет")])[1]')).to_be_visible()
    expect(page.locator('//span[contains(text(), "Рейтинг провайдеров")]')).to_be_visible()
    expect(page.locator('//div[contains(text(), "Период")]')).to_be_visible()
    expect(page.locator('(//div[contains(text(), "Интернет")])[1]')).to_be_visible()
    expect(page.locator('//input[@datatest="raiting_input_filter_period"]')).to_be_visible()
    expect(page.locator('//input[@datatest="raiting_input_filter_internet_type"]')).to_be_visible()
    for i in range(1, 2):
        expect(page.locator(f'(//div[@itemprop="offers"])[{i}]')).to_be_visible()
    expect(page.locator('//div[@id="OneClickForm"]')).to_be_visible()
    expect(page.locator('(//h2)[1]')).to_be_visible()
    expect(page.locator('(//h2)[2]')).to_be_visible()
    for i in range(1, 25):
        expect(page.locator(f'(//*[@id="root"]/div/div[1]/div[5]/div[5]/div[3]/div)[{i}]')).to_be_visible()


def test_rates_lenoblst(page: Page):
    page.goto('https://piter-online.net/leningradskaya-oblast/rates')
    check_header(page)
    footer_pol(page)
    search_tariffs(page)
    header_lenoblast(page)
    sorting(page)
    expect(page.locator('(//span[contains(text(), "Тарифы на интернет")])[1]')).to_be_visible()
    expect(page.locator('//h1')).to_be_visible()
    expect(page.locator('(//h2)[2]')).to_be_visible()
    for i in range(1, 4):
        expect(page.locator(f'(//div[@datatest="providers_provider_button"])[{i}]')).to_be_visible()
    expect(page.locator('(//h2)[4]')).to_be_visible()
    expect(page.locator('(//a[@datatest="top_provider_block"])[1]')).to_be_visible()
    expect(page.locator('(//h2)[1]')).to_be_visible()
    for i in range(1,9):
        expect(page.locator(f'(//h3[@itemprop="name"])[{i}]')).to_be_visible()
    expect(page.locator('(//h3[@itemprop="name"])[1]')).to_be_visible()


def test_providers_betatelekom(page: Page):
    page.goto('https://piter-online.net/leningradskaya-oblast/providers/beta-telekom')
    header_lenoblast(page)
    check_footer(page)
    footer_pol(page)
    check_header(page)
    expect(page.get_by_role("link", name="Подключить интернет")).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Провайдеры Ленинградской области")])[1]')).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Бета Телеком")])[1]')).to_be_visible()
    expect(page.get_by_role("heading", name="Тарифы на домашний интернет и ТВ Бета Телеком в Ленинградской области")).to_be_visible()
    expect(page.locator('//img[@itemprop="contentUrl"]')).to_be_visible()
    search_tariffs(page)
    expect(page.get_by_role("link", name="О провайдере")).to_be_visible()
    expect(page.get_by_text("контакты", exact=True)).to_be_visible()
    expect(page.get_by_text("Город")).to_be_visible()
    expect(page.get_by_text("Главный офис")).to_be_visible()
    expect(page.get_by_text("Юридическое наименование")).to_be_visible()
    expect(page.get_by_text("другое")).to_be_visible()
    expect(page.get_by_role("heading", name="Топ провайдеров в Ленинградской области")).to_be_visible()
    expect(page.get_by_role("link", name="Тарифы провайдера Дом.ру Дом.ру")).to_be_visible()
    expect(page.get_by_role("link", name="Тарифы провайдера МТС МТС")).to_be_visible()
    expect(page.get_by_role("link", name="Тарифы провайдера Ростелеком Ростелеком")).to_be_visible()
    expect(page.get_by_role("heading", name="Недавно подключенные тарифы в Ленинградской области")).to_be_visible()
    for i in range(2, 6):
        expect(page.locator(f'(//span[contains(text(), "Подключить")])[{i}]')).to_be_visible()
    expect(page.get_by_role("heading", name="Частые вопросы")).to_be_visible()


def test_providers_betateleko(page: Page):
    page.goto('https://piter-online.net/leningradskaya-oblast/providers/beta-telekom')
    header_lenoblast(page)
    check_footer(page)
    footer_pol(page)
    check_header(page)
    expect(page.get_by_role("link", name="Подключить интернет")).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Провайдеры Ленинградской области")])[1]')).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Бета Телеком")])[1]')).to_be_visible()
    expect(page.get_by_role("heading", name="Тарифы на домашний интернет и ТВ Бета Телеком в Ленинградской области")).to_be_visible()
    expect(page.locator('//img[@itemprop="contentUrl"]')).to_be_visible()
    search_tariffs(page)
    expect(page.get_by_role("link", name="О провайдере")).to_be_visible()
    expect(page.get_by_text("контакты", exact=True)).to_be_visible()
    expect(page.get_by_text("Город")).to_be_visible()
    expect(page.get_by_text("Главный офис")).to_be_visible()
    expect(page.get_by_text("Юридическое наименование")).to_be_visible()
    expect(page.get_by_text("другое")).to_be_visible()
    expect(page.get_by_role("heading", name="Топ провайдеров в Ленинградской области")).to_be_visible()
    expect(page.get_by_role("link", name="Тарифы провайдера Дом.ру Дом.ру")).to_be_visible()
    expect(page.get_by_role("link", name="Тарифы провайдера МТС МТС")).to_be_visible()
    expect(page.get_by_role("link", name="Тарифы провайдера Ростелеком Ростелеком")).to_be_visible()
    expect(page.get_by_role("heading", name="Недавно подключенные тарифы в Ленинградской области")).to_be_visible()
    for i in range(2, 6):
        expect(page.locator(f'(//span[contains(text(), "Подключить")])[{i}]')).to_be_visible()
    expect(page.get_by_role("heading", name="Частые вопросы")).to_be_visible()


def test_operatory_lonoblast(page: Page):
    page.goto('https://piter-online.net/leningradskaya-oblast/operatory')
    header_lenoblast(page)
    check_footer(page)
    footer_pol(page)
    check_header_operator_page(page)
    expect(page.get_by_role("link", name="Подключить интернет")).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Мобильные операторы")])[1]')).to_be_visible()
    expect(page.get_by_role("heading", name="Мобильные операторы")).to_be_visible()
    for i in range(1, 7):
        expect(page.locator(f'(//span[contains(text(), "Подробнее")])[{i}]')).to_be_visible()
    for i in range(1, 7):
        expect(page.locator(f'(//div[@datatest="operators_operator_button"])[{i}]')).to_be_visible()