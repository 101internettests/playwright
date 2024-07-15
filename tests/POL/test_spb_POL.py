from playwright.sync_api import Page, expect
from pages.main_page import check_header, search_tariffs, one_click_form, tariffs_block, blue_form, sorting_second, personal_data, tags_for_operatory
from pages.main_page import footer_pol, blue_form_second, search_tariffs_second, sorting, check_footer, terms_of_use, tags_mobile, check_header_operator_page
from pages.main_page import feedback_page, page_internet_in_office, rating_page, operators_menu_block, contact_page_pol, contact_feedback
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


def test_reviews_page(page: Page):
    page.goto('https://piter-online.net/reviews')
    check_header(page)
    footer_pol(page)
    one_click_form(page)
    header_spb(page)
    expect(page.get_by_role("heading", name="Отзывы об интернет-провайдерах Санкт-Петербурга")).to_be_visible()
    expect(page.get_by_role("link", name="Подключить интернет")).to_be_visible()
    expect(page.get_by_text("Отзывы о провайдерах в Санкт-Петербурге")).to_be_visible()
    expect(page.locator("#OneClickForm div").filter(has_text="Подберем интернет за 2").first).to_be_visible()
    expect(page.get_by_role("img", name="Фото формы в один клик")).to_be_visible()
    page.get_by_text("Номер телефона").click()
    page.locator("[data-test=\"waitingCall_button\"]").click()
    expect(page.get_by_label("Номер телефона")).to_be_visible()
    expect(page.get_by_role("link", name="оставить отзыв")).to_be_visible()
    expect(page.locator('//span[contains(text(), "Подключить интернет")]')).to_be_visible()
    expect(page.locator('(//h1)[1]')).to_be_visible()
    expect(page.locator('(//div[contains(text(), "Провайдер")])[1]')).to_be_visible()
    expect(page.locator('(//div[contains(text(), "Отзыв")])[1]')).to_be_visible()
    expect(page.locator('(//div[contains(text(), "УСЛУГА")])[1]')).to_be_visible()
    expect(page.locator('(//input[@name="change_providers"])[1]')).to_be_visible()
    expect(page.locator('(//input[@name="change_review"])[1]')).to_be_visible()
    expect(page.locator('(//input[@name="change_services"])[1]')).to_be_visible()
    expect(page.locator('(//a[@datatest="main_allreviews_button"])[2]')).to_be_visible()
    expect(page.locator('(//input[@value="Сначала новые отзывы "])[1]')).to_be_visible()
    for i in range(1, 20):
        expect(page.locator(f'(//div[@itemprop="review"])[{i}]')).to_be_visible()
    for i in range(1, 20):
        expect(page.locator(f'(//div[@itemprop="reviewRating"])[{i}]')).to_be_visible()
    for i in range(1, 20):
        expect(page.locator(f'(//div[@itemprop="reviewBody description"])[{i}]')).to_be_visible()
    for i in range(1, 20):
        expect(page.locator(f'(//textarea[@aria-labelledby="label"])[{i}]')).to_be_visible()
    for i in range(1, 20):
        expect(page.locator(f'(//button[@datatest="review_comment_send"])[{i}]')).to_be_visible()
    for i in range(1, 15):
        expect(page.locator(f'(//span[contains(text(), "Отзыв засчитан")])[{i}]')).to_be_visible()
    expect(page.locator('(//div[@aria-label="call"])[1]')).to_be_visible()
    expect(page.locator('(//div[@class="container"]//div[@class="row"])[5]')).to_be_visible()
    for i in range(1, 6):
        expect(page.locator(f'(//a[@aria-label="Переключить страницу"])[{i}]')).to_be_visible()


def test_spb_reviews2_page(page: Page):
    page.goto('https://piter-online.net/reviews/2')
    check_header(page)
    footer_pol(page)
    one_click_form(page)
    header_spb(page)
    check_footer(page)
    expect(page.get_by_role("heading", name="Отзывы об интернет-провайдерах Санкт-Петербурга")).to_be_visible()
    expect(page.get_by_role("link", name="Подключить интернет")).to_be_visible()
    expect(page.locator("#OneClickForm div").filter(has_text="Подберем интернет за 2").first).to_be_visible()
    expect(page.get_by_role("img", name="Фото формы в один клик")).to_be_visible()
    page.get_by_text("Номер телефона").click()
    page.locator("[data-test=\"waitingCall_button\"]").click()
    expect(page.get_by_label("Номер телефона")).to_be_visible()
    expect(page.get_by_role("link", name="оставить отзыв")).to_be_visible()
    expect(page.locator('//span[contains(text(), "Подключить интернет")]')).to_be_visible()
    expect(page.locator('(//h1)[1]')).to_be_visible()
    expect(page.locator('(//div[contains(text(), "Провайдер")])[1]')).to_be_visible()
    expect(page.locator('(//div[contains(text(), "Отзыв")])[1]')).to_be_visible()
    expect(page.locator('(//div[contains(text(), "УСЛУГА")])[1]')).to_be_visible()
    expect(page.locator('(//input[@name="change_providers"])[1]')).to_be_visible()
    expect(page.locator('(//input[@name="change_review"])[1]')).to_be_visible()
    expect(page.locator('(//input[@name="change_services"])[1]')).to_be_visible()
    expect(page.locator('(//a[@datatest="main_allreviews_button"])[2]')).to_be_visible()
    expect(page.locator('(//input[@value="Сначала новые отзывы "])[1]')).to_be_visible()
    for i in range(1, 20):
        expect(page.locator(f'(//div[@itemprop="review"])[{i}]')).to_be_visible()
    for i in range(1, 20):
        expect(page.locator(f'(//div[@itemprop="reviewRating"])[{i}]')).to_be_visible()
    for i in range(1, 20):
        expect(page.locator(f'(//div[@itemprop="reviewBody description"])[{i}]')).to_be_visible()
    for i in range(1, 20):
        expect(page.locator(f'(//textarea[@aria-labelledby="label"])[{i}]')).to_be_visible()
    for i in range(1, 20):
        expect(page.locator(f'(//button[@datatest="review_comment_send"])[{i}]')).to_be_visible()
    for i in range(1, 15):
        expect(page.locator(f'(//span[contains(text(), "Отзыв засчитан")])[{i}]')).to_be_visible()
    expect(page.locator('(//div[@aria-label="call"])[1]')).to_be_visible()
    expect(page.locator('(//div[@class="container"]//div[@class="row"])[5]')).to_be_visible()
    for i in range(1, 6):
        expect(page.locator(f'(//a[@aria-label="Переключить страницу"])[{i}]')).to_be_visible()


def test_spb_actions(page: Page):
    page.goto('https://piter-online.net/actions')
    check_header(page)
    footer_pol(page)
    check_footer(page)
    header_spb(page)
    expect(page.get_by_role("link", name="Подключить интернет")).to_be_visible()
    expect(page.locator('//span[contains(text(), "Акции на домашний интернет")]')).to_be_visible()
    expect(page.locator('//h1')).to_be_visible()
    sorting_second(page)
    expect(page.locator('//h2')).to_be_visible()
    for i in range(2, 20):
        expect(page.locator(f'(//span[contains(text(), "Подключить")])[{i}]')).to_be_visible()


def test_spb_actions2(page: Page):
    page.goto('https://piter-online.net/actions/2')
    check_header(page)
    footer_pol(page)
    check_footer(page)
    header_spb(page)
    expect(page.get_by_role("link", name="Подключить интернет")).to_be_visible()
    expect(page.locator('//span[contains(text(), "Акции на домашний интернет")]')).to_be_visible()
    expect(page.locator('//h1')).to_be_visible()
    sorting_second(page)
    expect(page.locator('//h2')).to_be_visible()
    for i in range(2, 20):
        expect(page.locator(f'(//span[contains(text(), "Подключить")])[{i}]')).to_be_visible()


def test_spb_terms_of_use(page: Page):
    page.goto('https://piter-online.net/about/terms-of-use')
    check_header(page)
    check_footer(page)
    footer_pol(page)
    header_spb(page)
    terms_of_use(page)


def test_spb_personal_data(page: Page):
    page.goto('https://piter-online.net/about/personal-data')
    check_header(page)
    check_footer(page)
    footer_pol(page)
    header_spb(page)
    personal_data(page)


def test_spb_contact_feedback(page: Page):
    page.goto('https://piter-online.net/feedback')
    feedback_page(page)


def test_sat_spb_page(page: Page):
    page.goto('https://piter-online.net/orders/sat')
    check_header(page)
    check_footer(page)
    footer_pol(page)
    header_spb(page)
    expect(page.locator('//h1')).to_be_visible()
    for i in range(1, 2):
        expect(page.locator(f'(//input[@datatest="order_form_input_name"])[{i}]')).to_be_visible()
    for i in range(1, 2):
        expect(page.locator(f'(//input[@datatest="order_form_input_tel"])[{i}]')).to_be_visible()
    for i in range(1, 2):
        expect(page.locator(f'(//input[@value="Нужна консультация "])[{i}]')).to_be_visible()
    for i in range(1, 2):
        expect(page.locator(f'(//div[@data-test="order_form_input_connect_button"])[{i}]')).to_be_visible()
    expect(page.locator('//div[contains(text(), "Есть из чего выбрать!")]')).to_be_visible()
    expect(page.locator('//div[contains(text(), "Максимально оперативно")]')).to_be_visible()
    expect(page.locator('//div[contains(text(), "Широкий спектр решений")]')).to_be_visible()
    expect(page.locator('//div[contains(text(), "Подключиться прямо сейчас:")]')).to_be_visible()
    expect(page.locator('//div[contains(text(), "отзывы о провайдерах")]')).to_be_visible()
    expect(page.locator('(//a[contains(text(), "оставить отзыв")])[1]')).to_be_visible()
    expect(page.locator('(//a[contains(text(), "все отзывы")])[1]')).to_be_visible()
    for i in range(1, 4):
        expect(page.locator(f'(//div[@itemtype="https://schema.org/Review"])[{i}]')).to_be_visible()


def test_office_spb_page(page: Page):
    page.goto('https://piter-online.net/orders/office')
    check_header(page)
    check_footer(page)
    footer_pol(page)
    header_spb(page)
    expect(page.locator('//h1')).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Введите улицу")])[1]')).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Дом")])[1]')).to_be_visible()
    expect(page.locator('(//input[@aria-labelledby="label"])[3]')).to_be_visible()
    expect(page.locator('//div[contains(text(), "Запустить тендер")]')).to_be_visible()
    expect(page.locator('//div[contains(text(), "Есть из чего выбрать!")]')).to_be_visible()
    expect(page.locator('//div[contains(text(), "Максимально оперативно")]')).to_be_visible()
    expect(page.locator('//div[contains(text(), "Широкий спектр решений")]')).to_be_visible()
    expect(page.locator('//div[contains(text(), "Широкий спектр решений")]')).to_be_visible()
    for i in range(1, 3):
        expect(page.locator(f'(//div[@datatest="business_inoffice_button"])[{i}]')).to_be_visible()
    expect(page.locator('(//div[@class="col-12"])[4]')).to_be_visible()
    expect(page.locator('//div[contains(text(), "Малому бизнесу")]')).to_be_visible()
    expect(page.locator('//div[contains(text(), "Среднему бизнесу")]')).to_be_visible()
    expect(page.locator('//div[contains(text(), "Крупному бизнесу")]')).to_be_visible()
    expect(page.locator('//div[contains(text(), "отзывы о провайдерах")]')).to_be_visible()
    expect(page.locator('(//a[contains(text(), "оставить отзыв")])[1]')).to_be_visible()
    expect(page.locator('(//a[contains(text(), "все отзывы")])[1]')).to_be_visible()
    for i in range(1, 4):
        expect(page.locator(f'(//div[@itemtype="https://schema.org/Review"])[{i}]')).to_be_visible()


def test_business_mosk_page(page: Page):
    page.goto('https://piter-online.net/business')
    check_header(page)
    check_footer(page)
    footer_pol(page)
    header_spb(page)
    page_internet_in_office(page)
    expect(page.locator('//h1')).to_be_visible()
    expect(page.locator('//input[@datatest="business_order_input_person"]')).to_be_visible()
    expect(page.locator('//input[@datatest="business_order_input_tel"]')).to_be_visible()
    expect(page.locator('(//input[@datatest="main_input_street_home_new"])[1]')).to_be_visible()
    expect(page.locator('(//input[@datatest="main_input_street_home_new"])[2]')).to_be_visible()


def test_address_page(page: Page):
    page.goto('https://piter-online.net/address')
    check_header(page)
    check_footer(page)
    footer_pol(page)
    header_spb(page)
    search_tariffs(page)
    expect(page.get_by_role("heading", name="Топ провайдеров в  Санкт-Петербурге")).to_be_visible()
    expect(page.get_by_role("heading", name="Зона покрытия провайдеров в районах Санкт-Петербурга")).to_be_visible()
    expect(page.get_by_role("link", name="Тарифы провайдера Дом.ру Дом.ру")).to_be_visible()
    expect(page.get_by_role("link", name="Тарифы провайдера МТС МТС")).to_be_visible()
    expect(page.get_by_role("link", name="Тарифы провайдера Ростелеком Ростелеком")).to_be_visible()
    expect(page.get_by_text("А", exact=True)).to_be_visible()
    expect(page.get_by_text("Г", exact=True)).to_be_visible()
    expect(page.get_by_text("К", exact=True).first).to_be_visible()
    expect(page.get_by_text("Л", exact=True)).to_be_visible()
    expect(page.get_by_text("М", exact=True)).to_be_visible()
    expect(page.get_by_text("Н", exact=True)).to_be_visible()
    expect(page.get_by_text("Р", exact=True)).to_be_visible()
    expect(page.get_by_text("С", exact=True).first).to_be_visible()
    expect(page.get_by_text("Ф", exact=True)).to_be_visible()
    expect(page.get_by_text("Ю", exact=True)).to_be_visible()
    expect(page.get_by_role("heading", name="Частые вопросы")).to_be_visible()
    for i in range(1, 6):
        expect(page.locator(f'(//h3)[{i}]')).to_be_visible()


def test_address_admiralteyskaya(page: Page):
    page.goto('https://piter-online.net/address/%D0%B0%D0%B4%D0%BC%D0%B8%D1%80%D0%B0%D0%BB%D1%82%D0%B5%D0%B9%D1%81%D0%BA%D0%B8%D0%B9-id1192')
    check_header(page)
    check_footer(page)
    footer_pol(page)
    header_spb(page)
    search_tariffs(page)
    blue_form(page)
    expect(page.get_by_role("link", name="Подключить интернет")).to_be_visible()
    expect(page.get_by_text("Интернет провайдеры в Адмиралтейский")).to_be_visible()
    expect(page.get_by_role("heading", name="Подключить домашний интернет в р. Адмиралтейский",
                            exact=True)).to_be_visible()
    expect(page.get_by_role("heading", name="Поиск провайдеров по адресу р. Адмиралтейский")).to_be_visible()
    expect(page.get_by_role("heading", name="Лучшие интернет тарифы р. Адмиралтейский")).to_be_visible()
    expect(page.get_by_role("heading", name="Проверьте подключение интернета р. Адмиралтейский")).to_be_visible()
    expect(page.get_by_role("heading", name="Как подключить домашний интернет в р. Адмиралтейский")).to_be_visible()
    for i in range(1, 4):
        expect(page.locator(f'(//h3)[{i}]')).to_be_visible()
    for i in range(1, 16):
        expect(page.locator(f'(//div[@datatest="providers_provider_button"])[{i}]')).to_be_visible()
    for i in range(2, 30):
        expect(page.locator(f'(//span[contains(text(), "Подключить")])[{i}]')).to_be_visible()
    for i in range(5, 20):
        expect(page.locator(f'(//a[@aria-label])[{i}]')).to_be_visible()
    for i in range(1, 5):
        expect(page.locator(f'(//h2)[{i}]')).to_be_visible()
    for i in range(1, 5):
        expect(page.locator(f'(//div[@itemprop="mainEntity"])[{i}]')).to_be_visible()


def test_address_admiralteyskaya_kaz(page: Page):
    page.goto(
            'https://piter-online.net/address/%D0%B0%D0%B4%D0%BC%D0%B8%D1%80%D0%B0%D0%BB%D1%82%D0%B5%D0%B9%D1%81%D0%BA%D0%B8%D0%B9-id1192/%D1%83%D0%BB-%D0%BA%D0%B0%D0%B7%D0%B0%D0%BD%D1%81%D0%BA%D0%B0%D1%8F-id268000')
    check_header(page)
    check_footer(page)
    footer_pol(page)
    header_spb(page)
    expect(page.locator('(//div[contains(text(), "показать тарифы")])[1]')).to_be_visible()
    expect(page.locator('(//div[@datatest="providers_find_adress"])[1]')).to_be_visible()
    expect(page.locator('(//div[@datatest="providers_find_adress"]//span[contains(text(), "Дом")])[1]')).to_be_visible()
    expect(page.locator(
        '(//div[@datatest="providers_find_adress"]//div[contains(text(), "Проверить")])[1]')).to_be_visible()
    expect(page.get_by_role("link", name="Подключить интернет")).to_be_visible()
    expect(page.get_by_text("Интернет провайдеры в Адмиралтейский")).to_be_visible()
    for i in range(1, 4):
        expect(page.locator(f'(//h3)[{i}]')).to_be_visible()
    for i in range(1, 9):
        expect(page.locator(f'(//div[@datatest="providers_provider_button"])[{i}]')).to_be_visible()
    for i in range(2, 18):
        expect(page.locator(f'(//span[contains(text(), "Подключить")])[{i}]')).to_be_visible()
    for i in range(5, 13):
        expect(page.locator(f'(//a[@aria-label])[{i}]')).to_be_visible()
    for i in range(1, 6):
        expect(page.locator(f'(//h2)[{i}]')).to_be_visible()
    for i in range(1, 5):
        expect(page.locator(f'(//div[@itemprop="mainEntity"])[{i}]')).to_be_visible()
    expect(page.get_by_role("heading", name="Интернет-провайдеры на ул. Казанская, Санкт-Петербурге")).to_be_visible()
    expect(
        page.get_by_role("heading", name="Поиск провайдеров по адресу ул. Казанская (Адмиралтейский)")).to_be_visible()
    expect(page.get_by_role("heading", name="Выберите свой дом на ул. Казанская (Адмиралтейский)")).to_be_visible()
    expect(page.get_by_role("heading",
                            name="Тарифы домашнего интернета на ул. Казанская (Адмиралтейский)")).to_be_visible()
    expect(page.get_by_text(
        "Мы выбрали для вас самые популярные предложения провайдеров на вашей улице. Всег")).to_be_visible()
    expect(page.get_by_text("ПОКАЗАТЬ ЕЩЁ")).to_be_visible()
    expect(page.get_by_role("link", name="Оставить отзыв")).to_be_visible()
    expect(
        page.get_by_role("heading", name="Как подключить интернет на ул. Казанская (Адмиралтейский)?")).to_be_visible()
    expect(page.get_by_role("heading", name="другие улицы в Санкт-Петербурге")).to_be_visible()


def test_address_house(page: Page):
    page.goto(
            'https://piter-online.net/rates?house_id=1384615')
    check_header(page)
    check_footer(page)
    footer_pol(page)
    header_spb(page)
    search_tariffs(page)
    check_tags(page)
    expect(page.get_by_role("link", name="Подключить интернет")).to_be_visible()
    expect(page.get_by_text("Тарифы на интернет", exact=True)).to_be_visible()
    expect(page.get_by_role("heading", name="Тарифы на интернет в Санкт-Петербурге")).to_be_visible()
    expect(page.get_by_role("heading", name="Найти интернет-провайдеров по адресу")).to_be_visible()
    expect(page.get_by_text("Узнайте, какие предложения доступны в вашем доме")).to_be_visible()
    for i in range(2, 24):
        expect(page.locator(f'(//span[contains(text(), "Подключить")])[{i}]')).to_be_visible()
    for i in range(1, 8):
        expect(page.locator(f'(//h2)[{i}]')).to_be_visible()
    expect(page.get_by_role("heading", name="Топ провайдеров в Санкт-Петербурге")).to_be_visible()
    expect(page.get_by_role("link", name="Тарифы провайдера Дом.ру Дом.ру")).to_be_visible()
    expect(page.get_by_role("link", name="Тарифы провайдера МТС МТС")).to_be_visible()
    expect(page.get_by_role("link", name="Тарифы провайдера Ростелеком Ростелеком")).to_be_visible()
    for i in range(1, 4):
        expect(page.locator(f'(//h3)[{i}]')).to_be_visible()
    for i in range(1, 30):
        expect(page.locator(f'(//div[@datatest="providers_provider_button"])[{i}]')).to_be_visible()
    for i in range(5, 35):
        expect(page.locator(f'(//a[@aria-label])[{i}]')).to_be_visible()
    for i in range(1, 5):
        expect(page.locator(f'(//div[@itemprop="mainEntity"])[{i}]')).to_be_visible()


def test_business_spb_addresspage(page: Page):
    page.goto('https://piter-online.net/business?house_id=3169364')
    check_header(page)
    check_footer(page)
    footer_pol(page)
    header_spb(page)
    page_internet_in_office(page)
    expect(page.locator('//h1')).to_be_visible()
    expect(page.locator('//input[@datatest="business_order_input_person"]')).to_be_visible()
    expect(page.locator('//input[@datatest="business_order_input_tel"]')).to_be_visible()
    expect(page.locator('(//input[@datatest="main_input_street_home_new"])[1]')).to_be_visible()
    expect(page.locator('(//input[@datatest="main_input_street_home_new"])[2]')).to_be_visible()


def test_rating_beeline(page: Page):
    page.goto('https://piter-online.net/rating/beeline')
    check_header(page)
    check_footer(page)
    footer_pol(page)
    header_spb(page)
    expect(page.locator('//img[@alt="Лого провайдера"]')).to_be_visible()
    expect(page.get_by_role("link", name="Подключить интернет")).to_be_visible()
    expect(page.get_by_role("link", name="Провайдеры Санкт-Петербурга")).to_be_visible()
    expect(page.locator("#provider_banner").get_by_text("билайн", exact=True)).to_be_visible()
    expect(page.get_by_role("heading", name="Отзывы о провайдере билайн в Санкт-Петербурге")).to_be_visible()
    expect(page.locator("#provider_banner").get_by_text("Оставить заявку")).to_be_visible()
    expect(page.locator("#provider_banner").get_by_text("Подключение")).to_be_visible()
    expect(page.get_by_role("link", name="+7 (812) 605-80-34")).to_be_visible()
    expect(page.locator("#provider_banner").get_by_text("Техподдержка")).to_be_visible()
    expect(page.get_by_role("link", name="+7 (800) 700-80-00")).to_be_visible()
    expect(page.get_by_text("Проверить доступность билайн по адресу")).to_be_visible()
    search_tariffs(page)
    expect(page.get_by_role("link", name="О провайдере")).to_be_visible()
    expect(page.locator('(//a[contains(text(), "Тарифы")])[3]')).to_be_visible()
    expect(page.get_by_role("link", name="акции", exact=True)).to_be_visible()
    expect(page.get_by_text("Оставить заявку").nth(1)).to_be_visible()
    rating_page(page)
    for i in range(1, 10):
        expect(page.locator(f'(//div[@itemprop="review"])[{i}]')).to_be_visible()
    for i in range(1, 10):
        expect(page.locator(f'(//div[@itemprop="reviewRating"])[{i}]')).to_be_visible()
    for i in range(1, 10):
        expect(page.locator(f'(//div[@itemprop="reviewBody description"])[{i}]')).to_be_visible()
    for i in range(1, 10):
        expect(page.locator(f'(//textarea[@aria-labelledby="label"])[{i}]')).to_be_visible()
    for i in range(1, 10):
        expect(page.locator(f'(//button[@datatest="review_comment_send"])[{i}]')).to_be_visible()
    for i in range(1, 10):
        expect(page.locator(f'(//span[contains(text(), "Отзыв засчитан")])[{i}]')).to_be_visible()
    expect(page.locator('(//div[@aria-label="call"])[1]')).to_be_visible()
    for i in range(1, 6):
        expect(page.locator(f'(//a[@aria-label="Переключить страницу"])[{i}]')).to_be_visible()


def test_rating_beeline2(page: Page):
    page.goto('https://piter-online.net/rating/beeline/2')
    check_header(page)
    check_footer(page)
    footer_pol(page)
    header_spb(page)
    expect(page.locator('//img[@alt="Лого провайдера"]')).to_be_visible()
    expect(page.get_by_role("link", name="Подключить интернет")).to_be_visible()
    expect(page.get_by_role("link", name="Провайдеры Санкт-Петербурга")).to_be_visible()
    expect(page.locator("#provider_banner").get_by_text("билайн", exact=True)).to_be_visible()
    expect(page.get_by_role("heading", name="Отзывы о провайдере билайн (beeline) в Санкт-Петербурге")).to_be_visible()
    expect(page.locator("#provider_banner").get_by_text("Оставить заявку")).to_be_visible()
    expect(page.locator("#provider_banner").get_by_text("Подключение")).to_be_visible()
    expect(page.get_by_role("link", name="+7 (812) 605-80-34")).to_be_visible()
    expect(page.locator("#provider_banner").get_by_text("Техподдержка")).to_be_visible()
    expect(page.get_by_role("link", name="+7 (800) 700-80-00")).to_be_visible()
    expect(page.get_by_text("Проверить доступность билайн по адресу")).to_be_visible()
    search_tariffs(page)
    expect(page.get_by_role("link", name="О провайдере")).to_be_visible()
    expect(page.locator('(//a[contains(text(), "Тарифы")])[3]')).to_be_visible()
    expect(page.get_by_role("link", name="акции", exact=True)).to_be_visible()
    expect(page.get_by_text("Оставить заявку").nth(1)).to_be_visible()
    rating_page(page)
    for i in range(1, 10):
        expect(page.locator(f'(//div[@itemprop="review"])[{i}]')).to_be_visible()
    for i in range(1, 10):
        expect(page.locator(f'(//div[@itemprop="reviewRating"])[{i}]')).to_be_visible()
    for i in range(1, 10):
        expect(page.locator(f'(//div[@itemprop="reviewBody description"])[{i}]')).to_be_visible()
    for i in range(1, 10):
        expect(page.locator(f'(//textarea[@aria-labelledby="label"])[{i}]')).to_be_visible()
    for i in range(1, 10):
        expect(page.locator(f'(//button[@datatest="review_comment_send"])[{i}]')).to_be_visible()
    for i in range(1, 10):
        expect(page.locator(f'(//span[contains(text(), "Отзыв засчитан")])[{i}]')).to_be_visible()
    expect(page.locator('(//div[@aria-label="call"])[1]')).to_be_visible()
    for i in range(1, 6):
        expect(page.locator(f'(//a[@aria-label="Переключить страницу"])[{i}]')).to_be_visible()


def test_provider_mts_rates(page: Page):
    page.goto('https://piter-online.net/providers/mts/rates/online-kinoteatr')
    check_header(page)
    check_footer(page)
    footer_pol(page)
    header_spb(page)
    expect(page.get_by_role("link", name="Подключить интернет")).to_be_visible()
    expect(page.get_by_role("link", name="Провайдеры Санкт-Петербурга")).to_be_visible()
    expect(page.locator('//span[contains(text(), "МТС")]')).to_be_visible()
    expect(page.locator('//span[contains(text(), "Тарифы")]')).to_be_visible()
    expect(page.locator('//span[contains(text(), "Онлайн-кинотеатр")]')).to_be_visible()
    expect(page.get_by_role("heading", name="Тарифы домашнего интернета МТС с подпиской на онлайн-кинотеатр в Санкт-Петербурге")).to_be_visible()
    expect(page.locator('//img[@alt="Лого провайдера"]')).to_be_visible()
    expect(page.locator('(//div[contains(text(), "Оставить заявку")])[2]')).to_be_visible()
    expect(page.locator("#provider_banner").get_by_text("Подключение")).to_be_visible()
    expect(page.get_by_role("link", name="+7 (812) 605-81-23")).to_be_visible()
    expect(page.locator("#provider_banner").get_by_text("Техподдержка")).to_be_visible()
    expect(page.get_by_role("link", name="+7 (800) 250-08-90")).to_be_visible()
    expect(page.get_by_text("Проверить доступность МТС по адресу")).to_be_visible()
    search_tariffs(page)
    expect(page.get_by_role("link", name="О провайдере")).to_be_visible()
    expect(page.locator('(//a[contains(text(), "Тарифы")])[3]')).to_be_visible()
    expect(page.get_by_role("link", name="акции", exact=True)).to_be_visible()
    sorting_second(page)
    for i in range(1, 15):
        expect(page.locator(f'(//div[@datatest="providers_form_inspect_connect_tariff_button"])[{i}]')).to_be_visible()
    for i in range(1, 2):
        expect(page.locator(f'(//a[@aria-label="Переключить страницу"])[{i}]')).to_be_visible()
    expect(page.locator('(//div[contains(text(), "Оставить заявку")])[2]')).to_be_visible()
    expect(page.locator('//h2')).to_be_visible()


def test_provider_mts_online_kinoteatr(page: Page):
    page.goto('https://piter-online.net/providers/mts/rates/online-kinoteatr')
    check_header(page)
    check_footer(page)
    footer_pol(page)
    header_spb(page)
    expect(page.get_by_role("link", name="Подключить интернет")).to_be_visible()
    expect(page.get_by_role("link", name="Провайдеры Санкт-Петербурга")).to_be_visible()
    expect(page.locator('//span[contains(text(), "МТС")]')).to_be_visible()
    expect(page.locator('//span[contains(text(), "Тарифы")]')).to_be_visible()
    expect(page.locator('//span[contains(text(), "Онлайн-кинотеатр")]')).to_be_visible()
    expect(page.get_by_role("heading", name="Тарифы домашнего интернета МТС с подпиской на онлайн-кинотеатр в Санкт-Петербурге")).to_be_visible()
    expect(page.locator('//img[@alt="Лого провайдера"]')).to_be_visible()
    expect(page.locator('(//div[contains(text(), "Оставить заявку")])[2]')).to_be_visible()
    expect(page.locator("#provider_banner").get_by_text("Подключение")).to_be_visible()
    expect(page.get_by_role("link", name="+7 (812) 605-81-23")).to_be_visible()
    expect(page.locator("#provider_banner").get_by_text("Техподдержка")).to_be_visible()
    expect(page.get_by_role("link", name="+7 (800) 250-08-90")).to_be_visible()
    expect(page.get_by_text("Проверить доступность МТС по адресу")).to_be_visible()
    search_tariffs(page)
    expect(page.get_by_role("link", name="О провайдере")).to_be_visible()
    expect(page.locator('(//a[contains(text(), "Тарифы")])[3]')).to_be_visible()
    expect(page.get_by_role("link", name="акции", exact=True)).to_be_visible()
    sorting_second(page)
    for i in range(1, 7):
        expect(page.locator(f'(//div[@datatest="providers_form_inspect_connect_tariff_button"])[{i}]')).to_be_visible()
    for i in range(1, 2):
        expect(page.locator(f'(//a[@aria-label="Переключить страницу"])[{i}]')).to_be_visible()
    expect(page.locator('(//div[contains(text(), "Оставить заявку")])[2]')).to_be_visible()
    expect(page.locator('//h2')).to_be_visible()


def test_provider_megafon_internet_mobil_svyaz(page: Page):
    page.goto('https://piter-online.net/providers/megafon/rates/internet-i-mobilnaya-svyaz')
    check_header(page)
    check_footer(page)
    footer_pol(page)
    header_spb(page)
    expect(page.get_by_role("link", name="Подключить интернет")).to_be_visible()
    expect(page.get_by_role("link", name="Провайдеры Санкт-Петербурга")).to_be_visible()
    expect(page.locator('//span[contains(text(), "МегаФон")]')).to_be_visible()
    expect(page.locator('//span[contains(text(), "Тарифы")]')).to_be_visible()
    expect(page.locator('//span[contains(text(), "Интернет и мобильная связь")]')).to_be_visible()
    expect(page.get_by_role("heading", name="Тарифы МегаФон на интернет и мобильную связь в Санкт-Петербурге")).to_be_visible()
    expect(page.locator('//img[@alt="Лого провайдера"]')).to_be_visible()
    expect(page.locator('(//div[contains(text(), "Оставить заявку")])[2]')).to_be_visible()
    expect(page.locator("#provider_banner").get_by_text("Подключение")).to_be_visible()
    expect(page.get_by_role("link", name="+7 (812) 605-80-64")).to_be_visible()
    expect(page.locator("#provider_banner").get_by_text("Техподдержка")).to_be_visible()
    expect(page.get_by_role("link", name="+7 (800) 550-05-00")).to_be_visible()
    expect(page.get_by_text("Проверить доступность МегаФон по адресу")).to_be_visible()
    search_tariffs(page)
    expect(page.get_by_role("link", name="О провайдере")).to_be_visible()
    expect(page.locator('(//a[contains(text(), "Тарифы")])[3]')).to_be_visible()
    expect(page.get_by_role("link", name="акции", exact=True)).to_be_visible()
    sorting_second(page)
    for i in range(2, 3):
        expect(page.locator(f'(//span[contains(text(), "Подключить")])[{i}]')).to_be_visible()
    expect(page.locator('(//div[contains(text(), "Оставить заявку")])[2]')).to_be_visible()
    expect(page.locator('//h2')).to_be_visible()


def test_provider_rostelecom_internet_tv_mobile(page: Page):
    page.goto('https://piter-online.net/providers/rostelecom/rates/internet-tv-mobile')
    check_header(page)
    check_footer(page)
    footer_pol(page)
    header_spb(page)
    expect(page.get_by_role("link", name="Подключить интернет")).to_be_visible()
    expect(page.get_by_role("link", name="Провайдеры Санкт-Петербурга")).to_be_visible()
    expect(page.locator('//span[contains(text(), "Ростелеком")]')).to_be_visible()
    expect(page.locator('//span[contains(text(), "Тарифы")]')).to_be_visible()
    expect(page.locator('//span[contains(text(), "Интернет+тв+мобильная связь")]')).to_be_visible()
    expect(page.get_by_role("heading", name="Тарифные планы Ростелеком на ТВ, интернет и мобильную связь в Санкт-Петербурге")).to_be_visible()
    expect(page.locator('//img[@alt="Лого провайдера"]')).to_be_visible()
    expect(page.locator('(//div[contains(text(), "Оставить заявку")])[2]')).to_be_visible()
    expect(page.locator("#provider_banner").get_by_text("Подключение")).to_be_visible()
    expect(page.get_by_role("link", name="+7 (812) 605-80-89")).to_be_visible()
    expect(page.locator("#provider_banner").get_by_text("Техподдержка")).to_be_visible()
    expect(page.get_by_role("link", name="+7 (800) 100-08-00")).to_be_visible()
    expect(page.get_by_text("Проверить доступность Ростелеком по адресу")).to_be_visible()
    search_tariffs(page)
    expect(page.get_by_role("link", name="О провайдере")).to_be_visible()
    expect(page.locator('(//a[contains(text(), "Тарифы")])[3]')).to_be_visible()
    expect(page.get_by_role("link", name="акции", exact=True)).to_be_visible()
    sorting_second(page)
    for i in range(2, 9):
        expect(page.locator(f'(//span[contains(text(), "Подключить")])[{i}]')).to_be_visible()
    expect(page.locator('(//div[contains(text(), "Оставить заявку")])[2]')).to_be_visible()
    expect(page.locator('//h2')).to_be_visible()


def test_provider_rostelecom(page: Page):
    page.goto('https://piter-online.net/providers/rostelecom')
    check_header(page)
    check_footer(page)
    footer_pol(page)
    header_spb(page)
    expect(page.get_by_role("link", name="Подключить интернет")).to_be_visible()
    expect(page.get_by_role("link", name="Провайдеры Санкт-Петербурга")).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Ростелеком")])[1]')).to_be_visible()
    expect(page.get_by_role("heading", name="Ростелеком – интернет-провайдер в Санкт-Петербурге")).to_be_visible()
    expect(page.locator('//img[@alt="Лого провайдера"]')).to_be_visible()
    expect(page.locator('(//div[contains(text(), "Оставить заявку")])[2]')).to_be_visible()
    expect(page.locator("#provider_banner").get_by_text("Подключение")).to_be_visible()
    expect(page.get_by_role("link", name="+7 (812) 605-80-89")).to_be_visible()
    expect(page.locator("#provider_banner").get_by_text("Техподдержка")).to_be_visible()
    expect(page.get_by_role("link", name="+7 (800) 100-08-00")).to_be_visible()
    expect(page.get_by_text("Проверить доступность Ростелеком по адресу")).to_be_visible()
    search_tariffs(page)
    expect(page.get_by_role("link", name="О провайдере")).to_be_visible()
    expect(page.locator('(//a[contains(text(), "Тарифы")])[3]')).to_be_visible()
    expect(page.get_by_role("link", name="акции", exact=True)).to_be_visible()
    for i in range(2, 7):
        expect(page.locator(f'(//span[contains(text(), "Подключить")])[{i}]')).to_be_visible()
    expect(page.locator('(//div[contains(text(), "Оставить заявку")])[2]')).to_be_visible()
    expect(page.locator('(//a[contains(text(), "Все тарифы")])[1]')).to_be_visible()
    expect(page.locator('//div[@data-test="countRates"]')).to_be_visible()
    expect(page.locator('//div[contains(text(), "Отзывы наших клиентов")]')).to_be_visible()
    for i in range(1, 8):
        expect(page.locator(f'(//div[@itemtype="https://schema.org/Review"])[{i}]')).to_be_visible()
    expect(page.locator('(//a[contains(text(), "все отзывы")])[2]')).to_be_visible()
    expect(page.locator('//div[@itemtype="http://schema.org/Organization"]')).to_be_visible()
    expect(page.locator('//span[contains(text(), "контакты")]')).to_be_visible()
    expect(page.locator('(//h2)[1]')).to_be_visible()


def test_provider_rostelecom_internet_tv(page: Page):
    page.goto('https://piter-online.net/providers/rostelecom/rates/internet-i-tv')
    check_header(page)
    check_footer(page)
    footer_pol(page)
    header_spb(page)
    expect(page.get_by_role("link", name="Подключить интернет")).to_be_visible()
    expect(page.get_by_role("link", name="Провайдеры Санкт-Петербурга")).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Ростелеком")])[1]')).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Тарифы")])[1]')).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Интернет+тв")])[1]')).to_be_visible()
    expect(page.get_by_role("heading", name="Тарифные планы Ростелеком на интернет и телевидение в Санкт-Петербурге")).to_be_visible()
    expect(page.locator('//img[@alt="Лого провайдера"]')).to_be_visible()
    expect(page.locator('(//div[contains(text(), "Оставить заявку")])[2]')).to_be_visible()
    expect(page.locator("#provider_banner").get_by_text("Подключение")).to_be_visible()
    expect(page.get_by_role("link", name="+7 (812) 605-80-89")).to_be_visible()
    expect(page.locator("#provider_banner").get_by_text("Техподдержка")).to_be_visible()
    expect(page.get_by_role("link", name="+7 (800) 100-08-00")).to_be_visible()
    expect(page.get_by_text("Проверить доступность Ростелеком по адресу")).to_be_visible()
    search_tariffs(page)
    expect(page.get_by_role("link", name="О провайдере")).to_be_visible()
    expect(page.locator('(//a[contains(text(), "Тарифы")])[3]')).to_be_visible()
    expect(page.get_by_role("link", name="акции", exact=True)).to_be_visible()
    for i in range(2, 7):
        expect(page.locator(f'(//span[contains(text(), "Подключить")])[{i}]')).to_be_visible()
    expect(page.locator('(//div[contains(text(), "Оставить заявку")])[2]')).to_be_visible()
    expect(page.locator('(//h2)[1]')).to_be_visible()


def test_provider_rostelecom_dom_internet(page: Page):
    page.goto('https://piter-online.net/providers/rostelecom/rates/nedorogoj-domashnij-internet')
    check_header(page)
    check_footer(page)
    footer_pol(page)
    header_spb(page)
    expect(page.get_by_role("link", name="Подключить интернет")).to_be_visible()
    expect(page.get_by_role("link", name="Провайдеры Санкт-Петербурга")).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Ростелеком")])[1]')).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Тарифы")])[1]')).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Дешевый интернет")])[1]')).to_be_visible()
    expect(page.get_by_role("heading", name="Выгодные тарифы Ростелеком на интернет в Санкт-Петербурге")).to_be_visible()
    expect(page.locator('//img[@alt="Лого провайдера"]')).to_be_visible()
    expect(page.locator('(//div[contains(text(), "Оставить заявку")])[2]')).to_be_visible()
    expect(page.locator("#provider_banner").get_by_text("Подключение")).to_be_visible()
    expect(page.get_by_role("link", name="+7 (812) 605-80-89")).to_be_visible()
    expect(page.locator("#provider_banner").get_by_text("Техподдержка")).to_be_visible()
    expect(page.get_by_role("link", name="+7 (800) 100-08-00")).to_be_visible()
    expect(page.get_by_text("Проверить доступность Ростелеком по адресу")).to_be_visible()
    search_tariffs(page)
    expect(page.get_by_role("link", name="О провайдере")).to_be_visible()
    expect(page.locator('(//a[contains(text(), "Тарифы")])[3]')).to_be_visible()
    expect(page.get_by_role("link", name="акции", exact=True)).to_be_visible()
    for i in range(2, 16):
        expect(page.locator(f'(//span[contains(text(), "Подключить")])[{i}]')).to_be_visible()
    for i in range(1, 2):
        expect(page.locator(f'(//a[@aria-label="Переключить страницу"])[{i}]')).to_be_visible()
    expect(page.locator('(//div[contains(text(), "Оставить заявку")])[2]')).to_be_visible()
    expect(page.locator('(//h2)[1]')).to_be_visible()


def test_provider_rostelecom_rates(page: Page):
    page.goto('https://piter-online.net/providers/rostelecom/rates')
    check_header(page)
    check_footer(page)
    footer_pol(page)
    header_spb(page)
    expect(page.get_by_role("link", name="Подключить интернет")).to_be_visible()
    expect(page.get_by_role("link", name="Провайдеры Санкт-Петербурга")).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Ростелеком")])[1]')).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Тарифы")])[1]')).to_be_visible()
    expect(page.get_by_role("heading", name="Тарифные планы от Ростелеком в Санкт-Петербурге")).to_be_visible()
    expect(page.locator('//img[@alt="Лого провайдера"]')).to_be_visible()
    expect(page.locator('(//div[contains(text(), "Оставить заявку")])[2]')).to_be_visible()
    expect(page.locator("#provider_banner").get_by_text("Подключение")).to_be_visible()
    expect(page.get_by_role("link", name="+7 (812) 605-80-89")).to_be_visible()
    expect(page.locator("#provider_banner").get_by_text("Техподдержка")).to_be_visible()
    expect(page.get_by_role("link", name="+7 (800) 100-08-00")).to_be_visible()
    expect(page.get_by_text("Проверить доступность Ростелеком по адресу")).to_be_visible()
    search_tariffs(page)
    expect(page.get_by_role("link", name="О провайдере")).to_be_visible()
    expect(page.locator('(//a[contains(text(), "Тарифы")])[3]')).to_be_visible()
    expect(page.get_by_role("link", name="акции", exact=True)).to_be_visible()
    for i in range(2, 16):
        expect(page.locator(f'(//span[contains(text(), "Подключить")])[{i}]')).to_be_visible()
    for i in range(1, 2):
        expect(page.locator(f'(//a[@aria-label="Переключить страницу"])[{i}]')).to_be_visible()
    expect(page.locator('(//div[contains(text(), "Оставить заявку")])[2]')).to_be_visible()
    expect(page.locator('(//h2)[1]')).to_be_visible()


def test_provider_mts_online_cinema(page: Page):
    page.goto('https://piter-online.net/providers/mts/rates/online-kinoteatr')
    check_header(page)
    check_footer(page)
    footer_pol(page)
    header_spb(page)
    expect(page.get_by_role("link", name="Подключить интернет")).to_be_visible()
    expect(page.get_by_role("link", name="Провайдеры Санкт-Петербурга")).to_be_visible()
    expect(page.locator('(//span[contains(text(), "МТС")])[1]')).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Тарифы")])[1]')).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Онлайн-кинотеатр")])[1]')).to_be_visible()
    expect(page.get_by_role("heading", name="Тарифы домашнего интернета МТС с подпиской на онлайн-кинотеатр в Санкт-Петербурге")).to_be_visible()
    expect(page.locator('//img[@alt="Лого провайдера"]')).to_be_visible()
    expect(page.locator('(//div[contains(text(), "Оставить заявку")])[2]')).to_be_visible()
    expect(page.locator("#provider_banner").get_by_text("Подключение")).to_be_visible()
    expect(page.get_by_role("link", name="+7 (812) 605-81-23")).to_be_visible()
    expect(page.locator("#provider_banner").get_by_text("Техподдержка")).to_be_visible()
    expect(page.get_by_role("link", name="+7 (800) 250-08-90")).to_be_visible()
    expect(page.get_by_text("Проверить доступность МТС по адресу")).to_be_visible()
    search_tariffs(page)
    expect(page.get_by_role("link", name="О провайдере")).to_be_visible()
    expect(page.locator('(//a[contains(text(), "Тарифы")])[3]')).to_be_visible()
    expect(page.get_by_role("link", name="акции", exact=True)).to_be_visible()
    for i in range(2, 16):
        expect(page.locator(f'(//span[contains(text(), "Подключить")])[{i}]')).to_be_visible()
    for i in range(1, 2):
        expect(page.locator(f'(//a[@aria-label="Переключить страницу"])[{i}]')).to_be_visible()
    expect(page.locator('(//div[contains(text(), "Оставить заявку")])[2]')).to_be_visible()
    expect(page.locator('(//h2)[1]')).to_be_visible()


def test_providers_beeline(page: Page):
    page.goto('https://piter-online.net/providers/actions/beeline')
    check_header(page)
    check_footer(page)
    footer_pol(page)
    header_spb(page)
    expect(page.get_by_role("link", name="Подключить интернет")).to_be_visible()
    expect(page.get_by_role("link", name="Провайдеры Санкт-Петербурга")).to_be_visible()
    expect(page.locator('(//span[contains(text(), "билайн")])[1]')).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Акции")])[1]')).to_be_visible()
    expect(page.get_by_role("heading", name="Акции интернет-провайдера билайн в Санкт-Петербурге")).to_be_visible()
    expect(page.locator('//img[@alt="Лого провайдера"]')).to_be_visible()
    expect(page.locator('(//div[contains(text(), "Оставить заявку")])[2]')).to_be_visible()
    expect(page.locator("#provider_banner").get_by_text("Подключение")).to_be_visible()
    expect(page.get_by_role("link", name="+7 (812) 605-80-34")).to_be_visible()
    expect(page.locator("#provider_banner").get_by_text("Техподдержка")).to_be_visible()
    expect(page.get_by_role("link", name="+7 (800) 700-80-00")).to_be_visible()
    expect(page.get_by_text("Проверить доступность билайн по адресу")).to_be_visible()
    search_tariffs(page)
    sorting_second(page)
    expect(page.get_by_role("link", name="О провайдере")).to_be_visible()
    expect(page.locator('(//a[contains(text(), "Тарифы")])[3]')).to_be_visible()
    expect(page.get_by_role("link", name="акции", exact=True)).to_be_visible()
    for i in range(2, 16):
        expect(page.locator(f'(//span[contains(text(), "Подключить")])[{i}]')).to_be_visible()
    expect(page.locator('(//div[contains(text(), "Оставить заявку")])[2]')).to_be_visible()
    expect(page.locator('(//h2)[1]')).to_be_visible()


def test_spb_partners(page: Page):
    page.goto('https://piter-online.net/about/partners')
    check_header_operator_page(page)
    check_footer(page)
    footer_pol(page)
    header_spb(page)
    expect(page.locator('(//span[contains(text(), "Подключить интернет")])[1]')).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Сотрудничество")])[1]')).to_be_visible()
    expect(page.locator('//h1')).to_be_visible()
    expect(page.get_by_text("Стать партнером")).to_be_visible()
    expect(page.get_by_text(
        "Ставки - выше. Охват - шире. Выплаты - быстрее. Доброе человеческое отношение!")).to_be_visible()
    expect(page.get_by_text("Заполни заявку сейчас и начни зарабатывать больше вместе с лидером рынка")).to_be_visible()
    expect(page.get_by_placeholder("Ваше имя*")).to_be_visible()
    expect(page.get_by_placeholder("Ваш телефон*")).to_be_visible()
    expect(page.get_by_text("Отправить", exact=True)).to_be_visible()
    expect(page.get_by_text("Обратная связь").first).to_be_visible()
    expect(page.get_by_role("link", name="Обратная связь")).to_be_visible()
    expect(page.get_by_text("e-mail", exact=True)).to_be_visible()
    expect(page.get_by_role("link", name="pr@piter-online.net")).to_be_visible()


def test_spb_contacts(page: Page):
    page.goto('https://piter-online.net/about/contacts')
    contact_page_pol(page)


def test_operatory_mts(page: Page):
    page.goto('https://piter-online.net/operatory/mts')
    check_header_operator_page(page)
    check_footer(page)
    footer_pol(page)
    header_spb(page)
    expect(page.get_by_role("link", name="Подключить интернет")).to_be_visible()
    expect(page.get_by_role("link", name="Мобильные операторы")).to_be_visible()
    expect(page.locator('(//span[contains(text(), "МТС")])[1]')).to_be_visible()
    expect(page.get_by_role("heading", name="Оператор мобильной связи МТС")).to_be_visible()
    expect(page.locator('//img[@itemprop="contentUrl"]')).to_be_visible()
    expect(page.locator('(//div[contains(text(), "Подключение")])[1]')).to_be_visible()
    expect(page.locator('(//a[contains(text(), "+7  (800)  250-08-90")])[1]')).to_be_visible()
    expect(page.locator('(//div[contains(text(), "Техподдержка")])[1]')).to_be_visible()
    expect(page.get_by_role("link", name="Об операторе")).to_be_visible()
    expect(page.get_by_role("link", name="Тарифы").nth(1)).to_be_visible()
    expect(page.get_by_role("link", name="акции", exact=True)).to_be_visible()
    expect(page.get_by_role("link", name="в 1")).to_be_visible()
    tags_mobile(page)
    for i in range(1, 15):
        expect(page.locator(f'(//div[contains(text(), "Выбрать")])[{i}]')).to_be_visible()
    expect(page.get_by_text("ПОКАЗАТЬ ЕЩЁ")).to_be_visible()
    expect(page.get_by_role("heading", name="Отзывы жителей Санкт-Петербурга")).to_be_visible()
    expect(page.get_by_text("контакты", exact=True)).to_be_visible()
    expect(page.get_by_text("ГородСанкт-Петербург")).to_be_visible()
    expect(page.get_by_text("Главный офиспр-т Невский д.32 А")).to_be_visible()


def test_operatory_spb(page: Page):
    page.goto('https://piter-online.net/operatory')
    header_spb(page)
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


def test_operator_mts_ratesmobile(page: Page):
    page.goto('https://piter-online.net/operatory/mts/ratesmobile')
    check_header_operator_page(page)
    check_footer(page)
    footer_pol(page)
    header_spb(page)
    expect(page.get_by_role("link", name="Подключить интернет")).to_be_visible()
    expect(page.get_by_role("link", name="Мобильные операторы")).to_be_visible()
    expect(page.locator('(//span[contains(text(), "МТС")])[1]')).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Тарифы")])[1]')).to_be_visible()
    expect(page.get_by_role("heading", name="Мобильные тарифы МТС")).to_be_visible()
    expect(page.locator('//img[@itemprop="contentUrl"]')).to_be_visible()
    expect(page.locator("#operator_banner").get_by_text("Подключение")).to_be_visible()
    expect(page.locator('(//a[contains(text(), "+7  (800)  250-08-90")])[1]')).to_be_visible()
    expect(page.locator('(//div[contains(text(), "Техподдержка")])[1]')).to_be_visible()
    expect(page.get_by_role("link", name="Об операторе")).to_be_visible()
    expect(page.get_by_role("link", name="Тарифы").nth(1)).to_be_visible()
    expect(page.get_by_role("link", name="акции", exact=True)).to_be_visible()
    expect(page.get_by_role("link", name="в 1")).to_be_visible()
    tags_for_operatory(page)
    tags_mobile(page)
    for i in range(1, 15):
        expect(page.locator(f'(//div[contains(text(), "Выбрать")])[{i}]')).to_be_visible()
    expect(page.get_by_text("ПОКАЗАТЬ ЕЩЁ")).to_be_visible()


def test_operator_mts_ratesmobile_modem(page: Page):
    page.goto('https://piter-online.net/operatory/mts/ratesmobile/dlja-modema')
    check_header_operator_page(page)
    check_footer(page)
    footer_pol(page)
    header_spb(page)
    expect(page.get_by_role("link", name="Подключить интернет")).to_be_visible()
    expect(page.get_by_role("link", name="Мобильные операторы")).to_be_visible()
    expect(page.locator('(//span[contains(text(), "МТС")])[1]')).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Тарифы")])[1]')).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Для модема/роутера")])[1]')).to_be_visible()
    expect(page.get_by_role("heading", name="Тарифы МТС для модема 3g в Санкт-Петербурге")).to_be_visible()
    expect(page.locator('//img[@itemprop="contentUrl"]')).to_be_visible()
    expect(page.locator("#operator_banner").get_by_text("Подключение")).to_be_visible()
    expect(page.locator('(//a[contains(text(), "+7  (800)  250-08-90")])[1]')).to_be_visible()
    expect(page.locator('(//div[contains(text(), "Техподдержка")])[1]')).to_be_visible()
    expect(page.get_by_role("link", name="Об операторе")).to_be_visible()
    expect(page.get_by_role("link", name="Тарифы").nth(1)).to_be_visible()
    expect(page.get_by_role("link", name="акции", exact=True)).to_be_visible()
    expect(page.get_by_role("link", name="в 1")).to_be_visible()
    tags_for_operatory(page)
    tags_mobile(page)
    for i in range(1, 5):
        expect(page.locator(f'(//div[contains(text(), "Выбрать")])[{i}]')).to_be_visible()
    expect(page.locator('(//h2)[1]')).to_be_visible()


def test_operator_mts_ratesmobile_bezplaty(page: Page):
    page.goto('https://piter-online.net/operatory/mts/ratesmobile/bez-abonentskoj-platy')
    check_header_operator_page(page)
    check_footer(page)
    footer_pol(page)
    header_spb(page)
    expect(page.get_by_role("link", name="Подключить интернет")).to_be_visible()
    expect(page.get_by_role("link", name="Мобильные операторы")).to_be_visible()
    expect(page.locator('(//span[contains(text(), "МТС")])[1]')).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Тарифы")])[1]')).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Без абонентской платы")])[1]')).to_be_visible()
    expect(page.locator('(//h1)[1]')).to_be_visible()
    expect(page.locator('//img[@itemprop="contentUrl"]')).to_be_visible()
    expect(page.locator("#operator_banner").get_by_text("Подключение")).to_be_visible()
    expect(page.locator('(//a[contains(text(), "+7  (800)  250-08-90")])[1]')).to_be_visible()
    expect(page.locator('(//div[contains(text(), "Техподдержка")])[1]')).to_be_visible()
    expect(page.get_by_role("link", name="Об операторе")).to_be_visible()
    expect(page.get_by_role("link", name="Тарифы").nth(1)).to_be_visible()
    expect(page.get_by_role("link", name="акции", exact=True)).to_be_visible()
    expect(page.get_by_role("link", name="в 1")).to_be_visible()
    expect(page.locator('(//p[contains(text(), "К сожалению, у нас нет информации о тарифах оператора в этом регионе.")])[1]')).to_be_visible()
    tags_mobile(page)
    expect(page.locator('(//div[contains(text(), "Недавно подключенные тарифы в ")])[1]')).to_be_visible()
    for i in range(1, 7):
        expect(page.locator(f'(//div[contains(text(), "Выбрать")])[{i}]')).to_be_visible()


def test_operator_mts_ratesmobile_bezlimitnaja(page: Page):
    page.goto('https://piter-online.net/operatory/mts/ratesmobile/bezlimitnaja-svjaz')
    check_header_operator_page(page)
    check_footer(page)
    footer_pol(page)
    header_spb(page)
    expect(page.get_by_role("link", name="Подключить интернет")).to_be_visible()
    expect(page.get_by_role("link", name="Мобильные операторы")).to_be_visible()
    expect(page.locator('(//span[contains(text(), "МТС")])[1]')).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Тарифы")])[1]')).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Безлимитная связь")])[1]')).to_be_visible()
    expect(page.locator('(//h1)[1]')).to_be_visible()
    expect(page.locator('//img[@itemprop="contentUrl"]')).to_be_visible()
    expect(page.locator("#operator_banner").get_by_text("Подключение")).to_be_visible()
    expect(page.locator('(//a[contains(text(), "+7  (800)  250-08-90")])[1]')).to_be_visible()
    expect(page.locator('(//div[contains(text(), "Техподдержка")])[1]')).to_be_visible()
    expect(page.get_by_role("link", name="Об операторе")).to_be_visible()
    expect(page.get_by_role("link", name="Тарифы").nth(1)).to_be_visible()
    expect(page.get_by_role("link", name="акции", exact=True)).to_be_visible()
    expect(page.get_by_role("link", name="в 1")).to_be_visible()
    tags_for_operatory(page)
    tags_mobile(page)
    for i in range(1, 8):
        expect(page.locator(f'(//div[contains(text(), "Выбрать")])[{i}]')).to_be_visible()


def test_operator_mts_ratesmobile_bezlimitn_internet(page: Page):
    page.goto('https://piter-online.net/operatory/mts/ratesmobile/bezlimitnyj-internet')
    check_header_operator_page(page)
    check_footer(page)
    footer_pol(page)
    header_spb(page)
    expect(page.get_by_role("link", name="Подключить интернет")).to_be_visible()
    expect(page.get_by_role("link", name="Мобильные операторы")).to_be_visible()
    expect(page.locator('(//span[contains(text(), "МТС")])[1]')).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Тарифы")])[1]')).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Безлимитный интернет")])[1]')).to_be_visible()
    expect(page.locator('(//h1)[1]')).to_be_visible()
    expect(page.locator('//img[@itemprop="contentUrl"]')).to_be_visible()
    expect(page.locator("#operator_banner").get_by_text("Подключение")).to_be_visible()
    expect(page.locator('(//a[contains(text(), "+7  (800)  250-08-90")])[1]')).to_be_visible()
    expect(page.locator('(//div[contains(text(), "Техподдержка")])[1]')).to_be_visible()
    expect(page.get_by_role("link", name="Об операторе")).to_be_visible()
    expect(page.get_by_role("link", name="Тарифы").nth(1)).to_be_visible()
    expect(page.get_by_role("link", name="акции", exact=True)).to_be_visible()
    expect(page.get_by_role("link", name="в 1")).to_be_visible()
    tags_for_operatory(page)
    tags_mobile(page)
    for i in range(1, 13):
        expect(page.locator(f'(//div[contains(text(), "Выбрать")])[{i}]')).to_be_visible()


def test_operator_mts_ratesmobile_bezlimitn_porf(page: Page):
    page.goto('https://piter-online.net/operatory/mts/ratesmobile/bezlimitnaja-svjaz-po-rossii')
    check_header_operator_page(page)
    check_footer(page)
    footer_pol(page)
    header_spb(page)
    expect(page.get_by_role("link", name="Подключить интернет")).to_be_visible()
    expect(page.get_by_role("link", name="Мобильные операторы")).to_be_visible()
    expect(page.locator('(//span[contains(text(), "МТС")])[1]')).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Тарифы")])[1]')).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Безлимитная связь по России")])[1]')).to_be_visible()
    expect(page.locator('(//h1)[1]')).to_be_visible()
    expect(page.locator('//img[@itemprop="contentUrl"]')).to_be_visible()
    expect(page.locator("#operator_banner").get_by_text("Подключение")).to_be_visible()
    expect(page.locator('(//a[contains(text(), "+7  (800)  250-08-90")])[1]')).to_be_visible()
    expect(page.locator('(//div[contains(text(), "Техподдержка")])[1]')).to_be_visible()
    expect(page.get_by_role("link", name="Об операторе")).to_be_visible()
    expect(page.get_by_role("link", name="Тарифы").nth(1)).to_be_visible()
    expect(page.get_by_role("link", name="акции", exact=True)).to_be_visible()
    expect(page.get_by_role("link", name="в 1")).to_be_visible()
    expect(page.locator(
        '(//p[contains(text(), "К сожалению, у нас нет информации о тарифах оператора в этом регионе.")])[1]')).to_be_visible()
    tags_mobile(page)
    expect(page.locator('(//div[contains(text(), "Недавно подключенные тарифы в ")])[1]')).to_be_visible()
    for i in range(1, 7):
        expect(page.locator(f'(//div[contains(text(), "Выбрать")])[{i}]')).to_be_visible()


def test_operator_mts_ratesmobile_vygodnye(page: Page):
    page.goto('https://piter-online.net/operatory/mts/ratesmobile/vygodnye')
    check_header_operator_page(page)
    check_footer(page)
    footer_pol(page)
    header_spb(page)
    expect(page.get_by_role("link", name="Подключить интернет")).to_be_visible()
    expect(page.get_by_role("link", name="Мобильные операторы")).to_be_visible()
    expect(page.locator('(//span[contains(text(), "МТС")])[1]')).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Тарифы")])[1]')).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Выгодные")])[1]')).to_be_visible()
    expect(page.locator('(//h1)[1]')).to_be_visible()
    expect(page.locator('//img[@itemprop="contentUrl"]')).to_be_visible()
    expect(page.locator("#operator_banner").get_by_text("Подключение")).to_be_visible()
    expect(page.locator('(//a[contains(text(), "+7  (800)  250-08-90")])[1]')).to_be_visible()
    expect(page.locator('(//div[contains(text(), "Техподдержка")])[1]')).to_be_visible()
    expect(page.get_by_role("link", name="Об операторе")).to_be_visible()
    expect(page.get_by_role("link", name="Тарифы").nth(1)).to_be_visible()
    expect(page.get_by_role("link", name="акции", exact=True)).to_be_visible()
    expect(page.get_by_role("link", name="в 1")).to_be_visible()
    tags_for_operatory(page)
    tags_mobile(page)
    for i in range(1, 9):
        expect(page.locator(f'(//div[contains(text(), "Выбрать")])[{i}]')).to_be_visible()
    expect(page.locator('(//h2)[1]')).to_be_visible()


def test_operator_mts_ratesmobile_planshet(page: Page):
    page.goto('https://piter-online.net/operatory/mts/ratesmobile/dlja-plansheta')
    check_header_operator_page(page)
    check_footer(page)
    footer_pol(page)
    header_spb(page)
    expect(page.get_by_role("link", name="Подключить интернет")).to_be_visible()
    expect(page.get_by_role("link", name="Мобильные операторы")).to_be_visible()
    expect(page.locator('(//span[contains(text(), "МТС")])[1]')).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Тарифы")])[1]')).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Для планшета")])[1]')).to_be_visible()
    expect(page.locator('(//h1)[1]')).to_be_visible()
    expect(page.locator('//img[@itemprop="contentUrl"]')).to_be_visible()
    expect(page.locator("#operator_banner").get_by_text("Подключение")).to_be_visible()
    expect(page.locator('(//a[contains(text(), "+7  (800)  250-08-90")])[1]')).to_be_visible()
    expect(page.locator('(//div[contains(text(), "Техподдержка")])[1]')).to_be_visible()
    expect(page.get_by_role("link", name="Об операторе")).to_be_visible()
    expect(page.get_by_role("link", name="Тарифы").nth(1)).to_be_visible()
    expect(page.get_by_role("link", name="акции", exact=True)).to_be_visible()
    expect(page.get_by_role("link", name="в 1")).to_be_visible()
    tags_for_operatory(page)
    tags_mobile(page)
    for i in range(1, 5):
        expect(page.locator(f'(//div[contains(text(), "Выбрать")])[{i}]')).to_be_visible()


def test_operator_mts_ratesmobile_noutbuk(page: Page):
    page.goto('https://piter-online.net/operatory/mts/ratesmobile/dlja-noutbuka')
    check_header_operator_page(page)
    check_footer(page)
    footer_pol(page)
    header_spb(page)
    expect(page.get_by_role("link", name="Подключить интернет")).to_be_visible()
    expect(page.get_by_role("link", name="Мобильные операторы")).to_be_visible()
    expect(page.locator('(//span[contains(text(), "МТС")])[1]')).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Тарифы")])[1]')).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Для ноутбука")])[1]')).to_be_visible()
    expect(page.locator('(//h1)[1]')).to_be_visible()
    expect(page.locator('//img[@itemprop="contentUrl"]')).to_be_visible()
    expect(page.locator("#operator_banner").get_by_text("Подключение")).to_be_visible()
    expect(page.locator('(//a[contains(text(), "+7  (800)  250-08-90")])[1]')).to_be_visible()
    expect(page.locator('(//div[contains(text(), "Техподдержка")])[1]')).to_be_visible()
    expect(page.get_by_role("link", name="Об операторе")).to_be_visible()
    expect(page.get_by_role("link", name="Тарифы").nth(1)).to_be_visible()
    expect(page.get_by_role("link", name="акции", exact=True)).to_be_visible()
    expect(page.get_by_role("link", name="в 1")).to_be_visible()
    expect(page.locator(
        '(//p[contains(text(), "К сожалению, у нас нет информации о тарифах оператора в этом регионе.")])[1]')).to_be_visible()
    tags_mobile(page)
    expect(page.locator('(//div[contains(text(), "Недавно подключенные тарифы в ")])[1]')).to_be_visible()
    for i in range(1, 7):
        expect(page.locator(f'(//div[contains(text(), "Выбрать")])[{i}]')).to_be_visible()
    expect(page.locator('(//h2)[1]')).to_be_visible()


def test_operator_mts_ratesmobile_dlya_sng(page: Page):
    page.goto('https://piter-online.net/operatory/mts/ratesmobile/dlja-sng')
    check_header_operator_page(page)
    check_footer(page)
    footer_pol(page)
    header_spb(page)
    expect(page.get_by_role("link", name="Подключить интернет")).to_be_visible()
    expect(page.get_by_role("link", name="Мобильные операторы")).to_be_visible()
    expect(page.locator('(//span[contains(text(), "МТС")])[1]')).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Тарифы")])[1]')).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Для СНГ")])[1]')).to_be_visible()
    expect(page.locator('(//h1)[1]')).to_be_visible()
    expect(page.locator('//img[@itemprop="contentUrl"]')).to_be_visible()
    expect(page.locator("#operator_banner").get_by_text("Подключение")).to_be_visible()
    expect(page.locator('(//a[contains(text(), "+7  (800)  250-08-90")])[1]')).to_be_visible()
    expect(page.locator('(//div[contains(text(), "Техподдержка")])[1]')).to_be_visible()
    expect(page.get_by_role("link", name="Об операторе")).to_be_visible()
    expect(page.get_by_role("link", name="Тарифы").nth(1)).to_be_visible()
    expect(page.get_by_role("link", name="акции", exact=True)).to_be_visible()
    expect(page.get_by_role("link", name="в 1")).to_be_visible()
    expect(page.locator(
        '(//p[contains(text(), "К сожалению, у нас нет информации о тарифах оператора в этом регионе.")])[1]')).to_be_visible()
    tags_mobile(page)
    expect(page.locator('(//div[contains(text(), "Недавно подключенные тарифы в ")])[1]')).to_be_visible()
    for i in range(1, 7):
        expect(page.locator(f'(//div[contains(text(), "Выбрать")])[{i}]')).to_be_visible()


def test_operator_mts_ratesmobile_mezhdunarodnye(page: Page):
    page.goto('https://piter-online.net/operatory/mts/ratesmobile/mezhdunarodnye')
    check_header_operator_page(page)
    check_footer(page)
    footer_pol(page)
    header_spb(page)
    expect(page.get_by_role("link", name="Подключить интернет")).to_be_visible()
    expect(page.get_by_role("link", name="Мобильные операторы")).to_be_visible()
    expect(page.locator('(//span[contains(text(), "МТС")])[1]')).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Тарифы")])[1]')).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Роуминг за границей")])[1]')).to_be_visible()
    expect(page.locator('(//h1)[1]')).to_be_visible()
    expect(page.locator('//img[@itemprop="contentUrl"]')).to_be_visible()
    expect(page.locator("#operator_banner").get_by_text("Подключение")).to_be_visible()
    expect(page.locator('(//a[contains(text(), "+7  (800)  250-08-90")])[1]')).to_be_visible()
    expect(page.locator('(//div[contains(text(), "Техподдержка")])[1]')).to_be_visible()
    expect(page.get_by_role("link", name="Об операторе")).to_be_visible()
    expect(page.get_by_role("link", name="Тарифы").nth(1)).to_be_visible()
    expect(page.get_by_role("link", name="акции", exact=True)).to_be_visible()
    expect(page.get_by_role("link", name="в 1")).to_be_visible()
    tags_for_operatory(page)
    tags_mobile(page)
    for i in range(1, 3):
        expect(page.locator(f'(//div[contains(text(), "Выбрать")])[{i}]')).to_be_visible()
    expect(page.locator('(//h2)[1]')).to_be_visible()


def test_operator_mts_ratesmobile_optom(page: Page):
    page.goto('https://piter-online.net/operatory/mts/ratesmobile/optom')
    check_header_operator_page(page)
    check_footer(page)
    footer_pol(page)
    header_spb(page)
    expect(page.get_by_role("link", name="Подключить интернет")).to_be_visible()
    expect(page.get_by_role("link", name="Мобильные операторы")).to_be_visible()
    expect(page.locator('(//span[contains(text(), "МТС")])[1]')).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Тарифы")])[1]')).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Оптом")])[1]')).to_be_visible()
    expect(page.locator('(//h1)[1]')).to_be_visible()
    expect(page.locator('//img[@itemprop="contentUrl"]')).to_be_visible()
    expect(page.locator("#operator_banner").get_by_text("Подключение")).to_be_visible()
    expect(page.locator('(//a[contains(text(), "+7  (800)  250-08-90")])[1]')).to_be_visible()
    expect(page.locator('(//div[contains(text(), "Техподдержка")])[1]')).to_be_visible()
    expect(page.get_by_role("link", name="Об операторе")).to_be_visible()
    expect(page.get_by_role("link", name="Тарифы").nth(1)).to_be_visible()
    expect(page.get_by_role("link", name="акции", exact=True)).to_be_visible()
    expect(page.get_by_role("link", name="в 1")).to_be_visible()
    expect(page.locator(
        '(//p[contains(text(), "К сожалению, у нас нет информации о тарифах оператора в этом регионе.")])[1]')).to_be_visible()
    tags_mobile(page)
    expect(page.locator('(//div[contains(text(), "Недавно подключенные тарифы в ")])[1]')).to_be_visible()
    for i in range(1, 7):
        expect(page.locator(f'(//div[contains(text(), "Выбрать")])[{i}]')).to_be_visible()


def test_operator_mts_ratesmobile_porf(page: Page):
    page.goto('https://piter-online.net/operatory/mts/ratesmobile/po-rossii')
    check_header_operator_page(page)
    check_footer(page)
    footer_pol(page)
    header_spb(page)
    expect(page.get_by_role("link", name="Подключить интернет")).to_be_visible()
    expect(page.get_by_role("link", name="Мобильные операторы")).to_be_visible()
    expect(page.locator('(//span[contains(text(), "МТС")])[1]')).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Тарифы")])[1]')).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Связь по России")])[1]')).to_be_visible()
    expect(page.locator('(//h1)[1]')).to_be_visible()
    expect(page.locator('//img[@itemprop="contentUrl"]')).to_be_visible()
    expect(page.locator("#operator_banner").get_by_text("Подключение")).to_be_visible()
    expect(page.locator('(//a[contains(text(), "+7  (800)  250-08-90")])[1]')).to_be_visible()
    expect(page.locator('(//div[contains(text(), "Техподдержка")])[1]')).to_be_visible()
    expect(page.get_by_role("link", name="Об операторе")).to_be_visible()
    expect(page.get_by_role("link", name="Тарифы").nth(1)).to_be_visible()
    expect(page.get_by_role("link", name="акции", exact=True)).to_be_visible()
    expect(page.get_by_role("link", name="в 1")).to_be_visible()
    tags_for_operatory(page)
    tags_mobile(page)
    for i in range(1, 15):
        expect(page.locator(f'(//div[contains(text(), "Выбрать")])[{i}]')).to_be_visible()
    expect(page.locator('(//div[contains(text(), "ПОКАЗАТЬ ЕЩЁ")])[1]')).to_be_visible()
    expect(page.locator('(//h2)[1]')).to_be_visible()


def test_operator_megafon_ratesmobile_esim(page: Page):
    page.goto('https://piter-online.net/operatory/megafon/ratesmobile/esim')
    check_header_operator_page(page)
    check_footer(page)
    footer_pol(page)
    header_spb(page)
    expect(page.get_by_role("link", name="Подключить интернет")).to_be_visible()
    expect(page.get_by_role("link", name="Мобильные операторы")).to_be_visible()
    expect(page.locator('(//span[contains(text(), "МегаФон")])[1]')).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Тарифы")])[1]')).to_be_visible()
    expect(page.locator('(//span[contains(text(), "eSIM")])[1]')).to_be_visible()
    expect(page.locator('(//h1)[1]')).to_be_visible()
    expect(page.locator('//img[@itemprop="contentUrl"]')).to_be_visible()
    expect(page.locator("#operator_banner").get_by_text("Подключение")).to_be_visible()
    expect(page.locator('(//a[contains(text(), "+7  (800)  550-58-58")])[1]')).to_be_visible()
    expect(page.locator('(//div[contains(text(), "Техподдержка")])[1]')).to_be_visible()
    expect(page.get_by_role("link", name="Об операторе")).to_be_visible()
    expect(page.get_by_role("link", name="Тарифы").nth(1)).to_be_visible()
    expect(page.get_by_role("link", name="акции", exact=True)).to_be_visible()
    expect(page.get_by_role("link", name="в 1")).to_be_visible()
    tags_for_operatory(page)
    expect(page.get_by_role("link", name="Все", exact=True)).to_be_visible()
    expect(page.get_by_role("link", name="eSIM")).to_be_visible()
    expect(page.get_by_role("link", name="Для планшета")).to_be_visible()
    expect(page.get_by_role("link", name="Детские")).to_be_visible()
    expect(page.get_by_role("link", name="Безлимитная связь")).to_be_visible()
    expect(page.get_by_role("link", name="Связь по России")).to_be_visible()
    expect(page.get_by_role("link", name="Безлимитный интернет")).to_be_visible()
    expect(page.get_by_role("link", name="Перейти со своим номером")).to_be_visible()
    expect(page.get_by_role("link", name="Непубличные🔥")).to_be_visible()
    expect(page.get_by_role("link", name="Для модема/роутера")).to_be_visible()
    for i in range(1, 15):
        expect(page.locator(f'(//div[contains(text(), "Выбрать")])[{i}]')).to_be_visible()
    expect(page.locator('(//div[contains(text(), "ПОКАЗАТЬ ЕЩЁ")])[1]')).to_be_visible()
    expect(page.locator('(//h2)[1]')).to_be_visible()


def test_operator_megafon_ratesmobile_unikalnye(page: Page):
    page.goto('https://piter-online.net/operatory/megafon/ratesmobile/unikalnye')
    check_header_operator_page(page)
    check_footer(page)
    footer_pol(page)
    header_spb(page)
    expect(page.get_by_role("link", name="Подключить интернет")).to_be_visible()
    expect(page.get_by_role("link", name="Мобильные операторы")).to_be_visible()
    expect(page.locator('(//span[contains(text(), "МегаФон")])[1]')).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Тарифы")])[1]')).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Непубличные")])[1]')).to_be_visible()
    expect(page.locator('(//h1)[1]')).to_be_visible()
    expect(page.locator('//img[@itemprop="contentUrl"]')).to_be_visible()
    expect(page.locator("#operator_banner").get_by_text("Подключение")).to_be_visible()
    expect(page.locator('(//a[contains(text(), "+7  (800)  550-58-58")])[1]')).to_be_visible()
    expect(page.locator('(//div[contains(text(), "Техподдержка")])[1]')).to_be_visible()
    expect(page.get_by_role("link", name="Об операторе")).to_be_visible()
    expect(page.get_by_role("link", name="Тарифы").nth(1)).to_be_visible()
    expect(page.get_by_role("link", name="акции", exact=True)).to_be_visible()
    expect(page.get_by_role("link", name="в 1")).to_be_visible()
    tags_for_operatory(page)
    expect(page.get_by_role("link", name="Все", exact=True)).to_be_visible()
    expect(page.get_by_role("link", name="eSIM")).to_be_visible()
    expect(page.get_by_role("link", name="Для планшета")).to_be_visible()
    expect(page.get_by_role("link", name="Детские")).to_be_visible()
    expect(page.get_by_role("link", name="Безлимитная связь")).to_be_visible()
    expect(page.get_by_role("link", name="Связь по России")).to_be_visible()
    expect(page.get_by_role("link", name="Безлимитный интернет")).to_be_visible()
    expect(page.get_by_role("link", name="Перейти со своим номером")).to_be_visible()
    expect(page.get_by_role("link", name="Непубличные🔥")).to_be_visible()
    expect(page.get_by_role("link", name="Для модема/роутера")).to_be_visible()
    for i in range(1, 9):
        expect(page.locator(f'(//div[contains(text(), "Выбрать")])[{i}]')).to_be_visible()
    expect(page.locator('(//h2)[1]')).to_be_visible()


def test_operator_mts_ratesmobile_perenos_nomera(page: Page):
    page.goto('https://piter-online.net/operatory/mts/ratesmobile/perenos_nomera')
    check_header_operator_page(page)
    check_footer(page)
    footer_pol(page)
    header_spb(page)
    expect(page.get_by_role("link", name="Подключить интернет")).to_be_visible()
    expect(page.get_by_role("link", name="Мобильные операторы")).to_be_visible()
    expect(page.locator('(//span[contains(text(), "МТС")])[1]')).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Тарифы")])[1]')).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Перейти со своим номером")])[1]')).to_be_visible()
    expect(page.locator('(//h1)[1]')).to_be_visible()
    expect(page.locator('//img[@itemprop="contentUrl"]')).to_be_visible()
    expect(page.locator("#operator_banner").get_by_text("Подключение")).to_be_visible()
    expect(page.locator('(//a[contains(text(), "+7  (800)  250-08-90")])[1]')).to_be_visible()
    expect(page.locator('(//div[contains(text(), "Техподдержка")])[1]')).to_be_visible()
    expect(page.get_by_role("link", name="Об операторе")).to_be_visible()
    expect(page.get_by_role("link", name="Тарифы").nth(1)).to_be_visible()
    expect(page.get_by_role("link", name="акции", exact=True)).to_be_visible()
    expect(page.get_by_role("link", name="в 1")).to_be_visible()
    tags_for_operatory(page)
    tags_mobile(page)
    for i in range(1, 6):
        expect(page.locator(f'(//div[contains(text(), "Выбрать")])[{i}]')).to_be_visible()
    expect(page.locator('(//h2)[1]')).to_be_visible()


def test_operatory_mts_nomera(page: Page):
    page.goto('https://piter-online.net/operatory/mts/nomera')
    check_header_operator_page(page)
    check_footer(page)
    footer_pol(page)
    header_spb(page)
    expect(page.get_by_role("link", name="Подключить интернет")).to_be_visible()
    expect(page.get_by_role("link", name="Мобильные операторы")).to_be_visible()
    expect(page.locator('(//span[contains(text(), "МТС")])[1]')).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Номера")])[1]')).to_be_visible()
    expect(page.get_by_role("heading", name="Выбрать номер МТС")).to_be_visible()
    expect(page.locator('//img[@itemprop="contentUrl"]')).to_be_visible()
    expect(page.locator("#operator_banner").get_by_text("Подключение")).to_be_visible()
    expect(page.locator('(//a[contains(text(), "+7  (800)  250-08-90")])[1]')).to_be_visible()
    expect(page.locator('(//div[contains(text(), "Техподдержка")])[1]')).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Информация носит справочный характер и не является публичной офертой.")])[1]')).to_be_visible()
    expect(page.get_by_role("link", name="Бронзовые")).to_be_visible()
    expect(page.get_by_role("link", name="Серебряные")).to_be_visible()
    expect(page.get_by_role("link", name="Золотые")).to_be_visible()
    expect(page.get_by_role("link", name="Бесплатные")).to_be_visible()
    for i in range(2, 16):
        expect(page.locator(f'(//div[contains(text(), "Подключить")])[{i}]')).to_be_visible()
    expect(page.locator('(//div[contains(text(), "ПОКАЗАТЬ ЕЩЁ")])[1]')).to_be_visible()


def test_operatory_mts_nomera_zolotoj(page: Page):
    page.goto('https://piter-online.net/operatory/mts/nomera/zolotoj')
    check_header_operator_page(page)
    check_footer(page)
    footer_pol(page)
    header_spb(page)
    expect(page.get_by_role("link", name="Подключить интернет")).to_be_visible()
    expect(page.get_by_role("link", name="Мобильные операторы")).to_be_visible()
    expect(page.locator('(//span[contains(text(), "МТС")])[1]')).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Номера")])[1]')).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Золотые")])[1]')).to_be_visible()
    expect(page.get_by_role("heading", name="Золотые номера МТС на выбор")).to_be_visible()
    expect(page.locator('//img[@itemprop="contentUrl"]')).to_be_visible()
    expect(page.locator("#operator_banner").get_by_text("Подключение")).to_be_visible()
    expect(page.locator('(//a[contains(text(), "+7  (800)  250-08-90")])[1]')).to_be_visible()
    expect(page.locator('(//div[contains(text(), "Техподдержка")])[1]')).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Информация носит справочный характер и не является публичной офертой.")])[1]')).to_be_visible()
    expect(page.get_by_role("link", name="Бронзовые")).to_be_visible()
    expect(page.get_by_role("link", name="Серебряные")).to_be_visible()
    expect(page.get_by_role("link", name="Золотые")).to_be_visible()
    expect(page.get_by_role("link", name="Бесплатные")).to_be_visible()
    for i in range(1, 15):
        expect(page.locator(f'(//div[contains(text(), "Подключить")])[{i}]')).to_be_visible()
    expect(page.locator('(//div[contains(text(), "ПОКАЗАТЬ ЕЩЁ")])[1]')).to_be_visible()


def test_operatory_mts_nomera_bronzovyj(page: Page):
    page.goto('https://piter-online.net/operatory/mts/nomera/bronzovyj')
    check_header_operator_page(page)
    check_footer(page)
    footer_pol(page)
    header_spb(page)
    expect(page.get_by_role("link", name="Подключить интернет")).to_be_visible()
    expect(page.get_by_role("link", name="Мобильные операторы")).to_be_visible()
    expect(page.locator('(//span[contains(text(), "МТС")])[1]')).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Номера")])[1]')).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Бронзовые")])[1]')).to_be_visible()
    expect(page.get_by_role("heading", name="Бронзовые номера МТС на выбор")).to_be_visible()
    expect(page.locator('//img[@itemprop="contentUrl"]')).to_be_visible()
    expect(page.locator("#operator_banner").get_by_text("Подключение")).to_be_visible()
    expect(page.locator('(//a[contains(text(), "+7  (800)  250-08-90")])[1]')).to_be_visible()
    expect(page.locator('(//div[contains(text(), "Техподдержка")])[1]')).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Информация носит справочный характер и не является публичной офертой.")])[1]')).to_be_visible()
    expect(page.get_by_role("link", name="Бронзовые")).to_be_visible()
    expect(page.get_by_role("link", name="Серебряные")).to_be_visible()
    expect(page.get_by_role("link", name="Золотые")).to_be_visible()
    expect(page.get_by_role("link", name="Бесплатные")).to_be_visible()
    for i in range(1, 15):
        expect(page.locator(f'(//div[contains(text(), "Подключить")])[{i}]')).to_be_visible()
    expect(page.locator('(//div[contains(text(), "ПОКАЗАТЬ ЕЩЁ")])[1]')).to_be_visible()


def test_operatory_mts_nomera_serebrjanyj(page: Page):
    page.goto('https://piter-online.net/operatory/mts/nomera/serebrjanyj')
    check_header_operator_page(page)
    check_footer(page)
    footer_pol(page)
    header_spb(page)
    expect(page.get_by_role("link", name="Подключить интернет")).to_be_visible()
    expect(page.get_by_role("link", name="Мобильные операторы")).to_be_visible()
    expect(page.locator('(//span[contains(text(), "МТС")])[1]')).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Номера")])[1]')).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Серебряные")])[1]')).to_be_visible()
    expect(page.get_by_role("heading", name="Серебряные номера МТС на выбор")).to_be_visible()
    expect(page.locator('//img[@itemprop="contentUrl"]')).to_be_visible()
    expect(page.locator("#operator_banner").get_by_text("Подключение")).to_be_visible()
    expect(page.locator('(//a[contains(text(), "+7  (800)  250-08-90")])[1]')).to_be_visible()
    expect(page.locator('(//div[contains(text(), "Техподдержка")])[1]')).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Информация носит справочный характер и не является публичной офертой.")])[1]')).to_be_visible()
    expect(page.get_by_role("link", name="Бронзовые")).to_be_visible()
    expect(page.get_by_role("link", name="Серебряные")).to_be_visible()
    expect(page.get_by_role("link", name="Золотые")).to_be_visible()
    expect(page.get_by_role("link", name="Бесплатные")).to_be_visible()
    for i in range(1, 15):
        expect(page.locator(f'(//div[contains(text(), "Подключить")])[{i}]')).to_be_visible()
    expect(page.locator('(//div[contains(text(), "ПОКАЗАТЬ ЕЩЁ")])[1]')).to_be_visible()


def test_operatory_mts_nomera_besplatnye(page: Page):
    page.goto('https://piter-online.net/operatory/mts/nomera/besplatnye')
    check_header_operator_page(page)
    check_footer(page)
    footer_pol(page)
    header_spb(page)
    expect(page.get_by_role("link", name="Подключить интернет")).to_be_visible()
    expect(page.get_by_role("link", name="Мобильные операторы")).to_be_visible()
    expect(page.locator('(//span[contains(text(), "МТС")])[1]')).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Номера")])[1]')).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Бесплатные")])[1]')).to_be_visible()
    expect(page.get_by_role("heading", name="Бесплатные номера МТС на выбор")).to_be_visible()
    expect(page.locator('//img[@itemprop="contentUrl"]')).to_be_visible()
    expect(page.locator("#operator_banner").get_by_text("Подключение")).to_be_visible()
    expect(page.locator('(//a[contains(text(), "+7  (800)  250-08-90")])[1]')).to_be_visible()
    expect(page.locator('(//div[contains(text(), "Техподдержка")])[1]')).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Информация носит справочный характер и не является публичной офертой.")])[1]')).to_be_visible()
    expect(page.get_by_role("link", name="Бронзовые")).to_be_visible()
    expect(page.get_by_role("link", name="Серебряные")).to_be_visible()
    expect(page.get_by_role("link", name="Золотые")).to_be_visible()
    expect(page.get_by_role("link", name="Бесплатные")).to_be_visible()
    for i in range(1, 4):
        expect(page.locator(f'(//div[contains(text(), "Подключить")])[{i}]')).to_be_visible()


def test_operatory_tele2_actions(page: Page):
    page.goto('https://piter-online.net/operatory/tele-2/actions')
    check_header_operator_page(page)
    check_footer(page)
    footer_pol(page)
    header_spb(page)
    expect(page.get_by_role("link", name="Подключить интернет")).to_be_visible()
    expect(page.get_by_role("link", name="Мобильные операторы")).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Теле 2")])[1]')).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Акции")])[1]')).to_be_visible()
    expect(page.locator('(//h1)[1]')).to_be_visible()
    expect(page.locator('//img[@itemprop="contentUrl"]')).to_be_visible()
    expect(page.locator("#operator_banner").get_by_text("Подключение")).to_be_visible()
    expect(page.locator('(//a[contains(text(), "+7  (812)  989-00-22")])[1]')).to_be_visible()
    expect(page.locator('(//div[contains(text(), "Техподдержка")])[1]')).to_be_visible()
    expect(page.locator('(//a[contains(text(), "+7 (495) 979-76-11")])[1]')).to_be_visible()
    expect(page.get_by_role("link", name="Об операторе")).to_be_visible()
    expect(page.get_by_role("link", name="Тарифы").nth(1)).to_be_visible()
    expect(page.get_by_role("link", name="акции", exact=True)).to_be_visible()
    expect(page.get_by_role("link", name="в 1")).to_be_visible()
    tags_for_operatory(page)
    tags_mobile(page)
    for i in range(1, 7):
        expect(page.locator(f'(//div[contains(text(), "Выбрать")])[{i}]')).to_be_visible()
    expect(page.locator('(//h2)[1]')).to_be_visible()