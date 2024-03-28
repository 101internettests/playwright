from playwright.sync_api import Page, expect


# Тест на проверку наличия всех элементов на странице
def test_first(page: Page):
    page.goto('https://piter-online.net/')
    expect(page.locator('//div[@id="HeaderMenu"]')).to_be_visible()
    expect(page.locator('(// a[@ aria-label="call"])[1]')).to_contain_text('БЕСПЛАТНАЯ КОНСУЛЬТАЦИЯ')
    expect(page.locator('(// div[@ datatest="main_button_enter"])[1]')).to_be_visible()
    expect(page.locator('//h1[contains(text(), "Подключить лучший домашний интернет по адресу")]')).to_contain_text('Подключить лучший домашний интернет по адресу')
    expect(page.locator('(//div[contains(text(), "Введите ваш адрес и сравните всех провайдеров своего дома в одной '
                        'удобной таблице. В ней есть вся информация, необходимая для выбора провайдера: тарифы, '
                        'сведения о прочих опциях, народный рейтинг провайдеров.")])[1]')).to_be_visible()
    expect(page.locator('(//input[@ datatest="main_input_street_home_new"])[1]')).to_be_visible()
    expect(page.locator('(//input[@ datatest="main_input_street_home_new"])[2]')).to_be_visible()
    expect(page.locator('(//input[@ value="В квартиру "])[1]')).to_be_visible()
    expect(page.locator('(// div[@ data-test="find_tohome_button"])[1]')).to_contain_text('показать тарифы')
    expect(page.locator('//div[@datatest="main_raitingprovider_button"]')).to_have_text('Рейтинг провайдеров')
    expect(page.locator('//div[@datatest="main_comparetariff_button"]')).to_have_text('Выгодные пакеты интернета3 в 1')
    expect(page.locator('//div[@class="col-sm-6 col-lg-4"]')).to_contain_text('получили нашу помощь в выборе интернета за  15 лет')
    expect(page.locator('//div[@class="onlyNotMd onlyNotSm onlyNotXs col-lg-4"]')).to_contain_text('Бесплатная консультация')
    expect(page.locator('//div[@datatest="main_inflat_button"]')).to_contain_text('ИнтернетВ квартиру')
    expect(page.locator('//div[@datatest="main_inhouse_button"]')).to_contain_text('ИнтернетНа дачу')
    expect(page.locator('//div[@datatest="main_inoffice_button"]')).to_contain_text('ИнтернетВ офис')
    expect(page.locator('(//div[@style="align-self:center"])[1]')).to_have_text('Выгодные тарифы')
    expect(page.locator('(//a[@datatest="providers_provider_alltariff_button"])[1]')).to_have_text('Показать все')
    expect(page.locator('//div[@id="OneClickForm"]')).to_be_visible()
    expect(page.locator('(//div[contains(text(), "Топ провайдеров в ")])[2]')).to_contain_text('Топ провайдеров в ')
    expect(page.locator('(//div[@style="align-self:center"])[2]')).to_have_text('Рейтинг провайдеров домашнего интернета')
    expect(page.locator('//div[@class="row"]//div[@class="col"]')).to_be_visible()
    expect(page.locator('(//div[@style="align-self:center"])[3]')).to_have_text('отзывы о провайдерах')
    expect(page.locator('(//a[@datatest="main_allreviews_button"][contains(text(), "оставить отзыв")])[1]')).to_have_text('оставить отзыв')
    expect(page.locator('(//a[@datatest="main_allreviews_button"][contains(text(), "все отзывы")])[1]')).to_have_text('все отзывы')
    expect(page.locator('//div[@class="row"]//div[@class="col-12 col-sm-6 col-md-4 col-lg-3"]').nth(4))
    expect(page.locator('//div[contains(text(), "Выберите район в ")]')).to_contain_text('Выберите район в ')
    expect(page.locator('//div[contains(text(), "Все")]')).to_be_visible()
    expect(page.locator('//div[@datatest="main_footer"]')).to_be_visible()
    expect(page.locator('//div[contains(text(), "© 2008-2024 «Питер On-line» — поиск провайдеров по адресу")]')).to_contain_text('© 2008-2024 «Питер On-line» — поиск провайдеров по адресу')
    expect(page.locator('//div[contains(text(), "Мы в соцсетях")]')).to_contain_text('Мы в соцсетях')
    expect(page.get_by_role('link', name='https://vk.com/spbonlinerf')).to_be_enabled()
    expect(page.get_by_role('link', name='https://ok.ru/group/53245494165570')).to_be_enabled()
    expect(page.get_by_role('link', name='yan-dzen')).to_be_enabled()