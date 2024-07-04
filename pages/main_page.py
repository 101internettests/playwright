import pytest
from playwright.sync_api import Page, expect


def check_header(page: Page):
    expect(page.locator("#HeaderMenu")).to_contain_text("БЕСПЛАТНАЯ КОНСУЛЬТАЦИЯ")
    expect(page.locator("#HeaderMenu").get_by_role("link", name="call")).to_be_visible()
    expect(page.locator('(//div[@ datatest="main_button_enter"])[1]')).to_be_visible()
    expect(page.locator('(//div[@itemscope])[1]')).to_be_visible()
    expect(page.locator('(// div[@ datatest="main_button_enter"])[1]')).to_be_visible()
    expect(page.locator('(//a[contains(text(), "Поиск по адресу")])[1]')).to_be_visible()
    expect(page.locator('(//a[contains(text(), "провайдеры")])[1]')).to_be_visible()
    expect(page.locator('(//a[contains(text(), "рейтинг")])[1]')).to_be_visible()
    expect(page.locator('(//a[contains(text(), "Тарифы")])[1]')).to_be_visible()
    expect(page.locator('(//a[contains(text(), "Интернет в офис")])[1]')).to_be_visible()


def search_tariffs(page: Page):
    expect(page.locator('(//span[contains(text(), "Введите улицу")])[1]')).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Дом")])[1]')).to_be_visible()
    # expect(page.locator('(//span[contains(text(), "Тип подключения")])[1]')).to_be_visible()
    expect(page.locator('(//div[contains(text(), "показать тарифы")])[1]')).to_be_visible()


def search_tariffs_second(page: Page):
    expect(page.locator('(//span[contains(text(), "Введите улицу")])[1]')).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Дом")])[1]')).to_be_visible()
    # expect(page.locator('(//span[contains(text(), "Тип подключения")])[1]')).to_be_visible()
    expect(page.locator('(//div[contains(text(), "найти")])[1]')).to_be_visible()


def one_click_form(page: Page):
    expect(page.locator('//div[@id="OneClickForm"]')).to_be_visible()


def tariffs_block(page: Page):
    expect(page.locator('//div[@data-test="countRates"]')).to_be_visible()


def blue_form(page: Page):
    expect(page.locator('(//div[@datatest="providers_find_adress"])[1]')).to_be_visible()
    expect(page.locator('(//div[@datatest="providers_find_adress"]//span[contains(text(), "Введите улицу")])[1]')).to_be_visible()
    expect(page.locator('(//div[@datatest="providers_find_adress"]//span[contains(text(), "Дом")])[1]')).to_be_visible()
    expect(page.locator('(//div[@datatest="providers_find_adress"]//div[contains(text(), "Проверить")])[1]')).to_be_visible()


def blue_form_second(page: Page):
    expect(page.locator('(//div[@datatest="providers_find_adress"])[2]')).to_be_visible()
    expect(page.locator('(//div[@datatest="providers_find_adress"]//span[contains(text(), "Введите улицу")])[2]')).to_be_visible()
    expect(page.locator('(//div[@datatest="providers_find_adress"]//span[contains(text(), "Дом")])[2]')).to_be_visible()
    expect(page.locator('(//div[@datatest="providers_find_adress"]//div[contains(text(), "Проверить")])[2]')).to_be_visible()


def check_footer(page: Page):
    expect(page.locator('//section')).to_be_visible()
    expect(page.locator('//footer')).to_be_visible()
    expect(page.locator(
        '//span[contains(text(), "© 2008-2024 «101 Интернет» — поиск провайдеров по адресу")]')).to_contain_text(
        '© 2008-2024 «101 Интернет» — поиск провайдеров по адресу')
    expect(page.get_by_role("link", name="https://vk.com/ru101internet"))
    expect(page.get_by_role('link', name='https://www.odnoklassniki.ru/group/51961592610882'))
    expect(page.get_by_role('link', name='yan-dzen'))


def footer_mol(page: Page):
    expect(page.locator('//section')).to_be_visible()
    expect(page.locator('//footer')).to_be_visible()
    expect(page.locator(
        '//span[contains(text(), "© 2008-2024 «Москва Онлайн» — поиск провайдеров по адресу")]')).to_contain_text(
        '© 2008-2024 «Москва Онлайн» — поиск провайдеров по адресу')
    expect(page.get_by_role("link", name="https://vk.com/ru101internet"))
    expect(page.get_by_role('link', name='https://www.odnoklassniki.ru/group/51961592610882'))
    expect(page.get_by_role('link', name='yan-dzen'))


def footer_pol(page: Page):
    expect(page.locator('//section')).to_be_visible()
    expect(page.locator('//footer')).to_be_visible()
    expect(page.locator(
        '//span[contains(text(), "© 2008-2024 «Питер Онлайн» — поиск провайдеров по адресу")]')).to_contain_text(
        '© 2008-2024 «Питер Онлайн» — поиск провайдеров по адресу')
    expect(page.get_by_role("link", name="https://vk.com/ru101internet"))
    expect(page.get_by_role('link', name='https://www.odnoklassniki.ru/group/51961592610882'))
    expect(page.get_by_role('link', name='yan-dzen'))


def sorting(page: Page):
    expect(page.locator('//div[contains(text(), "Сортировка")]')).to_be_visible()
    expect(page.locator('//input[@name="select_providers"]')).to_be_visible()


def page_internet_in_office(page: Page):
    expect(page.get_by_text("Контактное лицо*")).to_be_visible()
    expect(page.get_by_text("Ваш телефон*")).to_be_visible()
    expect(page.get_by_text("Контактное лицо*Ваш телефон*+")).to_be_visible()
    expect(page.get_by_text("Адрес подключения*")).to_be_visible()
    expect(page.locator(
        '//div[contains(text(), "Если необходимо подключить несколько адресов - нажмите на «+»")]')).to_be_visible()
    for i in range(1, 3):
        expect(page.locator(f'(//span[contains(text(), "*")])[{i}]')).to_be_visible()
    expect(page.locator('//input[@datatest="business_order_input_person"]')).to_be_visible()
    expect(page.locator('//input[@datatest="business_order_input_tel"]')).to_be_visible()
    expect(page.locator('(//input[@datatest="main_input_street_home_new"])[1]')).to_be_visible()
    expect(page.locator('(//input[@datatest="main_input_street_home_new"])[2]')).to_be_visible()
    expect(page.locator('//div[contains(text(), "Место подключения")]')).to_be_visible()
    expect(page.locator('//label[@datatest="business_order_ownoffice_button"]')).to_be_visible()
    expect(page.locator('//label[@datatest="business_order_officenetwork_button"]')).to_be_visible()
    expect(page.locator('//label[@datatest="business_order_ownbuilding_button"]')).to_be_visible()
    expect(page.locator('//div[contains(text(), "Тип помещения")]')).to_be_visible()
    expect(page.locator('(//input[@aria-labelledby="label"])[3]')).to_be_visible()
    expect(page.locator('//input[@autocomplete="on"]')).to_be_visible()
    expect(page.locator('//div[contains(text(), "Услуги")]')).to_be_visible()
    expect(page.locator('//label[@for="tender__services0"]')).to_be_visible()
    expect(page.locator('//label[@for="tender__services1"]')).to_be_visible()
    expect(page.locator('//label[@for="tender__services2"]')).to_be_visible()
    expect(page.locator('//label[@for="tender__services3"]')).to_be_visible()
    expect(page.locator('//label[@for="tender__services4"]')).to_be_visible()
    expect(page.locator('//label[@for="tender__services5"]')).to_be_visible()
    expect(page.locator('//label[@for="tender__services6"]')).to_be_visible()
    expect(page.locator('//div[contains(text(), "СКОРОСТЬ")]')).to_be_visible()
    expect(page.locator('//div[contains(text(), "Технология")]')).to_be_visible()
    expect(page.locator('//input[@datatest="business_order_input_internetspeed"]')).to_be_visible()
    expect(page.locator('//input[@datatest="business_order_input_technology"]')).to_be_visible()
    expect(page.locator('//label[@datatest="business_order_input_services_changeprovider"]')).to_be_visible()
    expect(page.locator('//label[@datatest="business_order_input_services_reservecanal"]')).to_be_visible()
    expect(page.locator('//label[@datatest="business_order_input_services_wantconnect"]')).to_be_visible()
    expect(page.locator('//div[contains(text(), "Название организации")]')).to_be_visible()
    expect(page.locator('//div[contains(text(), "ВЕБ-САЙТ")]')).to_be_visible()
    expect(page.locator('//div[contains(text(), "Комментарий")]')).to_be_visible()
    expect(page.locator('//input[@datatest="business_order_input_nameorg"]')).to_be_visible()
    expect(page.locator('//input[@datatest="business_order_input_site"]')).to_be_visible()
    expect(page.locator('//textarea[@datatest="business_order_input_comment"]')).to_be_visible()
    for i in range(1, 2):
        expect(page.locator(f'(//div[@data-test="business_order_tenderbbutton"])[{i}]')).to_be_visible()


def feedback_page(page: Page):
    expect(page.locator('//h1')).to_be_visible()
    expect(page.locator('(//span[@class="icon24 icon-close"])[1]')).to_be_visible()
    expect(page.locator('//div[contains(text(), "ПРОВАЙДЕР")]')).to_be_visible()
    for i in range(1, 4):
        expect(page.locator(f'(//div[contains(text(), "Интернет")])[{i}]')).to_be_visible()
    expect(page.locator('//input[@datatest="feedback_input_provider"]')).to_be_visible()
    expect(page.locator('//input[@datatest="feedback_input_internettype"]')).to_be_visible()
    expect(page.locator('//div[contains(text(), "Оцените сервис провайдера по 5-балльной шкале. Если вы не пользовались услугой - не оценивайте этот пункт. Прежде, чем дать негативную оценку - убедитесь, что проблема действительно была на стороне провайдера.")]')).to_be_visible()
    expect(page.locator('//div[contains(text(), "Как долго вы пользуетесь услугами провайдера?")]')).to_be_visible()
    expect(page.get_by_text("Меньше 3 месяцев")).to_be_visible()
    expect(page.get_by_text("месяца - 1 год")).to_be_visible()
    expect(page.get_by_text("год и больше")).to_be_visible()
    expect(page.get_by_text("Какой услугой провайдера вы пользовались?")).to_be_visible()
    expect(page.get_by_text("Домашний интернет")).to_be_visible()
    expect(page.get_by_text("Интернет и ТВ")).to_be_visible()
    expect(page.get_by_text("Интернет и мобильная связь")).to_be_visible()
    expect(page.get_by_text("Интернет", exact=True).nth(1)).to_be_visible()
    expect(page.get_by_text(
        "Связь всегда стабильна. Качество услуг соответствует ожиданиям, долговременных перебоев не случается")).to_be_visible()
    expect(page.get_by_text("Стабильная скорость")).to_be_visible()
    expect(page.get_by_text(
        "Скорость передачи данных соответствует заявленной в тарифе. Она не «проседает» даже в вечерние часы")).to_be_visible()
    expect(page.get_by_text("Телевидение")).to_be_visible()
    expect(page.get_by_text(
        "Качество телевизионного сигнала стабильно. Отсутствуют разрывы картинки. Изображение синхронно со звуком")).to_be_visible()
    expect(page.get_by_text("Монтажники")).to_be_visible()
    expect(page.get_by_text(
        "Уровень клиентского сервиса соответствует заявленному. Устранение неполадок происходит в кратчайшие сроки")).to_be_visible()
    expect(page.get_by_text("Техподдержка")).to_be_visible()
    expect(page.get_by_text(
        "Время ожидания ответа оператора составляет не более пяти минут. Квалифицированность операторов не вызывает сомнений")).to_be_visible()
    expect(page.get_by_text("Забота")).to_be_visible()
    expect(page.get_by_text(
        "Консультанты всегда вежливы и приветливы. Отзывчивые и терпеливые операторы всегда оказывают необходимую поддержку")).to_be_visible()
    expect(page.get_by_text("Оборудование", exact=True)).to_be_visible()
    expect(page.get_by_text("Предоставляемые провайдером роутер, ТВ-приставка и прочее оборудование")).to_be_visible()
    expect(page.get_by_text("Ваш адрес")).to_be_visible()
    expect(page.get_by_label("Выберите").nth(2)).to_be_visible()
    expect(page.get_by_label("Выберите").nth(2)).to_be_visible()
    expect(page.get_by_text("Дом", exact=True)).to_be_visible()
    expect(page.get_by_text("Ваш отзыв")).to_be_visible()
    expect(page.get_by_text("Минимальная длина отзыва 100")).to_be_visible()
    expect(page.locator("#root textarea")).to_be_visible()
    expect(page.locator("[data-test=\"feedback_next_button\"]")).to_be_visible()
    expect(page.get_by_text(
        "Нажимая на кнопку \"Отправить отзыв\", вы даёте Согласие на обработку персональных")).to_be_visible()
    page.get_by_label("call").click()
    expect(page.get_by_role("img", name="Поддержка")).to_be_visible()
    expect(page.locator("[data-test=\"waitingCall_button\"]")).to_be_visible()
    expect(page.get_by_text(
        "Нажимая на кнопку \"Жду звонка\", вы даёте Согласие на обработку персональных данн")).to_be_visible()
    expect(page.get_by_text("Мы сделаем всё за вас!")).to_be_visible()
    expect(page.get_by_text("Нужно только оставить номер телефона :)")).to_be_visible()


def sorting_providers_rates(page: Page):
    expect(page.locator('//div[contains(text(), "Район")]')).to_be_visible()
    expect(page.locator('//div[contains(text(), "Скорость (мбит/c)")]')).to_be_visible()
    expect(page.locator('//div[contains(text(), "Цена в месяц (руб)")]')).to_be_visible()
    expect(page.locator('//div[contains(text(), "Сортировка")]')).to_be_visible()
    expect(page.locator('//input[@datatest="providers_input_filter_district"]')).to_be_visible()
    expect(page.locator('//div[@datatest="providers_provider_input_internetspeed"]')).to_be_visible()
    expect(page.locator('//div[@datatest="providers_provider_input_priceinmonth"]')).to_be_visible()
    expect(page.locator('//input[@value="Сначала популярные "]')).to_be_visible()