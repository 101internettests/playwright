import allure
from playwright.sync_api import Page, expect


@allure.step("Проверка хедера")
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


@allure.step("Проверка хедера на странице операторов")
def check_header_operator_page(page: Page):
    expect(page.locator('(//div[@ datatest="main_button_enter"])[1]')).to_be_visible()
    expect(page.locator('(//div[@itemscope])[1]')).to_be_visible()
    expect(page.locator('(// div[@ datatest="main_button_enter"])[1]')).to_be_visible()
    expect(page.locator('(//a[contains(text(), "Поиск по адресу")])[1]')).to_be_visible()
    expect(page.locator('(//a[contains(text(), "провайдеры")])[1]')).to_be_visible()
    expect(page.locator('(//a[contains(text(), "рейтинг")])[1]')).to_be_visible()
    expect(page.locator('(//a[contains(text(), "Тарифы")])[1]')).to_be_visible()
    expect(page.locator('(//a[contains(text(), "Интернет в офис")])[1]')).to_be_visible()


@allure.step("Проверка блока ввода адреса для поиска тарифов")
def search_tariffs(page: Page):
    expect(page.locator('(//span[contains(text(), "Введите улицу")])[1]')).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Дом")])[1]')).to_be_visible()
    # expect(page.locator('(//span[contains(text(), "Тип подключения")])[1]')).to_be_visible()
    expect(page.locator('(//div[contains(text(), "показать тарифы")])[1]')).to_be_visible()


@allure.step("Проверка блока ввода адреса для поиска тарифов вариант 2")
def search_tariffs_second(page: Page):
    expect(page.locator('(//span[contains(text(), "Введите улицу")])[1]')).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Дом")])[1]')).to_be_visible()
    # expect(page.locator('(//span[contains(text(), "Тип подключения")])[1]')).to_be_visible()
    expect(page.locator('(//div[contains(text(), "найти")])[1]')).to_be_visible()


@allure.step("Проверка формы в один клик")
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


@allure.step("Проверка футера")
def check_footer(page: Page):
    expect(page.locator('//section')).to_be_visible()
    expect(page.locator('//footer')).to_be_visible()
    expect(page.get_by_role("link", name="https://vk.com/ru101internet"))
    expect(page.get_by_role('link', name='https://www.odnoklassniki.ru/group/51961592610882'))
    expect(page.get_by_role('link', name='yan-dzen'))
    expect(page.get_by_text("Тарифы для дома")).to_be_visible()
    expect(page.locator("section").get_by_role("link", name="Поиск по адресу")).to_be_visible()
    expect(page.get_by_text("Мобильная связь", exact=True)).to_be_visible()
    expect(page.locator("section")).to_contain_text("Провайдеры в")
    expect(page.get_by_role("link", name="Все провайдеры")).to_be_visible()
    expect(page.get_by_role("link", name="Отзывы о провайдерах")).to_be_visible()
    expect(page.get_by_role("link", name="Рейтинг провайдеров", exact=True)).to_be_visible()
    expect(page.get_by_role("link", name="Акции провайдеров")).to_be_visible()
    expect(page.locator("section").get_by_role("link", name="Интернет в офис")).to_be_visible()
    expect(page.get_by_role("link", name="Интернет на дачу", exact=True)).to_be_visible()
    expect(page.get_by_text("Мобильная связь", exact=True)).to_be_visible()
    expect(page.get_by_role("link", name="О нас")).to_be_visible()
    expect(page.get_by_role("link", name="Оплата и гарантии")).to_be_visible()
    expect(page.get_by_role("link", name="Блог")).to_be_visible()
    # expect(page.get_by_role("link", name="Отзывы о компании")).to_be_visible()
    expect(page.get_by_role("link", name="Контакты")).to_be_visible()
    expect(page.get_by_role("link", name="Карьера")).to_be_visible()
    expect(page.get_by_role("link", name="Сотрудничество")).to_be_visible()
    expect(page.get_by_role("link", name="Карта сайта")).to_be_visible()
    expect(page.get_by_role("link", name="Документы")).to_be_visible()
    expect(page.get_by_role("link", name="Политика обработки персональных данных")).to_be_visible()


@allure.step("Проверка футера МОЛ")
def footer_mol(page: Page):
    expect(page.locator('//section')).to_be_visible()
    expect(page.locator('//footer')).to_be_visible()
    expect(page.locator(
        '//span[contains(text(), "© 2008-2024 «Москва Онлайн» — поиск провайдеров по адресу")]')).to_contain_text(
        '© 2008-2024 «Москва Онлайн» — поиск провайдеров по адресу')
    expect(page.get_by_role("link", name="https://vk.com/ru101internet"))
    expect(page.get_by_role('link', name='https://www.odnoklassniki.ru/group/51961592610882'))
    expect(page.get_by_role('link', name='yan-dzen'))


@allure.step("Проверка футера ПОЛ")
def footer_pol(page: Page):
    expect(page.locator('//section')).to_be_visible()
    expect(page.locator('//footer')).to_be_visible()
    expect(page.locator(
        '//span[contains(text(), "© 2008-2024 «Питер Онлайн» — поиск провайдеров по адресу")]')).to_contain_text(
        '© 2008-2024 «Питер Онлайн» — поиск провайдеров по адресу')
    expect(page.get_by_role("link", name="https://vk.com/ru101internet"))
    expect(page.get_by_role('link', name='https://www.odnoklassniki.ru/group/51961592610882'))
    expect(page.get_by_role('link', name='yan-dzen'))


@allure.step("Проверка блока сортировки")
def sorting(page: Page):
    expect(page.locator('//div[contains(text(), "Сортировка")]')).to_be_visible()
    expect(page.locator('//input[@name="select_providers"]')).to_be_visible()


@allure.step("Проверка блока сортировки вариант 2")
def sorting_second(page: Page):
    expect(page.locator('//div[contains(text(), "Сортировка")]')).to_be_visible()
    expect(page.locator('//input[@value="Сначала популярные "]')).to_be_visible()


@allure.step("Проверка страницы интернета в офисе")
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


@allure.step("Проверка страницы обратной связи")
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


@allure.step("Проверка блока фильтров")
def sorting_providers_rates(page: Page):
    expect(page.locator('//div[contains(text(), "Район")]')).to_be_visible()
    expect(page.locator('//div[contains(text(), "Скорость (мбит/c)")]')).to_be_visible()
    expect(page.locator('//div[contains(text(), "Цена в месяц (руб)")]')).to_be_visible()
    expect(page.locator('//div[contains(text(), "Сортировка")]')).to_be_visible()
    expect(page.locator('//input[@datatest="providers_input_filter_district"]')).to_be_visible()
    expect(page.locator('//div[@datatest="providers_provider_input_internetspeed"]')).to_be_visible()
    expect(page.locator('//div[@datatest="providers_provider_input_priceinmonth"]')).to_be_visible()
    expect(page.locator('//input[@value="Сначала популярные "]')).to_be_visible()


@allure.step("Проверка заглушки")
def ooops_stub(page: Page):
    expect(page.locator('//span[@class="icon48 icon-hearts"]')).to_be_visible()
    expect(page.locator('//div[contains(text(), "Упс")]')).to_be_visible()
    expect(page.locator('//div[contains(text(), "Похоже, что по вашему запросу нет подходящих тарифов. Попробуйте сбросить значения фильтров.")]')).to_be_visible()
    expect(page.locator('//div[contains(text(), "Сбросить фильтры")]')).to_be_visible()


@allure.step("Проверка страницы пользовательское соглашение")
def terms_of_use(page: Page):
    expect(page.get_by_role("link", name="Подключить интернет")).to_be_visible()
    expect(page.locator('//span[contains(text(), "Пользовательское соглашение")]')).to_be_visible()
    expect(page.locator('//h1')).to_be_visible()
    for i in range(1, 10):
        expect(page.locator(f'(//h2)[{i}]')).to_be_visible()
    expect(page.locator('//h1')).to_be_visible()
    expect(page.locator("#root")).to_contain_text("Настоящее Пользовательское соглашение")
    expect(page.locator("#root")).to_contain_text("1.1.")
    expect(page.locator("#root")).to_contain_text("1.4.")
    expect(page.locator("#root")).to_contain_text("2.1.")
    expect(page.locator("#root")).to_contain_text("2.7.")
    expect(page.locator("#root")).to_contain_text("3.1.")
    expect(page.locator("#root")).to_contain_text("3.10.")
    expect(page.locator("#root")).to_contain_text("4.1.")
    expect(page.locator("#root")).to_contain_text("4.3.")
    expect(page.locator("#root")).to_contain_text("5.1.")
    expect(page.locator("#root")).to_contain_text("5.5.")
    expect(page.locator("#root")).to_contain_text("6.1.")
    expect(page.locator("#root")).to_contain_text("6.8.")
    expect(page.locator("#root")).to_contain_text("7.1.")
    expect(page.locator("#root")).to_contain_text("7.5.")
    expect(page.locator("#root")).to_contain_text("8.1.")
    expect(page.locator("#root")).to_contain_text("8.5.")
    expect(page.locator("#root")).to_contain_text("9.1.")
    expect(page.locator("#root")).to_contain_text("9.4.")


@allure.step("Проверка страницы политики обработки персональных данных")
def personal_data(page: Page):
    expect(page.get_by_role("link", name="Подключить интернет")).to_be_visible()
    expect(page.locator('//span[contains(text(), "Политика обработки персональных данных")]')).to_be_visible()
    expect(page.locator('//h1')).to_be_visible()
    for i in range(1, 9):
        expect(page.locator(f'(//h2)[{i}]')).to_be_visible()
    expect(page.locator("#root")).to_contain_text("Назначение и область действия документа")
    expect(page.locator("#root")).to_contain_text("1.1.")
    expect(page.locator("#root")).to_contain_text("1.2.")
    expect(page.locator("#root")).to_contain_text("2.1.")
    expect(page.locator("#root")).to_contain_text("3.1.")
    expect(page.locator("#root")).to_contain_text("3.15.")
    expect(page.locator("#root")).to_contain_text("4.1.")
    expect(page.locator("#root")).to_contain_text("4.2.")
    expect(page.locator("#root")).to_contain_text("5.1.")
    expect(page.locator("#root")).to_contain_text("6.1")
    expect(page.locator("#root")).to_contain_text("6.4.")
    expect(page.get_by_text("ПРИЛОЖЕНИЕ №1")).to_be_visible()
    expect(page.get_by_text("ПРИЛОЖЕНИЕ №2")).to_be_visible()
    expect(page.get_by_role("link", name="Пользовательское соглашение")).to_be_visible()
    expect(page.get_by_text("Согласие на обработку персональных данных.pdf")).to_be_visible()


@allure.step("Проверка страницы обратной связи")
def contact_feedback(page: Page):
    expect(page.get_by_role("heading", name="Обратная связь")).to_be_visible()
    expect(page.get_by_text("Вы представляете компанию?*")).to_be_visible()
    expect(page.locator('//div[contains(text(), "Да")]')).to_be_visible()
    expect(page.locator('(//div[contains(text(), "Нет")])[1]')).to_be_visible()
    expect(page.get_by_text("Причина обращения?*")).to_be_visible()
    expect(page.get_by_text("На сайте что-то не работает или работает некорректно")).to_be_visible()
    expect(page.get_by_text("Неточности в информации на сайте")).to_be_visible()
    expect(page.get_by_text("Предложить идею")).to_be_visible()
    expect(page.get_by_text("Хочу у вас/c вами работать!")).to_be_visible()
    expect(page.get_by_text("Я знаю провайдера, которого у вас нет!")).to_be_visible()
    expect(page.get_by_text("Сообщение*")).to_be_visible()
    expect(page.get_by_text(
        "Сообщение*Пожалуйста, изложите суть обращения. Укажите ссылки, если это необходи")).to_be_visible()
    expect(page.get_by_text("Хочу получить ответ")).to_be_visible()
    expect(page.get_by_text("Отправить", exact=True)).to_be_visible()
    expect(page.get_by_text(
        "Нажимая на кнопку \"Отправить\", вы даёте Согласие на обработку персональных данны")).to_be_visible()
    expect(page.get_by_role("heading")).to_contain_text("Обратная связь")
    expect(page.locator("form")).to_contain_text("Вы представляете компанию?*")
    expect(page.locator("form")).to_contain_text("Причина обращения?*")
    expect(page.locator("form")).to_contain_text("На сайте что-то не работает или работает некорректно")
    expect(page.locator("form")).to_contain_text("Неточности в информации на сайте")
    expect(page.locator("form")).to_contain_text("Предложить идею")
    expect(page.locator("form")).to_contain_text("Хочу у вас/c вами работать!")
    expect(page.locator("form")).to_contain_text("Я знаю провайдера, которого у вас нет!")
    expect(page.locator("form")).to_contain_text("Сообщение*")
    expect(page.get_by_role("paragraph")).to_contain_text(
        "Пожалуйста, изложите суть обращения. Укажите ссылки, если это необходимо")
    expect(page.locator("form")).to_contain_text("Хочу получить ответ")
    expect(page.locator("form")).to_contain_text("Отправить")


@allure.step("Проверка страницы контактов")
def contact_page(page: Page):
    expect(page.get_by_role("link", name="Подключить интернет")).to_be_visible()
    expect(page.locator("span").filter(has_text="Контакты")).to_be_visible()
    expect(page.get_by_role("heading", name="Контакты")).to_be_visible()
    expect(page.get_by_text("Сотрудничество и реклама")).to_be_visible()
    expect(page.get_by_text("Для резюме")).to_be_visible()
    expect(page.get_by_text("Контактный центр")).to_be_visible()
    expect(page.get_by_text("Рассмотрим предложения о сотрудничестве и рекламе")).to_be_visible()
    expect(page.get_by_text("Резюме с рассказом о себе высылайте нам")).to_be_visible()
    expect(page.get_by_text("Единый телефон контактного центра")).to_be_visible()
    expect(page.get_by_label("mail").first).to_be_visible()
    expect(page.get_by_text("hr@101internet.ru")).to_be_visible()
    expect(page.get_by_text("+7 800 302-32-76", exact=True)).to_be_visible()
    expect(page.get_by_text("Схема проезда")).to_be_visible()
    expect(page.frame_locator("iframe[title=\"Схема проезда в офис 101 интернет на Яндекс Картах\"]").locator(
        ".search-placemark-icons__active > svg")).to_be_visible()
    page.get_by_text("Адрес: Россия, Москва, Тихая ул., 33, офис").click()
    expect(page.get_by_text("Тел.: +7 800 302-32-")).to_be_visible()
    expect(page.get_by_text("Время работы")).to_be_visible()
    expect(page.get_by_text(
        "Консультация физических лицПонедельник - воскресеньеКруглосуточноКонсультация юр")).to_be_visible()
    expect(page.get_by_text("Реквизиты ООО \"ИНТЕРНЕТ ПРОМОУШЕН\"")).to_be_visible()
    expect(page.get_by_text("ООО \"ИНТЕРНЕТ ПРОМОУШЕН\"Юридический адрес: 390005")).to_be_visible()
    expect(page.get_by_text("Стать партнером")).to_be_visible()
    expect(page.get_by_placeholder("Ваше имя*")).to_be_visible()
    expect(page.get_by_placeholder("Ваш телефон*")).to_be_visible()
    expect(page.get_by_text("Отправить", exact=True)).to_be_visible()
    expect(page.get_by_text("Обратная связь").first).to_be_visible()
    expect(page.get_by_role("link", name="Обратная связь")).to_be_visible()
    expect(page.get_by_text("Обратная связьe-mailpr@")).to_be_visible()
    expect(page.get_by_role("heading", name="Частые вопросы")).to_be_visible()


@allure.step("Проверка страницы контактов")
def contact_page_pol(page: Page):
    expect(page.get_by_role("link", name="Подключить интернет")).to_be_visible()
    expect(page.locator("span").filter(has_text="Контакты")).to_be_visible()
    expect(page.get_by_role("heading", name="Контакты")).to_be_visible()
    expect(page.get_by_text("Сотрудничество и реклама")).to_be_visible()
    expect(page.get_by_text("Контактный центр")).to_be_visible()
    expect(page.get_by_text("Рассмотрим предложения о сотрудничестве и рекламе")).to_be_visible()
    expect(page.get_by_text("Единый телефон контактного центра")).to_be_visible()
    expect(page.get_by_label("mail").first).to_be_visible()
    expect(page.locator('(//a[contains(text(), "+7 (812) 635-33-61")])[1]')).to_be_visible()
    expect(page.get_by_text("Схема проезда")).to_be_visible()
    expect(page.get_by_placeholder("Ваше имя*")).to_be_visible()
    expect(page.get_by_placeholder("Ваш телефон*")).to_be_visible()
    expect(page.get_by_text("Отправить", exact=True)).to_be_visible()
    expect(page.get_by_text("Обратная связь").first).to_be_visible()
    expect(page.get_by_role("link", name="Обратная связь")).to_be_visible()
    expect(page.get_by_text("Как добраться?")).to_be_visible()
    expect(
        page.get_by_text("На общественном транспорте: до станции метро Площадь Александра Невского-2")).to_be_visible()
    expect(page.get_by_text("Адрес офиса компании")).to_be_visible()
    expect(page.get_by_text("г. Санкт-Петербург, Невский проспект, стр")).to_be_visible()
    expect(page.get_by_text("Почтовый адрес")).to_be_visible()
    expect(page.get_by_text("Россия, Санкт-Петербург,")).to_be_visible()
    expect(page.get_by_text("Время работы")).to_be_visible()
    expect(page.get_by_text("Реквизиты")).to_be_visible()
    expect(page.get_by_text("Стать партнером")).to_be_visible()
    expect(page.get_by_role("link", name="Обратная связь")).to_be_visible()
    expect(page.get_by_text("e-mail", exact=True)).to_be_visible()
    expect(page.get_by_text("e-mailpr@piter-online.net")).to_be_visible()
    expect(page.get_by_role("heading", name="Частые вопросы")).to_be_visible()


@allure.step("Проверка мобильных тегов")
def tags_mobile(page: Page):
    expect(page.get_by_role("link", name="Все", exact=True)).to_be_visible()
    expect(page.get_by_role("link", name="eSIM")).to_be_visible()
    expect(page.get_by_role("link", name="Роуминг за границей")).to_be_visible()
    expect(page.get_by_role("link", name="Семейные")).to_be_visible()
    expect(page.get_by_role("link", name="Выгодные")).to_be_visible()
    expect(page.get_by_role("link", name="Для планшета")).to_be_visible()
    expect(page.get_by_role("link", name="Детские")).to_be_visible()
    expect(page.get_by_role("link", name="Безлимитная связь")).to_be_visible()
    expect(page.get_by_role("link", name="Связь по России")).to_be_visible()
    expect(page.get_by_role("link", name="Безлимитный интернет")).to_be_visible()
    expect(page.get_by_role("link", name="Перейти со своим номером")).to_be_visible()
    expect(page.get_by_role("link", name="Непубличные🔥")).to_be_visible()
    expect(page.get_by_role("link", name="Для модема/роутера")).to_be_visible()


@allure.step("Проверка блоков тегов")
def tags_for_operatory(page: Page):
    expect(page.get_by_text("минуты", exact=True)).to_be_visible()
    expect(page.get_by_text("интернет (гб)")).to_be_visible()
    expect(page.get_by_text("абонентская плата (руб)")).to_be_visible()
    for i in range(1, 3):
        expect(page.locator(f'(//div[@tabindex="-1"])[{i}]')).to_be_visible()


@allure.step("Проверка тегов у номеров")
def tags_nomera_mobile(page: Page):
    expect(page.get_by_role("link", name="Все", exact=True)).to_be_visible()
    expect(page.get_by_role("link", name="Бронзовые")).to_be_visible()
    expect(page.get_by_role("link", name="Серебряные")).to_be_visible()
    expect(page.get_by_role("link", name="Золотые")).to_be_visible()
    expect(page.get_by_role("link", name="Платиновые")).to_be_visible()
    expect(page.get_by_role("link", name="Бесплатные")).to_be_visible()


@allure.step("Проверка страницы номеров")
def nomera_page(page: Page):
    expect(page.get_by_role("link", name="Федеральные")).to_be_visible()
    expect(page.get_by_role("link", name="VIP")).to_be_visible()
    expect(page.get_by_role("link", name="Подключить интернет")).to_be_visible()
    expect(page.get_by_role("link", name="Номера")).to_be_visible()
    expect(page.locator('//div[contains(text(), "ПОКАЗАТЬ ЕЩЁ")]')).to_be_visible()
    expect(page.locator('//h2[contains(text(), "Частые вопросы")]')).to_be_visible()
    expect(page.locator(
        '//span[contains(text(), "Информация носит справочный характер и не является публичной офертой.")]')).to_be_visible()
    for i in range(1, 15):
        expect(page.locator(f'(//div[contains(text(), "Подключить На официальном сайте")])[{i}]')).to_be_visible()


@allure.step("Проверка страницы мобильных опервторов")
def cellular_network(page: Page):
    expect(page.get_by_role("link", name="Подключить интернет")).to_be_visible()
    expect(page.get_by_role("link", name="Тарифы сотовой связи")).to_be_visible()
    expect(page.get_by_text("КОНСТРУКТОР (new!)")).to_be_visible()
    expect(page.get_by_text("СПИСОК ТАРИФОВ")).to_be_visible()
    expect(page.locator('//h2[contains(text(), "Частые вопросы")]')).to_be_visible()
    expect(page.locator('//div[contains(text(), "Сортировка")]')).to_be_visible()
    expect(page.locator('//input[@value="Сначала популярные "]')).to_be_visible()


@allure.step("Проверка блока с выбором раздела")
def operators_menu_block(page: Page):
    expect(page.get_by_role("link", name="Об операторе")).to_be_visible()
    expect(page.get_by_role("link", name="Тарифы").nth(1)).to_be_visible()
    expect(page.get_by_role("link", name="Номера").nth(1)).to_be_visible()
    expect(page.get_by_role("link", name="акции", exact=True)).to_be_visible()
    expect(page.get_by_role("link", name="в 1")).to_be_visible()


@allure.step("Проверка блока с выбором раздела")
def rating_page(page: Page):
    expect(page.locator('//div[contains(text(), "Полезные")]')).to_be_visible()
    expect(page.locator('//div[contains(text(), "Новые")]')).to_be_visible()
    expect(page.locator('//div[contains(text(), "Старые")]')).to_be_visible()