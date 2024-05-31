from playwright.sync_api import Page, expect


# тест без города
def test_select_region(page: Page):
    page.goto('https://101internet.ru/select-region')
    expect(page.locator('//span[contains(text(), "Выберите город или регион")]')).to_be_visible()
    expect(page.locator('//input[@placeholder="Введите первые 3 буквы"]')).to_be_visible()
    for i in range(1, 34):
        expect(page.locator(f'(//a[@datatest="main_region_choose"][@href])[{i}]')).to_be_visible()
    for i in range(1, 24):
        expect(page.locator(f'(//*[@id="root"]/div/div[2]/div/div/div/div/div[3]/div)[{i}]')).to_be_visible()
    expect(page.locator('//div[@class="components__slider-button"]')).to_be_visible()
    expect(page.locator('(//span[@class="icon24 icon-close"])[1]')).to_be_visible()


# Тест на проверку наличия всех элементов на первой странице
def test_without_city_main(page: Page):
    page.goto('https://101internet.ru')
    expect(page.locator('//div[@id="HeaderMenu"]')).to_be_visible()
    expect(page.locator('(// a[@ aria-label="call"])[1]')).to_contain_text('БЕСПЛАТНАЯ КОНСУЛЬТАЦИЯ')
    expect(page.locator('(// div[@ datatest="main_button_enter"])[1]')).to_be_visible()
    expect(page.locator('//h1[contains(text(), "Подключить интернет")]')).to_contain_text('Подключить интернет')
    expect(page.locator('(//div[contains(text(), "Введите адрес и сравните тарифы всех провайдеров в своём доме - '
                        'подключайтесь с гарантией 90 дней!")])[1]')).to_be_visible()
    expect(page.locator('(//input[@ datatest="main_input_street_home_new"])[1]')).to_be_visible()
    expect(page.locator('(//input[@ datatest="main_input_street_home_new"])[2]')).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Тип подключения")])[1]')).to_be_visible()
    expect(page.locator('(//button[@ data-test="find_tohome_button"])[1]')).to_contain_text('показать тарифы')
    expect(page.locator('//div[@datatest="main_raitingprovider_button"]')).to_have_text('Рейтинг провайдеров')
    expect(page.locator('//div[@datatest="main_comparetariff_button"]')).to_have_text('Выгодные пакеты интернета3 в 1')
    expect(page.locator('//div[@class="col-sm-6 col-lg-4"]')).to_contain_text('получили нашу помощь в выборе интернета за  15 лет')
    expect(page.locator('//div[@class="onlyNotMd onlyNotSm onlyNotXs col-lg-4"]')).to_contain_text('Бесплатная консультация')
    expect(page.locator('//div[@datatest="main_inflat_button"]')).to_contain_text('ИнтернетВ квартиру')
    expect(page.locator('//div[@datatest="main_inhouse_button"]')).to_contain_text('ИнтернетНа дачу')
    expect(page.locator('//div[@datatest="main_inoffice_button"]')).to_contain_text('ИнтернетВ офис')
    expect(page.locator('(//a[@datatest="providers_provider_alltariff_button"])[1]')).to_have_text('Показать все')
    expect(page.locator('//div[@id="OneClickForm"]')).to_be_visible()
    # expect(page.locator('(//h2[contains(text(), "Наши партнеры в Абакане")])[2]')).to_contain_text('Наши партнеры в Абакане ')
    expect(page.locator('(//div[@class="row"])[7]')).to_be_visible()
    # expect(page.locator('//h2[contains(text(), "Отзывы о провайдерах домашнего интернета в Абакане")]')).to_have_text('Отзывы о провайдерах домашнего интернета в Абакане')
    expect(page.locator('(//a[@datatest="main_allreviews_button"][contains(text(), "оставить отзыв")])[1]')).to_have_text('оставить отзыв')
    expect(page.locator('(//a[@datatest="main_allreviews_button"][contains(text(), "все отзывы")])[1]')).to_have_text('все отзывы')
    expect(page.locator('//div[@class="row"]//div[@class="col-12 col-sm-6 col-md-4 col-lg-3"]').nth(4))
    expect(page.locator('(//h2)[9]')).to_be_visible()
    expect(page.locator('(//div[contains(text(), "Все")])[1]')).to_be_visible()
    expect(page.locator('//footer')).to_be_visible()
    expect(page.locator('//span[contains(text(), "© 2008-2024 «101 Интернет» — поиск провайдеров по адресу")]')).to_contain_text('© 2008-2024 «101 Интернет» — поиск провайдеров по адресу')
    expect(page.get_by_role("link", name="https://vk.com/ru101internet"))
    expect(page.get_by_role('link', name='https://www.odnoklassniki.ru/group/51961592610882'))
    expect(page.get_by_role('link', name='yan-dzen'))


def test_personal_datarates_without(page: Page):
    page.goto('https://101internet.ru/about/personal-data')
    expect(page.locator('(//a[@aria-label="/"] )[2]')).to_be_visible()
    expect(page.locator('(//a[contains(text(), "Поиск по адресу")])[1]')).to_be_visible()
    expect(page.locator('(//a[contains(text(), "провайдеры")])[1]')).to_be_visible()
    expect(page.locator('(//a[contains(text(), "рейтинг")])[1]')).to_be_visible()
    expect(page.locator('(//a[contains(text(), "Тарифы")])[1]')).to_be_visible()
    expect(page.locator('(//a[contains(text(), "Интернет в офис")])[1]')).to_be_visible()
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
    expect(page.locator('//footer')).to_be_visible()
    expect(page.locator('//section')).to_be_visible()
    expect(page.locator(
        '//span[contains(text(), "© 2008-2024 «101 Интернет» — поиск провайдеров по адресу")]')).to_contain_text(
        '© 2008-2024 «101 Интернет» — поиск провайдеров по адресу')
    expect(page.get_by_role("link", name="https://vk.com/ru101internet"))
    expect(page.get_by_role('link', name='https://www.odnoklassniki.ru/group/51961592610882'))
    expect(page.get_by_role('link', name='yan-dzen'))


def test_terms_of_use(page: Page):
    page.goto('https://101internet.ru/about/terms-of-use')
    expect(page.locator('(//a[@aria-label="/"] )[2]')).to_be_visible()
    expect(page.locator('(//a[contains(text(), "Поиск по адресу")])[1]')).to_be_visible()
    expect(page.locator('(//a[contains(text(), "провайдеры")])[1]')).to_be_visible()
    expect(page.locator('(//a[contains(text(), "рейтинг")])[1]')).to_be_visible()
    expect(page.locator('(//a[contains(text(), "Тарифы")])[1]')).to_be_visible()
    expect(page.locator('(//a[contains(text(), "Интернет в офис")])[1]')).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Подключить интернет")])[1]')).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Пользовательское соглашение")])[1]')).to_be_visible()
    expect(page.locator('//h1')).to_be_visible()
    for i in range(1, 10):
        expect(page.locator(f'(//h2)[{i}]')).to_be_visible()
    for i in range(1, 64):
        expect(page.locator(f'(//p)[{i}]')).to_be_visible()
    expect(page.locator('//footer')).to_be_visible()
    expect(page.locator('//section')).to_be_visible()
    expect(page.locator(
        '//span[contains(text(), "© 2008-2024 «101 Интернет» — поиск провайдеров по адресу")]')).to_contain_text(
        '© 2008-2024 «101 Интернет» — поиск провайдеров по адресу')
    expect(page.get_by_role("link", name="https://vk.com/ru101internet"))
    expect(page.get_by_role('link', name='https://www.odnoklassniki.ru/group/51961592610882'))
    expect(page.get_by_role('link', name='yan-dzen'))