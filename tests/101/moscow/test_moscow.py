from playwright.sync_api import Page, expect
from pages.main_page import check_header, search_tariffs, one_click_form, tariffs_block, blue_form, feedback_page, sorting_providers_rates, contact_feedback
from pages.main_page import check_footer, blue_form_second, search_tariffs_second, sorting, page_internet_in_office, ooops_stub, terms_of_use, personal_data
from pages.main_site_pages.moscow_page import check_header_moscow, check_tags, check_provider_rostel_tags, check_provider_onlime_tags


def test_reviews_page(page: Page):
    page.goto('https://101internet.ru/moskva/reviews')
    check_header(page)
    check_footer(page)
    one_click_form(page)
    check_header_moscow(page)
    expect(page.get_by_role("heading", name="Отзывы о провайдерах домашнего интернета Москвы")).to_be_visible()
    expect(page.get_by_role("link", name="Подключить интернет")).to_be_visible()
    expect(page.get_by_text("Отзывы об интернет-провайдерах")).to_be_visible()
    expect(page.locator("#OneClickForm div").filter(has_text="Подберем интернет за 2").first).to_be_visible()
    expect(page.get_by_role("img", name="Фото формы в один клик")).to_be_visible()
    page.get_by_text("Номер телефона").click()
    page.locator("[data-test=\"waitingCall_button\"]").click()
    expect(page.get_by_label("Номер телефона")).to_be_visible()
    expect(page.get_by_role("link", name="оставить отзыв")).to_be_visible()
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


def test_review2_page(page: Page):
    page.goto('https://101internet.ru/moskva/reviews/2')
    check_header(page)
    check_footer(page)
    one_click_form(page)
    check_header_moscow(page)
    expect(page.get_by_role("link", name="Подключить интернет")).to_be_visible()
    expect(page.get_by_text("Отзывы об интернет-провайдерах Москвы")).to_be_visible()
    expect(page.locator("#OneClickForm div").filter(has_text="Подберем интернет за 2").first).to_be_visible()
    expect(page.get_by_role("img", name="Фото формы в один клик")).to_be_visible()
    page.get_by_text("Номер телефона").click()
    page.locator("[data-test=\"waitingCall_button\"]").click()
    expect(page.get_by_label("Номер телефона")).to_be_visible()
    expect(page.get_by_role("link", name="оставить отзыв")).to_be_visible()
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


def test_address_page(page: Page):
    page.goto('https://101internet.ru/moskva/address')
    check_header(page)
    check_footer(page)
    check_header_moscow(page)
    search_tariffs(page)
    expect(page.get_by_role("heading", name="Топ провайдеров в Москве")).to_be_visible()
    expect(page.get_by_role("link", name="Тарифы провайдера билайн билайн")).to_be_visible()
    expect(page.get_by_role("heading", name="Топ провайдеров в Москве")).to_be_visible()
    expect(page.get_by_role("link", name="Тарифы провайдера билайн билайн")).to_be_visible()
    expect(page.get_by_role("link", name="Тарифы провайдера Онлайм Онлайм")).to_be_visible()
    expect(page.get_by_text("З", exact=True).nth(1)).to_be_visible()
    expect(page.get_by_text("А", exact=True).first).to_be_visible()
    expect(page.get_by_text("Н", exact=True).first).to_be_visible()
    expect(page.get_by_text("С", exact=True).nth(1)).to_be_visible()
    expect(page.get_by_text("П", exact=True).first).to_be_visible()
    expect(page.locator(".app328 > div:nth-child(4)").first).to_be_visible()
    expect(page.get_by_text("Л", exact=True).first).to_be_visible()
    expect(page.get_by_text("Ш", exact=True).first).to_be_visible()
    expect(page.get_by_text("Г", exact=True).first).to_be_visible()
    expect(page.get_by_text("Л", exact=True).first).to_be_visible()
    expect(page.get_by_text("М", exact=True).first).to_be_visible()
    expect(page.get_by_text("С", exact=True).first).to_be_visible()
    expect(page.get_by_text("Ю", exact=True)).to_be_visible()
    expect(page.get_by_text("Е", exact=True).first).to_be_visible()
    expect(page.get_by_role("heading", name="Выберите поселение")).to_be_visible()
    expect(page.get_by_text("1", exact=True)).to_be_visible()
    expect(page.get_by_text("Д", exact=True).nth(2)).to_be_visible()
    expect(page.get_by_text("Н", exact=True).nth(1)).to_be_visible()
    expect(page.get_by_text("Ф", exact=True).nth(1)).to_be_visible()
    expect(page.get_by_text("Л", exact=True).nth(1)).to_be_visible()
    expect(page.get_by_text("Д", exact=True).nth(1)).to_be_visible()
    expect(page.get_by_role("heading", name="Зона покрытия интернет-провайдеров в районах Москвы")).to_be_visible()
    expect(page.locator("#root")).to_contain_text("Как работать с картой покрытия")
    expect(page.get_by_role("heading", name="Частые вопросы")).to_be_visible()
    expect(page.get_by_role("heading",
                            name="Как узнать какие интернет-провайдеры есть по адресу в Москве?")).to_be_visible()


def test_address_bogogod_page(page: Page):
    page.goto('https://101internet.ru/moskva/address/%D0%B1%D0%BE%D0%B3%D0%BE%D1%80%D0%BE%D0%B4%D1%81%D0%BA%D0%BE%D0%B5-id1063')
    check_header(page)
    check_footer(page)
    check_header_moscow(page)
    search_tariffs(page)
    blue_form(page)
    expect(page.get_by_role("heading", name="Лучшие интернет тарифы р. Богородское")).to_be_visible()
    expect(page.get_by_text("Количество доступных к подключению тарифов – 398")).to_be_visible()
    for i in range(1, 16):
        expect(page.locator(f'(//div[@datatest="providers_provider_button"])[{i}]')).to_be_visible()
    for i in range(2, 30):
        expect(page.locator(f'(//span[contains(text(), "Подключить")])[{i}]')).to_be_visible()
    for i in range(5, 22):
        expect(page.locator(f'(//a[@aria-label])[{i}]')).to_be_visible()
    for i in range(1, 5):
        expect(page.locator(f'(//h2)[{i}]')).to_be_visible()
    for i in range(1, 5):
        expect(page.locator(f'(//div[@itemprop="mainEntity"])[{i}]')).to_be_visible()


def test_address_bogogod_street_page(page: Page):
    page.goto('https://101internet.ru/moskva/address/%D0%B1%D0%BE%D0%B3%D0%BE%D1%80%D0%BE%D0%B4%D1%81%D0%BA%D0%BE%D0%B5-id1063/%D1%83%D0%BB-%D0%B4%D0%B5%D1%82%D1%81%D0%BA%D0%B0%D1%8F-id266631')
    check_header(page)
    check_footer(page)
    check_header_moscow(page)
    expect(page.locator('(//span[contains(text(), "Дом")])[1]')).to_be_visible()
    expect(page.locator('(//div[contains(text(), "показать тарифы")])[1]')).to_be_visible()
    expect(page.locator('(//div[@datatest="providers_find_adress"])[1]')).to_be_visible()
    expect(page.locator('(//div[@datatest="providers_find_adress"]//span[contains(text(), "Дом")])[1]')).to_be_visible()
    expect(page.locator(
        '(//div[@datatest="providers_find_adress"]//div[contains(text(), "Проверить")])[1]')).to_be_visible()
    expect(page.get_by_role("heading", name="Выберите свой дом на ул. Детская (Богородское)")).to_be_visible()
    expect(page.get_by_text("8 – столько домов на вашей улице обслуживают официальные партнёры нашего сервиса. Чтобы проверить, какие провайдеры подключены в вашем доме, найдите его в списке или воспользуйтесь поиском по адресу")).to_be_visible()
    for i in range(1, 10):
        expect(page.locator(f'(//div[@datatest="providers_provider_button"])[{i}]')).to_be_visible()
    for i in range(2, 21):
        expect(page.locator(f'(//span[contains(text(), "Подключить")])[{i}]')).to_be_visible()
    for i in range(5, 14):
        expect(page.locator(f'(//a[@aria-label])[{i}]')).to_be_visible()
    for i in range(1, 6):
        expect(page.locator(f'(//h2)[{i}]')).to_be_visible()
    for i in range(1, 5):
        expect(page.locator(f'(//div[@itemprop="mainEntity"])[{i}]')).to_be_visible()


def test_rates_mosk_page(page: Page):
    page.goto('https://101internet.ru/moskva/rates?house_id=3047559')
    check_header(page)
    check_footer(page)
    check_header_moscow(page)
    search_tariffs(page)
    check_tags(page)
    expect(page.locator('//div[contains(text(), "Тип интернета")]')).to_be_visible()
    expect(page.locator('(//div[contains(text(), "Провайдер")])[1]')).to_be_visible()
    expect(page.locator('//div[contains(text(), "Сортировка")]')).to_be_visible()
    expect(page.locator('//span[contains(text(), "Неважно")]')).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Любой")])[1]')).to_be_visible()
    expect(page.locator('//input[@value="Сначала популярные "]')).to_be_visible()
    for i in range(1, 30):
        expect(page.locator(f'(//div[@datatest="providers_provider_button"])[{i}]')).to_be_visible()
    for i in range(2, 30):
        expect(page.locator(f'(//span[contains(text(), "Подключить")])[{i}]')).to_be_visible()
    for i in range(5, 35):
        expect(page.locator(f'(//a[@aria-label])[{i}]')).to_be_visible()
    for i in range(1, 8):
        expect(page.locator(f'(//h2)[{i}]')).to_be_visible()
    for i in range(1, 6):
        expect(page.locator(f'(//div[@itemprop="mainEntity"])[{i}]')).to_be_visible()
    for i in range(1, 5):
        expect(page.locator(f'(//a[@aria-label="Переключить страницу"])[{i}]')).to_be_visible()
    for i in range(1, 8):
        expect(page.locator(f'(//a[@datatest="top_provider_block"])[{i}]')).to_be_visible()


def test_rates2_mosk_page(page: Page):
    page.goto('https://101internet.ru/moskva/rates/2?house_id=3047559')
    check_header(page)
    check_footer(page)
    check_header_moscow(page)
    search_tariffs(page)
    check_tags(page)
    expect(page.locator('//div[contains(text(), "Тип интернета")]')).to_be_visible()
    expect(page.locator('(//div[contains(text(), "Провайдер")])[1]')).to_be_visible()
    expect(page.locator('//div[contains(text(), "Сортировка")]')).to_be_visible()
    expect(page.locator('//span[contains(text(), "Неважно")]')).to_be_visible()
    expect(page.locator('(//span[contains(text(), "Любой")])[1]')).to_be_visible()
    expect(page.locator('//input[@value="Сначала популярные "]')).to_be_visible()
    for i in range(1, 30):
        expect(page.locator(f'(//div[@datatest="providers_provider_button"])[{i}]')).to_be_visible()
    for i in range(5, 35):
        expect(page.locator(f'(//a[@aria-label])[{i}]')).to_be_visible()
    for i in range(1, 6):
        expect(page.locator(f'(//h2)[{i}]')).to_be_visible()
    for i in range(1, 6):
        expect(page.locator(f'(//div[@itemprop="mainEntity"])[{i}]')).to_be_visible()
    for i in range(1, 5):
        expect(page.locator(f'(//a[@aria-label="Переключить страницу"])[{i}]')).to_be_visible()
    for i in range(1, 8):
        expect(page.locator(f'(//a[@datatest="top_provider_block"])[{i}]')).to_be_visible()


def test_sat_mosk_page(page: Page):
    page.goto('https://101internet.ru/moskva/orders/sat')
    check_header(page)
    check_footer(page)
    check_header_moscow(page)
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


def test_office_mosk_page(page: Page):
    page.goto('https://101internet.ru/moskva/orders/office')
    check_header(page)
    check_footer(page)
    check_header_moscow(page)
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
    expect(page.locator('//div[contains(text(), "Малому бизнесу")]')).to_be_visible()
    expect(page.locator('//div[contains(text(), "Среднему бизнесу")]')).to_be_visible()
    expect(page.locator('//div[contains(text(), "Крупному бизнесу")]')).to_be_visible()
    expect(page.locator('//div[contains(text(), "отзывы о провайдерах")]')).to_be_visible()
    expect(page.locator('(//a[contains(text(), "оставить отзыв")])[1]')).to_be_visible()
    expect(page.locator('(//a[contains(text(), "все отзывы")])[1]')).to_be_visible()
    for i in range(1, 4):
        expect(page.locator(f'(//div[@itemtype="https://schema.org/Review"])[{i}]')).to_be_visible()


def test_business_mosk_page(page: Page):
    page.goto('https://101internet.ru/moskva/business')
    check_header(page)
    check_footer(page)
    check_header_moscow(page)
    page_internet_in_office(page)
    expect(page.locator('//h1')).to_be_visible()
    expect(page.locator('//input[@datatest="business_order_input_person"]')).to_be_visible()
    expect(page.locator('//input[@datatest="business_order_input_tel"]')).to_be_visible()
    expect(page.locator('(//input[@datatest="main_input_street_home_new"])[1]')).to_be_visible()
    expect(page.locator('(//input[@datatest="main_input_street_home_new"])[2]')).to_be_visible()


def test_business_mosk_addresspage(page: Page):
    page.goto('https://101internet.ru/moskva/business?house_id=193448')
    check_header(page)
    check_footer(page)
    check_header_moscow(page)
    page_internet_in_office(page)
    expect(page.locator('//h1')).to_be_visible()
    expect(page.locator('//input[@datatest="business_order_input_person"]')).to_be_visible()
    expect(page.locator('//input[@datatest="business_order_input_tel"]')).to_be_visible()
    expect(page.locator('(//input[@datatest="main_input_street_home_new"])[1]')).to_be_visible()
    expect(page.locator('(//input[@datatest="main_input_street_home_new"])[2]')).to_be_visible()


def test_feedback_page(page: Page):
    page.goto('https://101internet.ru/moskva/feedback')
    feedback_page(page)


def test_partners_page(page: Page):
    page.goto('https://101internet.ru/moskva/about/partners')
    check_header(page)
    check_footer(page)
    check_header_moscow(page)
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
    expect(page.get_by_role("link", name="pr@101internet.ru")).to_be_visible()


def test_provider_mts_page(page: Page):
    page.goto('https://101internet.ru/moskva/providers/mts')
    check_header(page)
    check_footer(page)
    check_header_moscow(page)
    expect(page.locator('//img[@alt="Лого провайдера"]')).to_be_visible()
    expect(page.get_by_role("link", name="Подключить интернет")).to_be_visible()
    expect(page.get_by_role("link", name="Провайдеры Москвы")).to_be_visible()
    expect(page.locator("#provider_banner").get_by_text("МТС", exact=True)).to_be_visible()
    expect(page.get_by_role("heading", name="Домашний интернет от провайдера МТС в Москве")).to_be_visible()
    expect(page.locator("#provider_banner").get_by_text("Оставить заявку")).to_be_visible()
    expect(page.locator("#provider_banner").get_by_text("Подключение")).to_be_visible()
    expect(page.get_by_role("link", name="+7 (495) 106-82-")).to_be_visible()
    expect(page.locator("#provider_banner").get_by_text("Техподдержка")).to_be_visible()
    expect(page.get_by_role("link", name="+7 (800) 250-08-")).to_be_visible()
    expect(page.get_by_text("Проверить доступность МТС по адресу")).to_be_visible()
    search_tariffs(page)
    expect(page.get_by_role("link", name="О провайдере")).to_be_visible()
    expect(page.locator('(//a[contains(text(), "Тарифы")])[3]')).to_be_visible()
    expect(page.get_by_role("link", name="акции", exact=True)).to_be_visible()
    expect(page.get_by_text("Тарифы", exact=True).nth(3)).to_be_visible()
    expect(page.get_by_role("link", name="Все тарифы").first).to_be_visible()
    expect(page.get_by_text("Оставить заявку").nth(1)).to_be_visible()
    for i in range(1, 4):
        expect(page.locator(f'(//div[@datatest="providers_form_inspect_connect_tariff_button"])[{i}]')).to_be_visible()
    expect(page.locator('//div[@data-test="countRates"]')).to_be_visible()
    expect(page.locator('//div[contains(text(), "Отзывы наших клиентов")]')).to_be_visible()
    expect(page.locator('(//a[contains(text(), "Все тарифы")])[1]')).to_be_visible()
    for i in range(1, 7):
        expect(page.locator(f'(//div[@itemtype="https://schema.org/Review"])[{i}]')).to_be_visible()
    expect(page.locator('(//a[contains(text(), "все отзывы")])[2]')).to_be_visible()
    expect(page.locator('//div[@itemtype="http://schema.org/Organization"]')).to_be_visible()
    expect(page.locator('(//h2)[1]')).to_be_visible()


def test_provider_rostelecom(page: Page):
    page.goto('https://101internet.ru/moskva/providers/rostelecom/rates')
    check_header(page)
    check_footer(page)
    check_header_moscow(page)
    expect(page.locator('//img[@alt="Лого провайдера"]')).to_be_visible()
    expect(page.get_by_role("link", name="Подключить интернет")).to_be_visible()
    expect(page.get_by_role("link", name="Провайдеры Москвы")).to_be_visible()
    expect(page.locator('//span[contains(text(), "Ростелеком")]')).to_be_visible()
    expect(page.locator('//span[contains(text(), "Тарифы")]')).to_be_visible()
    expect(page.get_by_role("heading", name="Тарифные планы интернет-провайдера Ростелеком в Москве")).to_be_visible()
    expect(page.locator('(//div[contains(text(), "Оставить заявку")])[2]')).to_be_visible()
    expect(page.locator("#provider_banner").get_by_text("Подключение")).to_be_visible()
    expect(page.get_by_role("link", name="+7 (499) 372-33-55")).to_be_visible()
    expect(page.locator("#provider_banner").get_by_text("Техподдержка")).to_be_visible()
    expect(page.get_by_role("link", name="+7 (800) 100-08-00")).to_be_visible()
    expect(page.get_by_text("Проверить доступность Ростелеком по адресу")).to_be_visible()
    search_tariffs(page)
    expect(page.get_by_role("link", name="О провайдере")).to_be_visible()
    expect(page.locator('(//a[contains(text(), "Тарифы")])[3]')).to_be_visible()
    expect(page.get_by_role("link", name="акции", exact=True)).to_be_visible()
    check_provider_rostel_tags(page)
    expect(page.locator('//div[contains(text(), "Район")]')).to_be_visible()
    expect(page.locator('//div[contains(text(), "Скорость (мбит/c)")]')).to_be_visible()
    expect(page.locator('//div[contains(text(), "Цена в месяц (руб)")]')).to_be_visible()
    expect(page.locator('//div[contains(text(), "Сортировка")]')).to_be_visible()
    expect(page.locator('//input[@datatest="providers_input_filter_district"]')).to_be_visible()
    expect(page.locator('//div[@datatest="providers_provider_input_internetspeed"]')).to_be_visible()
    expect(page.locator('//div[@datatest="providers_provider_input_priceinmonth"]')).to_be_visible()
    expect(page.locator('//input[@value="Сначала популярные "]')).to_be_visible()
    for i in range(1, 15):
        expect(page.locator(f'(//div[@datatest="providers_form_inspect_connect_tariff_button"])[{i}]')).to_be_visible()
    for i in range(1, 4):
        expect(page.locator(f'(//a[@aria-label="Переключить страницу"])[{i}]')).to_be_visible()
    expect(page.locator('(//h2)[1]')).to_be_visible()


def test_provider2_rostelecom(page: Page):
    page.goto('https://101internet.ru/moskva/providers/rostelecom/rates/2')
    check_header(page)
    check_footer(page)
    check_header_moscow(page)
    expect(page.locator('//img[@alt="Лого провайдера"]')).to_be_visible()
    expect(page.get_by_role("link", name="Подключить интернет")).to_be_visible()
    expect(page.get_by_role("link", name="Провайдеры Москвы")).to_be_visible()
    expect(page.locator('//span[contains(text(), "Ростелеком")]')).to_be_visible()
    expect(page.locator('//span[contains(text(), "Тарифы")]')).to_be_visible()
    expect(page.get_by_role("heading", name="Тарифные планы интернет-провайдера Ростелеком в Москве")).to_be_visible()
    expect(page.locator('(//div[contains(text(), "Оставить заявку")])[2]')).to_be_visible()
    expect(page.locator("#provider_banner").get_by_text("Подключение")).to_be_visible()
    expect(page.get_by_role("link", name="+7 (499) 372-33-55")).to_be_visible()
    expect(page.locator("#provider_banner").get_by_text("Техподдержка")).to_be_visible()
    expect(page.get_by_role("link", name="+7 (800) 100-08-00")).to_be_visible()
    expect(page.get_by_text("Проверить доступность Ростелеком по адресу")).to_be_visible()
    search_tariffs(page)
    expect(page.get_by_role("link", name="О провайдере")).to_be_visible()
    expect(page.locator('(//a[contains(text(), "Тарифы")])[3]')).to_be_visible()
    expect(page.get_by_role("link", name="акции", exact=True)).to_be_visible()
    check_provider_rostel_tags(page)
    sorting_providers_rates(page)
    for i in range(1, 15):
        expect(page.locator(f'(//div[@datatest="providers_form_inspect_connect_tariff_button"])[{i}]')).to_be_visible()
    for i in range(1, 4):
        expect(page.locator(f'(//a[@aria-label="Переключить страницу"])[{i}]')).to_be_visible()


def test_provider_onlime_rostelecom(page: Page):
    page.goto('https://101internet.ru/moskva/providers/onlime/rates/internet-i-mobilnaya-svyaz')
    check_header(page)
    check_footer(page)
    check_header_moscow(page)
    expect(page.get_by_role("link", name="Подключить интернет")).to_be_visible()
    expect(page.get_by_role("link", name="Провайдеры Москвы")).to_be_visible()
    expect(page.locator('//span[contains(text(), "Онлайм")]')).to_be_visible()
    expect(page.locator('//span[contains(text(), "Тарифы")]')).to_be_visible()
    expect(page.locator('//span[contains(text(), "Интернет и мобильная связь")]')).to_be_visible()
    expect(page.get_by_role("heading", name="Тарифы Онлайм на домашний интернет и мобильную связь в Москве")).to_be_visible()
    expect(page.locator('//img[@alt="Лого провайдера"]')).to_be_visible()
    expect(page.locator('(//div[contains(text(), "Оставить заявку")])[2]')).to_be_visible()
    expect(page.locator("#provider_banner").get_by_text("Подключение")).to_be_visible()
    expect(page.get_by_role("link", name="+7 (499) 372-33-55")).to_be_visible()
    expect(page.locator("#provider_banner").get_by_text("Техподдержка")).to_be_visible()
    expect(page.get_by_role("link", name="+7 (800) 707-12-12")).to_be_visible()
    expect(page.get_by_text("Проверить доступность Онлайм по адресу")).to_be_visible()
    expect(page.locator('//span[contains(text(), "Провайдер объединился с компанией ")]')).to_be_visible()
    search_tariffs(page)
    expect(page.get_by_role("link", name="О провайдере")).to_be_visible()
    expect(page.locator('(//a[contains(text(), "Тарифы")])[3]')).to_be_visible()
    expect(page.get_by_role("link", name="акции", exact=True)).to_be_visible()
    check_provider_onlime_tags(page)
    expect(page.locator('//div[contains(text(), "Район")]')).to_be_visible()
    expect(page.locator('//input[@datatest="providers_input_filter_district"]')).to_be_visible()
    expect(page.locator('//div[contains(text(), "Сортировка")]')).to_be_visible()
    expect(page.locator('//input[@value="Сначала популярные "]')).to_be_visible()
    for i in range(1, 8):
        expect(page.locator(f'(//div[@datatest="button_form_inspect_connect_tariff_tag_button"])[{i}]')).to_be_visible()
    expect(page.locator('(//div[contains(text(), "Оставить заявку")])[2]')).to_be_visible()
    expect(page.locator('//h2')).to_be_visible()


def test_provider_mts_home(page: Page):
    page.goto('https://101internet.ru/moskva/providers/mts-home')
    check_header(page)
    check_footer(page)
    check_header_moscow(page)
    expect(page.get_by_role("link", name="Подключить интернет")).to_be_visible()
    expect(page.get_by_role("link", name="Провайдеры Москвы")).to_be_visible()
    expect(page.locator('(//span[contains(text(), "МТС Home")])[1]')).to_be_visible()
    expect(page.get_by_role("heading", name="МТС Home (MTS Home) — интернет-провайдер Москвы")).to_be_visible()
    expect(page.locator('//img[@alt="Лого провайдера"]')).to_be_visible()
    expect(page.locator('(//div[contains(text(), "Оставить заявку")])[2]')).to_be_visible()
    expect(page.locator("#provider_banner").get_by_text("Подключение")).to_be_visible()
    expect(page.get_by_role("link", name="+7 (495) 106-82-09")).to_be_visible()
    expect(page.locator("#provider_banner").get_by_text("Техподдержка")).to_be_visible()
    expect(page.get_by_text("Проверить доступность МТС Home по адресу")).to_be_visible()
    search_tariffs(page)
    expect(page.get_by_role("link", name="О провайдере")).to_be_visible()
    expect(page.locator('(//a[contains(text(), "Тарифы")])[3]')).to_be_visible()
    expect(page.get_by_role("link", name="акции", exact=True)).to_be_visible()
    expect(page.locator('(//div[contains(text(), "Тарифы")])[1]')).to_be_visible()
    expect(page.locator('(//a[contains(text(), "Все тарифы")])[1]')).to_be_visible()
    for i in range(1, 5):
        expect(page.locator(f'(//div[@datatest="providers_form_inspect_connect_tariff_button"])[{i}]')).to_be_visible()
    expect(page.locator('(//div[contains(text(), "Оставить заявку")])[2]')).to_be_visible()
    expect(page.locator('//div[@data-test="countRates"]')).to_be_visible()
    expect(page.locator('//div[contains(text(), "Отзывы наших клиентов")]')).to_be_visible()
    for i in range(1, 4):
        expect(page.locator(f'(//div[@itemtype="https://schema.org/Review"])[{i}]')).to_be_visible()
    expect(page.locator('(//a[contains(text(), "все отзывы")])[2]')).to_be_visible()
    expect(page.locator('//div[@itemtype="http://schema.org/Organization"]')).to_be_visible()
    expect(page.locator('//span[contains(text(), "контакты")]')).to_be_visible()
    expect(page.locator('//h2')).to_be_visible()


def test_provider_mts_rostelecom_tv_mib(page: Page):
    page.goto('https://101internet.ru/moskva/providers/mts-home/rates/internet-tv-mobile')
    check_header(page)
    check_footer(page)
    check_header_moscow(page)
    expect(page.get_by_role("link", name="Подключить интернет")).to_be_visible()
    expect(page.get_by_role("link", name="Провайдеры Москвы")).to_be_visible()
    expect(page.locator('//span[contains(text(), "МТС Home")]')).to_be_visible()
    expect(page.locator('//span[contains(text(), "Тарифы")]')).to_be_visible()
    expect(page.locator('//span[contains(text(), "Интернет+тв+мобильная связь")]')).to_be_visible()
    expect(page.get_by_role("heading", name="Тарифы МТС Home на интернет, ТВ и мобильную связь в Москве")).to_be_visible()
    expect(page.locator('//img[@alt="Лого провайдера"]')).to_be_visible()
    expect(page.locator('(//div[contains(text(), "Оставить заявку")])[2]')).to_be_visible()
    expect(page.locator("#provider_banner").get_by_text("Подключение")).to_be_visible()
    expect(page.get_by_role("link", name="+7 (495) 106-82-09")).to_be_visible()
    expect(page.locator("#provider_banner").get_by_text("Техподдержка")).to_be_visible()
    expect(page.get_by_text("Проверить доступность МТС Home по адресу")).to_be_visible()
    search_tariffs(page)
    expect(page.get_by_role("link", name="О провайдере")).to_be_visible()
    expect(page.locator('(//a[contains(text(), "Тарифы")])[3]')).to_be_visible()
    expect(page.get_by_role("link", name="акции", exact=True)).to_be_visible()
    expect(page.locator('(//a[@href="/moskva/providers/mts-home/rates/internet-tv-mobile"])[1]')).to_be_visible()
    expect(page.locator('(//a[@href="/moskva/providers/mts-home/rates/domashnij-internet"])[1]')).to_be_visible()
    expect(
        page.locator('(//a[@href="/moskva/providers/mts-home/rates/nedorogoj-domashnij-internet"])[1]')).to_be_visible()
    expect(page.locator('(//a[@href="/moskva/providers/mts-home/rates/online-kinoteatr"])[1]')).to_be_visible()
    expect(page.locator('//div[contains(text(), "Сортировка")]')).to_be_visible()
    expect(page.locator('//input[@value="Сначала популярные "]')).to_be_visible()
    for i in range(1, 8):
        expect(page.locator(f'(//div[@datatest="button_form_inspect_connect_tariff_tag_button"])[{i}]')).to_be_visible()
    expect(page.locator('(//div[contains(text(), "Оставить заявку")])[2]')).to_be_visible()
    expect(page.locator('//h2')).to_be_visible()


def test_provider_mts_rostelecom_internet_tv(page: Page):
    page.goto('https://101internet.ru/moskva/providers/mts-home/rates/internet-i-tv')
    check_header(page)
    check_footer(page)
    check_header_moscow(page)
    expect(page.get_by_role("link", name="Подключить интернет")).to_be_visible()
    expect(page.get_by_role("link", name="Провайдеры Москвы")).to_be_visible()
    expect(page.locator('//span[contains(text(), "МТС Home")]')).to_be_visible()
    expect(page.locator('//span[contains(text(), "Тарифы")]')).to_be_visible()
    expect(page.locator('//span[contains(text(), "Интернет+тв")]')).to_be_visible()
    expect(page.get_by_role("heading", name="Тарифы МТС Home на интернет и телевидение в Москве")).to_be_visible()
    expect(page.locator('//img[@alt="Лого провайдера"]')).to_be_visible()
    expect(page.locator('(//div[contains(text(), "Оставить заявку")])[2]')).to_be_visible()
    expect(page.locator("#provider_banner").get_by_text("Подключение")).to_be_visible()
    expect(page.get_by_role("link", name="+7 (495) 106-82-09")).to_be_visible()
    expect(page.locator("#provider_banner").get_by_text("Техподдержка")).to_be_visible()
    expect(page.get_by_text("Проверить доступность МТС Home по адресу")).to_be_visible()
    search_tariffs(page)
    expect(page.get_by_role("link", name="О провайдере")).to_be_visible()
    expect(page.locator('(//a[contains(text(), "Тарифы")])[3]')).to_be_visible()
    expect(page.get_by_role("link", name="акции", exact=True)).to_be_visible()
    expect(page.locator('(//a[@href="/moskva/providers/mts-home/rates/internet-tv-mobile"])[1]')).to_be_visible()
    expect(page.locator('(//a[@href="/moskva/providers/mts-home/rates/domashnij-internet"])[1]')).to_be_visible()
    expect(
        page.locator('(//a[@href="/moskva/providers/mts-home/rates/nedorogoj-domashnij-internet"])[1]')).to_be_visible()
    expect(page.locator('(//a[@href="/moskva/providers/mts-home/rates/online-kinoteatr"])[1]')).to_be_visible()
    expect(page.locator('//div[contains(text(), "Сортировка")]')).to_be_visible()
    expect(page.locator('//input[@value="Сначала популярные "]')).to_be_visible()
    ooops_stub(page)
    expect(page.locator('(//div[contains(text(), "Оставить заявку")])[2]')).to_be_visible()
    expect(page.locator('//h2')).to_be_visible()


def test_provider_mts_online_kinoteatr(page: Page):
    page.goto('https://101internet.ru/moskva/providers/mts-home/rates/online-kinoteatr')
    check_header(page)
    check_footer(page)
    check_header_moscow(page)
    expect(page.get_by_role("link", name="Подключить интернет")).to_be_visible()
    expect(page.get_by_role("link", name="Провайдеры Москвы")).to_be_visible()
    expect(page.locator('//span[contains(text(), "МТС Home")]')).to_be_visible()
    expect(page.locator('//span[contains(text(), "Тарифы")]')).to_be_visible()
    expect(page.locator('//span[contains(text(), "Онлайн-кинотеатр")]')).to_be_visible()
    expect(page.get_by_role("heading", name="Тарифы домашнего интернета МТС Home с подпиской на онлайн-кинотеатр в Москве")).to_be_visible()
    expect(page.locator('//img[@alt="Лого провайдера"]')).to_be_visible()
    expect(page.locator('(//div[contains(text(), "Оставить заявку")])[2]')).to_be_visible()
    expect(page.locator("#provider_banner").get_by_text("Подключение")).to_be_visible()
    expect(page.get_by_role("link", name="+7 (495) 106-82-09")).to_be_visible()
    expect(page.locator("#provider_banner").get_by_text("Техподдержка")).to_be_visible()
    expect(page.get_by_text("Проверить доступность МТС Home по адресу")).to_be_visible()
    search_tariffs(page)
    expect(page.get_by_role("link", name="О провайдере")).to_be_visible()
    expect(page.locator('(//a[contains(text(), "Тарифы")])[3]')).to_be_visible()
    expect(page.get_by_role("link", name="акции", exact=True)).to_be_visible()
    expect(page.locator('(//a[@href="/moskva/providers/mts-home/rates/internet-tv-mobile"])[1]')).to_be_visible()
    expect(page.locator('(//a[@href="/moskva/providers/mts-home/rates/domashnij-internet"])[1]')).to_be_visible()
    expect(
        page.locator('(//a[@href="/moskva/providers/mts-home/rates/nedorogoj-domashnij-internet"])[1]')).to_be_visible()
    expect(page.locator('(//a[@href="/moskva/providers/mts-home/rates/online-kinoteatr"])[1]')).to_be_visible()
    expect(page.locator('//div[contains(text(), "Сортировка")]')).to_be_visible()
    expect(page.locator('//input[@value="Сначала популярные "]')).to_be_visible()
    for i in range(1, 15):
        expect(page.locator(f'(//div[@datatest="providers_form_inspect_connect_tariff_button"])[{i}]')).to_be_visible()
    expect(page.locator('(//div[contains(text(), "Оставить заявку")])[2]')).to_be_visible()
    expect(page.locator('//h2')).to_be_visible()


def test_provider_mts_rates_nedorogoi(page: Page):
    page.goto('https://101internet.ru/moskva/providers/mts-home/rates/nedorogoj-domashnij-internet')
    check_header(page)
    check_footer(page)
    check_header_moscow(page)
    expect(page.get_by_role("link", name="Подключить интернет")).to_be_visible()
    expect(page.get_by_role("link", name="Провайдеры Москвы")).to_be_visible()
    expect(page.locator('//span[contains(text(), "МТС Home")]')).to_be_visible()
    expect(page.locator('//span[contains(text(), "Тарифы")]')).to_be_visible()
    expect(page.locator('//span[contains(text(), "Дешевый интернет")]')).to_be_visible()
    expect(page.get_by_role("heading", name="Выгодные тарифы МТС Home на интернет в Москве")).to_be_visible()
    expect(page.locator('//img[@alt="Лого провайдера"]')).to_be_visible()
    expect(page.locator('(//div[contains(text(), "Оставить заявку")])[2]')).to_be_visible()
    expect(page.locator("#provider_banner").get_by_text("Подключение")).to_be_visible()
    expect(page.get_by_role("link", name="+7 (495) 106-82-09")).to_be_visible()
    expect(page.locator("#provider_banner").get_by_text("Техподдержка")).to_be_visible()
    expect(page.get_by_text("Проверить доступность МТС Home по адресу")).to_be_visible()
    search_tariffs(page)
    expect(page.get_by_role("link", name="О провайдере")).to_be_visible()
    expect(page.locator('(//a[contains(text(), "Тарифы")])[3]')).to_be_visible()
    expect(page.get_by_role("link", name="акции", exact=True)).to_be_visible()
    expect(page.locator('(//a[@href="/moskva/providers/mts-home/rates/internet-tv-mobile"])[1]')).to_be_visible()
    expect(page.locator('(//a[@href="/moskva/providers/mts-home/rates/domashnij-internet"])[1]')).to_be_visible()
    expect(
        page.locator('(//a[@href="/moskva/providers/mts-home/rates/nedorogoj-domashnij-internet"])[1]')).to_be_visible()
    expect(page.locator('(//a[@href="/moskva/providers/mts-home/rates/online-kinoteatr"])[1]')).to_be_visible()
    expect(page.locator('//div[contains(text(), "Сортировка")]')).to_be_visible()
    expect(page.locator('//input[@value="Сначала популярные "]')).to_be_visible()
    for i in range(1, 12):
        expect(page.locator(f'(//div[@datatest="providers_form_inspect_connect_tariff_button"])[{i}]')).to_be_visible()
    expect(page.locator('(//div[contains(text(), "Оставить заявку")])[2]')).to_be_visible()
    expect(page.locator('//h2')).to_be_visible()


def test_provider_onlime(page: Page):
    page.goto('https://101internet.ru/moskva/providers/onlime/rates')
    check_header(page)
    check_footer(page)
    check_header_moscow(page)
    expect(page.get_by_role("link", name="Подключить интернет")).to_be_visible()
    expect(page.get_by_role("link", name="Провайдеры Москвы")).to_be_visible()
    expect(page.locator('//span[contains(text(), "Онлайм")]')).to_be_visible()
    expect(page.locator('//span[contains(text(), "Тарифы")]')).to_be_visible()
    expect(page.get_by_role("heading", name="Тарифные планы интернет-провайдера Онлайм в Москве")).to_be_visible()
    expect(page.locator('(//div[contains(text(), "Оставить заявку")])[2]')).to_be_visible()
    expect(page.locator("#provider_banner").get_by_text("Подключение")).to_be_visible()
    expect(page.get_by_role("link", name="+7 (499) 372-33-55")).to_be_visible()
    expect(page.locator("#provider_banner").get_by_text("Техподдержка")).to_be_visible()
    expect(page.get_by_role("link", name="+7 (800) 707-12-12")).to_be_visible()
    expect(page.locator('//span[contains(text(), "Провайдер объединился с компанией ")]')).to_be_visible()
    expect(page.get_by_text("Проверить доступность Онлайм по адресу")).to_be_visible()
    search_tariffs(page)
    expect(page.get_by_role("link", name="О провайдере")).to_be_visible()
    expect(page.locator('(//a[contains(text(), "Тарифы")])[3]')).to_be_visible()
    expect(page.get_by_role("link", name="акции", exact=True)).to_be_visible()
    sorting_providers_rates(page)
    check_provider_onlime_tags(page)
    for i in range(1, 15):
        expect(page.locator(f'(//div[@datatest="providers_form_inspect_connect_tariff_button"])[{i}]')).to_be_visible()
    expect(page.locator('(//div[contains(text(), "Оставить заявку")])[2]')).to_be_visible()
    for i in range(1, 4):
        expect(page.locator(f'(//a[@aria-label="Переключить страницу"])[{i}]')).to_be_visible()


def test_provider_mts(page: Page):
    page.goto('https://101internet.ru/moskva/rating/mts')
    check_header(page)
    check_footer(page)
    check_header_moscow(page)
    expect(page.get_by_role("link", name="Подключить интернет")).to_be_visible()
    expect(page.get_by_role("link", name="Провайдеры Москвы")).to_be_visible()
    expect(page.locator('//span[contains(text(), "МТС")]')).to_be_visible()
    expect(page.locator('//span[contains(text(), "Отзывы")]')).to_be_visible()
    expect(page.get_by_role("heading", name="Отзывы о домашнем интернете МТС в Москве")).to_be_visible()
    expect(page.locator('//img[@alt="Лого провайдера"]')).to_be_visible()
    expect(page.locator('(//div[contains(text(), "Оставить заявку")])[2]')).to_be_visible()
    expect(page.locator("#provider_banner").get_by_text("Подключение")).to_be_visible()
    expect(page.get_by_role("link", name="+7 (495) 106-82-09")).to_be_visible()
    expect(page.locator("#provider_banner").get_by_text("Техподдержка")).to_be_visible()
    expect(page.get_by_role("link", name="+7 (800) 250-08-90")).to_be_visible()
    expect(page.get_by_text("Проверить доступность МТС по адресу")).to_be_visible()
    search_tariffs(page)
    expect(page.get_by_role("link", name="О провайдере")).to_be_visible()
    expect(page.locator('(//a[contains(text(), "Тарифы")])[3]')).to_be_visible()
    expect(page.get_by_role("link", name="акции", exact=True)).to_be_visible()
    expect(page.locator('//div[contains(text(), "Полезные")]')).to_be_visible()
    expect(page.locator('//div[contains(text(), "Новые")]')).to_be_visible()
    expect(page.locator('//div[contains(text(), "Старые")]')).to_be_visible()
    expect(page.locator('//a[contains(text(), "оставить отзыв")]')).to_be_visible()
    for i in range(1, 10):
        expect(page.locator(f'(//div[@itemprop="review"])[{i}]')).to_be_visible()
    for i in range(1, 10):
        expect(page.locator(f'(//textarea[@aria-labelledby="label"])[{i}]')).to_be_visible()
    for i in range(1, 10):
        expect(page.locator(f'(//button[@aria-label="Оставить отзыв"])[{i}]')).to_be_visible()
    expect(page.locator('(//div[contains(text(), "Лучшие тарифы МТС в Москве")])[1]')).to_be_visible()
    for i in range(1, 3):
        expect(page.locator(f'(//span[contains(text(), "Подключить по акции")])[{i}]')).to_be_visible()
    expect(page.locator('(//div[contains(text(), "Оставить заявку")])[2]')).to_be_visible()
    for i in range(1, 5):
        expect(page.locator(f'(//a[@aria-label="Переключить страницу"])[{i}]')).to_be_visible()
    expect(page.locator('//h2')).to_be_visible()


def test_provider_mts2(page: Page):
    page.goto('https://101internet.ru/moskva/rating/mts/2')
    check_header(page)
    check_footer(page)
    check_header_moscow(page)
    expect(page.get_by_role("link", name="Подключить интернет")).to_be_visible()
    expect(page.get_by_role("link", name="Провайдеры Москвы")).to_be_visible()
    expect(page.locator('//span[contains(text(), "МТС")]')).to_be_visible()
    expect(page.locator('//span[contains(text(), "Отзывы")]')).to_be_visible()
    expect(page.get_by_role("heading", name="Отзывы о провайдере МТС (MTS) в Москве")).to_be_visible()
    expect(page.locator('//img[@alt="Лого провайдера"]')).to_be_visible()
    expect(page.locator('(//div[contains(text(), "Оставить заявку")])[2]')).to_be_visible()
    expect(page.locator("#provider_banner").get_by_text("Подключение")).to_be_visible()
    expect(page.get_by_role("link", name="+7 (495) 106-82-09")).to_be_visible()
    expect(page.locator("#provider_banner").get_by_text("Техподдержка")).to_be_visible()
    expect(page.get_by_role("link", name="+7 (800) 250-08-90")).to_be_visible()
    expect(page.get_by_text("Проверить доступность МТС по адресу")).to_be_visible()
    search_tariffs(page)
    expect(page.get_by_role("link", name="О провайдере")).to_be_visible()
    expect(page.locator('(//a[contains(text(), "Тарифы")])[3]')).to_be_visible()
    expect(page.get_by_role("link", name="акции", exact=True)).to_be_visible()
    expect(page.locator('//div[contains(text(), "Полезные")]')).to_be_visible()
    expect(page.locator('//div[contains(text(), "Новые")]')).to_be_visible()
    expect(page.locator('//div[contains(text(), "Старые")]')).to_be_visible()
    expect(page.locator('//a[contains(text(), "оставить отзыв")]')).to_be_visible()
    for i in range(1, 10):
        expect(page.locator(f'(//div[@itemprop="review"])[{i}]')).to_be_visible()
    for i in range(1, 10):
        expect(page.locator(f'(//textarea[@aria-labelledby="label"])[{i}]')).to_be_visible()
    for i in range(1, 10):
        expect(page.locator(f'(//button[@aria-label="Оставить отзыв"])[{i}]')).to_be_visible()
    expect(page.locator('(//div[contains(text(), "Лучшие тарифы МТС в Москве")])[1]')).to_be_visible()
    for i in range(1, 3):
        expect(page.locator(f'(//span[contains(text(), "Подключить по акции")])[{i}]')).to_be_visible()
    expect(page.locator('(//div[contains(text(), "Оставить заявку")])[2]')).to_be_visible()
    for i in range(1, 5):
        expect(page.locator(f'(//a[@aria-label="Переключить страницу"])[{i}]')).to_be_visible()


def test_provider_akado(page: Page):
    page.goto('https://101internet.ru/moskva/providers/actions/akado')
    check_header(page)
    check_footer(page)
    check_header_moscow(page)
    expect(page.get_by_role("link", name="Подключить интернет")).to_be_visible()
    expect(page.get_by_role("link", name="Провайдеры Москвы")).to_be_visible()
    expect(page.locator('//span[contains(text(), "Акадо")]')).to_be_visible()
    expect(page.locator('//span[contains(text(), "Акции")]')).to_be_visible()
    expect(page.get_by_role("heading", name="Акции интернет-провайдера Акадо в Москве")).to_be_visible()
    expect(page.locator('//img[@alt="Лого провайдера"]')).to_be_visible()
    expect(page.locator("#provider_banner").get_by_text("Подключение")).to_be_visible()
    expect(page.get_by_role("link", name="+7 (495) 487-07-28")).to_be_visible()
    expect(page.locator("#provider_banner").get_by_text("Техподдержка")).to_be_visible()
    expect(page.get_by_role("link", name="+7 (499) 940-00-00")).to_be_visible()
    expect(page.get_by_text("Проверить доступность Акадо по адресу")).to_be_visible()
    search_tariffs(page)
    expect(page.get_by_role("link", name="О провайдере")).to_be_visible()
    expect(page.locator('(//a[contains(text(), "Тарифы")])[3]')).to_be_visible()
    expect(page.get_by_role("link", name="акции", exact=True)).to_be_visible()
    expect(page.locator('//h2')).to_be_visible()
    expect(page.locator('//h2')).to_be_visible()
    expect(page.locator('//div[contains(text(), "Сортировка")]')).to_be_visible()
    expect(page.locator('//input[@value="Сначала популярные "]')).to_be_visible()
    for i in range(1, 5):
        expect(page.locator(f'(//span[contains(text(), "Подключить по акции")])[{i}]')).to_be_visible()


def test_provider_mgts(page: Page):
    page.goto('https://101internet.ru/moskva/providers/actions/mgts')
    check_header(page)
    check_footer(page)
    check_header_moscow(page)
    expect(page.get_by_role("link", name="Подключить интернет")).to_be_visible()
    expect(page.get_by_role("link", name="Провайдеры Москвы")).to_be_visible()
    expect(page.locator('//span[contains(text(), "МГТС")]')).to_be_visible()
    expect(page.locator('//span[contains(text(), "Акции")]')).to_be_visible()
    expect(page.get_by_role("heading", name="Акции интернет-провайдера МГТС в Москве")).to_be_visible()
    expect(page.locator('//img[@alt="Лого провайдера"]')).to_be_visible()
    expect(page.locator("#provider_banner").get_by_text("Подключение")).to_be_visible()
    expect(page.get_by_role("link", name="+7 (495) 106-82-09")).to_be_visible()
    expect(page.locator("#provider_banner").get_by_text("Техподдержка")).to_be_visible()
    expect(page.get_by_text("Проверить доступность МГТС по адресу")).to_be_visible()
    expect(page.locator('//span[contains(text(), "Провайдер объединился с компанией ")]')).to_be_visible()
    search_tariffs(page)
    expect(page.get_by_role("link", name="О провайдере")).to_be_visible()
    expect(page.locator('(//a[contains(text(), "Тарифы")])[3]')).to_be_visible()
    expect(page.get_by_role("link", name="акции", exact=True)).to_be_visible()
    expect(page.locator('//div[contains(text(), "Сортировка")]')).to_be_visible()
    expect(page.locator('//input[@value="Сначала популярные "]')).to_be_visible()
    expect(page.locator('//h2')).to_be_visible()
    for i in range(1, 16):
        expect(page.locator(f'(//span[contains(text(), "Подключить сегодня 🔥")])[{i}]')).to_be_visible()
    expect(page.locator('(//div[contains(text(), "Оставить заявку")])[2]')).to_be_visible()


def test_provider_rinet(page: Page):
    page.goto('https://101internet.ru/moskva/providers/actions/rinet')
    check_header(page)
    check_footer(page)
    check_header_moscow(page)
    expect(page.get_by_role("link", name="Подключить интернет")).to_be_visible()
    expect(page.get_by_role("link", name="Провайдеры Москвы")).to_be_visible()
    expect(page.locator('//span[contains(text(), "Ринет | Дом.ру")]')).to_be_visible()
    expect(page.locator('//span[contains(text(), "Акции")]')).to_be_visible()
    expect(page.get_by_role("heading", name="Акции интернет-провайдера Ринет | Дом.ру в Москве")).to_be_visible()
    expect(page.locator('//img[@alt="Лого провайдера"]')).to_be_visible()
    expect(page.locator("#provider_banner").get_by_text("Подключение")).to_be_visible()
    expect(page.get_by_role("link", name="+7 (495) 152-39-29")).to_be_visible()
    expect(page.locator("#provider_banner").get_by_text("Техподдержка")).to_be_visible()
    expect(page.get_by_role("link", name="+7 (495) 981-45-71")).to_be_visible()
    expect(page.get_by_text("Проверить доступность Ринет | Дом.ру по адресу")).to_be_visible()
    expect(page.locator('//span[contains(text(), "Провайдер объединился с компанией ")]')).to_be_visible()
    search_tariffs(page)
    expect(page.get_by_role("link", name="О провайдере")).to_be_visible()
    expect(page.locator('(//a[contains(text(), "Тарифы")])[3]')).to_be_visible()
    expect(page.get_by_role("link", name="акции", exact=True)).to_be_visible()
    expect(page.locator('//div[contains(text(), "Сортировка")]')).to_be_visible()
    expect(page.locator('//input[@value="Сначала популярные "]')).to_be_visible()
    expect(page.locator('//h2')).to_be_visible()
    for i in range(1, 16):
        expect(page.locator(f'(//span[contains(text(), "Подключить по акции")])[{i}]')).to_be_visible()


def test_moskva_actions(page: Page):
    page.goto('https://101internet.ru/moskva/actions')
    check_header(page)
    check_footer(page)
    check_header_moscow(page)
    expect(page.get_by_role("link", name="Подключить интернет")).to_be_visible()
    expect(page.locator('//span[contains(text(), "Акции на домашний интернет")]')).to_be_visible()
    expect(page.locator('//h1')).to_be_visible()
    expect(page.locator('//div[contains(text(), "Сортировка")]')).to_be_visible()
    expect(page.locator('//input[@value="Сначала популярные "]')).to_be_visible()
    expect(page.locator('//h2')).to_be_visible()
    for i in range(2, 22):
        expect(page.locator(f'(//span[contains(text(), "Подключить")])[{i}]')).to_be_visible()


def test_moskva_actions2(page: Page):
    page.goto('https://101internet.ru/moskva/actions/2')
    check_header(page)
    check_footer(page)
    check_header_moscow(page)
    expect(page.get_by_role("link", name="Подключить интернет")).to_be_visible()
    expect(page.locator('//span[contains(text(), "Акции на домашний интернет")]')).to_be_visible()
    expect(page.locator('//h1')).to_be_visible()
    expect(page.locator('//div[contains(text(), "Сортировка")]')).to_be_visible()
    expect(page.locator('//input[@value="Сначала популярные "]')).to_be_visible()
    expect(page.locator('//h2')).to_be_visible()
    for i in range(2, 22):
        expect(page.locator(f'(//span[contains(text(), "Подключить")])[{i}]')).to_be_visible()


def test_moskva_terms_of_use(page: Page):
    page.goto('https://101internet.ru/moskva/about/terms-of-use')
    check_header(page)
    check_footer(page)
    check_header_moscow(page)
    terms_of_use(page)


def test_moskva_personal_data(page: Page):
    page.goto('https://101internet.ru/moskva/about/personal-data')
    check_header(page)
    check_footer(page)
    check_header_moscow(page)
    personal_data(page)


def test_moskva_contact_feedback(page: Page):
    page.goto('https://101internet.ru/moskva/contact-feedback')
    contact_feedback(page)


