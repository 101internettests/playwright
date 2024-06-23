from playwright.sync_api import Page, expect


# Тест на проверку наличия всех элементов на странице
def test_first_lenoblst(page: Page):
    page.goto('https://piter-online.net/leningradskaya-oblast')
    expect(page.locator('//h1[contains(text(), "Подключить лучший домашний интернет в Ленинградской области")]')).to_contain_text('Подключить лучший домашний интернет в Ленинградской области')
    expect(page.locator('(//div[contains(text(), "Подключить домашний интернет просто - введите свой адрес, а мы поможем выбрать тариф для дома. Даем гарантию на 90 дней и начисляем кэшбэк до 1000 рублей!")])[1]')).to_be_visible()
    expect(page.locator('//div[@datatest="main_raitingprovider_button"]')).to_have_text('Рейтинг провайдеров')
    expect(page.locator('//div[@datatest="main_comparetariff_button"]')).to_have_text('Выгодные пакеты интернета3 в 1')
    expect(page.locator('//div[@class="col-sm-6 col-lg-4"]')).to_contain_text('получили нашу помощь в выборе интернета за  15 лет')
    expect(page.locator('//div[@class="onlyNotMd onlyNotSm onlyNotXs col-lg-4"]')).to_contain_text('Бесплатная консультация')
    expect(page.locator('//div[@datatest="main_inflat_button"]')).to_contain_text('ИнтернетВ квартиру')
    expect(page.locator('//div[@datatest="main_inhouse_button"]')).to_contain_text('ИнтернетНа дачу')
    expect(page.locator('//div[@datatest="main_inoffice_button"]')).to_contain_text('ИнтернетВ офис')
    expect(page.locator('//h2[contains(text(), "Самые выгодные интернет тарифы для дома в Ленинградской области")]')).to_have_text('Самые выгодные интернет тарифы для дома в Ленинградской области')
    expect(page.locator('(//a[@datatest="providers_provider_alltariff_button"])[1]')).to_have_text('Показать все')
    expect(page.locator('//div[@id="OneClickForm"]')).to_be_visible()
    expect(page.locator('(//h2[contains(text(), "Топ провайдеров в Ленинградской области")])[2]')).to_contain_text('Топ провайдеров в Ленинградской области')
    expect(page.locator('(//div[@class="row"])[7]')).to_be_visible()
    expect(page.locator('(//a[@datatest="main_allreviews_button"][contains(text(), "оставить отзыв")])[1]')).to_have_text('оставить отзыв')
    expect(page.locator('(//a[@datatest="main_allreviews_button"][contains(text(), "все отзывы")])[1]')).to_have_text('все отзывы')
    expect(page.locator('//div[@class="row"]//div[@class="col-12 col-sm-6 col-md-4 col-lg-3"]').nth(4))
    expect(page.locator('//h2[contains(text(), "Подключить интернет домой в любом районе Ленинградской области")]')).to_contain_text('Подключить интернет домой в любом районе Ленинградской области')


def test_tohome_lenoblst(page: Page):
    page.goto('https://piter-online.net/leningradskaya-oblast/orders/tohome')
    expect(page.locator('(//span[contains(text(), "Подключить интернет")])[1]')).to_be_visible()
    expect(page.locator('//span[contains(text(), "поиск по адресу")]')).to_be_visible()
    expect(page.locator('//h1[contains(text(), "Провайдеры домашнего интернета по адресу в Ленинградской области")]')).to_be_visible()
    expect(page.locator('(//h2)[4]')).to_be_visible()
    expect(page.locator('(//h2)[5]')).to_be_visible()
    expect(page.locator('//div[@data-test="countRates"]')).to_be_visible()
    expect(page.locator('(//h2)[6]')).to_be_visible()
    expect(page.locator('//div[@datatest="providers_find_adress"]')).to_be_visible()
    expect(page.locator('(//h2)[1]')).to_be_visible()
    expect(page.locator('(//h2)[2]')).to_be_visible()
    expect(page.locator('(//div[@itemscope])[1]')).to_be_visible()


def test_providers_lenoblst(page: Page):
    page.goto('https://piter-online.net/leningradskaya-oblast/providers')
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
    expect(page.locator('(//span[contains(text(), "Тарифы на интернет")])[1]')).to_be_visible()
    expect(page.locator('//h1')).to_be_visible()
    expect(page.locator('(//h2)[2]')).to_be_visible()
    for i in range(1, 4):
        expect(page.locator(f'(//div[@datatest="providers_provider_button"])[{i}]')).to_be_visible()
    # expect(page.locator('(//div[@datatest="providers_find_adress"])[1]')).to_be_visible()
    # expect(page.locator('(//div[@datatest="providers_callback2"])[1]')).to_be_visible()
    expect(page.locator('(//h2)[4]')).to_be_visible()
    expect(page.locator('(//a[@datatest="top_provider_block"])[1]')).to_be_visible()
    expect(page.locator('(//h2)[1]')).to_be_visible()
    for i in range(1, 18):
        expect(page.locator(f'(//h3[@itemprop="name"])[{i}]')).to_be_visible()
    expect(page.locator('(//h3[@itemprop="name"])[1]')).to_be_visible()