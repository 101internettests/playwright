from playwright.sync_api import Page, expect


# Тест на проверку наличия всех элементов на странице
def test_first(page: Page):
    page.goto('https://piter-online.net/')
    expect(page.locator('//div[@id="HeaderMenu"]')).to_be_visible()
    expect(page.locator('(// a[@ aria-label="call"])[1]')).to_contain_text('БЕСПЛАТНАЯ КОНСУЛЬТАЦИЯ')
    expect(page.locator('(// div[@ datatest="main_button_enter"])[1]')).to_be_visible()
    expect(page.locator('//h1[contains(text(), "Подключить лучший домашний интернет в Санкт-Петербурге")]')).to_contain_text('Подключить лучший домашний интернет в Санкт-Петербурге')
    expect(page.locator('(//div[contains(text(), "Подключить домашний интернет просто - введите свой адрес, а мы поможем выбрать тариф для дома. Даем гарантию на 90 дней и начисляем кэшбэк до 1000 рублей!")])[1]')).to_be_visible()
    expect(page.locator('(//input[@ datatest="main_input_street_home_new"])[1]')).to_be_visible()
    expect(page.locator('(//input[@ datatest="main_input_street_home_new"])[2]')).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Тип подключения")])[1]')).to_be_visible()
    expect(page.locator('(// div[@ data-test="find_tohome_button"])[1]')).to_contain_text('показать тарифы')
    expect(page.locator('//div[@datatest="main_raitingprovider_button"]')).to_have_text('Рейтинг провайдеров')
    expect(page.locator('//div[@datatest="main_comparetariff_button"]')).to_have_text('Выгодные пакеты интернета3 в 1')
    expect(page.locator('//div[@class="col-sm-6 col-lg-4"]')).to_contain_text('получили нашу помощь в выборе интернета за  15 лет')
    expect(page.locator('//div[@class="onlyNotMd onlyNotSm onlyNotXs col-lg-4"]')).to_contain_text('Бесплатная консультация')
    expect(page.locator('//div[@datatest="main_inflat_button"]')).to_contain_text('ИнтернетВ квартиру')
    expect(page.locator('//div[@datatest="main_inhouse_button"]')).to_contain_text('ИнтернетНа дачу')
    expect(page.locator('//div[@datatest="main_inoffice_button"]')).to_contain_text('ИнтернетВ офис')
    expect(page.locator('//h2[contains(text(), "Самые выгодные интернет тарифы для дома в Санкт-Петербурге")]')).to_have_text('Самые выгодные интернет тарифы для дома в Санкт-Петербурге')
    expect(page.locator('(//a[@datatest="providers_provider_alltariff_button"])[1]')).to_have_text('Показать все')
    expect(page.locator('//div[@id="OneClickForm"]')).to_be_visible()
    expect(page.locator('(//h2[contains(text(), "Топ провайдеров в Санкт-Петербурге")])[2]')).to_contain_text('Топ провайдеров в Санкт-Петербурге')
    expect(page.locator('(//div[@class="row"])[7]')).to_be_visible()
    expect(page.locator('(//a[@datatest="main_allreviews_button"][contains(text(), "оставить отзыв")])[1]')).to_have_text('оставить отзыв')
    expect(page.locator('(//a[@datatest="main_allreviews_button"][contains(text(), "все отзывы")])[1]')).to_have_text('все отзывы')
    expect(page.locator('//div[@class="row"]//div[@class="col-12 col-sm-6 col-md-4 col-lg-3"]').nth(4))
    expect(page.locator('//h2[contains(text(), "Подключить интернет домой в любом районе Санкт-Петербурга")]')).to_contain_text('Подключить интернет домой в любом районе Санкт-Петербурга')
    expect(page.locator('//footer')).to_be_visible()
    expect(page.locator('//span[contains(text(), "© 2008-2024 «Питер Онлайн» — поиск провайдеров по адресу")]')).to_contain_text('© 2008-2024 «Питер Онлайн» — поиск провайдеров по адресу')
    expect(page.get_by_role("link", name="https://vk.com/ru101internet"))
    expect(page.get_by_role('link', name='https://www.odnoklassniki.ru/group/51961592610882'))
    expect(page.get_by_role('link', name='yan-dzen'))