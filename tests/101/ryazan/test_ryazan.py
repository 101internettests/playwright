from playwright.sync_api import Page, expect
from pages.main_page import check_header, search_tariffs, one_click_form, tariffs_block, blue_form
from pages.main_page import check_footer, blue_form_second, search_tariffs_second, sorting
from pages.main_site_pages.ryazan_page import review, check_tags, check_header_ryazan


def test_mani_page(page: Page):
    page.goto('https://101internet.ru/ryazan')
    check_header(page)
    check_footer(page)
    review(page)
    one_click_form(page)
    blue_form(page)
    search_tariffs(page)
    check_header_ryazan(page)
    expect(page.locator('//h1[contains(text(), "Подключить интернет")]')).to_contain_text('Подключить интернет')
    expect(page.locator('(//div[contains(text(), "Введите адрес и сравните тарифы всех провайдеров в своём доме – подключайтесь с гарантией 90 дней!")])[1]')).to_be_visible()
    expect(page.locator('(//input[@ datatest="main_input_street_home_new"])[1]')).to_be_visible()
    expect(page.locator('(//input[@ datatest="main_input_street_home_new"])[2]')).to_be_visible()
    expect(page.locator('//div[@datatest="main_raitingprovider_button"]')).to_have_text('Рейтинг провайдеров')
    expect(page.locator('//div[@datatest="main_comparetariff_button"]')).to_have_text('Выгодные пакеты интернета3 в 1')
    expect(page.locator('//div[@class="col-sm-6 col-lg-4"]')).to_contain_text('получили нашу помощь в выборе интернета за  15 лет')
    expect(page.locator('//div[@class="onlyNotMd onlyNotSm onlyNotXs col-lg-4"]')).to_contain_text('Бесплатная консультация')
    expect(page.locator('//div[@datatest="main_inflat_button"]')).to_contain_text('ИнтернетВ квартиру')
    expect(page.locator('//div[@datatest="main_inhouse_button"]')).to_contain_text('ИнтернетНа дачу')
    expect(page.locator('//div[@datatest="main_inoffice_button"]')).to_contain_text('ИнтернетВ офис')
    expect(page.locator('(//a[@datatest="providers_provider_alltariff_button"])[1]')).to_have_text('Показать все')
    expect(page.locator('(//h2[contains(text(), "Наши партнеры в Рязани")])[2]')).to_contain_text('Наши партнеры в Рязани ')
    expect(page.locator('(//div[@class="row"])[7]')).to_be_visible()
    expect(page.locator('//div[@class="row"]//div[@class="col-12 col-sm-6 col-md-4 col-lg-3"]').nth(4))
    expect(page.locator('(//h2)[9]')).to_be_visible()
    expect(page.locator('(//div[contains(text(), "Все")])[1]')).to_be_visible()


def test_tohome(page: Page):
    page.goto('https://101internet.ru/ryazan/orders/tohome')
    check_header(page)
    check_footer(page)
    one_click_form(page)
    blue_form(page)
    search_tariffs(page)
    check_header_ryazan(page)
    expect(page.locator('(//span[contains(text(), "Подключить интернет")])[1]')).to_be_visible()
    expect(page.locator('//span[contains(text(), "поиск по адресу")]')).to_be_visible()
    expect(page.locator('//h1[contains(text(), "Провайдеры интернета по адресу в Рязани")]')).to_be_visible()
    expect(page.locator('(//h2)[4]')).to_be_visible()
    expect(page.locator('//ul[@style]')).to_be_visible()
    expect(page.locator('(//h2)[5]')).to_be_visible()
    expect(page.locator('//div[@data-test="countRates"]')).to_be_visible()
    expect(page.locator('(//h2)[6]')).to_be_visible()
    expect(page.locator('(//h2)[7]')).to_be_visible()
    expect(page.locator('//div[@datatest="providers_find_adress"]')).to_be_visible()
    expect(page.locator('(//h2)[1]')).to_be_visible()
    expect(page.locator('(//h2)[2]')).to_be_visible()
    expect(page.locator('(//div[@itemscope])[1]')).to_be_visible()


def test_providers(page: Page):
    page.goto('https://101internet.ru/ryazan/providers')
    check_header(page)
    check_footer(page)
    blue_form(page)
    blue_form_second(page)
    search_tariffs_second(page)
    check_header_ryazan(page)
    expect(page.locator('(//span[contains(text(), "Подключить интернет")])[1]')).to_be_visible()
    expect(page.locator('//span[contains(text(), "Провайдеры Рязани")]')).to_be_visible()
    expect(page.locator('(//a[@datatest="top_provider_block"])[1]')).to_be_visible()
    for i in range(1, 19):
        expect(page.locator(f'(//div[@datatest="providers_provider_button"])[{i}]')).to_be_visible()
    for i in range(2, 4):
        expect(page.locator(f'(//p[@align="left"])[{i}]')).to_be_visible()
    for i in range(1, 6):
        expect(page.locator(f'(//h2)[{i}]')).to_be_visible()
    expect(page.locator('(//ol[@align="left"])[1]')).to_be_visible()


def test_rating(page: Page):
    page.goto('https://101internet.ru/ryazan/rating')
    check_header(page)
    check_footer(page)
    search_tariffs_second(page)
    check_header_ryazan(page)
    expect(page.locator('(//span[contains(text(), "Подключить интернет")])[1]')).to_be_visible()
    expect(page.locator('//span[contains(text(), "Рейтинг провайдеров")]')).to_be_visible()
    expect(page.locator('//div[contains(text(), "Период")]')).to_be_visible()
    expect(page.locator('//div[contains(text(), "Интернет")]')).to_be_visible()
    expect(page.locator('//input[@datatest="raiting_input_filter_period"]')).to_be_visible()
    expect(page.locator('//input[@datatest="raiting_input_filter_internet_type"]')).to_be_visible()
    for i in range(1, 3):
        expect(page.locator(f'(//div[@itemprop="offers"])[{i}]')).to_be_visible()
    expect(page.locator('(//h2)[1]')).to_be_visible()
    expect(page.locator('(//h2)[2]')).to_be_visible()


def test_rates(page: Page):
    page.goto('https://101internet.ru/ryazan/rates')
    check_header(page)
    check_footer(page)
    search_tariffs(page)
    check_header_ryazan(page)
    sorting(page)
    expect(page.locator('(//span[contains(text(), "Подключить интернет")])[1]')).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Тарифы на интернет")])[1]')).to_be_visible()
    expect(page.locator('(//h1)[1]')).to_be_visible()
    expect(page.locator('(//h2)[2]')).to_be_visible()
    expect(page.locator('(//h2)[3]')).to_be_visible()
    expect(page.locator('(//p[@align="left"])[1]')).to_be_visible()
    expect(page.locator('(//a[@aria-current="page"])[4]')).to_be_visible()
    for i in range(1, 4):
        expect(page.locator(f'(//div[@datatest="providers_provider_button"])[{i}]')).to_be_visible()
    expect(page.locator('(//h2)[4]')).to_be_visible()
    expect(page.locator('(//h2)[5]')).to_be_visible()
    expect(page.locator('(//a[@datatest="top_provider_block"])[1]')).to_be_visible()
    for i in range(1, 10):
        expect(page.locator(f'(//h3[@itemprop="name"])[{i}]')).to_be_visible()
    expect(page.locator('(//h3[@itemprop="name"])[1]')).to_be_visible()


def test_personal_datarates(page: Page):
    page.goto('https://101internet.ru/ryazan/about/personal-data')
    check_header(page)
    check_footer(page)
    expect(page.locator('(//span[contains(text(), "Подключить интернет")])[1]')).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Политика обработки персональных данных")])[1]')).to_be_visible()
    expect(page.locator('//h1')).to_be_visible()
    expect(page.locator('//h1')).to_be_visible()
    for i in range(1, 9):
        expect(page.locator(f'(//h2)[{i}]')).to_be_visible()
    expect(page.locator('//h1')).to_be_visible()
    for i in range(1, 68):
        expect(page.locator(f'(//p)[{i}]')).to_be_visible()
    expect(page.locator('//div[contains(text(), "ПРИЛОЖЕНИЕ №1 к «Политике обработки персональных данных в Обществе».pdf")]')).to_be_visible()
    expect(page.locator('//div[contains(text(), "ПРИЛОЖЕНИЕ №2 к «Политике обработки персональных данных в Обществе».pdf")]')).to_be_visible()
    expect(page.locator('//a[contains(text(), "Пользовательское соглашение")]')).to_be_visible()
    expect(page.locator('//div[contains(text(), "Согласие на обработку персональных данных.pdf")]')).to_be_visible()
    expect(page.locator('//div[contains(text(), "Описание функциональных характеристик.pdf")]')).to_be_visible()
    expect(page.locator('//div[contains(text(), "Руководство пользователя.pdf")]')).to_be_visible()


def test_internet_i_mobilnaya_svyaz(page: Page):
    page.goto('https://101internet.ru/ryazan/rates/internet-i-mobilnaya-svyaz')
    check_header(page)
    check_footer(page)
    search_tariffs(page)
    check_header_ryazan(page)
    check_tags(page)
    sorting(page)
    expect(page.locator('(//span[contains(text(), "Подключить интернет")])[1]')).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Тарифы на интернет")])[1]')).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Интернет и мобильная связь")])[1]')).to_be_visible()
    expect(page.locator('//h1')).to_be_visible()
    expect(page.locator('(//h2)[1]')).to_be_visible()
    expect(page.locator('(//h2)[2]')).to_be_visible()
    expect(page.locator('(//h2)[4]')).to_be_visible()
    expect(page.locator('(//a[@href="/ryazan/ratesmobile"])[1]')).to_be_visible()
    expect(page.locator('(//div[contains(text(), "ПРОВАЙДЕР")])[1]')).to_be_visible()
    for i in range(2, 12):
        expect(page.locator(f'(//div[@itemprop="offers"])[{i}]')).to_be_visible()
    for i in range(2, 12):
        expect(page.locator(f'(//span[contains(text(), "Подключить")])[{i}]')).to_be_visible()
    expect(page.locator('//div[@datatest="providers_find_adress"]')).to_be_visible()
    expect(page.locator('//div[@datatest="providers_callback2"]')).to_be_visible()
    for i in range(1, 7):
        expect(page.locator(f'(//a[@datatest="top_provider_block"])[{i}]')).to_be_visible()
    for i in range(1, 18):
        expect(page.locator(f'(//h3)[{i}]')).to_be_visible()


def test_internet_tv_mobile(page: Page):
    page.goto('https://101internet.ru/ryazan/rates/internet-tv-mobile')
    check_header(page)
    check_footer(page)
    search_tariffs(page)
    check_header_ryazan(page)
    check_tags(page)
    sorting(page)
    expect(page.locator('(//span[contains(text(), "Подключить интернет")])[1]')).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Тарифы на интернет")])[1]')).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Интернет+тв+мобильная связь")])[1]')).to_be_visible()
    expect(page.locator('//h1')).to_be_visible()
    expect(page.locator('(//h2)[1]')).to_be_visible()
    expect(page.locator('(//h2)[2]')).to_be_visible()
    expect(page.locator('(//h2)[4]')).to_be_visible()
    expect(page.locator('(//a[@href="/ryazan/ratesmobile"])[1]')).to_be_visible()
    expect(page.locator('(//div[contains(text(), "ПРОВАЙДЕР")])[1]')).to_be_visible()
    expect(page.locator('//input[@name="sort_tariffs"]')).to_be_visible()
    for i in range(2, 16):
        expect(page.locator(f'(//div[@itemprop="offers"])[{i}]')).to_be_visible()
    for i in range(2, 12):
        expect(page.locator(f'(//span[contains(text(), "Подключить")])[{i}]')).to_be_visible()
    expect(page.locator('//div[@datatest="providers_find_adress"]')).to_be_visible()
    expect(page.locator('//div[@datatest="providers_callback2"]')).to_be_visible()
    for i in range(1, 7):
        expect(page.locator(f'(//a[@datatest="top_provider_block"])[{i}]')).to_be_visible()
    for i in range(1, 14):
        expect(page.locator(f'(//h3)[{i}]')).to_be_visible()
