from playwright.sync_api import Page, expect
from pages.main_page import check_header, search_tariffs, one_click_form, tariffs_block, blue_form, sorting_second, \
    personal_data, contact_page
from pages.main_page import footer_mol, blue_form_second, search_tariffs_second, sorting, page_internet_in_office, \
    terms_of_use, rating_page, check_header_operator_page
from pages.main_page import tags_for_operatory, tags_mobile
from pages.MOL.balashika_page import review, check_tags, check_header_balashixa, tags_yota, page_nomera


def test_first_bal(page: Page):
    page.goto('https://www.moskvaonline.ru/balashiha')
    check_header(page)
    footer_mol(page)
    review(page)
    one_click_form(page)
    blue_form(page)
    search_tariffs(page)
    check_header_balashixa(page)
    expect(page.locator('//h1[contains(text(), "Подключить домашний интернет в Балашихе")]')).to_contain_text(
        'Подключить домашний интернет в Балашихе')
    expect(page.locator(
        '(//div[contains(text(), "Введите ваш адрес и сравните тарифы провайдеров Балашихи. Гарантия до 90 дней и кэшбэк до 1000 рублей!")])[1]')).to_be_visible()
    expect(page.locator('//div[@datatest="main_raitingprovider_button"]')).to_have_text('Рейтинг провайдеров')
    expect(page.locator('//div[@datatest="main_comparetariff_button"]')).to_have_text('Выгодные пакеты интернета3 в 1')
    expect(page.locator('//div[@class="col-sm-6 col-lg-4"]')).to_contain_text(
        'получили нашу помощь в выборе интернета за  15 лет')
    expect(page.locator('//div[@class="onlyNotMd onlyNotSm onlyNotXs col-lg-4"]')).to_contain_text(
        'Бесплатная консультация')
    expect(page.locator('//div[@datatest="main_inflat_button"]')).to_contain_text('ИнтернетВ квартиру')
    expect(page.locator('//div[@datatest="main_inhouse_button"]')).to_contain_text('ИнтернетНа дачу')
    expect(page.locator('//div[@datatest="main_inoffice_button"]')).to_contain_text('ИнтернетВ офис')
    expect(page.locator('//h2[contains(text(), "Выгодные тарифы домашнего интернета в Балашихе")]')).to_have_text(
        'Выгодные тарифы домашнего интернета в Балашихе')
    expect(page.locator('(//a[@datatest="providers_provider_alltariff_button"])[1]')).to_have_text('Показать все')
    expect(
        page.locator('(//h2[contains(text(), "Топ провайдеров домашнего интернета в Балашихе")])[2]')).to_contain_text(
        'Топ провайдеров домашнего интернета в Балашихе')
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
    expect(page.locator(
        '(//div[contains(text(), "Введите ваш адрес и сравните всех провайдеров своего дома в одной удобной таблице.") ])[1]')).to_be_visible()
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
    expect(page.locator(
        '(//p[contains(text(), "Введите ваш адрес и сравните всех провайдеров своего дома в одной удобной таблице") ])[1]')).to_be_visible()
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
    page.goto(
        'https://www.moskvaonline.ru/balashiha/address/%D0%B1%D0%B0%D0%BB%D0%B0%D1%88%D0%B8%D1%85%D0%B0-id422/%D1%83%D0%BB-%D0%B1%D1%8B%D0%BA%D0%BE%D0%B2%D1%81%D0%BA%D0%BE%D0%B3%D0%BE-id265284')
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
    expect(page.locator(
        '(//p[contains(text(), "Введите ваш адрес и сравните всех провайдеров своего дома в одной удобной таблице") ])[1]')).to_be_visible()
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
    page.goto(
        'https://www.moskvaonline.ru/balashiha/address/%D0%B1%D0%B0%D0%BB%D0%B0%D1%88%D0%B8%D1%85%D0%B0-id422/%D1%83%D0%BB-%D0%B1%D1%8B%D0%BA%D0%BE%D0%B2%D1%81%D0%BA%D0%BE%D0%B3%D0%BE-id265284')
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
    expect(page.locator(
        '(//p[contains(text(), "Введите ваш адрес и сравните всех провайдеров своего дома в одной удобной таблице") ])[1]')).to_be_visible()
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
    expect(
        page.locator('(//a[@href="/balashiha/providers/mts/rates/nedorogoj-domashnij-internet"])[1]')).to_be_visible()
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


def test_provider_onlime_rates2(page: Page):
    page.goto('https://www.moskvaonline.ru/balashiha/providers/onlime/rates/2')
    check_header(page)
    footer_mol(page)
    check_header_balashixa(page)
    expect(page.locator('//img[@alt="Лого провайдера"]')).to_be_visible()
    expect(page.get_by_role("link", name="Подключить интернет")).to_be_visible()
    expect(page.get_by_role("link", name="Провайдеры Балашихи")).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Онлайм")])[1]')).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Тарифы")])[1]')).to_be_visible()
    expect(page.locator('//h1')).to_be_visible()
    expect(page.locator("#provider_banner").get_by_text("Оставить заявку")).to_be_visible()
    expect(page.locator("#provider_banner").get_by_text("Подключение")).to_be_visible()
    expect(page.get_by_role("link", name="+7 (800) 707-80-00")).to_be_visible()
    expect(page.locator("#provider_banner").get_by_text("Техподдержка")).to_be_visible()
    expect(page.get_by_role("link", name="+7 (800) 707-12-12")).to_be_visible()
    expect(page.get_by_text("Проверить доступность Онлайм по адресу")).to_be_visible()
    search_tariffs(page)
    expect(page.get_by_role("link", name="О провайдере")).to_be_visible()
    expect(page.locator('(//a[contains(text(), "Тарифы")])[3]')).to_be_visible()
    expect(page.get_by_role("link", name="акции", exact=True)).to_be_visible()
    expect(page.locator('(//a[@href="/balashiha/rates/internet-i-mobilnaya-svyaz"])[1]')).to_be_visible()
    sorting_second(page)
    expect(page.get_by_text("Оставить заявку").nth(1)).to_be_visible()
    for i in range(1, 11):
        expect(page.locator(f'(//div[@datatest="providers_form_inspect_connect_tariff_button"])[{i}]')).to_be_visible()


def test_provider_mts_home_tag(page: Page):
    page.goto('https://www.moskvaonline.ru/balashiha/providers/mts-home/rates/internet-tv-mobile')
    check_header(page)
    footer_mol(page)
    check_header_balashixa(page)
    expect(page.locator('//img[@alt="Лого провайдера"]')).to_be_visible()
    expect(page.get_by_role("link", name="Подключить интернет")).to_be_visible()
    expect(page.get_by_role("link", name="Провайдеры Балашихи")).to_be_visible()
    expect(page.locator('(//span[contains(text(), "МТС Home")])[1]')).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Тарифы")])[1]')).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Интернет+тв+мобильная связь")])[1]')).to_be_visible()
    expect(page.locator('//h1')).to_be_visible()
    expect(page.locator("#provider_banner").get_by_text("Оставить заявку")).to_be_visible()
    expect(page.locator("#provider_banner").get_by_text("Подключение")).to_be_visible()
    expect(page.locator("#provider_banner").get_by_text("Техподдержка")).to_be_visible()
    expect(page.get_by_text("Проверить доступность МТС Home по адресу")).to_be_visible()
    search_tariffs(page)
    expect(page.get_by_role("link", name="О провайдере")).to_be_visible()
    expect(page.locator('(//a[contains(text(), "Тарифы")])[3]')).to_be_visible()
    expect(page.locator('(//a[contains(text(), "Отзывы")])[1]')).to_be_visible()
    expect(page.get_by_role("link", name="акции", exact=True)).to_be_visible()
    sorting_second(page)
    expect(page.get_by_text("Оставить заявку").nth(1)).to_be_visible()
    for i in range(1, 8):
        expect(page.locator(f'(//div[@datatest="button_form_inspect_connect_tariff_tag_button"])[{i}]')).to_be_visible()
    expect(page.locator('//h2')).to_be_visible()


def test_provider_rostelecom_internet_i_mobile(page: Page):
    page.goto('https://www.moskvaonline.ru/balashiha/providers/rostelecom/rates/internet-i-mobilnaya-svyaz')
    check_header(page)
    footer_mol(page)
    check_header_balashixa(page)
    expect(page.locator('//img[@alt="Лого провайдера"]')).to_be_visible()
    expect(page.get_by_role("link", name="Подключить интернет")).to_be_visible()
    expect(page.get_by_role("link", name="Провайдеры Балашихи")).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Ростелеком")])[1]')).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Тарифы")])[1]')).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Интернет и мобильная связь")])[1]')).to_be_visible()
    expect(page.locator('//h1')).to_be_visible()
    expect(page.locator("#provider_banner").get_by_text("Оставить заявку")).to_be_visible()
    expect(page.locator("#provider_banner").get_by_text("Подключение")).to_be_visible()
    expect(page.get_by_role("link", name="+7 (800) 302-65-79")).to_be_visible()
    expect(page.locator("#provider_banner").get_by_text("Техподдержка")).to_be_visible()
    expect(page.get_by_role("link", name="+7 (800) 100-08-00")).to_be_visible()
    expect(page.get_by_text("Проверить доступность Ростелеком по адресу")).to_be_visible()
    search_tariffs(page)
    expect(page.get_by_role("link", name="О провайдере")).to_be_visible()
    expect(page.locator('(//a[contains(text(), "Тарифы")])[3]')).to_be_visible()
    expect(page.locator('(//a[contains(text(), "Отзывы")])[1]')).to_be_visible()
    expect(page.get_by_role("link", name="акции", exact=True)).to_be_visible()
    sorting_second(page)
    expect(page.get_by_text("Оставить заявку").nth(1)).to_be_visible()
    for i in range(1, 2):
        expect(page.locator(f'(//div[@datatest="button_form_inspect_connect_tariff_tag_button"])[{i}]')).to_be_visible()


def test_provider_rostelecom_dom_internet(page: Page):
    page.goto('https://www.moskvaonline.ru/balashiha/providers/rostelecom/rates/internet-i-tv')
    check_header(page)
    footer_mol(page)
    check_header_balashixa(page)
    expect(page.locator('//img[@alt="Лого провайдера"]')).to_be_visible()
    expect(page.get_by_role("link", name="Подключить интернет")).to_be_visible()
    expect(page.get_by_role("link", name="Провайдеры Балашихи")).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Ростелеком")])[1]')).to_be_visible()
    expect(page.locator("#provider_banner").get_by_role("link", name="Тарифы")).to_be_visible()
    expect(page.get_by_text("Интернет+тв", exact=True)).to_be_visible()
    expect(page.locator('//h1')).to_be_visible()
    expect(page.locator("#provider_banner").get_by_text("Оставить заявку")).to_be_visible()
    expect(page.locator("#provider_banner").get_by_text("Подключение")).to_be_visible()
    expect(page.get_by_role("link", name="+7 (800) 302-65-79")).to_be_visible()
    expect(page.locator("#provider_banner").get_by_text("Техподдержка")).to_be_visible()
    expect(page.get_by_role("link", name="+7 (800) 100-08-00")).to_be_visible()
    expect(page.get_by_text("Проверить доступность Ростелеком по адресу")).to_be_visible()
    search_tariffs(page)
    expect(page.get_by_role("link", name="О провайдере")).to_be_visible()
    expect(page.locator('(//a[contains(text(), "Тарифы")])[3]')).to_be_visible()
    expect(page.locator('(//a[contains(text(), "Отзывы")])[1]')).to_be_visible()
    expect(page.get_by_role("link", name="акции", exact=True)).to_be_visible()
    sorting_second(page)
    expect(page.get_by_text("Оставить заявку").nth(1)).to_be_visible()
    for i in range(1, 6):
        expect(page.locator(f'(//div[@datatest="providers_form_inspect_connect_tariff_button"])[{i}]')).to_be_visible()


def test_provider_mtshome_dominternet(page: Page):
    page.goto('https://www.moskvaonline.ru/balashiha/providers/mts-home/rates/nedorogoj-domashnij-internet')
    check_header(page)
    footer_mol(page)
    check_header_balashixa(page)
    expect(page.locator('//img[@alt="Лого провайдера"]')).to_be_visible()
    expect(page.get_by_role("link", name="Подключить интернет")).to_be_visible()
    expect(page.get_by_role("link", name="Провайдеры Балашихи")).to_be_visible()
    expect(page.locator('(//span[contains(text(), "МТС Home")])[1]')).to_be_visible()
    expect(page.locator("#provider_banner").get_by_role("link", name="Тарифы")).to_be_visible()
    expect(page.get_by_text("Дешевый интернет", exact=True)).to_be_visible()
    expect(page.locator('//h1')).to_be_visible()
    expect(page.locator("#provider_banner").get_by_text("Оставить заявку")).to_be_visible()
    expect(page.locator("#provider_banner").get_by_text("Подключение")).to_be_visible()
    expect(page.locator("#provider_banner").get_by_text("Техподдержка")).to_be_visible()
    expect(page.get_by_text("Проверить доступность МТС Home по адресу")).to_be_visible()
    search_tariffs(page)
    expect(page.get_by_role("link", name="О провайдере")).to_be_visible()
    expect(page.locator('(//a[contains(text(), "Тарифы")])[3]')).to_be_visible()
    expect(page.locator('(//a[contains(text(), "Отзывы")])[1]')).to_be_visible()
    expect(page.get_by_role("link", name="акции", exact=True)).to_be_visible()
    sorting_second(page)
    expect(page.get_by_text("Оставить заявку").nth(1)).to_be_visible()
    for i in range(1, 12):
        expect(page.locator(f'(//div[@datatest="providers_form_inspect_connect_tariff_button"])[{i}]')).to_be_visible()
    expect(page.locator('//h2')).to_be_visible()


def test_provider_onlime_internet_tv(page: Page):
    page.goto('https://www.moskvaonline.ru/balashiha/providers/onlime/rates/internet-i-tv')
    check_header(page)
    footer_mol(page)
    check_header_balashixa(page)
    expect(page.locator('//img[@alt="Лого провайдера"]')).to_be_visible()
    expect(page.get_by_role("link", name="Подключить интернет")).to_be_visible()
    expect(page.get_by_role("link", name="Провайдеры Балашихи")).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Онлайм")])[1]')).to_be_visible()
    expect(page.locator("#provider_banner").get_by_role("link", name="Тарифы")).to_be_visible()
    expect(page.get_by_text("Интернет+тв", exact=True)).to_be_visible()
    expect(page.locator('//h1')).to_be_visible()
    expect(page.locator("#provider_banner").get_by_text("Оставить заявку")).to_be_visible()
    expect(page.locator("#provider_banner").get_by_text("Подключение")).to_be_visible()
    expect(page.get_by_role("link", name="+7 (800) 707-80-00")).to_be_visible()
    expect(page.locator("#provider_banner").get_by_text("Техподдержка")).to_be_visible()
    expect(page.get_by_role("link", name="+7 (800) 707-12-12")).to_be_visible()
    expect(page.get_by_text("Проверить доступность Онлайм по адресу")).to_be_visible()
    search_tariffs(page)
    expect(page.get_by_role("link", name="О провайдере")).to_be_visible()
    expect(page.locator('(//a[contains(text(), "Тарифы")])[3]')).to_be_visible()
    expect(page.locator('(//a[contains(text(), "Отзывы")])[1]')).to_be_visible()
    expect(page.get_by_role("link", name="акции", exact=True)).to_be_visible()
    sorting_second(page)
    expect(page.get_by_text("Оставить заявку").nth(1)).to_be_visible()
    for i in range(1, 6):
        expect(page.locator(f'(//div[@datatest="providers_form_inspect_connect_tariff_button"])[{i}]')).to_be_visible()
    expect(page.locator('//h2')).to_be_visible()


def test_provider_onlime_onlime_cinema(page: Page):
    page.goto('https://www.moskvaonline.ru/balashiha/providers/onlime/rates/online-kinoteatr')
    check_header(page)
    footer_mol(page)
    check_header_balashixa(page)
    expect(page.locator('//img[@alt="Лого провайдера"]')).to_be_visible()
    expect(page.get_by_role("link", name="Подключить интернет")).to_be_visible()
    expect(page.get_by_role("link", name="Провайдеры Балашихи")).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Онлайм")])[1]')).to_be_visible()
    expect(page.locator("#provider_banner").get_by_role("link", name="Тарифы")).to_be_visible()
    expect(page.get_by_text("Онлайн-кинотеатр", exact=True)).to_be_visible()
    expect(page.locator('//h1')).to_be_visible()
    expect(page.locator("#provider_banner").get_by_text("Оставить заявку")).to_be_visible()
    expect(page.locator("#provider_banner").get_by_text("Подключение")).to_be_visible()
    expect(page.get_by_role("link", name="+7 (800) 707-80-00")).to_be_visible()
    expect(page.locator("#provider_banner").get_by_text("Техподдержка")).to_be_visible()
    expect(page.get_by_role("link", name="+7 (800) 707-12-12")).to_be_visible()
    expect(page.get_by_text("Проверить доступность Онлайм по адресу")).to_be_visible()
    search_tariffs(page)
    expect(page.get_by_role("link", name="О провайдере")).to_be_visible()
    expect(page.locator('(//a[contains(text(), "Тарифы")])[3]')).to_be_visible()
    expect(page.get_by_role("link", name="акции", exact=True)).to_be_visible()
    sorting_second(page)
    expect(page.get_by_text("Оставить заявку").nth(1)).to_be_visible()
    for i in range(1, 10):
        expect(page.locator(f'(//div[@datatest="providers_form_inspect_connect_tariff_button"])[{i}]')).to_be_visible()
    expect(page.locator('//h2')).to_be_visible()


def test_provider_onlime(page: Page):
    page.goto('https://www.moskvaonline.ru/balashiha/providers/onlime')
    check_header(page)
    footer_mol(page)
    check_header_balashixa(page)
    expect(page.locator('//img[@alt="Лого провайдера"]')).to_be_visible()
    expect(page.get_by_role("link", name="Подключить интернет")).to_be_visible()
    expect(page.get_by_role("link", name="Провайдеры Балашихи")).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Онлайм")])[1]')).to_be_visible()
    expect(page.locator('//h1')).to_be_visible()
    expect(page.locator("#provider_banner").get_by_text("Оставить заявку")).to_be_visible()
    expect(page.locator("#provider_banner").get_by_text("Подключение")).to_be_visible()
    expect(page.get_by_role("link", name="+7 (800) 707-80-00")).to_be_visible()
    expect(page.locator("#provider_banner").get_by_text("Техподдержка")).to_be_visible()
    expect(page.get_by_role("link", name="+7 (800) 707-12-12")).to_be_visible()
    expect(page.get_by_text("Проверить доступность Онлайм по адресу")).to_be_visible()
    expect(page.get_by_role("link", name="О провайдере")).to_be_visible()
    expect(page.locator('(//a[contains(text(), "Тарифы")])[3]')).to_be_visible()
    expect(page.get_by_role("link", name="акции", exact=True)).to_be_visible()
    expect(page.get_by_text("Оставить заявку").nth(1)).to_be_visible()
    for i in range(1, 6):
        expect(page.locator(f'(//div[@datatest="providers_form_inspect_connect_tariff_button"])[{i}]')).to_be_visible()
    expect(page.locator('//h2')).to_be_visible()
    expect(page.locator('(//span[contains(text(), "контакты")])[1]')).to_be_visible()
    expect(page.locator('(//div[@itemtype="http://schema.org/Organization"])[1]')).to_be_visible()


def test_rating_rostelecom(page: Page):
    page.goto('https://www.moskvaonline.ru/balashiha/rating/rostelecom')
    check_header(page)
    footer_mol(page)
    check_header_balashixa(page)
    expect(page.locator('//img[@alt="Лого провайдера"]')).to_be_visible()
    expect(page.get_by_role("link", name="Подключить интернет")).to_be_visible()
    expect(page.get_by_role("link", name="Провайдеры Балашихи")).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Ростелеком")])[1]')).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Отзывы")])[1]')).to_be_visible()
    expect(page.locator('//h1')).to_be_visible()
    expect(page.locator("#provider_banner").get_by_text("Оставить заявку")).to_be_visible()
    expect(page.locator("#provider_banner").get_by_text("Подключение")).to_be_visible()
    expect(page.locator("#provider_banner").get_by_text("Техподдержка")).to_be_visible()
    expect(page.get_by_text("Проверить доступность Ростелеком по адресу")).to_be_visible()
    expect(page.get_by_role("link", name="О провайдере")).to_be_visible()
    expect(page.locator('(//a[contains(text(), "Тарифы")])[3]')).to_be_visible()
    expect(page.locator('(//a[contains(text(), "Отзывы")])[1]')).to_be_visible()
    expect(page.get_by_role("link", name="акции", exact=True)).to_be_visible()
    rating_page(page)
    expect(page.get_by_role("link", name="О провайдере")).to_be_visible()
    expect(page.locator('(//a[contains(text(), "Тарифы")])[3]')).to_be_visible()
    expect(page.get_by_role("link", name="акции", exact=True)).to_be_visible()
    expect(page.locator('//a[contains(text(), "оставить отзыв")]')).to_be_visible()
    for i in range(1, 10):
        expect(page.locator(f'(//div[@itemprop="review"])[{i}]')).to_be_visible()
    for i in range(1, 10):
        expect(page.locator(f'(//textarea[@aria-labelledby="label"])[{i}]')).to_be_visible()
    for i in range(1, 10):
        expect(page.locator(f'(//button[@aria-label="Оставить отзыв"])[{i}]')).to_be_visible()
    expect(page.locator('(//div[contains(text(), "Лучшие тарифы Ростелеком в Балашихе")])[1]')).to_be_visible()
    for i in range(1, 3):
        expect(page.locator(f'(//span[contains(text(), "Подключить по акции")])[{i}]')).to_be_visible()
    expect(page.locator('(//div[contains(text(), "Оставить заявку")])[2]')).to_be_visible()
    for i in range(1, 5):
        expect(page.locator(f'(//a[@aria-label="Переключить страницу"])[{i}]')).to_be_visible()


def test_rating_rostelecom2(page: Page):
    page.goto('https://www.moskvaonline.ru/balashiha/rating/rostelecom/2')
    check_header(page)
    footer_mol(page)
    check_header_balashixa(page)
    expect(page.locator('//img[@alt="Лого провайдера"]')).to_be_visible()
    expect(page.get_by_role("link", name="Подключить интернет")).to_be_visible()
    expect(page.get_by_role("link", name="Провайдеры Балашихи")).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Ростелеком")])[1]')).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Отзывы")])[1]')).to_be_visible()
    expect(page.locator('//h1')).to_be_visible()
    expect(page.locator("#provider_banner").get_by_text("Оставить заявку")).to_be_visible()
    expect(page.locator("#provider_banner").get_by_text("Подключение")).to_be_visible()
    expect(page.locator("#provider_banner").get_by_text("Техподдержка")).to_be_visible()
    expect(page.get_by_text("Проверить доступность Ростелеком по адресу")).to_be_visible()
    expect(page.get_by_role("link", name="О провайдере")).to_be_visible()
    expect(page.locator('(//a[contains(text(), "Тарифы")])[3]')).to_be_visible()
    expect(page.locator('(//a[contains(text(), "Отзывы")])[1]')).to_be_visible()
    expect(page.get_by_role("link", name="акции", exact=True)).to_be_visible()
    rating_page(page)
    expect(page.get_by_role("link", name="О провайдере")).to_be_visible()
    expect(page.locator('(//a[contains(text(), "Тарифы")])[3]')).to_be_visible()
    expect(page.get_by_role("link", name="акции", exact=True)).to_be_visible()
    expect(page.locator('//a[contains(text(), "оставить отзыв")]')).to_be_visible()
    for i in range(1, 10):
        expect(page.locator(f'(//div[@itemprop="review"])[{i}]')).to_be_visible()
    for i in range(1, 10):
        expect(page.locator(f'(//textarea[@aria-labelledby="label"])[{i}]')).to_be_visible()
    for i in range(1, 10):
        expect(page.locator(f'(//button[@aria-label="Оставить отзыв"])[{i}]')).to_be_visible()
    expect(page.locator('(//div[contains(text(), "Лучшие тарифы Ростелеком в Балашихе")])[1]')).to_be_visible()
    for i in range(1, 3):
        expect(page.locator(f'(//span[contains(text(), "Подключить по акции")])[{i}]')).to_be_visible()
    expect(page.locator('(//div[contains(text(), "Оставить заявку")])[2]')).to_be_visible()
    for i in range(1, 5):
        expect(page.locator(f'(//a[@aria-label="Переключить страницу"])[{i}]')).to_be_visible()


def test_rating_rostelecom_sortold(page: Page):
    page.goto('https://www.moskvaonline.ru/balashiha/rating/mts?sort=old')
    check_header(page)
    footer_mol(page)
    check_header_balashixa(page)
    expect(page.locator('//img[@alt="Лого провайдера"]')).to_be_visible()
    expect(page.get_by_role("link", name="Подключить интернет")).to_be_visible()
    expect(page.get_by_role("link", name="Провайдеры Балашихи")).to_be_visible()
    expect(page.locator('(//span[contains(text(), "МТС")])[1]')).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Отзывы")])[1]')).to_be_visible()
    expect(page.locator('//h1')).to_be_visible()
    expect(page.locator("#provider_banner").get_by_text("Оставить заявку")).to_be_visible()
    expect(page.locator("#provider_banner").get_by_text("Подключение")).to_be_visible()
    expect(page.locator("#provider_banner").get_by_text("Техподдержка")).to_be_visible()
    expect(page.get_by_text("Проверить доступность МТС по адресу")).to_be_visible()
    expect(page.get_by_role("link", name="О провайдере")).to_be_visible()
    expect(page.locator('(//a[contains(text(), "Тарифы")])[3]')).to_be_visible()
    expect(page.locator('(//a[contains(text(), "Отзывы")])[1]')).to_be_visible()
    expect(page.get_by_role("link", name="акции", exact=True)).to_be_visible()
    rating_page(page)
    expect(page.get_by_role("link", name="О провайдере")).to_be_visible()
    expect(page.locator('(//a[contains(text(), "Тарифы")])[3]')).to_be_visible()
    expect(page.get_by_role("link", name="акции", exact=True)).to_be_visible()
    expect(page.locator('//a[contains(text(), "оставить отзыв")]')).to_be_visible()
    expect(page.locator('(//div[@itemprop="review"])[1]')).to_be_visible()
    expect(page.locator('(//textarea[@aria-labelledby="label"])[1]')).to_be_visible()
    expect(page.locator('(//button[@aria-label="Оставить отзыв"])[1]')).to_be_visible()
    expect(page.locator('(//div[contains(text(), "Лучшие тарифы МТС в Балашихе")])[1]')).to_be_visible()
    expect(page.locator('(//button[@aria-label="Оставить отзыв"])[1]')).to_be_visible()
    for i in range(1, 3):
        expect(page.locator(f'(//span[contains(text(), "Подключить по акции")])[{i}]')).to_be_visible()
    expect(page.locator('(//div[contains(text(), "Оставить заявку")])[2]')).to_be_visible()


def test_providers_actions_rostelecom(page: Page):
    page.goto('https://www.moskvaonline.ru/balashiha/providers/actions/rostelecom')
    check_header(page)
    footer_mol(page)
    check_header_balashixa(page)
    expect(page.locator('//img[@alt="Лого провайдера"]')).to_be_visible()
    expect(page.get_by_role("link", name="Подключить интернет")).to_be_visible()
    expect(page.get_by_role("link", name="Провайдеры Балашихи")).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Ростелеком")])[1]')).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Акции")])[1]')).to_be_visible()
    expect(page.locator('//h1')).to_be_visible()
    expect(page.locator("#provider_banner").get_by_text("Оставить заявку")).to_be_visible()
    expect(page.locator("#provider_banner").get_by_text("Подключение")).to_be_visible()
    expect(page.get_by_role("link", name="+7 (800) 302-65-79")).to_be_visible()
    expect(page.locator("#provider_banner").get_by_text("Техподдержка")).to_be_visible()
    expect(page.get_by_role("link", name="+7 (800) 100-08-00")).to_be_visible()
    expect(page.get_by_text("Проверить доступность Ростелеком по адресу")).to_be_visible()
    expect(page.get_by_role("link", name="О провайдере")).to_be_visible()
    expect(page.locator('(//a[contains(text(), "Тарифы")])[3]')).to_be_visible()
    expect(page.locator('(//a[contains(text(), "Отзывы")])[1]')).to_be_visible()
    expect(page.get_by_role("link", name="акции", exact=True)).to_be_visible()
    for i in range(1, 10):
        expect(page.locator(f'(//span[contains(text(), "Подключить по акции")])[{i}]')).to_be_visible()
    expect(page.locator('(//div[contains(text(), "Оставить заявку")])[2]')).to_be_visible()
    for i in range(1, 2):
        expect(page.locator(f'(//h2)[{i}]')).to_be_visible()


def test_rating_akado(page: Page):
    page.goto('https://www.moskvaonline.ru/balashiha/rating/akado')
    check_header(page)
    footer_mol(page)
    check_header_balashixa(page)
    expect(page.locator('//img[@alt="Лого провайдера"]')).to_be_visible()
    expect(page.get_by_role("link", name="Подключить интернет")).to_be_visible()
    expect(page.get_by_role("link", name="Провайдеры Балашихи")).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Акадо")])[1]')).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Отзывы")])[1]')).to_be_visible()
    expect(page.locator('//h1')).to_be_visible()
    expect(page.locator("#provider_banner").get_by_text("Подключение")).to_be_visible()
    expect(page.get_by_role("link", name="+7 (495) 966-13-12")).to_be_visible()
    expect(page.locator("#provider_banner").get_by_text("Техподдержка")).to_be_visible()
    expect(page.get_by_role("link", name="+7 (499) 940-00-00")).to_be_visible()
    expect(page.get_by_text("Проверить доступность Акадо по адресу")).to_be_visible()
    expect(page.get_by_role("link", name="О провайдере")).to_be_visible()
    expect(page.locator('(//a[contains(text(), "Тарифы")])[3]')).to_be_visible()
    expect(page.locator('(//a[contains(text(), "Отзывы")])[1]')).to_be_visible()
    expect(page.get_by_role("link", name="акции", exact=True)).to_be_visible()
    rating_page(page)
    expect(page.locator('//a[contains(text(), "оставить отзыв")]')).to_be_visible()
    for i in range(1, 5):
        expect(page.locator(f'(//div[@itemprop="review"])[{i}]')).to_be_visible()
    for i in range(1, 5):
        expect(page.locator(f'(//textarea[@aria-labelledby="label"])[{i}]')).to_be_visible()
    for i in range(1, 5):
        expect(page.locator(f'(//button[@aria-label="Оставить отзыв"])[{i}]')).to_be_visible()
    expect(page.locator('(//div[contains(text(), "Лучшие тарифы Акадо в Балашихе")])[1]')).to_be_visible()
    for i in range(1, 3):
        expect(page.locator(f'(//span[contains(text(), "Подключить по акции")])[{i}]')).to_be_visible()


def test_providers_itc_electron(page: Page):
    page.goto('https://www.moskvaonline.ru/balashiha/providers/itc-electron')
    check_header(page)
    footer_mol(page)
    check_header_balashixa(page)
    expect(page.get_by_role("link", name="Подключить интернет")).to_be_visible()
    expect(page.get_by_role("link", name="Провайдеры Балашихи")).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Электрон-Телеком")])[1]')).to_be_visible()
    expect(page.locator('//img[@alt="Лого провайдера"]')).to_be_visible()
    expect(page.locator('//h1')).to_be_visible()
    expect(page.get_by_text("Проверить доступность Электрон-Телеком по адресу")).to_be_visible()
    search_tariffs(page)
    expect(page.get_by_role("link", name="О провайдере")).to_be_visible()
    expect(page.locator('//span[contains(text(), "контакты")]')).to_be_visible()
    expect(page.get_by_role("heading", name="Топ провайдеров в Балашихе")).to_be_visible()
    expect(page.get_by_role("link", name="Тарифы провайдера Ростелеком Ростелеком")).to_be_visible()
    expect(page.get_by_role("link", name="Тарифы провайдера Онлайм Онлайм")).to_be_visible()
    expect(page.get_by_role("link", name="Тарифы провайдера МТС Home")).to_be_visible()
    expect(page.get_by_role("heading", name="Недавно подключенные тарифы в Балашихе")).to_be_visible()
    expect(page.get_by_role("heading", name="Частые вопросы")).to_be_visible()
    for i in range(1, 5):
        expect(page.locator(f'(//span[contains(text(), "Подключить")])[{i}]')).to_be_visible()


def test_rating_virgin_connect(page: Page):
    page.goto('https://www.moskvaonline.ru/balashiha/rating/virgin-connect')
    check_header(page)
    footer_mol(page)
    check_header_balashixa(page)
    expect(page.locator('//img[@alt="Лого провайдера"]')).to_be_visible()
    expect(page.get_by_role("link", name="Подключить интернет")).to_be_visible()
    expect(page.get_by_role("link", name="Провайдеры Балашихи")).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Верджин Коннект")])[1]')).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Отзывы")])[1]')).to_be_visible()
    expect(page.locator('//h1')).to_be_visible()
    expect(page.get_by_text("Проверить доступность Верджин Коннект по адресу")).to_be_visible()
    search_tariffs(page)
    expect(page.get_by_role("link", name="О провайдере")).to_be_visible()
    expect(page.locator('(//a[contains(text(), "Отзывы")])[1]')).to_be_visible()
    rating_page(page)
    expect(page.locator('//a[contains(text(), "оставить отзыв")]')).to_be_visible()
    for i in range(1, 10):
        expect(page.locator(f'(//div[@itemprop="review"])[{i}]')).to_be_visible()
    for i in range(1, 10):
        expect(page.locator(f'(//textarea[@aria-labelledby="label"])[{i}]')).to_be_visible()
    for i in range(1, 10):
        expect(page.locator(f'(//button[@aria-label="Оставить отзыв"])[{i}]')).to_be_visible()
    expect(page.locator('(//h2[contains(text(), "Недавно подключенные тарифы в Балашихе")])[1]')).to_be_visible()
    for i in range(1, 5):
        expect(page.locator(f'(//span[contains(text(), "Проверить адрес")])[{i}]')).to_be_visible()
    for i in range(1, 2):
        expect(page.locator(f'(//a[@aria-label="Переключить страницу"])[{i}]')).to_be_visible()


def test_provider_inetcom(page: Page):
    page.goto('https://www.moskvaonline.ru/balashiha/providers/inetcom')
    check_header(page)
    footer_mol(page)
    check_header_balashixa(page)
    expect(page.locator('//img[@alt="Лого провайдера"]')).to_be_visible()
    expect(page.get_by_role("link", name="Подключить интернет")).to_be_visible()
    expect(page.get_by_role("link", name="Провайдеры Балашихи")).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Инетком")])[1]')).to_be_visible()
    expect(page.locator('//h1')).to_be_visible()
    expect(page.locator("#provider_banner").get_by_text("Подключение")).to_be_visible()
    expect(page.locator('(//a[contains(text(), "+7  (495)  744-02-03")])[1]')).to_be_visible()
    expect(page.locator("#provider_banner").get_by_text("Техподдержка")).to_be_visible()
    expect(page.get_by_text("Проверить доступность Инетком по адресу")).to_be_visible()
    search_tariffs(page)
    expect(page.get_by_role("link", name="О провайдере")).to_be_visible()
    expect(page.locator('(//a[contains(text(), "Тарифы")])[3]')).to_be_visible()
    expect(page.locator('(//a[contains(text(), "Отзывы")])[3]')).to_be_visible()
    for i in range(1, 6):
        expect(page.locator(f'(//div[@datatest="providers_form_inspect_connect_tariff_button"])[{i}]')).to_be_visible()
    expect(page.get_by_text("Отзывы наших клиентов")).to_be_visible()
    expect(page.get_by_role("link", name="Все тарифы").nth(1)).to_be_visible()
    expect(page.get_by_role("link", name="оставить отзыв")).to_be_visible()
    expect(page.get_by_role("heading", name="Частые вопросы")).to_be_visible()
    for i in range(1, 3):
        expect(page.locator(f'(//div[@itemtype="https://schema.org/Review"])[{i}]')).to_be_visible()


def test_rating_inetcom(page: Page):
    page.goto('https://www.moskvaonline.ru/balashiha/rating/inetcom')
    check_header(page)
    footer_mol(page)
    check_header_balashixa(page)
    expect(page.locator('//img[@alt="Лого провайдера"]')).to_be_visible()
    expect(page.get_by_role("link", name="Подключить интернет")).to_be_visible()
    expect(page.get_by_role("link", name="Провайдеры Балашихи")).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Инетком")])[1]')).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Отзывы")])[1]')).to_be_visible()
    expect(page.locator('//h1')).to_be_visible()
    expect(page.locator("#provider_banner").get_by_text("Подключение")).to_be_visible()
    expect(page.locator('(//a[contains(text(), "+7  (495)  744-02-03")])[1]')).to_be_visible()
    expect(page.locator("#provider_banner").get_by_text("Техподдержка")).to_be_visible()
    expect(page.get_by_text("Проверить доступность Инетком по адресу")).to_be_visible()
    search_tariffs(page)
    expect(page.get_by_role("link", name="О провайдере")).to_be_visible()
    expect(page.locator('(//a[contains(text(), "Отзывы")])[1]')).to_be_visible()
    rating_page(page)
    expect(page.locator('//a[contains(text(), "оставить отзыв")]')).to_be_visible()
    for i in range(1, 5):
        expect(page.locator(f'(//div[@itemprop="review"])[{i}]')).to_be_visible()
    for i in range(1, 5):
        expect(page.locator(f'(//textarea[@aria-labelledby="label"])[{i}]')).to_be_visible()
    for i in range(1, 5):
        expect(page.locator(f'(//button[@aria-label="Оставить отзыв"])[{i}]')).to_be_visible()
    expect(page.locator('(//div[contains(text(), "Лучшие тарифы Инетком в Балашихе")])[1]')).to_be_visible()
    for i in range(1, 3):
        expect(page.locator(f'(//span[contains(text(), "Подключить")])[{i}]')).to_be_visible()


def test_bal_operatory(page: Page):
    page.goto('https://www.moskvaonline.ru/balashiha/operatory')
    check_header_operator_page(page)
    footer_mol(page)
    expect(page.locator('(//span[contains(text(), "Подключить интернет")])[1]')).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Мобильные операторы")])[1]')).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Мобильные операторы")])[1]')).to_be_visible()
    for i in range(1, 7):
        expect(page.locator(f'(//span[contains(text(), "Подробнее")])[{i}]')).to_be_visible()
    for i in range(1, 7):
        expect(page.locator(f'(//div[@datatest="operators_operator_button"])[{i}]')).to_be_visible()


def test_bal_ratesmobile(page: Page):
    page.goto('https://www.moskvaonline.ru/balashiha/ratesmobile')
    check_header_operator_page(page)
    footer_mol(page)
    check_header_balashixa(page)
    page_nomera(page)
    tags_for_operatory(page)
    tags_mobile(page)
    for i in range(1, 15):
        expect(page.locator(f'(//div[contains(text(), "Выбрать")])[{i}]')).to_be_visible()


def test_operator_mts_ratesmobile_bal(page: Page):
    page.goto('https://www.moskvaonline.ru/balashiha/operatory/mts/ratesmobile')
    check_header_operator_page(page)
    footer_mol(page)
    check_header_balashixa(page)
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


def test_operator_mts_ratesmobile_modem_bal(page: Page):
    page.goto('https://www.moskvaonline.ru/balashiha/operatory/mts/ratesmobile/dlja-modema')
    check_header_operator_page(page)
    footer_mol(page)
    check_header_balashixa(page)
    expect(page.get_by_role("link", name="Подключить интернет")).to_be_visible()
    expect(page.get_by_role("link", name="Мобильные операторы")).to_be_visible()
    expect(page.locator('(//span[contains(text(), "МТС")])[1]')).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Тарифы")])[1]')).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Для модема/роутера")])[1]')).to_be_visible()
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


def test_operator_mts_ratesmobile_esim_bal(page: Page):
    page.goto('https://www.moskvaonline.ru/balashiha/operatory/mts/ratesmobile/esim')
    check_header_operator_page(page)
    footer_mol(page)
    check_header_balashixa(page)
    expect(page.get_by_role("link", name="Подключить интернет")).to_be_visible()
    expect(page.get_by_role("link", name="Мобильные операторы")).to_be_visible()
    expect(page.locator('(//span[contains(text(), "МТС")])[1]')).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Тарифы")])[1]')).to_be_visible()
    expect(page.locator('(//span[contains(text(), "eSIM")])[1]')).to_be_visible()
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


def test_operator_mts_ratesmobile_porf(page: Page):
    page.goto('https://www.moskvaonline.ru/balashiha/operatory/mts/ratesmobile/po-rossii')
    check_header_operator_page(page)
    footer_mol(page)
    check_header_balashixa(page)
    expect(page.get_by_role("link", name="Подключить интернет")).to_be_visible()
    expect(page.get_by_role("link", name="Мобильные операторы")).to_be_visible()
    expect(page.locator('(//span[contains(text(), "МТС")])[1]')).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Тарифы")])[1]')).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Связь по России")])[1]')).to_be_visible()
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


def test_operator_mts_ratesmobile_perenos_nomera(page: Page):
    page.goto('https://www.moskvaonline.ru/balashiha/operatory/mts/ratesmobile/perenos_nomera')
    check_header_operator_page(page)
    footer_mol(page)
    check_header_balashixa(page)
    expect(page.get_by_role("link", name="Подключить интернет")).to_be_visible()
    expect(page.get_by_role("link", name="Мобильные операторы")).to_be_visible()
    expect(page.locator('(//span[contains(text(), "МТС")])[1]')).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Тарифы")])[1]')).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Перейти со своим номером")])[1]')).to_be_visible()
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


def test_operator_mts_ratesmobile_mezhdunarodnye(page: Page):
    page.goto('https://www.moskvaonline.ru/balashiha/operatory/mts/ratesmobile/mezhdunarodnye')
    check_header_operator_page(page)
    footer_mol(page)
    check_header_balashixa(page)
    expect(page.get_by_role("link", name="Подключить интернет")).to_be_visible()
    expect(page.get_by_role("link", name="Мобильные операторы")).to_be_visible()
    expect(page.locator('(//span[contains(text(), "МТС")])[1]')).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Тарифы")])[1]')).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Роуминг за границей")])[1]')).to_be_visible()
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


def test_operator_mts_ratesmobile_vygodnye(page: Page):
    page.goto('https://www.moskvaonline.ru/balashiha/operatory/mts/ratesmobile/vygodnye')
    check_header_operator_page(page)
    footer_mol(page)
    check_header_balashixa(page)
    expect(page.get_by_role("link", name="Подключить интернет")).to_be_visible()
    expect(page.get_by_role("link", name="Мобильные операторы")).to_be_visible()
    expect(page.locator('(//span[contains(text(), "МТС")])[1]')).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Тарифы")])[1]')).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Выгодные")])[1]')).to_be_visible()
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


def test_operator_mts_ratesmobile_semeinye(page: Page):
    page.goto('https://www.moskvaonline.ru/balashiha/operatory/mts/ratesmobile/semeinye')
    check_header_operator_page(page)
    footer_mol(page)
    check_header_balashixa(page)
    expect(page.get_by_role("link", name="Подключить интернет")).to_be_visible()
    expect(page.get_by_role("link", name="Мобильные операторы")).to_be_visible()
    expect(page.locator('(//span[contains(text(), "МТС")])[1]')).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Тарифы")])[1]')).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Семейные")])[1]')).to_be_visible()
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


def test_operator_mts_ratesmobile_detskie(page: Page):
    page.goto('https://www.moskvaonline.ru/balashiha/operatory/mts/ratesmobile/detskie')
    check_header_operator_page(page)
    footer_mol(page)
    check_header_balashixa(page)
    expect(page.get_by_role("link", name="Подключить интернет")).to_be_visible()
    expect(page.get_by_role("link", name="Мобильные операторы")).to_be_visible()
    expect(page.locator('(//span[contains(text(), "МТС")])[1]')).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Тарифы")])[1]')).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Детские")])[1]')).to_be_visible()
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


def test_operator_mts_ratesmobile_unikalnye(page: Page):
    page.goto('https://www.moskvaonline.ru/balashiha/operatory/mts/ratesmobile/unikalnye')
    check_header_operator_page(page)
    footer_mol(page)
    check_header_balashixa(page)
    expect(page.get_by_role("link", name="Подключить интернет")).to_be_visible()
    expect(page.get_by_role("link", name="Мобильные операторы")).to_be_visible()
    expect(page.locator('(//span[contains(text(), "МТС")])[1]')).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Тарифы")])[1]')).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Непубличные")])[1]')).to_be_visible()
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
    for i in range(1, 10):
        expect(page.locator(f'(//div[contains(text(), "Выбрать")])[{i}]')).to_be_visible()
    expect(page.locator('(//h2)[1]')).to_be_visible()


def test_operator_mts_ratesmobile_bezlim_intern(page: Page):
    page.goto('https://www.moskvaonline.ru/balashiha/operatory/mts/ratesmobile/bezlimitnyj-internet')
    check_header_operator_page(page)
    footer_mol(page)
    check_header_balashixa(page)
    expect(page.get_by_role("link", name="Подключить интернет")).to_be_visible()
    expect(page.get_by_role("link", name="Мобильные операторы")).to_be_visible()
    expect(page.locator('(//span[contains(text(), "МТС")])[1]')).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Тарифы")])[1]')).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Безлимитный интернет")])[1]')).to_be_visible()
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
    expect(page.locator('(//h2)[1]')).to_be_visible()


def test_operator_mts_ratesmobile_bezlim_sviaz(page: Page):
    page.goto('https://www.moskvaonline.ru/balashiha/operatory/mts/ratesmobile/bezlimitnaja-svjaz')
    check_header_operator_page(page)
    footer_mol(page)
    check_header_balashixa(page)
    expect(page.get_by_role("link", name="Подключить интернет")).to_be_visible()
    expect(page.get_by_role("link", name="Мобильные операторы")).to_be_visible()
    expect(page.locator('(//span[contains(text(), "МТС")])[1]')).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Тарифы")])[1]')).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Безлимитная связь")])[1]')).to_be_visible()
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
    expect(page.locator('(//h2)[1]')).to_be_visible()


def test_operator_mts_ratesmobile_planshet(page: Page):
    page.goto('https://www.moskvaonline.ru/balashiha/operatory/mts/ratesmobile/dlja-plansheta')
    check_header_operator_page(page)
    footer_mol(page)
    check_header_balashixa(page)
    expect(page.get_by_role("link", name="Подключить интернет")).to_be_visible()
    expect(page.get_by_role("link", name="Мобильные операторы")).to_be_visible()
    expect(page.locator('(//span[contains(text(), "МТС")])[1]')).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Тарифы")])[1]')).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Для планшета")])[1]')).to_be_visible()
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


def test_operator_yota_ratesmobile(page: Page):
    page.goto('https://www.moskvaonline.ru/balashiha/operatory/yota/ratesmobile')
    check_header_operator_page(page)
    footer_mol(page)
    check_header_balashixa(page)
    expect(page.get_by_role("link", name="Подключить интернет")).to_be_visible()
    expect(page.get_by_role("link", name="Мобильные операторы")).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Йота")])[1]')).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Тарифы")])[1]')).to_be_visible()
    expect(page.locator('//img[@itemprop="contentUrl"]')).to_be_visible()
    expect(page.locator("#operator_banner").get_by_text("Подключение")).to_be_visible()
    expect(page.locator('(//a[contains(text(), "+7  (800)  550-00-07")])[1]')).to_be_visible()
    expect(page.locator('(//div[contains(text(), "Техподдержка")])[1]')).to_be_visible()
    expect(page.get_by_role("link", name="Об операторе")).to_be_visible()
    expect(page.get_by_role("link", name="Тарифы").nth(1)).to_be_visible()
    expect(page.get_by_role("link", name="акции", exact=True)).to_be_visible()
    expect(page.get_by_role("link", name="в 1")).to_be_visible()
    tags_for_operatory(page)
    tags_yota(page)
    for i in range(1, 4):
        expect(page.locator(f'(//div[contains(text(), "Выбрать")])[{i}]')).to_be_visible()
    expect(page.locator('(//h2)[1]')).to_be_visible()


def test_operator_yota_ratesmobile_esim_planshet(page: Page):
    urls = [
        'https://www.moskvaonline.ru/balashiha/operatory/yota/ratesmobile/esim',
        'https://www.moskvaonline.ru/balashiha/operatory/yota/ratesmobile/dlja-plansheta'
    ]
    for url in urls:
        page.goto(url)
        check_header_operator_page(page)
        footer_mol(page)
        check_header_balashixa(page)
        expect(page.get_by_role("link", name="Подключить интернет")).to_be_visible()
        expect(page.get_by_role("link", name="Мобильные операторы")).to_be_visible()
        expect(page.locator('(//span[contains(text(), "Йота")])[1]')).to_be_visible()
        expect(page.locator('(//span[contains(text(), "Тарифы")])[1]')).to_be_visible()
        expect(page.locator('//img[@itemprop="contentUrl"]')).to_be_visible()
        expect(page.locator("#operator_banner").get_by_text("Подключение")).to_be_visible()
        expect(page.locator('(//a[contains(text(), "+7  (800)  550-00-07")])[1]')).to_be_visible()
        expect(page.locator('(//div[contains(text(), "Техподдержка")])[1]')).to_be_visible()
        expect(page.get_by_role("link", name="Об операторе")).to_be_visible()
        expect(page.get_by_role("link", name="Тарифы").nth(1)).to_be_visible()
        expect(page.get_by_role("link", name="акции", exact=True)).to_be_visible()
        expect(page.get_by_role("link", name="в 1")).to_be_visible()
        tags_for_operatory(page)
        tags_yota(page)
        for i in range(1, 3):
            expect(page.locator(f'(//div[contains(text(), "Выбрать")])[{i}]')).to_be_visible()
        expect(page.locator('(//h2)[1]')).to_be_visible()


def test_operator_yota_ratesmobile_noutbuka_bezlimitimnt_vygodnye_dlyamodema(page: Page):
    urls = [
        'https://www.moskvaonline.ru/balashiha/operatory/yota/ratesmobile/dlja-noutbuka',
        'https://www.moskvaonline.ru/balashiha/operatory/yota/ratesmobile/bezlimitnyj-internet',
        'https://www.moskvaonline.ru/balashiha/operatory/yota/ratesmobile/vygodnye',
        'https://www.moskvaonline.ru/balashiha/operatory/yota/ratesmobile/dlja-modema'
    ]
    for url in urls:
        page.goto(url)
        check_header_operator_page(page)
        footer_mol(page)
        check_header_balashixa(page)
        expect(page.get_by_role("link", name="Подключить интернет")).to_be_visible()
        expect(page.get_by_role("link", name="Мобильные операторы")).to_be_visible()
        expect(page.locator('(//span[contains(text(), "Йота")])[1]')).to_be_visible()
        expect(page.locator('(//span[contains(text(), "Тарифы")])[1]')).to_be_visible()
        expect(page.locator('//img[@itemprop="contentUrl"]')).to_be_visible()
        expect(page.locator("#operator_banner").get_by_text("Подключение")).to_be_visible()
        expect(page.locator('(//a[contains(text(), "+7  (800)  550-00-07")])[1]')).to_be_visible()
        expect(page.locator('(//div[contains(text(), "Техподдержка")])[1]')).to_be_visible()
        expect(page.get_by_role("link", name="Об операторе")).to_be_visible()
        expect(page.get_by_role("link", name="Тарифы").nth(1)).to_be_visible()
        expect(page.get_by_role("link", name="акции", exact=True)).to_be_visible()
        expect(page.get_by_role("link", name="в 1")).to_be_visible()
        tags_for_operatory(page)
        tags_yota(page)
        expect(page.locator('(//div[contains(text(), "Выбрать")])[1]')).to_be_visible()
        expect(page.locator('(//h2)[1]')).to_be_visible()


def test_operator_yota_ratesmobile_perenos_porf(page: Page):
    urls = [
        'https://www.moskvaonline.ru/balashiha/operatory/yota/ratesmobile/perenos_nomera',
        'https://www.moskvaonline.ru/balashiha/operatory/yota/ratesmobile/po-rossii'
    ]
    for url in urls:
        page.goto(url)
    check_header_operator_page(page)
    footer_mol(page)
    check_header_balashixa(page)
    expect(page.get_by_role("link", name="Подключить интернет")).to_be_visible()
    expect(page.get_by_role("link", name="Мобильные операторы")).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Йота")])[1]')).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Тарифы")])[1]')).to_be_visible()
    expect(page.locator('//img[@itemprop="contentUrl"]')).to_be_visible()
    expect(page.locator("#operator_banner").get_by_text("Подключение")).to_be_visible()
    expect(page.locator('(//a[contains(text(), "+7  (800)  550-00-07")])[1]')).to_be_visible()
    expect(page.locator('(//div[contains(text(), "Техподдержка")])[1]')).to_be_visible()
    expect(page.get_by_role("link", name="Об операторе")).to_be_visible()
    expect(page.get_by_role("link", name="Тарифы").nth(1)).to_be_visible()
    expect(page.get_by_role("link", name="акции", exact=True)).to_be_visible()
    expect(page.get_by_role("link", name="в 1")).to_be_visible()
    tags_for_operatory(page)
    tags_yota(page)
    for i in range(1, 2):
        expect(page.locator(f'(//div[contains(text(), "Выбрать")])[{i}]')).to_be_visible()


def test_operator_sbermobile_actions(page: Page):
    page.goto('https://www.moskvaonline.ru/balashiha/operatory/sbermobile/actions')
    check_header_operator_page(page)
    footer_mol(page)
    check_header_balashixa(page)
    expect(page.get_by_role("link", name="Подключить интернет")).to_be_visible()
    expect(page.get_by_role("link", name="Мобильные операторы")).to_be_visible()
    expect(page.locator('(//span[contains(text(), "СберМобайл")])[1]')).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Акции")])[1]')).to_be_visible()
    expect(page.locator('//img[@itemprop="contentUrl"]')).to_be_visible()
    expect(page.locator("#operator_banner").get_by_text("Подключение")).to_be_visible()
    expect(page.locator('(//a[contains(text(), "+7 (499) 651-44-44")])[1]')).to_be_visible()
    expect(page.locator('(//div[contains(text(), "Техподдержка")])[1]')).to_be_visible()
    expect(page.get_by_role("link", name="Об операторе")).to_be_visible()
    expect(page.get_by_role("link", name="Тарифы").nth(1)).to_be_visible()
    expect(page.get_by_role("link", name="акции", exact=True)).to_be_visible()
    expect(page.get_by_role("link", name="Номера")).to_be_visible()
    tags_for_operatory(page)
    expect(page.get_by_role("link", name="Все", exact=True)).to_be_visible()
    expect(page.get_by_role("link", name="eSIM")).to_be_visible()
    expect(page.get_by_role("link", name="Выгодные")).to_be_visible()
    expect(page.get_by_role("link", name="Связь по России")).to_be_visible()
    expect(page.get_by_role("link", name="Перейти со своим номером")).to_be_visible()
    for i in range(1, 3):
        expect(page.locator(f'(//div[contains(text(), "Выбрать")])[{i}]')).to_be_visible()
    expect(page.locator('(//h2)[1]')).to_be_visible()


def test_bal_ratesmobile_bezplaty(page: Page):
    page.goto('https://www.moskvaonline.ru/balashiha/ratesmobile/bez-abonentskoj-platy')
    check_header_operator_page(page)
    footer_mol(page)
    check_header_balashixa(page)
    page_nomera(page)
    expect(page.locator('//span[contains(text(), "Без абонентской платы")]')).to_be_visible()
    tags_mobile(page)
    tags_for_operatory(page)
    tags_mobile(page)
    expect(page.locator('(//div[contains(text(), "Выбрать")])[1]')).to_be_visible()


def test_bal_ratesmobile_bezlimit(page: Page):
    urls = [
        'https://www.moskvaonline.ru/balashiha/ratesmobile/bezlimitnaja-svjaz',
        'https://www.moskvaonline.ru/balashiha/ratesmobile/bezlimitnyj-internet',
        'https://www.moskvaonline.ru/balashiha/ratesmobile/po-rossii',
        'https://www.moskvaonline.ru/balashiha/ratesmobile/dlja-modema',
        'https://www.moskvaonline.ru/balashiha/ratesmobile/dlja-plansheta',
        'https://www.moskvaonline.ru/balashiha/ratesmobile/esim',
        'https://www.moskvaonline.ru/balashiha/ratesmobile/unikalnye'
    ]
    for url in urls:
        page.goto(url)
    check_header_operator_page(page)
    footer_mol(page)
    check_header_balashixa(page)
    page_nomera(page)
    tags_mobile(page)
    tags_for_operatory(page)
    tags_mobile(page)
    for i in range(1, 15):
        expect(page.locator(f'(//div[contains(text(), "Выбрать")])[{i}]')).to_be_visible()
    expect(page.get_by_text("ПОКАЗАТЬ ЕЩЁ")).to_be_visible()
    expect(page.locator('(//h2)[1]')).to_be_visible()


def test_operator_mezhdunarodnye(page: Page):
    page.goto('https://www.moskvaonline.ru/balashiha/ratesmobile/mezhdunarodnye')
    check_header_operator_page(page)
    footer_mol(page)
    check_header_balashixa(page)
    page_nomera(page)
    expect(page.locator('//span[contains(text(), "Роуминг за границей")]')).to_be_visible()
    tags_mobile(page)
    tags_for_operatory(page)
    tags_mobile(page)
    for i in range(1, 6):
        expect(page.locator(f'(//div[contains(text(), "Выбрать")])[{i}]')).to_be_visible()
    expect(page.locator('(//h2)[1]')).to_be_visible()


def test_operator_noutbuk(page: Page):
    page.goto('https://www.moskvaonline.ru/balashiha/ratesmobile/dlja-noutbuka')
    check_header_operator_page(page)
    footer_mol(page)
    check_header_balashixa(page)
    page_nomera(page)
    expect(page.locator('//span[contains(text(), "Для ноутбука")]')).to_be_visible()
    tags_mobile(page)
    tags_for_operatory(page)
    tags_mobile(page)
    for i in range(1, 2):
        expect(page.locator(f'(//div[contains(text(), "Выбрать")])[{i}]')).to_be_visible()
    expect(page.locator('(//h2)[1]')).to_be_visible()


def test_operator_vygodnye(page: Page):
    urls = [
        'https://www.moskvaonline.ru/balashiha/ratesmobile/vygodnye',
        'https://www.moskvaonline.ru/balashiha/ratesmobile/semeinye'
    ]
    for url in urls:
        page.goto(url)
    check_header_operator_page(page)
    footer_mol(page)
    check_header_balashixa(page)
    page_nomera(page)
    tags_mobile(page)
    tags_for_operatory(page)
    tags_mobile(page)
    for i in range(1, 13):
        expect(page.locator(f'(//div[contains(text(), "Выбрать")])[{i}]')).to_be_visible()
    expect(page.get_by_text("ПОКАЗАТЬ ЕЩЁ")).to_be_visible()


def test_operator_tele2_bezlimitnaja(page: Page):
    page.goto('https://www.moskvaonline.ru/balashiha/operatory/tele-2/ratesmobile/bezlimitnaja-svjaz')
    check_header_operator_page(page)
    footer_mol(page)
    check_header_balashixa(page)
    expect(page.get_by_role("link", name="Подключить интернет")).to_be_visible()
    expect(page.locator('//span[contains(text(), "Мобильные операторы")]')).to_be_visible()
    expect(page.locator('//span[contains(text(), "Теле 2")]')).to_be_visible()
    expect(page.locator('//span[contains(text(), "Тарифы")]')).to_be_visible()
    expect(page.locator('//span[contains(text(), "Безлимитная связь")]')).to_be_visible()
    expect(page.locator('//img[@itemprop="contentUrl"]')).to_be_visible()
    expect(page.locator("#operator_banner").get_by_text("Подключение")).to_be_visible()
    expect(page.locator('(//a[contains(text(), "+7  (812)  989-00-22")])[1]')).to_be_visible()
    expect(page.locator('(//div[contains(text(), "Техподдержка")])[1]')).to_be_visible()
    expect(page.locator('(//a[contains(text(), "+7 (495) 979-76-11")])[1]')).to_be_visible()
    expect(page.get_by_role("link", name="Об операторе")).to_be_visible()
    expect(page.get_by_role("link", name="Тарифы").nth(1)).to_be_visible()
    expect(page.get_by_role("link", name="акции", exact=True)).to_be_visible()
    expect(page.get_by_role("link", name="Номера")).to_be_visible()
    tags_for_operatory(page)
    expect(page.get_by_role("link", name="Все", exact=True)).to_be_visible()
    expect(page.get_by_role("link", name="eSIM")).to_be_visible()
    expect(page.get_by_role("link", name="Выгодные")).to_be_visible()
    expect(page.get_by_role("link", name="Связь по России")).to_be_visible()
    expect(page.get_by_role("link", name="Перейти со своим номером")).to_be_visible()
    for i in range(1, 7):
        expect(page.locator(f'(//div[contains(text(), "Выбрать")])[{i}]')).to_be_visible()
    expect(page.locator('(//h2)[1]')).to_be_visible()


def test_operator_tele2_pf(page: Page):
    page.goto('https://www.moskvaonline.ru/balashiha/operatory/tele-2/ratesmobile/po-rossii')
    check_header_operator_page(page)
    footer_mol(page)
    check_header_balashixa(page)
    expect(page.get_by_role("link", name="Подключить интернет")).to_be_visible()
    expect(page.locator('//span[contains(text(), "Мобильные операторы")]')).to_be_visible()
    expect(page.locator('//span[contains(text(), "Теле 2")]')).to_be_visible()
    expect(page.locator('//span[contains(text(), "Тарифы")]')).to_be_visible()
    expect(page.locator('//span[contains(text(), "Связь по России")]')).to_be_visible()
    expect(page.locator('//img[@itemprop="contentUrl"]')).to_be_visible()
    expect(page.locator("#operator_banner").get_by_text("Подключение")).to_be_visible()
    expect(page.locator('(//a[contains(text(), "+7  (812)  989-00-22")])[1]')).to_be_visible()
    expect(page.locator('(//div[contains(text(), "Техподдержка")])[1]')).to_be_visible()
    expect(page.locator('(//a[contains(text(), "+7 (495) 979-76-11")])[1]')).to_be_visible()
    expect(page.get_by_role("link", name="Об операторе")).to_be_visible()
    expect(page.get_by_role("link", name="Тарифы").nth(1)).to_be_visible()
    expect(page.get_by_role("link", name="акции", exact=True)).to_be_visible()
    expect(page.get_by_role("link", name="Номера")).to_be_visible()
    tags_for_operatory(page)
    expect(page.get_by_role("link", name="Все", exact=True)).to_be_visible()
    expect(page.get_by_role("link", name="eSIM")).to_be_visible()
    expect(page.get_by_role("link", name="Выгодные")).to_be_visible()
    expect(page.get_by_role("link", name="Связь по России")).to_be_visible()
    expect(page.get_by_role("link", name="Перейти со своим номером")).to_be_visible()
    for i in range(1, 7):
        expect(page.locator(f'(//div[contains(text(), "Выбрать")])[{i}]')).to_be_visible()


def test_operator_tele2_perenos_nomera(page: Page):
    page.goto('https://www.moskvaonline.ru/balashiha/operatory/tele-2/ratesmobile/perenos_nomera')
    check_header_operator_page(page)
    footer_mol(page)
    check_header_balashixa(page)
    expect(page.get_by_role("link", name="Подключить интернет")).to_be_visible()
    expect(page.locator('//span[contains(text(), "Мобильные операторы")]')).to_be_visible()
    expect(page.locator('//span[contains(text(), "Теле 2")]')).to_be_visible()
    expect(page.locator('//span[contains(text(), "Тарифы")]')).to_be_visible()
    expect(page.locator('//span[contains(text(), "Перейти со своим номером")]')).to_be_visible()
    expect(page.locator('//img[@itemprop="contentUrl"]')).to_be_visible()
    expect(page.locator("#operator_banner").get_by_text("Подключение")).to_be_visible()
    expect(page.locator('(//a[contains(text(), "+7  (812)  989-00-22")])[1]')).to_be_visible()
    expect(page.locator('(//div[contains(text(), "Техподдержка")])[1]')).to_be_visible()
    expect(page.locator('(//a[contains(text(), "+7 (495) 979-76-11")])[1]')).to_be_visible()
    expect(page.get_by_role("link", name="Об операторе")).to_be_visible()
    expect(page.get_by_role("link", name="Тарифы").nth(1)).to_be_visible()
    expect(page.get_by_role("link", name="акции", exact=True)).to_be_visible()
    expect(page.get_by_role("link", name="Номера")).to_be_visible()
    tags_for_operatory(page)
    expect(page.get_by_role("link", name="Все", exact=True)).to_be_visible()
    expect(page.get_by_role("link", name="eSIM")).to_be_visible()
    expect(page.get_by_role("link", name="Выгодные")).to_be_visible()
    expect(page.get_by_role("link", name="Связь по России")).to_be_visible()
    expect(page.get_by_role("link", name="Перейти со своим номером")).to_be_visible()
    for i in range(1, 7):
        expect(page.locator(f'(//div[contains(text(), "Выбрать")])[{i}]')).to_be_visible()
    expect(page.locator('(//h2)[1]')).to_be_visible()


def test_operator_tele2_bezlimitnyj(page: Page):
    page.goto('https://www.moskvaonline.ru/balashiha/operatory/tele-2/ratesmobile/bezlimitnyj-internet')
    check_header_operator_page(page)
    footer_mol(page)
    check_header_balashixa(page)
    expect(page.get_by_role("link", name="Подключить интернет")).to_be_visible()
    expect(page.locator('//span[contains(text(), "Мобильные операторы")]')).to_be_visible()
    expect(page.locator('//span[contains(text(), "Теле 2")]')).to_be_visible()
    expect(page.locator('//span[contains(text(), "Тарифы")]')).to_be_visible()
    expect(page.locator('//span[contains(text(), "Безлимитный интернет")]')).to_be_visible()
    expect(page.locator('//img[@itemprop="contentUrl"]')).to_be_visible()
    expect(page.locator("#operator_banner").get_by_text("Подключение")).to_be_visible()
    expect(page.locator('(//a[contains(text(), "+7  (812)  989-00-22")])[1]')).to_be_visible()
    expect(page.locator('(//div[contains(text(), "Техподдержка")])[1]')).to_be_visible()
    expect(page.locator('(//a[contains(text(), "+7 (495) 979-76-11")])[1]')).to_be_visible()
    expect(page.get_by_role("link", name="Об операторе")).to_be_visible()
    expect(page.get_by_role("link", name="Тарифы").nth(1)).to_be_visible()
    expect(page.get_by_role("link", name="акции", exact=True)).to_be_visible()
    expect(page.get_by_role("link", name="Номера")).to_be_visible()
    tags_for_operatory(page)
    expect(page.get_by_role("link", name="Все", exact=True)).to_be_visible()
    expect(page.get_by_role("link", name="eSIM")).to_be_visible()
    expect(page.get_by_role("link", name="Выгодные")).to_be_visible()
    expect(page.get_by_role("link", name="Связь по России")).to_be_visible()
    expect(page.get_by_role("link", name="Перейти со своим номером")).to_be_visible()
    for i in range(1, 7):
        expect(page.locator(f'(//div[contains(text(), "Выбрать")])[{i}]')).to_be_visible()
    expect(page.locator('(//h2)[1]')).to_be_visible()

def test_operator_tele2_detskie(page: Page):
    page.goto('https://www.moskvaonline.ru/balashiha/operatory/tele-2/ratesmobile/detskie')
    check_header_operator_page(page)
    footer_mol(page)
    check_header_balashixa(page)
    expect(page.get_by_role("link", name="Подключить интернет")).to_be_visible()
    expect(page.locator('//span[contains(text(), "Мобильные операторы")]')).to_be_visible()
    expect(page.locator('//span[contains(text(), "Теле 2")]')).to_be_visible()
    expect(page.locator('//span[contains(text(), "Тарифы")]')).to_be_visible()
    expect(page.locator('//span[contains(text(), "Детские")]')).to_be_visible()
    expect(page.locator('//img[@itemprop="contentUrl"]')).to_be_visible()
    expect(page.locator("#operator_banner").get_by_text("Подключение")).to_be_visible()
    expect(page.locator('(//a[contains(text(), "+7  (812)  989-00-22")])[1]')).to_be_visible()
    expect(page.locator('(//div[contains(text(), "Техподдержка")])[1]')).to_be_visible()
    expect(page.locator('(//a[contains(text(), "+7 (495) 979-76-11")])[1]')).to_be_visible()
    expect(page.get_by_role("link", name="Об операторе")).to_be_visible()
    expect(page.get_by_role("link", name="Тарифы").nth(1)).to_be_visible()
    expect(page.get_by_role("link", name="акции", exact=True)).to_be_visible()
    expect(page.get_by_role("link", name="Номера")).to_be_visible()
    tags_for_operatory(page)
    expect(page.get_by_role("link", name="Все", exact=True)).to_be_visible()
    expect(page.get_by_role("link", name="eSIM")).to_be_visible()
    expect(page.get_by_role("link", name="Выгодные")).to_be_visible()
    expect(page.get_by_role("link", name="Связь по России")).to_be_visible()
    expect(page.get_by_role("link", name="Перейти со своим номером")).to_be_visible()
    for i in range(1, 6):
        expect(page.locator(f'(//div[contains(text(), "Выбрать")])[{i}]')).to_be_visible()


def test_operator_tele2_planshet(page: Page):
    page.goto('https://www.moskvaonline.ru/balashiha/operatory/tele-2/ratesmobile/dlja-plansheta')
    check_header_operator_page(page)
    footer_mol(page)
    check_header_balashixa(page)
    expect(page.get_by_role("link", name="Подключить интернет")).to_be_visible()
    expect(page.locator('//span[contains(text(), "Мобильные операторы")]')).to_be_visible()
    expect(page.locator('//span[contains(text(), "Теле 2")]')).to_be_visible()
    expect(page.locator('//span[contains(text(), "Тарифы")]')).to_be_visible()
    expect(page.locator('//span[contains(text(), "Для планшета")]')).to_be_visible()
    expect(page.locator('//img[@itemprop="contentUrl"]')).to_be_visible()
    expect(page.locator("#operator_banner").get_by_text("Подключение")).to_be_visible()
    expect(page.locator('(//a[contains(text(), "+7  (812)  989-00-22")])[1]')).to_be_visible()
    expect(page.locator('(//div[contains(text(), "Техподдержка")])[1]')).to_be_visible()
    expect(page.locator('(//a[contains(text(), "+7 (495) 979-76-11")])[1]')).to_be_visible()
    expect(page.get_by_role("link", name="Об операторе")).to_be_visible()
    expect(page.get_by_role("link", name="Тарифы").nth(1)).to_be_visible()
    expect(page.get_by_role("link", name="акции", exact=True)).to_be_visible()
    expect(page.get_by_role("link", name="Номера")).to_be_visible()
    tags_for_operatory(page)
    expect(page.get_by_role("link", name="Все", exact=True)).to_be_visible()
    expect(page.get_by_role("link", name="eSIM")).to_be_visible()
    expect(page.get_by_role("link", name="Выгодные")).to_be_visible()
    expect(page.get_by_role("link", name="Связь по России")).to_be_visible()
    expect(page.get_by_role("link", name="Перейти со своим номером")).to_be_visible()
    expect(page.locator('(//div[contains(text(), "Выбрать")])[1]')).to_be_visible()


def test_operator_tele2_esim(page: Page):
    page.goto('https://www.moskvaonline.ru/balashiha/operatory/tele-2/ratesmobile/esim')
    check_header_operator_page(page)
    footer_mol(page)
    check_header_balashixa(page)
    expect(page.get_by_role("link", name="Подключить интернет")).to_be_visible()
    expect(page.locator('//span[contains(text(), "Мобильные операторы")]')).to_be_visible()
    expect(page.locator('//span[contains(text(), "Теле 2")]')).to_be_visible()
    expect(page.locator('//span[contains(text(), "Тарифы")]')).to_be_visible()
    expect(page.locator('//span[contains(text(), "eSIM")]')).to_be_visible()
    expect(page.locator('//img[@itemprop="contentUrl"]')).to_be_visible()
    expect(page.locator("#operator_banner").get_by_text("Подключение")).to_be_visible()
    expect(page.locator('(//a[contains(text(), "+7  (812)  989-00-22")])[1]')).to_be_visible()
    expect(page.locator('(//div[contains(text(), "Техподдержка")])[1]')).to_be_visible()
    expect(page.locator('(//a[contains(text(), "+7 (495) 979-76-11")])[1]')).to_be_visible()
    expect(page.get_by_role("link", name="Об операторе")).to_be_visible()
    expect(page.get_by_role("link", name="Тарифы").nth(1)).to_be_visible()
    expect(page.get_by_role("link", name="акции", exact=True)).to_be_visible()
    expect(page.get_by_role("link", name="Номера")).to_be_visible()
    tags_for_operatory(page)
    expect(page.get_by_role("link", name="Все", exact=True)).to_be_visible()
    expect(page.get_by_role("link", name="eSIM")).to_be_visible()
    expect(page.get_by_role("link", name="Выгодные")).to_be_visible()
    expect(page.get_by_role("link", name="Связь по России")).to_be_visible()
    expect(page.get_by_role("link", name="Перейти со своим номером")).to_be_visible()
    for i in range(1, 9):
        expect(page.locator(f'(//div[contains(text(), "Выбрать")])[{i}]')).to_be_visible()


def test_operator_tele2_vygodnye(page: Page):
    page.goto('https://www.moskvaonline.ru/balashiha/operatory/tele-2/ratesmobile/vygodnye')
    check_header_operator_page(page)
    footer_mol(page)
    check_header_balashixa(page)
    expect(page.get_by_role("link", name="Подключить интернет")).to_be_visible()
    expect(page.locator('//span[contains(text(), "Мобильные операторы")]')).to_be_visible()
    expect(page.locator('//span[contains(text(), "Теле 2")]')).to_be_visible()
    expect(page.locator('//span[contains(text(), "Тарифы")]')).to_be_visible()
    expect(page.locator('//span[contains(text(), "Выгодные")]')).to_be_visible()
    expect(page.locator('//img[@itemprop="contentUrl"]')).to_be_visible()
    expect(page.locator("#operator_banner").get_by_text("Подключение")).to_be_visible()
    expect(page.locator('(//a[contains(text(), "+7  (812)  989-00-22")])[1]')).to_be_visible()
    expect(page.locator('(//div[contains(text(), "Техподдержка")])[1]')).to_be_visible()
    expect(page.locator('(//a[contains(text(), "+7 (495) 979-76-11")])[1]')).to_be_visible()
    expect(page.get_by_role("link", name="Об операторе")).to_be_visible()
    expect(page.get_by_role("link", name="Тарифы").nth(1)).to_be_visible()
    expect(page.get_by_role("link", name="акции", exact=True)).to_be_visible()
    expect(page.get_by_role("link", name="Номера")).to_be_visible()
    tags_for_operatory(page)
    expect(page.get_by_role("link", name="Все", exact=True)).to_be_visible()
    expect(page.get_by_role("link", name="eSIM")).to_be_visible()
    expect(page.get_by_role("link", name="Выгодные")).to_be_visible()
    expect(page.get_by_role("link", name="Связь по России")).to_be_visible()
    expect(page.get_by_role("link", name="Перейти со своим номером")).to_be_visible()
    for i in range(1, 8):
        expect(page.locator(f'(//div[contains(text(), "Выбрать")])[{i}]')).to_be_visible()
    expect(page.locator('(//h2)[1]')).to_be_visible()


def test_operator_tele2_mezhdunarodnye(page: Page):
    page.goto('https://www.moskvaonline.ru/balashiha/operatory/tele-2/ratesmobile/mezhdunarodnye')
    check_header_operator_page(page)
    footer_mol(page)
    check_header_balashixa(page)
    expect(page.get_by_role("link", name="Подключить интернет")).to_be_visible()
    expect(page.locator('//span[contains(text(), "Мобильные операторы")]')).to_be_visible()
    expect(page.locator('//span[contains(text(), "Теле 2")]')).to_be_visible()
    expect(page.locator('//span[contains(text(), "Тарифы")]')).to_be_visible()
    expect(page.locator('//span[contains(text(), "Роуминг за границей")]')).to_be_visible()
    expect(page.locator('//img[@itemprop="contentUrl"]')).to_be_visible()
    expect(page.locator("#operator_banner").get_by_text("Подключение")).to_be_visible()
    expect(page.locator('(//a[contains(text(), "+7  (812)  989-00-22")])[1]')).to_be_visible()
    expect(page.locator('(//div[contains(text(), "Техподдержка")])[1]')).to_be_visible()
    expect(page.locator('(//a[contains(text(), "+7 (495) 979-76-11")])[1]')).to_be_visible()
    expect(page.get_by_role("link", name="Об операторе")).to_be_visible()
    expect(page.get_by_role("link", name="Тарифы").nth(1)).to_be_visible()
    expect(page.get_by_role("link", name="акции", exact=True)).to_be_visible()
    expect(page.get_by_role("link", name="Номера")).to_be_visible()
    tags_for_operatory(page)
    expect(page.get_by_role("link", name="Все", exact=True)).to_be_visible()
    expect(page.get_by_role("link", name="eSIM")).to_be_visible()
    expect(page.get_by_role("link", name="Выгодные")).to_be_visible()
    expect(page.get_by_role("link", name="Связь по России")).to_be_visible()
    expect(page.get_by_role("link", name="Перейти со своим номером")).to_be_visible()
    for i in range(1, 3):
        expect(page.locator(f'(//div[contains(text(), "Выбрать")])[{i}]')).to_be_visible()
    expect(page.locator('(//h2)[1]')).to_be_visible()


def test_operator_tele2_modem(page: Page):
    page.goto('https://www.moskvaonline.ru/balashiha/operatory/tele-2/ratesmobile/dlja-modema')
    check_header_operator_page(page)
    footer_mol(page)
    check_header_balashixa(page)
    expect(page.get_by_role("link", name="Подключить интернет")).to_be_visible()
    expect(page.locator('//span[contains(text(), "Мобильные операторы")]')).to_be_visible()
    expect(page.locator('//span[contains(text(), "Теле 2")]')).to_be_visible()
    expect(page.locator('//span[contains(text(), "Тарифы")]')).to_be_visible()
    expect(page.locator('//span[contains(text(), "Для модема/роутера")]')).to_be_visible()
    expect(page.locator('//img[@itemprop="contentUrl"]')).to_be_visible()
    expect(page.locator("#operator_banner").get_by_text("Подключение")).to_be_visible()
    expect(page.locator('(//a[contains(text(), "+7  (812)  989-00-22")])[1]')).to_be_visible()
    expect(page.locator('(//div[contains(text(), "Техподдержка")])[1]')).to_be_visible()
    expect(page.locator('(//a[contains(text(), "+7 (495) 979-76-11")])[1]')).to_be_visible()
    expect(page.get_by_role("link", name="Об операторе")).to_be_visible()
    expect(page.get_by_role("link", name="Тарифы").nth(1)).to_be_visible()
    expect(page.get_by_role("link", name="акции", exact=True)).to_be_visible()
    expect(page.get_by_role("link", name="Номера")).to_be_visible()
    tags_for_operatory(page)
    expect(page.get_by_role("link", name="Все", exact=True)).to_be_visible()
    expect(page.get_by_role("link", name="eSIM")).to_be_visible()
    expect(page.get_by_role("link", name="Выгодные")).to_be_visible()
    expect(page.get_by_role("link", name="Связь по России")).to_be_visible()
    expect(page.get_by_role("link", name="Перейти со своим номером")).to_be_visible()
    for i in range(1, 3):
        expect(page.locator(f'(//div[contains(text(), "Выбрать")])[{i}]')).to_be_visible()
    expect(page.locator('(//h2)[1]')).to_be_visible()


def test_operator_tele2_semeinye(page: Page):
    page.goto('https://www.moskvaonline.ru/balashiha/operatory/tele-2/ratesmobile/semeinye')
    check_header_operator_page(page)
    footer_mol(page)
    check_header_balashixa(page)
    expect(page.get_by_role("link", name="Подключить интернет")).to_be_visible()
    expect(page.locator('//span[contains(text(), "Мобильные операторы")]')).to_be_visible()
    expect(page.locator('//span[contains(text(), "Теле 2")]')).to_be_visible()
    expect(page.locator('//span[contains(text(), "Тарифы")]')).to_be_visible()
    expect(page.locator('//span[contains(text(), "Семейные")]')).to_be_visible()
    expect(page.locator('//img[@itemprop="contentUrl"]')).to_be_visible()
    expect(page.locator("#operator_banner").get_by_text("Подключение")).to_be_visible()
    expect(page.locator('(//a[contains(text(), "+7  (812)  989-00-22")])[1]')).to_be_visible()
    expect(page.locator('(//div[contains(text(), "Техподдержка")])[1]')).to_be_visible()
    expect(page.locator('(//a[contains(text(), "+7 (495) 979-76-11")])[1]')).to_be_visible()
    expect(page.get_by_role("link", name="Об операторе")).to_be_visible()
    expect(page.get_by_role("link", name="Тарифы").nth(1)).to_be_visible()
    expect(page.get_by_role("link", name="акции", exact=True)).to_be_visible()
    expect(page.get_by_role("link", name="Номера")).to_be_visible()
    tags_for_operatory(page)
    expect(page.get_by_role("link", name="Все", exact=True)).to_be_visible()
    expect(page.get_by_role("link", name="eSIM")).to_be_visible()
    expect(page.get_by_role("link", name="Выгодные")).to_be_visible()
    expect(page.get_by_role("link", name="Связь по России")).to_be_visible()
    expect(page.get_by_role("link", name="Перейти со своим номером")).to_be_visible()
    for i in range(1, 6):
        expect(page.locator(f'(//div[contains(text(), "Выбрать")])[{i}]')).to_be_visible()


def test_operator_tele2_unikalnye(page: Page):
    page.goto('https://www.moskvaonline.ru/balashiha/operatory/tele-2/ratesmobile/unikalnye')
    check_header_operator_page(page)
    footer_mol(page)
    check_header_balashixa(page)
    expect(page.get_by_role("link", name="Подключить интернет")).to_be_visible()
    expect(page.locator('//span[contains(text(), "Мобильные операторы")]')).to_be_visible()
    expect(page.locator('//span[contains(text(), "Теле 2")]')).to_be_visible()
    expect(page.locator('//span[contains(text(), "Тарифы")]')).to_be_visible()
    expect(page.locator('//span[contains(text(), "Непубличные")]')).to_be_visible()
    expect(page.locator('//img[@itemprop="contentUrl"]')).to_be_visible()
    expect(page.locator("#operator_banner").get_by_text("Подключение")).to_be_visible()
    expect(page.locator('(//a[contains(text(), "+7  (812)  989-00-22")])[1]')).to_be_visible()
    expect(page.locator('(//div[contains(text(), "Техподдержка")])[1]')).to_be_visible()
    expect(page.locator('(//a[contains(text(), "+7 (495) 979-76-11")])[1]')).to_be_visible()
    expect(page.get_by_role("link", name="Об операторе")).to_be_visible()
    expect(page.get_by_role("link", name="Тарифы").nth(1)).to_be_visible()
    expect(page.get_by_role("link", name="акции", exact=True)).to_be_visible()
    expect(page.get_by_role("link", name="Номера")).to_be_visible()
    tags_for_operatory(page)
    expect(page.get_by_role("link", name="Все", exact=True)).to_be_visible()
    expect(page.get_by_role("link", name="eSIM")).to_be_visible()
    expect(page.get_by_role("link", name="Выгодные")).to_be_visible()
    expect(page.get_by_role("link", name="Связь по России")).to_be_visible()
    expect(page.get_by_role("link", name="Перейти со своим номером")).to_be_visible()
    for i in range(1, 4):
        expect(page.locator(f'(//div[contains(text(), "Выбрать")])[{i}]')).to_be_visible()
