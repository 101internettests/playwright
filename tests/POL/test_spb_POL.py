from playwright.sync_api import Page, expect
from pages.main_page import check_header, search_tariffs, one_click_form, tariffs_block, blue_form
from pages.main_page import footer_pol, blue_form_second, search_tariffs_second, sorting
from pages.POL.spb_page import review, check_tags, header_spb


def test_first(page: Page):
    page.goto('https://piter-online.net/')
    check_header(page)
    footer_pol(page)
    review(page)
    one_click_form(page)
    blue_form(page)
    search_tariffs(page)
    header_spb(page)
    expect(page.locator('//h1[contains(text(), "Подключить домашний интернет в Санкт-Петербурге")]')).to_be_visible()
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


def test_tohome(page: Page):
    page.goto('https://piter-online.net/orders/tohome')
    check_header(page)
    footer_pol(page)
    one_click_form(page)
    blue_form(page)
    search_tariffs(page)
    header_spb(page)
    tariffs_block(page)
    expect(page.locator('(//span[contains(text(), "Подключить интернет")])[1]')).to_be_visible()
    expect(page.locator('//span[contains(text(), "поиск по адресу")]')).to_be_visible()
    expect(page.locator('//h1[contains(text(), "Интернет по адресу в Санкт-Петербурге")]')).to_be_visible()
    expect(page.locator('//div[@data-test="countRates"]')).to_be_visible()
    expect(page.locator('//div[@datatest="providers_find_adress"]')).to_be_visible()
    expect(page.locator('(//div[@itemscope])[1]')).to_be_visible()
    for i in range(1, 2):
        expect(page.locator(f'(//h2)[{i}]')).to_be_visible()
    for i in range(4, 7):
        expect(page.locator(f'(//h2)[{i}]')).to_be_visible()


def test_providers(page: Page):
    page.goto('https://piter-online.net/providers')
    check_header(page)
    footer_pol(page)
    blue_form(page)
    blue_form_second(page)
    search_tariffs_second(page)
    header_spb(page)
    expect(page.locator('(//span[contains(text(), "Подключить интернет")])[1]')).to_be_visible()
    expect(page.locator('//span[contains(text(), "Провайдеры Санкт-Петербурга")]')).to_be_visible()
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
    for i in range(1, 6):
        expect(page.locator(f'(//a[@aria-label="Переключить страницу"])[{i}]')).to_be_visible()


def test_providers_second(page: Page):
    page.goto('https://piter-online.net/providers/2')
    check_header(page)
    footer_pol(page)
    blue_form(page)
    blue_form_second(page)
    search_tariffs_second(page)
    header_spb(page)
    expect(page.locator('(//span[contains(text(), "Подключить интернет")])[1]')).to_be_visible()
    expect(page.locator('//span[contains(text(), "Провайдеры Санкт-Петербурга")]')).to_be_visible()
    expect(page.locator('(//h2)[1]')).to_be_visible()
    expect(page.locator('(//h2)[3]')).to_be_visible()
    expect(page.locator('(//a[@datatest="top_provider_block"])[1]')).to_be_visible()
    for i in range(1, 30):
        expect(page.locator(f'(//div[@datatest="providers_provider_button"])[{i}]')).to_be_visible()
    expect(page.locator('(//h2)[3]')).to_be_visible()
    expect(page.locator('(//h2)[4]')).to_be_visible()
    expect(page.locator('(//div[@datatest="providers_find_adress"])[1]')).to_be_visible()
    expect(page.locator('(//div[@datatest="providers_find_adress"])[2]')).to_be_visible()
    for i in range(1, 6):
        expect(page.locator(f'(//a[@aria-label="Переключить страницу"])[{i}]')).to_be_visible()


def test_rating(page: Page):
    page.goto('https://piter-online.net/rating')
    check_header(page)
    footer_pol(page)
    search_tariffs_second(page)
    header_spb(page)
    expect(page.locator('(//span[contains(text(), "Подключить интернет")])[1]')).to_be_visible()
    expect(page.locator('//span[contains(text(), "Рейтинг провайдеров")]')).to_be_visible()
    expect(page.locator('//div[contains(text(), "Период")]')).to_be_visible()
    expect(page.locator('(//div[contains(text(), "Интернет")])[1]')).to_be_visible()
    expect(page.locator('//input[@datatest="raiting_input_filter_period"]')).to_be_visible()
    expect(page.locator('//input[@datatest="raiting_input_filter_internet_type"]')).to_be_visible()
    for i in range(1, 7):
        expect(page.locator(f'(//div[@itemprop="offers"])[{i}]')).to_be_visible()
    expect(page.locator('(//h2)[1]')).to_be_visible()
    expect(page.locator('(//h2)[2]')).to_be_visible()
    for i in range(1, 17):
        expect(page.locator(f'(//*[@id="root"]/div/div[1]/div[5]/div[5]/div[3]/div)[{i}]')).to_be_visible()


def test_rates(page: Page):
    page.goto('https://piter-online.net/rates')
    check_header(page)
    footer_pol(page)
    search_tariffs(page)
    header_spb(page)
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
    for i in range(1, 9):
        expect(page.locator(f'(//h3[@itemprop="name"])[{i}]')).to_be_visible()
    expect(page.locator('(//h3[@itemprop="name"])[1]')).to_be_visible()


def test_select_region(page: Page):
    page.goto('https://piter-online.net/select-region')
    expect(page.locator('//span[contains(text(), "Выберите город или регион")]')).to_be_visible()
    expect(page.locator('//input[@placeholder="Введите первые 3 буквы"]')).to_be_visible()
    for i in range(1, 3):
        expect(page.locator(f'(//a[@datatest="main_region_choose"][@href])[{i}]')).to_be_visible()
    expect(page.locator('(//div[contains(text(), "К")])[2]')).to_be_visible()
    expect(page.locator('(//div[contains(text(), "Л")])[2]')).to_be_visible()
    expect(page.locator('(//div[contains(text(), "С")])[2]')).to_be_visible()
    expect(page.locator('(//span[@class="icon24 icon-close"])[1]')).to_be_visible()


def test_internet_i_tv_mobile(page: Page):
    page.goto('https://piter-online.net/rates/internet-i-mobilnaya-svyaz')
    check_header(page)
    footer_pol(page)
    search_tariffs(page)
    header_spb(page)
    check_tags(page)
    sorting(page)
    expect(page.locator('(//span[contains(text(), "Подключить интернет")])[1]')).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Тарифы на интернет")])[1]')).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Интернет и мобильная связь")])[1]')).to_be_visible()
    expect(page.locator('//h1')).to_be_visible()
    expect(page.locator('(//h2)[1]')).to_be_visible()
    expect(page.locator('(//h2)[2]')).to_be_visible()
    expect(page.locator('(//h2)[4]')).to_be_visible()
    expect(page.locator('(//a[@href="/ratesmobile"])[1]')).to_be_visible()
    for i in range(2, 9):
        expect(page.locator(f'(//div[@itemprop="offers"])[{i}]')).to_be_visible()
    for i in range(2, 9):
        expect(page.locator(f'(//span[contains(text(), "Подключить")])[{i}]')).to_be_visible()
    expect(page.locator('//div[@datatest="providers_find_adress"]')).to_be_visible()
    expect(page.locator('//div[@datatest="providers_callback2"]')).to_be_visible()
    for i in range(1, 10):
        expect(page.locator(f'(//a[@datatest="top_provider_block"])[{i}]')).to_be_visible()
    for i in range(1, 14):
        expect(page.locator(f'(//h3)[{i}]')).to_be_visible()


def test_internet_tv_mobile(page: Page):
    page.goto('https://piter-online.net/rates/internet-tv-mobile')
    check_header(page)
    footer_pol(page)
    search_tariffs(page)
    header_spb(page)
    check_tags(page)
    sorting(page)
    expect(page.locator('(//span[contains(text(), "Подключить интернет")])[1]')).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Тарифы на интернет")])[1]')).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Интернет+тв+мобильная связь")])[1]')).to_be_visible()
    expect(page.locator('//h1')).to_be_visible()
    expect(page.locator('(//h2)[1]')).to_be_visible()
    expect(page.locator('(//h2)[2]')).to_be_visible()
    expect(page.locator('(//h2)[4]')).to_be_visible()
    expect(page.locator('(//a[@href="/ratesmobile"])[1]')).to_be_visible()
    for i in range(2, 16):
        expect(page.locator(f'(//div[@itemprop="offers"])[{i}]')).to_be_visible()
    for i in range(2, 16):
        expect(page.locator(f'(//span[contains(text(), "Подключить")])[{i}]')).to_be_visible()
    expect(page.locator('//div[@datatest="providers_find_adress"]')).to_be_visible()
    expect(page.locator('//div[@datatest="providers_callback2"]')).to_be_visible()
    for i in range(1, 22):
        expect(page.locator(f'(//a[@datatest="top_provider_block"])[{i}]')).to_be_visible()
    for i in range(1, 16):
        expect(page.locator(f'(//h3)[{i}]')).to_be_visible()


def test_internet_i_tv(page: Page):
    page.goto('https://piter-online.net/rates/internet-i-tv')
    check_header(page)
    footer_pol(page)
    search_tariffs(page)
    header_spb(page)
    check_tags(page)
    sorting(page)
    expect(page.locator('(//span[contains(text(), "Подключить интернет")])[1]')).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Тарифы на интернет")])[1]')).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Интернет+тв")])[1]')).to_be_visible()
    expect(page.locator('//h1')).to_be_visible()
    expect(page.locator('(//h2)[1]')).to_be_visible()
    expect(page.locator('(//h2)[2]')).to_be_visible()
    expect(page.locator('(//h2)[4]')).to_be_visible()
    expect(page.locator('(//a[@href="/ratesmobile"])[1]')).to_be_visible()
    for i in range(1, 27):
        expect(page.locator(f'(//div[@itemprop="offers"])[{i}]')).to_be_visible()
    for i in range(2, 27):
        expect(page.locator(f'(//span[contains(text(), "Подключить")])[{i}]')).to_be_visible()
    expect(page.locator('//div[@datatest="providers_find_adress"]')).to_be_visible()
    expect(page.locator('//div[@datatest="providers_callback2"]')).to_be_visible()
    for i in range(1, 22):
        expect(page.locator(f'(//a[@datatest="top_provider_block"])[{i}]')).to_be_visible()
    for i in range(1, 6):
        expect(page.locator(f'(//h3)[{i}]')).to_be_visible()


def test_nedorogoj_domashnij_internet(page: Page):
    page.goto('https://piter-online.net/rates/nedorogoj-domashnij-internet')
    check_header(page)
    footer_pol(page)
    search_tariffs(page)
    header_spb(page)
    check_tags(page)
    sorting(page)
    expect(page.locator('(//span[contains(text(), "Подключить интернет")])[1]')).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Тарифы на интернет")])[1]')).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Дешевый интернет")])[1]')).to_be_visible()
    expect(page.locator('//h1')).to_be_visible()
    expect(page.locator('(//h2)[1]')).to_be_visible()
    expect(page.locator('(//h2)[2]')).to_be_visible()
    expect(page.locator('(//h2)[4]')).to_be_visible()
    expect(page.locator('(//a[@href="/ratesmobile"])[1]')).to_be_visible()
    for i in range(1, 30):
        expect(page.locator(f'(//div[@itemprop="offers"])[{i}]')).to_be_visible()
    for i in range(2, 31):
        expect(page.locator(f'(//span[contains(text(), "Подключить")])[{i}]')).to_be_visible()
    expect(page.locator('//div[@datatest="providers_find_adress"]')).to_be_visible()
    expect(page.locator('//div[@datatest="providers_callback2"]')).to_be_visible()
    for i in range(1, 22):
        expect(page.locator(f'(//a[@datatest="top_provider_block"])[{i}]')).to_be_visible()
    for i in range(1, 19):
        expect(page.locator(f'(//h3)[{i}]')).to_be_visible()


def test_internet_300(page: Page):
    page.goto('https://piter-online.net/rates/internet-300-mbit')
    check_header(page)
    footer_pol(page)
    search_tariffs(page)
    header_spb(page)
    check_tags(page)
    sorting(page)
    expect(page.locator('(//span[contains(text(), "Подключить интернет")])[1]')).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Тарифы на интернет")])[1]')).to_be_visible()
    expect(page.locator('(//span[contains(text(), "300 мб/с")])[1]')).to_be_visible()
    expect(page.locator('//h1')).to_be_visible()
    expect(page.locator('(//h2)[1]')).to_be_visible()
    expect(page.locator('(//h2)[2]')).to_be_visible()
    expect(page.locator('(//h2)[4]')).to_be_visible()
    expect(page.locator('(//a[@href="/ratesmobile"])[1]')).to_be_visible()
    for i in range(1, 29):
        expect(page.locator(f'(//div[@itemprop="offers"])[{i}]')).to_be_visible()
    for i in range(2, 30):
        expect(page.locator(f'(//span[contains(text(), "Подключить")])[{i}]')).to_be_visible()
    expect(page.locator('//div[@datatest="providers_find_adress"]')).to_be_visible()
    expect(page.locator('//div[@datatest="providers_callback2"]')).to_be_visible()
    for i in range(1, 22):
        expect(page.locator(f'(//a[@datatest="top_provider_block"])[{i}]')).to_be_visible()
    for i in range(1, 19):
        expect(page.locator(f'(//h3)[{i}]')).to_be_visible()


def test_internet_100(page: Page):
    page.goto('https://piter-online.net/rates/internet-100-mbit')
    check_header(page)
    footer_pol(page)
    search_tariffs(page)
    header_spb(page)
    check_tags(page)
    sorting(page)
    expect(page.locator('(//span[contains(text(), "Подключить интернет")])[1]')).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Тарифы на интернет")])[1]')).to_be_visible()
    expect(page.locator('(//span[contains(text(), "100 мб/с")])[1]')).to_be_visible()
    expect(page.locator('//h1')).to_be_visible()
    expect(page.locator('(//h2)[1]')).to_be_visible()
    expect(page.locator('(//h2)[2]')).to_be_visible()
    expect(page.locator('(//h2)[4]')).to_be_visible()
    expect(page.locator('(//a[@href="/ratesmobile"])[1]')).to_be_visible()
    for i in range(1, 34):
        expect(page.locator(f'(//div[@itemprop="offers"])[{i}]')).to_be_visible()
    for i in range(2, 35):
        expect(page.locator(f'(//span[contains(text(), "Подключить")])[{i}]')).to_be_visible()
    expect(page.locator('//div[@datatest="providers_find_adress"]')).to_be_visible()
    expect(page.locator('//div[@datatest="providers_callback2"]')).to_be_visible()
    for i in range(1, 22):
        expect(page.locator(f'(//a[@datatest="top_provider_block"])[{i}]')).to_be_visible()
    for i in range(1, 16):
        expect(page.locator(f'(//h3)[{i}]')).to_be_visible()


def test_internet_500(page: Page):
    page.goto('https://piter-online.net/rates/internet-500-mbit')
    check_header(page)
    footer_pol(page)
    search_tariffs(page)
    header_spb(page)
    check_tags(page)
    sorting(page)
    expect(page.locator('(//span[contains(text(), "Подключить интернет")])[1]')).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Тарифы на интернет")])[1]')).to_be_visible()
    expect(page.locator('(//span[contains(text(), "500 мб/с")])[1]')).to_be_visible()
    expect(page.locator('//h1')).to_be_visible()
    expect(page.locator('(//h2)[1]')).to_be_visible()
    expect(page.locator('(//h2)[2]')).to_be_visible()
    expect(page.locator('(//h2)[4]')).to_be_visible()
    expect(page.locator('(//a[@href="/ratesmobile"])[1]')).to_be_visible()
    for i in range(1, 23):
        expect(page.locator(f'(//div[@itemprop="offers"])[{i}]')).to_be_visible()
    for i in range(2, 24):
        expect(page.locator(f'(//span[contains(text(), "Подключить")])[{i}]')).to_be_visible()
    expect(page.locator('//div[@datatest="providers_find_adress"]')).to_be_visible()
    expect(page.locator('//div[@datatest="providers_callback2"]')).to_be_visible()
    for i in range(1, 22):
        expect(page.locator(f'(//a[@datatest="top_provider_block"])[{i}]')).to_be_visible()
    for i in range(1, 18):
        expect(page.locator(f'(//h3)[{i}]')).to_be_visible()


def test_online_kinoteatr(page: Page):
    page.goto('https://piter-online.net/rates/online-kinoteatr')
    check_header(page)
    footer_pol(page)
    search_tariffs(page)
    header_spb(page)
    check_tags(page)
    sorting(page)
    expect(page.locator('(//span[contains(text(), "Подключить интернет")])[1]')).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Тарифы на интернет")])[1]')).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Онлайн-кинотеатр")])[1]')).to_be_visible()
    expect(page.locator('//h1')).to_be_visible()
    expect(page.locator('(//h2)[1]')).to_be_visible()
    expect(page.locator('(//h2)[2]')).to_be_visible()
    expect(page.locator('(//h2)[4]')).to_be_visible()
    expect(page.locator('(//a[@href="/ratesmobile"])[1]')).to_be_visible()
    for i in range(1, 25):
        expect(page.locator(f'(//div[@itemprop="offers"])[{i}]')).to_be_visible()
    for i in range(2, 26):
        expect(page.locator(f'(//span[contains(text(), "Подключить")])[{i}]')).to_be_visible()
    expect(page.locator('//div[@datatest="providers_find_adress"]')).to_be_visible()
    expect(page.locator('//div[@datatest="providers_callback2"]')).to_be_visible()
    for i in range(1, 22):
        expect(page.locator(f'(//a[@datatest="top_provider_block"])[{i}]')).to_be_visible()
    for i in range(1, 8):
        expect(page.locator(f'(//h3)[{i}]')).to_be_visible()