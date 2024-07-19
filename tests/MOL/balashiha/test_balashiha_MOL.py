from playwright.sync_api import Page, expect
from pages.main_page import check_header, search_tariffs, one_click_form, tariffs_block, blue_form, sorting_second, personal_data, contact_page
from pages.main_page import footer_mol, blue_form_second, search_tariffs_second, sorting, page_internet_in_office, terms_of_use
from pages.MOL.balashika_page import review, check_tags, check_header_balashixa


def test_first_bal(page: Page):
    page.goto('https://www.moskvaonline.ru/balashiha')
    check_header(page)
    footer_mol(page)
    review(page)
    one_click_form(page)
    blue_form(page)
    search_tariffs(page)
    check_header_balashixa(page)
    expect(page.locator('//h1[contains(text(), "Подключить домашний интернет в Балашихе")]')).to_contain_text('Подключить домашний интернет в Балашихе')
    expect(page.locator('(//div[contains(text(), "Введите ваш адрес и сравните тарифы провайдеров Балашихи. Гарантия до 90 дней и кэшбэк до 1000 рублей!")])[1]')).to_be_visible()
    expect(page.locator('//div[@datatest="main_raitingprovider_button"]')).to_have_text('Рейтинг провайдеров')
    expect(page.locator('//div[@datatest="main_comparetariff_button"]')).to_have_text('Выгодные пакеты интернета3 в 1')
    expect(page.locator('//div[@class="col-sm-6 col-lg-4"]')).to_contain_text('получили нашу помощь в выборе интернета за  15 лет')
    expect(page.locator('//div[@class="onlyNotMd onlyNotSm onlyNotXs col-lg-4"]')).to_contain_text('Бесплатная консультация')
    expect(page.locator('//div[@datatest="main_inflat_button"]')).to_contain_text('ИнтернетВ квартиру')
    expect(page.locator('//div[@datatest="main_inhouse_button"]')).to_contain_text('ИнтернетНа дачу')
    expect(page.locator('//div[@datatest="main_inoffice_button"]')).to_contain_text('ИнтернетВ офис')
    expect(page.locator('//h2[contains(text(), "Выгодные тарифы домашнего интернета в Балашихе")]')).to_have_text('Выгодные тарифы домашнего интернета в Балашихе')
    expect(page.locator('(//a[@datatest="providers_provider_alltariff_button"])[1]')).to_have_text('Показать все')
    expect(page.locator('(//h2[contains(text(), "Топ провайдеров домашнего интернета в Балашихе")])[2]')).to_contain_text('Топ провайдеров домашнего интернета в Балашихе')
    expect(page.locator('(//div[@class="row"])[7]')).to_be_visible()
    expect(page.locator('//div[@class="row"]//div[@class="col-12 col-sm-6 col-md-4 col-lg-3"]').nth(4))
    expect(page.locator('(//h2)[9]')).to_be_visible()


def test_tohome_bal(page: Page):
    page.goto('https://www.moskvaonline.ru/balashiha/orders/tohome')
    check_header(page)
    footer_mol(page)
    one_click_form(page)
    blue_form(page)
    search_tariffs(page)
    check_header_balashixa(page)
    expect(page.locator('(//span[contains(text(), "Подключить интернет")])[1]')).to_be_visible()
    expect(page.locator('//span[contains(text(), "поиск по адресу")]')).to_be_visible()
    expect(page.locator('//h1[contains(text(), "Интернет-провайдеры по адресу в Балашихе")]')).to_be_visible()
    expect(page.locator('(//h2)[4]')).to_be_visible()
    expect(page.locator('(//h2)[5]')).to_be_visible()
    expect(page.locator('//div[@data-test="countRates"]')).to_be_visible()
    expect(page.locator('(//h2)[6]')).to_be_visible()
    expect(page.locator('(//h2)[1]')).to_be_visible()
    expect(page.locator('(//h2)[2]')).to_be_visible()
    expect(page.locator('(//div[@itemscope])[1]')).to_be_visible()


def test_providers_bal(page: Page):
    page.goto('https://www.moskvaonline.ru/balashiha/providers')
    check_header(page)
    footer_mol(page)
    blue_form(page)
    blue_form_second(page)
    search_tariffs_second(page)
    check_header_balashixa(page)
    expect(page.locator('(//span[contains(text(), "Подключить интернет")])[1]')).to_be_visible()
    expect(page.locator('//span[contains(text(), "Провайдеры Балашихи")]')).to_be_visible()
    expect(page.locator('(//h2)[2]')).to_be_visible()
    expect(page.locator('(//h2)[4]')).to_be_visible()
    # expect(page.locator('(//h2)[5]')).to_be_visible()
    expect(page.locator('(//a[@datatest="top_provider_block"])[1]')).to_be_visible()
    for i in range(1, 19):
        expect(page.locator(f'(//div[@datatest="providers_provider_button"])[{i}]')).to_be_visible()
    expect(page.locator('(//h2)[6]')).to_be_visible()
    expect(page.locator('(//ol[@align="left"])[1]')).to_be_visible()
    expect(page.locator('(//div[@datatest="providers_find_adress"])[1]')).to_be_visible()
    expect(page.locator('(//div[@datatest="providers_find_adress"])[2]')).to_be_visible()


def test_rating_bal(page: Page):
    page.goto('https://www.moskvaonline.ru/balashiha/rating')
    check_header(page)
    footer_mol(page)
    search_tariffs_second(page)
    check_header_balashixa(page)
    expect(page.locator('(//span[contains(text(), "Подключить интернет")])[1]')).to_be_visible()
    expect(page.locator('//span[contains(text(), "Рейтинг провайдеров")]')).to_be_visible()
    expect(page.locator('//div[contains(text(), "Период")]')).to_be_visible()
    expect(page.locator('(//div[contains(text(), "Интернет")])[1]')).to_be_visible()
    expect(page.locator('//input[@datatest="raiting_input_filter_period"]')).to_be_visible()
    expect(page.locator('//input[@datatest="raiting_input_filter_internet_type"]')).to_be_visible()
    for i in range(1, 4):
        expect(page.locator(f'(//div[@itemprop="offers"])[{i}]')).to_be_visible()
    expect(page.locator('(//h2)[1]')).to_be_visible()
    expect(page.locator('(//h2)[2]')).to_be_visible()
    expect(page.locator('(//div[contains(text(),"Б")])[5]')).to_be_visible()


def test_rates_bal(page: Page):
    page.goto('https://www.moskvaonline.ru/balashiha/rates')
    check_header(page)
    footer_mol(page)
    search_tariffs(page)
    check_header_balashixa(page)
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


def test_internet_i_mobilnaya_svyaz(page: Page):
    page.goto('https://www.moskvaonline.ru/balashiha/rates/internet-i-mobilnaya-svyaz')
    check_header(page)
    footer_mol(page)
    search_tariffs(page)
    check_header_balashixa(page)
    check_tags(page)
    sorting(page)
    expect(page.locator('//span[contains(text(), "Подключить интернет")]')).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Тарифы на интернет")])[1]')).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Интернет и мобильная связь")])[1]')).to_be_visible()
    expect(page.locator('//h1')).to_be_visible()
    expect(page.locator('(//h2)[1]')).to_be_visible()
    expect(page.locator('(//h2)[2]')).to_be_visible()
    expect(page.locator('(//h2)[4]')).to_be_visible()
    expect(page.locator('(//div[contains(text(), "ПРОВАЙДЕР")])[1]')).to_be_visible()
    expect(page.locator('//input[@name="sort_tariffs"]')).to_be_visible()
    for i in range(2, 11):
        expect(page.locator(f'(//div[@itemprop="offers"])[{i}]')).to_be_visible()
    for i in range(2, 11):
        expect(page.locator(f'(//span[contains(text(), "Подключить")])[{i}]')).to_be_visible()
    expect(page.locator('//div[@datatest="providers_find_adress"]')).to_be_visible()
    expect(page.locator('//div[@datatest="providers_callback2"]')).to_be_visible()
    for i in range(1, 19):
        expect(page.locator(f'(//a[@datatest="top_provider_block"])[{i}]')).to_be_visible()
    for i in range(1, 20):
        expect(page.locator(f'(//h3)[{i}]')).to_be_visible()


def test_internet_tv_mobile(page: Page):
    page.goto('https://www.moskvaonline.ru/balashiha/rates/internet-tv-mobile')
    check_header(page)
    footer_mol(page)
    search_tariffs(page)
    check_header_balashixa(page)
    check_tags(page)
    sorting(page)
    expect(page.locator('//span[contains(text(), "Подключить интернет")]')).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Тарифы на интернет")])[1]')).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Интернет+тв+мобильная связь")])[1]')).to_be_visible()
    expect(page.locator('//h1')).to_be_visible()
    expect(page.locator('(//h2)[1]')).to_be_visible()
    expect(page.locator('(//h2)[2]')).to_be_visible()
    expect(page.locator('(//h2)[4]')).to_be_visible()
    expect(page.locator('(//div[contains(text(), "ПРОВАЙДЕР")])[1]')).to_be_visible()
    expect(page.locator('//input[@name="sort_tariffs"]')).to_be_visible()
    for i in range(2, 16):
        expect(page.locator(f'(//div[@itemprop="offers"])[{i}]')).to_be_visible()
    for i in range(2, 16):
        expect(page.locator(f'(//span[contains(text(), "Подключить")])[{i}]')).to_be_visible()
    expect(page.locator('//div[@datatest="providers_find_adress"]')).to_be_visible()
    expect(page.locator('//div[@datatest="providers_callback2"]')).to_be_visible()
    for i in range(1, 19):
        expect(page.locator(f'(//a[@datatest="top_provider_block"])[{i}]')).to_be_visible()
    for i in range(1, 16):
        expect(page.locator(f'(//h3)[{i}]')).to_be_visible()


def test_nedorogoj_domashnij_internet(page: Page):
    page.goto('https://www.moskvaonline.ru/balashiha/rates/nedorogoj-domashnij-internet')
    check_header(page)
    footer_mol(page)
    search_tariffs(page)
    check_header_balashixa(page)
    check_tags(page)
    sorting(page)
    expect(page.locator('//span[contains(text(), "Подключить интернет")]')).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Тарифы на интернет")])[1]')).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Дешевый интернет")])[1]')).to_be_visible()
    expect(page.locator('//h1')).to_be_visible()
    expect(page.locator('(//h2)[1]')).to_be_visible()
    expect(page.locator('(//h2)[2]')).to_be_visible()
    expect(page.locator('(//h2)[4]')).to_be_visible()
    expect(page.locator('(//div[contains(text(), "ПРОВАЙДЕР")])[1]')).to_be_visible()
    expect(page.locator('//input[@name="sort_providers"]')).to_be_visible()
    for i in range(2, 30):
        expect(page.locator(f'(//div[@itemprop="offers"])[{i}]')).to_be_visible()
    for i in range(2, 30):
        expect(page.locator(f'(//span[contains(text(), "Подключить")])[{i}]')).to_be_visible()
    expect(page.locator('//div[@datatest="providers_find_adress"]')).to_be_visible()
    expect(page.locator('//div[@datatest="providers_callback2"]')).to_be_visible()
    for i in range(1, 19):
        expect(page.locator(f'(//a[@datatest="top_provider_block"])[{i}]')).to_be_visible()
    for i in range(1, 20):
        expect(page.locator(f'(//h3)[{i}]')).to_be_visible()


def test_internet_100(page: Page):
    page.goto('https://www.moskvaonline.ru/balashiha/rates/internet-100-mbit')
    check_header(page)
    footer_mol(page)
    search_tariffs(page)
    check_header_balashixa(page)
    check_tags(page)
    sorting(page)
    expect(page.locator('//span[contains(text(), "Подключить интернет")]')).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Тарифы на интернет")])[1]')).to_be_visible()
    expect(page.locator('(//span[contains(text(), "100 мб/с")])[1]')).to_be_visible()
    expect(page.locator('//h1')).to_be_visible()
    expect(page.locator('(//h2)[1]')).to_be_visible()
    expect(page.locator('(//h2)[2]')).to_be_visible()
    expect(page.locator('(//h2)[4]')).to_be_visible()
    expect(page.locator('(//a[@href="/balashiha/ratesmobile"])[1]')).to_be_visible()
    expect(page.locator('(//div[contains(text(), "ПРОВАЙДЕР")])[1]')).to_be_visible()
    expect(page.locator('//input[@name="sort_providers"]')).to_be_visible()
    for i in range(2, 30):
        expect(page.locator(f'(//div[@itemprop="offers"])[{i}]')).to_be_visible()
    for i in range(2, 30):
        expect(page.locator(f'(//span[contains(text(), "Подключить")])[{i}]')).to_be_visible()
    expect(page.locator('//div[@datatest="providers_find_adress"]')).to_be_visible()
    expect(page.locator('//div[@datatest="providers_callback2"]')).to_be_visible()
    for i in range(1, 19):
        expect(page.locator(f'(//a[@datatest="top_provider_block"])[{i}]')).to_be_visible()
    for i in range(1, 16):
        expect(page.locator(f'(//h3)[{i}]')).to_be_visible()


def test_internet_300(page: Page):
    page.goto('https://www.moskvaonline.ru/balashiha/rates/internet-300-mbit')
    check_header(page)
    footer_mol(page)
    search_tariffs(page)
    check_header_balashixa(page)
    check_tags(page)
    sorting(page)
    expect(page.locator('//span[contains(text(), "Подключить интернет")]')).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Тарифы на интернет")])[1]')).to_be_visible()
    expect(page.locator('(//span[contains(text(), "300 мб/с")])[1]')).to_be_visible()
    expect(page.locator('//h1')).to_be_visible()
    expect(page.locator('(//h2)[1]')).to_be_visible()
    expect(page.locator('(//h2)[2]')).to_be_visible()
    expect(page.locator('(//h2)[4]')).to_be_visible()
    expect(page.locator('(//a[@href="/balashiha/ratesmobile"])[1]')).to_be_visible()
    for i in range(2, 20):
        expect(page.locator(f'(//div[@itemprop="offers"])[{i}]')).to_be_visible()
    for i in range(2, 20):
        expect(page.locator(f'(//span[contains(text(), "Подключить")])[{i}]')).to_be_visible()
    expect(page.locator('//div[@datatest="providers_find_adress"]')).to_be_visible()
    expect(page.locator('//div[@datatest="providers_callback2"]')).to_be_visible()
    for i in range(1, 19):
        expect(page.locator(f'(//a[@datatest="top_provider_block"])[{i}]')).to_be_visible()
    for i in range(1, 19):
        expect(page.locator(f'(//h3)[{i}]')).to_be_visible()


def test_internet_500(page: Page):
    page.goto('https://www.moskvaonline.ru/balashiha/rates/internet-500-mbit')
    check_header(page)
    footer_mol(page)
    search_tariffs(page)
    check_header_balashixa(page)
    check_tags(page)
    sorting(page)
    expect(page.locator('//span[contains(text(), "Подключить интернет")]')).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Тарифы на интернет")])[1]')).to_be_visible()
    expect(page.locator('(//span[contains(text(), "500 мб/с")])[1]')).to_be_visible()
    expect(page.locator('//h1')).to_be_visible()
    expect(page.locator('(//h2)[1]')).to_be_visible()
    expect(page.locator('(//h2)[2]')).to_be_visible()
    expect(page.locator('(//h2)[4]')).to_be_visible()
    expect(page.locator('(//a[@href="/balashiha/ratesmobile"])[1]')).to_be_visible()
    for i in range(2, 25):
        expect(page.locator(f'(//div[@itemprop="offers"])[{i}]')).to_be_visible()
    for i in range(2, 25):
        expect(page.locator(f'(//span[contains(text(), "Подключить")])[{i}]')).to_be_visible()
    expect(page.locator('//div[@datatest="providers_find_adress"]')).to_be_visible()
    expect(page.locator('//div[@datatest="providers_callback2"]')).to_be_visible()
    for i in range(1, 19):
        expect(page.locator(f'(//a[@datatest="top_provider_block"])[{i}]')).to_be_visible()
    for i in range(1, 18):
        expect(page.locator(f'(//h3)[{i}]')).to_be_visible()


def test_online_kinoteatr(page: Page):
    page.goto('https://www.moskvaonline.ru/balashiha/rates/online-kinoteatr')
    check_header(page)
    footer_mol(page)
    search_tariffs(page)
    check_header_balashixa(page)
    check_tags(page)
    sorting(page)
    expect(page.locator('//span[contains(text(), "Подключить интернет")]')).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Тарифы на интернет")])[1]')).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Онлайн-кинотеатр")])[1]')).to_be_visible()
    expect(page.locator('//h1')).to_be_visible()
    expect(page.locator('(//h2)[1]')).to_be_visible()
    expect(page.locator('(//h2)[2]')).to_be_visible()
    expect(page.locator('(//h2)[4]')).to_be_visible()
    expect(page.locator('(//a[@href="/balashiha/ratesmobile"])[1]')).to_be_visible()
    for i in range(2, 23):
        expect(page.locator(f'(//div[@itemprop="offers"])[{i}]')).to_be_visible()
    for i in range(2, 24):
        expect(page.locator(f'(//span[contains(text(), "Подключить")])[{i}]')).to_be_visible()
    expect(page.locator('//div[@datatest="providers_find_adress"]')).to_be_visible()
    expect(page.locator('//div[@datatest="providers_callback2"]')).to_be_visible()
    for i in range(1, 19):
        expect(page.locator(f'(//a[@datatest="top_provider_block"])[{i}]')).to_be_visible()
    for i in range(1, 8):
        expect(page.locator(f'(//h3)[{i}]')).to_be_visible()


def test_reviews(page: Page):
    page.goto('https://www.moskvaonline.ru/balashiha/reviews')
    check_header(page)
    footer_mol(page)
    check_header_balashixa(page)
    expect(page.locator('//span[contains(text(), "Подключить интернет")]')).to_be_visible()
    expect(page.locator('//span[contains(text(), "Подключить интернет")]')).to_be_visible()
    expect(page.locator('(//h1)[1]')).to_be_visible()
    expect(page.locator('(//div[@data-test="waitingCall_button"])[1]')).to_be_visible()
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


def test_reviews2(page: Page):
    page.goto('https://www.moskvaonline.ru/balashiha/reviews/2')
    check_header(page)
    footer_mol(page)
    check_header_balashixa(page)
    expect(page.locator('//span[contains(text(), "Подключить интернет")]')).to_be_visible()
    expect(page.locator('//span[contains(text(), "Подключить интернет")]')).to_be_visible()
    expect(page.locator('(//h1)[1]')).to_be_visible()
    expect(page.locator('(//div[@data-test="waitingCall_button"])[1]')).to_be_visible()
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


def test_address(page: Page):
    page.goto('https://www.moskvaonline.ru/balashiha/address')
    check_header(page)
    footer_mol(page)
    check_header_balashixa(page)
    search_tariffs(page)
    expect(page.locator('//span[contains(text(), "Подключить интернет")]')).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Карта покрытия")])[1]')).to_be_visible()
    expect(page.locator('(//h1)[1]')).to_be_visible()
    expect(page.locator('(//h2)[3]')).to_be_visible()
    expect(page.locator('(//div[contains(text(), "Введите ваш адрес и сравните всех провайдеров своего дома в одной удобной таблице.") ])[1]')).to_be_visible()
    expect(page.locator('(//h2)[5]')).to_be_visible()
    for i in range(1, 19):
        expect(page.locator(f'(//a[@datatest="top_provider_block"])[{i}]')).to_be_visible()
    expect(page.locator('(//h2)[6]')).to_be_visible()
    expect(page.locator('(//div[contains(text(), "Б")])[4]')).to_be_visible()
    expect(page.locator('(//h2)[1]')).to_be_visible()
    for i in range(1, 6):
        expect(page.locator(f'(//h3)[{i}]')).to_be_visible()
    for i in range(1, 6):
        expect(page.locator(f'(//p)[{i}]')).to_be_visible()
    expect(page.locator('(//h2)[2]')).to_be_visible()


def test_balashixa_address_region(page: Page):
    page.goto('https://www.moskvaonline.ru/balashiha/address/%D0%B1%D0%B0%D0%BB%D0%B0%D1%88%D0%B8%D1%85%D0%B0-id422')
    check_header(page)
    footer_mol(page)
    check_header_balashixa(page)
    search_tariffs(page)
    blue_form(page)
    expect(page.locator('//span[contains(text(), "Подключить интернет")]')).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Карта покрытия")])[1]')).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Интернет провайдеры в Балашиха")])[1]')).to_be_visible()
    expect(page.locator('(//h1)[1]')).to_be_visible()
    for i in range(1, 5):
        expect(page.locator(f'(//h2)[{i}]')).to_be_visible()
    expect(page.locator('(//p[contains(text(), "Введите ваш адрес и сравните всех провайдеров своего дома в одной удобной таблице") ])[1]')).to_be_visible()
    for i in range(1, 6):
        expect(page.locator(f'(//h3)[{i}]')).to_be_visible()
    for i in range(1, 15):
        expect(page.locator(f'(//div[@datatest="providers_provider_button"])[{i}]')).to_be_visible()
    for i in range(2, 30):
        expect(page.locator(f'(//span[contains(text(), "Подключить")])[{i}]')).to_be_visible()
    for i in range(5, 20):
        expect(page.locator(f'(//a[@aria-label])[{i}]')).to_be_visible()
    for i in range(1, 5):
        expect(page.locator(f'(//div[@itemprop="mainEntity"])[{i}]')).to_be_visible()


def test_balashixa_address_street(page: Page):
    page.goto('https://www.moskvaonline.ru/balashiha/address/%D0%B1%D0%B0%D0%BB%D0%B0%D1%88%D0%B8%D1%85%D0%B0-id422/%D1%83%D0%BB-%D0%B1%D1%8B%D0%BA%D0%BE%D0%B2%D1%81%D0%BA%D0%BE%D0%B3%D0%BE-id265284')
    check_header(page)
    footer_mol(page)
    check_header_balashixa(page)
    expect(page.locator('//span[contains(text(), "Подключить интернет")]')).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Карта покрытия")])[1]')).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Интернет провайдеры в Балашиха")])[1]')).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Быковского")])[1]')).to_be_visible()
    expect(page.locator('(//h1)[1]')).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Дом")])[1]')).to_be_visible()
    expect(page.locator('(//div[contains(text(), "показать тарифы")])[1]')).to_be_visible()
    expect(page.locator('(//div[@datatest="providers_find_adress"])[1]')).to_be_visible()
    expect(page.locator('(//div[@datatest="providers_find_adress"]//span[contains(text(), "Дом")])[1]')).to_be_visible()
    expect(page.locator(
        '(//div[@datatest="providers_find_adress"]//div[contains(text(), "Проверить")])[1]')).to_be_visible()
    expect(page.locator('(//div[@class="container"]//div[@class="col"])[1]')).to_be_visible()
    for i in range(1, 6):
        expect(page.locator(f'(//h2)[{i}]')).to_be_visible()
    expect(page.locator('(//p[contains(text(), "Введите ваш адрес и сравните всех провайдеров своего дома в одной удобной таблице") ])[1]')).to_be_visible()
    for i in range(1, 6):
        expect(page.locator(f'(//h3)[{i}]')).to_be_visible()
    for i in range(1, 5):
        expect(page.locator(f'(//div[@datatest="providers_provider_button"])[{i}]')).to_be_visible()
    for i in range(2, 11):
        expect(page.locator(f'(//span[contains(text(), "Подключить")])[{i}]')).to_be_visible()
    for i in range(5, 9):
        expect(page.locator(f'(//a[@aria-label])[{i}]')).to_be_visible()
    for i in range(1, 5):
        expect(page.locator(f'(//div[@itemprop="mainEntity"])[{i}]')).to_be_visible()


def test_balashixa_address_street2(page: Page):
    page.goto('https://www.moskvaonline.ru/balashiha/address/%D0%B1%D0%B0%D0%BB%D0%B0%D1%88%D0%B8%D1%85%D0%B0-id422/%D1%83%D0%BB-%D0%B1%D1%8B%D0%BA%D0%BE%D0%B2%D1%81%D0%BA%D0%BE%D0%B3%D0%BE-id265284')
    check_header(page)
    footer_mol(page)
    check_header_balashixa(page)
    expect(page.locator('(//span[contains(text(), "Дом")])[1]')).to_be_visible()
    expect(page.locator('(//div[contains(text(), "показать тарифы")])[1]')).to_be_visible()
    expect(page.locator('(//div[@datatest="providers_find_adress"])[1]')).to_be_visible()
    expect(page.locator('(//div[@datatest="providers_find_adress"]//span[contains(text(), "Дом")])[1]')).to_be_visible()
    expect(page.locator(
        '(//div[@datatest="providers_find_adress"]//div[contains(text(), "Проверить")])[1]')).to_be_visible()
    expect(page.locator('//span[contains(text(), "Подключить интернет")]')).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Карта покрытия")])[1]')).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Интернет провайдеры в Балашиха")])[1]')).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Быковского")])[1]')).to_be_visible()
    expect(page.locator('(//h1)[1]')).to_be_visible()
    expect(page.locator('(//div[@class="container"]//div[@class="col"])[1]')).to_be_visible()
    for i in range(1, 6):
        expect(page.locator(f'(//h2)[{i}]')).to_be_visible()
    expect(page.locator('(//p[contains(text(), "Введите ваш адрес и сравните всех провайдеров своего дома в одной удобной таблице") ])[1]')).to_be_visible()
    for i in range(1, 6):
        expect(page.locator(f'(//h3)[{i}]')).to_be_visible()
    for i in range(1, 5):
        expect(page.locator(f'(//div[@datatest="providers_provider_button"])[{i}]')).to_be_visible()
    for i in range(2, 11):
        expect(page.locator(f'(//span[contains(text(), "Подключить")])[{i}]')).to_be_visible()
    for i in range(5, 9):
        expect(page.locator(f'(//a[@aria-label])[{i}]')).to_be_visible()
    for i in range(1, 5):
        expect(page.locator(f'(//div[@itemprop="mainEntity"])[{i}]')).to_be_visible()


def test_balashixa_rates(page: Page):
    page.goto('https://www.moskvaonline.ru/balashiha/rates')
    check_header(page)
    footer_mol(page)
    check_header_balashixa(page)
    search_tariffs(page)
    expect(page.locator('//span[contains(text(), "Подключить интернет")]')).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Тарифы на интернет")])[1]')).to_be_visible()
    expect(page.locator('(//h1)[1]')).to_be_visible()
    for i in range(1, 8):
        expect(page.locator(f'(//h2)[{i}]')).to_be_visible()
    expect(page.locator('(//p[contains(text(), "Узнайте, какие тарифы доступны в вашем доме") ])[1]')).to_be_visible()
    check_tags(page)
    for i in range(1, 6):
        expect(page.locator(f'(//h3)[{i}]')).to_be_visible()
    for i in range(1, 20):
        expect(page.locator(f'(//div[@datatest="providers_provider_button"])[{i}]')).to_be_visible()
    for i in range(2, 25):
        expect(page.locator(f'(//span[contains(text(), "Подключить")])[{i}]')).to_be_visible()
    for i in range(5, 24):
        expect(page.locator(f'(//a[@aria-label])[{i}]')).to_be_visible()
    for i in range(1, 2):
        expect(page.locator(f'(//a[@aria-label="Переключить страницу"])[{i}]')).to_be_visible()
    expect(page.get_by_role("heading", name="Топ провайдеров в Балашихе")).to_be_visible()
    expect(page.get_by_role("link", name="Тарифы провайдера Онлайм Онлайм")).to_be_visible()
    expect(page.locator("li").filter(has_text="Ростелеком").first).to_be_visible()
    expect(page.get_by_role("link", name="Тарифы провайдера МТС Home")).to_be_visible()


def test_sat_balashixa_page(page: Page):
    page.goto('https://www.moskvaonline.ru/balashiha/orders/sat')
    check_header(page)
    footer_mol(page)
    check_header_balashixa(page)
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


def test_office_balashixa_page(page: Page):
    page.goto('https://www.moskvaonline.ru/balashiha/orders/office')
    check_header(page)
    footer_mol(page)
    check_header_balashixa(page)
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
    expect(page.locator('//div[contains(text(), "отзывы о провайдерах")]')).to_be_visible()
    expect(page.locator('(//a[contains(text(), "оставить отзыв")])[1]')).to_be_visible()
    expect(page.locator('(//a[contains(text(), "все отзывы")])[1]')).to_be_visible()
    for i in range(1, 4):
        expect(page.locator(f'(//div[@itemtype="https://schema.org/Review"])[{i}]')).to_be_visible()


def test_business_balashixa_page(page: Page):
    page.goto('https://www.moskvaonline.ru/balashiha/business')
    check_header(page)
    footer_mol(page)
    check_header_balashixa(page)
    page_internet_in_office(page)
    expect(page.locator('//h1')).to_be_visible()
    expect(page.locator('//input[@datatest="business_order_input_person"]')).to_be_visible()
    expect(page.locator('//input[@datatest="business_order_input_tel"]')).to_be_visible()
    expect(page.locator('(//input[@datatest="main_input_street_home_new"])[1]')).to_be_visible()
    expect(page.locator('(//input[@datatest="main_input_street_home_new"])[2]')).to_be_visible()


def test_provider_mts_page(page: Page):
    page.goto('https://www.moskvaonline.ru/balashiha/providers/mts')
    check_header(page)
    footer_mol(page)
    check_header_balashixa(page)
    expect(page.locator('//img[@alt="Лого провайдера"]')).to_be_visible()
    expect(page.get_by_role("link", name="Подключить интернет")).to_be_visible()
    expect(page.get_by_role("link", name="Провайдеры Балашихи")).to_be_visible()
    expect(page.locator("#provider_banner").get_by_text("МТС", exact=True)).to_be_visible()
    expect(page.locator("#provider_banner").get_by_text("Оставить заявку")).to_be_visible()
    expect(page.locator("#provider_banner").get_by_text("Подключение")).to_be_visible()
    expect(page.get_by_role("link", name="+7 (800) 300-94-62")).to_be_visible()
    expect(page.locator("#provider_banner").get_by_text("Техподдержка")).to_be_visible()
    expect(page.get_by_role("link", name="+7 (800) 250-08-90")).to_be_visible()
    expect(page.get_by_text("Проверить доступность МТС по адресу")).to_be_visible()
    search_tariffs(page)
    expect(page.get_by_role("link", name="О провайдере")).to_be_visible()
    expect(page.locator('(//a[contains(text(), "Тарифы")])[3]')).to_be_visible()
    expect(page.get_by_role("link", name="акции", exact=True)).to_be_visible()
    expect(page.get_by_text("Тарифы", exact=True).nth(3)).to_be_visible()
    expect(page.get_by_role("link", name="Все тарифы").first).to_be_visible()
    expect(page.get_by_text("Оставить заявку").nth(1)).to_be_visible()
    for i in range(1, 6):
        expect(page.locator(f'(//div[@datatest="providers_form_inspect_connect_tariff_button"])[{i}]')).to_be_visible()
    expect(page.locator('//div[@data-test="countRates"]')).to_be_visible()
    expect(page.locator('//div[contains(text(), "Отзывы о провайдере")]')).to_be_visible()
    expect(page.locator('(//a[contains(text(), "Все тарифы")])[1]')).to_be_visible()
    expect(page.locator('(//div[@itemtype="https://schema.org/Review"])[1]')).to_be_visible()
    expect(page.locator('(//a[contains(text(), "все отзывы")])[2]')).to_be_visible()
    expect(page.locator('//div[@itemtype="http://schema.org/Organization"]')).to_be_visible()
    expect(page.locator('(//h2)[1]')).to_be_visible()


def test_balashiha_provider_qwerty(page: Page):
    page.goto('https://www.moskvaonline.ru/balashiha/providers/qwerty')
    check_header(page)
    footer_mol(page)
    check_header_balashixa(page)
    expect(page.locator('//img[@alt="Лого провайдера"]')).to_be_visible()
    expect(page.get_by_role("link", name="Подключить интернет")).to_be_visible()
    expect(page.get_by_role("link", name="Провайдеры Балашихи")).to_be_visible()
    expect(page.locator("#provider_banner").get_by_text("КВЕРТИ", exact=True)).to_be_visible()
    expect(page.locator("#provider_banner").get_by_text("Оставить заявку")).to_be_visible()
    expect(page.locator("#provider_banner").get_by_text("Подключение")).to_be_visible()
    expect(page.get_by_role("link", name="+7 (495) 500-00-44")).to_be_visible()
    expect(page.locator("#provider_banner").get_by_text("Техподдержка")).to_be_visible()
    expect(page.get_by_role("link", name="+7 (495) 500-00-45")).to_be_visible()
    expect(page.locator('(//h1)[1]')).to_be_visible()
    expect(page.get_by_text("Проверить доступность КВЕРТИ по адресу")).to_be_visible()
    search_tariffs(page)
    expect(page.get_by_role("link", name="О провайдере")).to_be_visible()
    expect(page.locator('(//a[contains(text(), "Тарифы")])[3]')).to_be_visible()
    expect(page.locator('(//a[contains(text(), "Отзывы")])[1]')).to_be_visible()
    expect(page.get_by_text("Оставить заявку").nth(1)).to_be_visible()
    for i in range(1, 6):
        expect(page.locator(f'(//div[@datatest="providers_form_inspect_connect_tariff_button"])[{i}]')).to_be_visible()
    expect(page.locator('//div[@data-test="countRates"]')).to_be_visible()
    expect(page.locator('//div[contains(text(), "Отзывы наших клиентов")]')).to_be_visible()
    expect(page.locator('(//a[contains(text(), "Все тарифы")])[1]')).to_be_visible()
    expect(page.locator('(//div[@itemtype="https://schema.org/Review"])[1]')).to_be_visible()
    expect(page.locator('(//a[contains(text(), "все отзывы")])[2]')).to_be_visible()
    expect(page.locator('//div[@itemtype="http://schema.org/Organization"]')).to_be_visible()
    expect(page.locator('(//h2)[1]')).to_be_visible()
    for i in range(1, 6):
        expect(page.locator(f'(//div[@itemtype="https://schema.org/Review"])[{i}]')).to_be_visible()


def test_balashiha_provider_mts_rates(page: Page):
    page.goto('https://www.moskvaonline.ru/balashiha/providers/mts/rates')
    check_header(page)
    footer_mol(page)
    check_header_balashixa(page)
    expect(page.locator('//img[@alt="Лого провайдера"]')).to_be_visible()
    expect(page.get_by_role("link", name="Подключить интернет")).to_be_visible()
    expect(page.get_by_role("link", name="Провайдеры Балашихи")).to_be_visible()
    expect(page.locator("#provider_banner").get_by_text("МТС", exact=True)).to_be_visible()
    expect(page.locator('//span[contains(text(), "Тарифы")]')).to_be_visible()
    expect(page.locator("#provider_banner").get_by_text("Оставить заявку")).to_be_visible()
    expect(page.locator("#provider_banner").get_by_text("Подключение")).to_be_visible()
    expect(page.get_by_role("link", name="+7 (800) 300-94-62")).to_be_visible()
    expect(page.locator("#provider_banner").get_by_text("Техподдержка")).to_be_visible()
    expect(page.get_by_role("link", name="+7 (800) 250-08-90")).to_be_visible()
    expect(page.locator('(//h1)[1]')).to_be_visible()
    expect(page.get_by_text("Проверить доступность МТС по адресу")).to_be_visible()
    search_tariffs(page)
    expect(page.get_by_role("link", name="О провайдере")).to_be_visible()
    expect(page.locator('(//a[contains(text(), "Тарифы")])[3]')).to_be_visible()
    expect(page.locator('(//a[contains(text(), "Отзывы")])[1]')).to_be_visible()
    expect(page.get_by_role("link", name="акции", exact=True)).to_be_visible()
    expect(page.locator('(//a[@href="/balashiha/providers/mts/rates/internet-tv-mobile"])[1]')).to_be_visible()
    expect(page.locator('(//a[@href="/balashiha/providers/mts/rates/domashnij-internet"])[1]')).to_be_visible()
    expect(page.locator('(//a[@href="/balashiha/providers/mts/rates/nedorogoj-domashnij-internet"])[1]')).to_be_visible()
    expect(page.locator('(//a[@href="/balashiha/rates/online-kinoteatr"])[1]')).to_be_visible()
    sorting_second(page)
    for i in range(1, 15):
        expect(page.locator(f'(//div[@datatest="providers_form_inspect_connect_tariff_button"])[{i}]')).to_be_visible()
    expect(page.locator('(//h2)[1]')).to_be_visible()


def test_balashiha_operatory(page: Page):
    page.goto('https://www.moskvaonline.ru/balashiha/operatory')
    footer_mol(page)
    check_header_balashixa(page)
    expect(page.locator('(//span[contains(text(), "Подключить интернет")])[1]')).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Мобильные операторы")])[1]')).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Мобильные операторы")])[1]')).to_be_visible()
    for i in range(1, 7):
        expect(page.locator(f'(//span[contains(text(), "Подробнее")])[{i}]')).to_be_visible()
    for i in range(1, 7):
        expect(page.locator(f'(//div[@datatest="operators_operator_button"])[{i}]')).to_be_visible()


def test_balashiha_actions(page: Page):
    page.goto('https://www.moskvaonline.ru/balashiha/actions')
    check_header(page)
    footer_mol(page)
    check_header_balashixa(page)
    expect(page.get_by_role("link", name="Подключить интернет")).to_be_visible()
    expect(page.locator('//span[contains(text(), "Акции на домашний интернет")]')).to_be_visible()
    expect(page.locator('//h1')).to_be_visible()
    expect(page.locator('//div[contains(text(), "Сортировка")]')).to_be_visible()
    expect(page.locator('//input[@value="Сначала популярные "]')).to_be_visible()
    expect(page.locator('//h2')).to_be_visible()
    for i in range(2, 15):
        expect(page.locator(f'(//span[contains(text(), "Подключить")])[{i}]')).to_be_visible()


def test_balashiha_terms_of_use(page: Page):
    page.goto('https://www.moskvaonline.ru/balashiha/about/terms-of-use')
    check_header(page)
    footer_mol(page)
    check_header_balashixa(page)
    terms_of_use(page)


def test_balashiha_personal_data(page: Page):
    page.goto('https://www.moskvaonline.ru/balashiha/about/personal-data')
    check_header(page)
    footer_mol(page)
    check_header_balashixa(page)
    personal_data(page)


def test_partners_page(page: Page):
    page.goto('https://www.moskvaonline.ru/balashiha/about/partners')
    check_header(page)
    footer_mol(page)
    check_header_balashixa(page)
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