from playwright.sync_api import Page, expect
from pages.main_page import check_header, search_tariffs, one_click_form, tariffs_block, blue_form
from pages.main_page import footer_mol, blue_form_second, search_tariffs_second, sorting
from pages.MOL.moscow_page import review, check_tags, header_mol


def test_first(page: Page):
    page.goto('https://www.moskvaonline.ru/')
    check_header(page)
    footer_mol(page)
    review(page)
    one_click_form(page)
    blue_form(page)
    search_tariffs(page)
    header_mol(page)
    expect(page.locator('//h1[contains(text(), "Подключить домашний интернет в Москве")]')).to_contain_text('Подключить домашний интернет в Москве')
    expect(page.locator('(//div[contains(text(), "Введите ваш адрес и сравните тарифы провайдеров Москвы. Гарантия до 90 дней и кэшбэк до 1000 рублей!")])[1]')).to_be_visible()
    expect(page.locator('//div[@datatest="main_raitingprovider_button"]')).to_have_text('Рейтинг провайдеров')
    expect(page.locator('//div[@datatest="main_comparetariff_button"]')).to_have_text('Выгодные пакеты интернета3 в 1')
    expect(page.locator('//div[@class="col-sm-6 col-lg-4"]')).to_contain_text('получили нашу помощь в выборе интернета за  15 лет')
    expect(page.locator('//div[@class="onlyNotMd onlyNotSm onlyNotXs col-lg-4"]')).to_contain_text('Бесплатная консультация')
    expect(page.locator('//div[@datatest="main_inflat_button"]')).to_contain_text('ИнтернетВ квартиру')
    expect(page.locator('//div[@datatest="main_inhouse_button"]')).to_contain_text('ИнтернетНа дачу')
    expect(page.locator('//div[@datatest="main_inoffice_button"]')).to_contain_text('ИнтернетВ офис')
    expect(page.locator('//h2[contains(text(), "Выгодные тарифы домашнего интернета в Москве")]')).to_have_text('Выгодные тарифы домашнего интернета в Москве')
    expect(page.locator('(//a[@datatest="providers_provider_alltariff_button"])[1]')).to_have_text('Показать все')
    expect(page.locator('(//h2[contains(text(), "Топ провайдеров домашнего интернета в Москве")])[2]')).to_contain_text('Топ провайдеров домашнего интернета в Москве')
    expect(page.locator('(//div[@class="row"])[7]')).to_be_visible()
    expect(page.locator('//div[@class="row"]//div[@class="col-12 col-sm-6 col-md-4 col-lg-3"]').nth(4))
    expect(page.locator('(//h2)[9]')).to_be_visible()


def test_tohome(page: Page):
    page.goto('https://www.moskvaonline.ru/orders/tohome')
    check_header(page)
    footer_mol(page)
    one_click_form(page)
    blue_form(page)
    search_tariffs(page)
    header_mol(page)
    expect(page.locator('(//span[contains(text(), "Подключить интернет")])[1]')).to_be_visible()
    expect(page.locator('//span[contains(text(), "поиск по адресу")]')).to_be_visible()
    expect(page.locator('//h1[contains(text(), "Интернет-провайдеры по адресу в Москве")]')).to_be_visible()
    expect(page.locator('(//h2)[4]')).to_be_visible()
    expect(page.locator('(//h2)[5]')).to_be_visible()
    expect(page.locator('//div[@data-test="countRates"]')).to_be_visible()
    expect(page.locator('(//h2)[6]')).to_be_visible()
    expect(page.locator('//div[@datatest="providers_find_adress"]')).to_be_visible()
    expect(page.locator('(//h2)[1]')).to_be_visible()
    expect(page.locator('(//h2)[2]')).to_be_visible()
    expect(page.locator('(//div[@itemscope])[1]')).to_be_visible()


def test_providers(page: Page):
    page.goto('https://www.moskvaonline.ru/providers')
    check_header(page)
    footer_mol(page)
    blue_form(page)
    blue_form_second(page)
    search_tariffs_second(page)
    header_mol(page)
    expect(page.locator('(//span[contains(text(), "Подключить интернет")])[1]')).to_be_visible()
    expect(page.locator('//span[contains(text(), "Провайдеры Москвы")]')).to_be_visible()
    expect(page.locator('(//h2)[2]')).to_be_visible()
    expect(page.locator('(//h2)[4]')).to_be_visible()
    expect(page.locator('(//h2)[6]')).to_be_visible()
    expect(page.locator('(//a[@datatest="top_provider_block"])[1]')).to_be_visible()
    for i in range(1, 19):
        expect(page.locator(f'(//div[@datatest="providers_provider_button"])[{i}]')).to_be_visible()
    expect(page.locator('(//h2)[6]')).to_be_visible()
    expect(page.locator('(//ol[@align="left"])[1]')).to_be_visible()
    expect(page.locator('(//div[@datatest="providers_find_adress"])[1]')).to_be_visible()
    expect(page.locator('(//div[@datatest="providers_find_adress"])[2]')).to_be_visible()
    for i in range(1, 6):
        expect(page.locator(f'(//a[@aria-label="Переключить страницу"])[{i}]')).to_be_visible()


def test_providers_2(page: Page):
    page.goto('https://www.moskvaonline.ru/providers/2')
    check_header(page)
    footer_mol(page)
    blue_form(page)
    blue_form_second(page)
    search_tariffs_second(page)
    header_mol(page)
    expect(page.locator('(//span[contains(text(), "Подключить интернет")])[1]')).to_be_visible()
    expect(page.locator('//span[contains(text(), "Провайдеры Москвы")]')).to_be_visible()
    expect(page.locator('(//h2)[3]')).to_be_visible()
    expect(page.locator('(//h2)[4]')).to_be_visible()
    expect(page.locator('(//a[@datatest="top_provider_block"])[1]')).to_be_visible()
    for i in range(1, 19):
        expect(page.locator(f'(//div[@datatest="providers_provider_button"])[{i}]')).to_be_visible()
    expect(page.locator('(//div[@datatest="providers_find_adress"])[1]')).to_be_visible()
    expect(page.locator('(//div[@datatest="providers_find_adress"])[2]')).to_be_visible()
    for i in range(1, 6):
        expect(page.locator(f'(//a[@aria-label="Переключить страницу"])[{i}]')).to_be_visible()


def test_rating(page: Page):
    page.goto('https://www.moskvaonline.ru/rating')
    check_header(page)
    footer_mol(page)
    search_tariffs_second(page)
    header_mol(page)
    expect(page.locator('(//span[contains(text(), "Подключить интернет")])[1]')).to_be_visible()
    expect(page.locator('//span[contains(text(), "Рейтинг провайдеров")]')).to_be_visible()
    expect(page.locator('//div[contains(text(), "Период")]')).to_be_visible()
    expect(page.locator('(//div[contains(text(), "Интернет")])[1]')).to_be_visible()
    expect(page.locator('//input[@datatest="raiting_input_filter_period"]')).to_be_visible()
    expect(page.locator('//input[@datatest="raiting_input_filter_internet_type"]')).to_be_visible()
    for i in range(1, 7):
        expect(page.locator(f'(//div[@itemprop="offers"])[{i}]')).to_be_visible()
    expect(page.locator('(//h2)[2]')).to_be_visible()
    for i in range(1, 28):
        expect(page.locator(f'(//*[@id="root"]/div/div[1]/div[4]/div[5]/div[3]/div)[{i}]')).to_be_visible()


def test_rates(page: Page):
    page.goto('https://www.moskvaonline.ru/rates')
    check_header(page)
    footer_mol(page)
    search_tariffs(page)
    header_mol(page)
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
    page.goto('https://www.moskvaonline.ru/select-region')
    expect(page.locator('//span[contains(text(), "Выберите город или регион")]')).to_be_visible()
    expect(page.locator('//input[@placeholder="Введите первые 3 буквы"]')).to_be_visible()
    for i in range(1, 34):
        expect(page.locator(f'(//a[@datatest="main_region_choose"][@href])[{i}]')).to_be_visible()
    for i in range(1, 20):
        expect(page.locator(f'(//*[@id="root"]/div/div[1]/div/div/div/div/div[3]/div)[{i}]')).to_be_visible()
    expect(page.locator('//div[@class="components__slider-button"]')).to_be_visible()
    expect(page.locator('(//span[@class="icon24 icon-close"])[1]')).to_be_visible()


def test_internet_i_mobilnaya_svyaz(page: Page):
    page.goto('https://www.moskvaonline.ru/rates/internet-i-mobilnaya-svyaz')
    check_header(page)
    footer_mol(page)
    search_tariffs(page)
    header_mol(page)
    check_tags(page)
    sorting(page)
    expect(page.locator('//span[contains(text(), "Подключить интернет")]')).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Тарифы на интернет")])[1]')).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Интернет и мобильная связь")])[1]')).to_be_visible()
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
    for i in range(1, 28):
        expect(page.locator(f'(//a[@datatest="top_provider_block"])[{i}]')).to_be_visible()
    for i in range(1, 20):
        expect(page.locator(f'(//h3)[{i}]')).to_be_visible()


def test_internet_tv_mobile(page: Page):
    page.goto('https://www.moskvaonline.ru/rates/internet-tv-mobile')
    check_header(page)
    footer_mol(page)
    search_tariffs(page)
    header_mol(page)
    check_tags(page)
    sorting(page)
    expect(page.locator('//span[contains(text(), "Подключить интернет")]')).to_be_visible()
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
    for i in range(1, 28):
        expect(page.locator(f'(//a[@datatest="top_provider_block"])[{i}]')).to_be_visible()
    for i in range(1, 16):
        expect(page.locator(f'(//h3)[{i}]')).to_be_visible()


def test_nedorogoj_domashnij_internet(page: Page):
    page.goto('https://www.moskvaonline.ru/rates/nedorogoj-domashnij-internet')
    check_header(page)
    footer_mol(page)
    search_tariffs(page)
    header_mol(page)
    check_tags(page)
    sorting(page)
    expect(page.locator('//span[contains(text(), "Подключить интернет")]')).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Тарифы на интернет")])[1]')).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Дешевый интернет")])[1]')).to_be_visible()
    expect(page.locator('//h1')).to_be_visible()
    expect(page.locator('(//h2)[1]')).to_be_visible()
    expect(page.locator('(//h2)[2]')).to_be_visible()
    expect(page.locator('(//h2)[4]')).to_be_visible()
    expect(page.locator('(//a[@href="/ratesmobile"])[1]')).to_be_visible()
    for i in range(2, 40):
        expect(page.locator(f'(//div[@itemprop="offers"])[{i}]')).to_be_visible()
    for i in range(2, 40):
        expect(page.locator(f'(//span[contains(text(), "Подключить")])[{i}]')).to_be_visible()
    expect(page.locator('//div[@datatest="providers_find_adress"]')).to_be_visible()
    expect(page.locator('//div[@datatest="providers_callback2"]')).to_be_visible()
    for i in range(1, 28):
        expect(page.locator(f'(//a[@datatest="top_provider_block"])[{i}]')).to_be_visible()
    for i in range(1, 20):
        expect(page.locator(f'(//h3)[{i}]')).to_be_visible()


def test_internet_100(page: Page):
    page.goto('https://www.moskvaonline.ru/rates/internet-100-mbit')
    check_header(page)
    footer_mol(page)
    search_tariffs(page)
    header_mol(page)
    check_tags(page)
    sorting(page)
    expect(page.locator('//span[contains(text(), "Подключить интернет")]')).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Тарифы на интернет")])[1]')).to_be_visible()
    expect(page.locator('(//span[contains(text(), "100 мб/с")])[1]')).to_be_visible()
    expect(page.locator('//h1')).to_be_visible()
    expect(page.locator('(//h2)[1]')).to_be_visible()
    expect(page.locator('(//h2)[2]')).to_be_visible()
    expect(page.locator('(//h2)[4]')).to_be_visible()
    expect(page.locator('(//a[@href="/ratesmobile"])[1]')).to_be_visible()
    for i in range(2, 39):
        expect(page.locator(f'(//div[@itemprop="offers"])[{i}]')).to_be_visible()
    for i in range(2, 39):
        expect(page.locator(f'(//span[contains(text(), "Подключить")])[{i}]')).to_be_visible()
    expect(page.locator('//div[@datatest="providers_find_adress"]')).to_be_visible()
    expect(page.locator('//div[@datatest="providers_callback2"]')).to_be_visible()
    for i in range(1, 28):
        expect(page.locator(f'(//a[@datatest="top_provider_block"])[{i}]')).to_be_visible()
    for i in range(1, 16):
        expect(page.locator(f'(//h3)[{i}]')).to_be_visible()


def test_internet_300(page: Page):
    page.goto('https://www.moskvaonline.ru/rates/internet-300-mbit')
    check_header(page)
    footer_mol(page)
    search_tariffs(page)
    header_mol(page)
    check_tags(page)
    sorting(page)
    expect(page.locator('//span[contains(text(), "Подключить интернет")]')).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Тарифы на интернет")])[1]')).to_be_visible()
    expect(page.locator('(//span[contains(text(), "300 мб/с")])[1]')).to_be_visible()
    expect(page.locator('//h1')).to_be_visible()
    expect(page.locator('(//h2)[1]')).to_be_visible()
    expect(page.locator('(//h2)[2]')).to_be_visible()
    expect(page.locator('(//h2)[4]')).to_be_visible()
    expect(page.locator('(//a[@href="/ratesmobile"])[1]')).to_be_visible()
    for i in range(2, 37):
        expect(page.locator(f'(//div[@itemprop="offers"])[{i}]')).to_be_visible()
    for i in range(2, 37):
        expect(page.locator(f'(//span[contains(text(), "Подключить")])[{i}]')).to_be_visible()
    expect(page.locator('//div[@datatest="providers_find_adress"]')).to_be_visible()
    expect(page.locator('//div[@datatest="providers_callback2"]')).to_be_visible()
    for i in range(1, 28):
        expect(page.locator(f'(//a[@datatest="top_provider_block"])[{i}]')).to_be_visible()
    for i in range(1, 19):
        expect(page.locator(f'(//h3)[{i}]')).to_be_visible()


def test_internet_500(page: Page):
    page.goto('https://www.moskvaonline.ru/rates/internet-500-mbit')
    check_header(page)
    footer_mol(page)
    search_tariffs(page)
    header_mol(page)
    check_tags(page)
    sorting(page)
    expect(page.locator('//span[contains(text(), "Подключить интернет")]')).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Тарифы на интернет")])[1]')).to_be_visible()
    expect(page.locator('(//span[contains(text(), "500 мб/с")])[1]')).to_be_visible()
    expect(page.locator('//h1')).to_be_visible()
    expect(page.locator('(//h2)[1]')).to_be_visible()
    expect(page.locator('(//h2)[2]')).to_be_visible()
    expect(page.locator('(//h2)[4]')).to_be_visible()
    expect(page.locator('(//a[@href="/ratesmobile"])[1]')).to_be_visible()
    for i in range(2, 38):
        expect(page.locator(f'(//div[@itemprop="offers"])[{i}]')).to_be_visible()
    for i in range(2, 38):
        expect(page.locator(f'(//span[contains(text(), "Подключить")])[{i}]')).to_be_visible()
    expect(page.locator('//div[@datatest="providers_find_adress"]')).to_be_visible()
    expect(page.locator('//div[@datatest="providers_callback2"]')).to_be_visible()
    for i in range(1, 28):
        expect(page.locator(f'(//a[@datatest="top_provider_block"])[{i}]')).to_be_visible()
    for i in range(1, 18):
        expect(page.locator(f'(//h3)[{i}]')).to_be_visible()


def test_online_kinoteatr(page: Page):
    page.goto('https://www.moskvaonline.ru/rates/online-kinoteatr')
    check_header(page)
    footer_mol(page)
    search_tariffs(page)
    header_mol(page)
    check_tags(page)
    sorting(page)
    expect(page.locator('//span[contains(text(), "Подключить интернет")]')).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Тарифы на интернет")])[1]')).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Онлайн-кинотеатр")])[1]')).to_be_visible()
    expect(page.locator('//h1')).to_be_visible()
    expect(page.locator('(//h2)[1]')).to_be_visible()
    expect(page.locator('(//h2)[2]')).to_be_visible()
    expect(page.locator('(//h2)[4]')).to_be_visible()
    expect(page.locator('(//a[@href="/ratesmobile"])[1]')).to_be_visible()
    expect(page.locator('(//div[contains(text(), "ПРОВАЙДЕР")])[1]')).to_be_visible()
    expect(page.locator('//input[@name="sort_providers"]')).to_be_visible()
    for i in range(2, 34):
        expect(page.locator(f'(//div[@itemprop="offers"])[{i}]')).to_be_visible()
    for i in range(2, 34):
        expect(page.locator(f'(//span[contains(text(), "Подключить")])[{i}]')).to_be_visible()
    expect(page.locator('//div[@datatest="providers_find_adress"]')).to_be_visible()
    expect(page.locator('//div[@datatest="providers_callback2"]')).to_be_visible()
    for i in range(1, 28):
        expect(page.locator(f'(//a[@datatest="top_provider_block"])[{i}]')).to_be_visible()
    for i in range(1, 8):
        expect(page.locator(f'(//h3)[{i}]')).to_be_visible()


def test_reviews(page: Page):
    page.goto('https://www.moskvaonline.ru/reviews')
    check_header(page)
    footer_mol(page)
    header_mol(page)
    expect(page.locator('//span[contains(text(), "Подключить интернет")]')).to_be_visible()
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


def test_reviews2(page: Page):
    page.goto('https://www.moskvaonline.ru/reviews/2')
    check_header(page)
    footer_mol(page)
    header_mol(page)
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
    for i in range(1, 18):
        expect(page.locator(f'(//span[contains(text(), "Отзыв засчитан")])[{i}]')).to_be_visible()
    expect(page.locator('(//div[@aria-label="call"])[1]')).to_be_visible()
    expect(page.locator('(//div[@class="container"]//div[@class="row"])[5]')).to_be_visible()
    for i in range(1, 6):
        expect(page.locator(f'(//a[@aria-label="Переключить страницу"])[{i}]')).to_be_visible()


def test_address(page: Page):
    page.goto('https://www.moskvaonline.ru/address')
    check_header(page)
    footer_mol(page)
    header_mol(page)
    expect(page.locator('//span[contains(text(), "Подключить интернет")]')).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Карта покрытия")])[1]')).to_be_visible()
    expect(page.locator('(//h1)[1]')).to_be_visible()
    expect(page.locator('(//h2)[3]')).to_be_visible()
    expect(page.locator('(//div[contains(text(), "Введите ваш адрес и сравните всех провайдеров своего дома в одной удобной таблице.") ])[1]')).to_be_visible()
    expect(page.locator('(//h2)[5]')).to_be_visible()
    for i in range(1, 28):
        expect(page.locator(f'(//a[@datatest="top_provider_block"])[{i}]')).to_be_visible()
    expect(page.locator('(//h2)[6]')).to_be_visible()
    expect(page.locator('(//div[contains(text(), "А")])[5]')).to_be_visible()
    expect(page.locator('(//div[contains(text(), "Б")])[4]')).to_be_visible()
    expect(page.locator('(//div[contains(text(), "Б")])[5]')).to_be_visible()
    expect(page.locator('(//div[contains(text(), "В")])[4]')).to_be_visible()
    expect(page.locator('(//div[contains(text(), "В")])[5]')).to_be_visible()
    expect(page.locator('(//div[contains(text(), "Г")])[3]')).to_be_visible()
    expect(page.locator('(//div[contains(text(), "Г")])[4]')).to_be_visible()
    expect(page.locator('(//div[contains(text(), "З")])[1]')).to_be_visible()
    expect(page.locator('(//div[contains(text(), "З")])[2]')).to_be_visible()
    expect(page.locator('(//div[contains(text(), "Л")])[6]')).to_be_visible()
    expect(page.locator('(//div[contains(text(), "Л")])[7]')).to_be_visible()
    expect(page.locator('(//div[contains(text(), "П")])[3]')).to_be_visible()
    expect(page.locator('(//div[contains(text(), "П")])[4]')).to_be_visible()
    expect(page.locator('(//div[contains(text(), "Т")])[12]')).to_be_visible()
    expect(page.locator('(//div[contains(text(), "Т")])[13]')).to_be_visible()
    expect(page.locator('(//div[contains(text(), "Т")])[14]')).to_be_visible()
    expect(page.locator('(//h2)[1]')).to_be_visible()
    for i in range(1, 6):
        expect(page.locator(f'(//h3)[{i}]')).to_be_visible()
    for i in range(1, 6):
        expect(page.locator(f'(//p)[{i}]')).to_be_visible()
    expect(page.locator('(//h2)[2]')).to_be_visible()