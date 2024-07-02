from playwright.sync_api import Page, expect
from pages.main_page import check_header, search_tariffs, one_click_form, tariffs_block, blue_form
from pages.main_page import check_footer, blue_form_second, search_tariffs_second, sorting
from pages.main_site_pages.moscow_page import check_header_moscow, check_tags


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


