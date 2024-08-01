import allure
import pytest
from playwright.sync_api import Page, expect
from time import sleep


@allure.step("Проверка хедера")
def check_header(page: Page):
    page.locator('(//a[@datatest="main_internet_button"])[1]').click()
    page.get_by_role("link", name="Подключить интернет").click()
    page.get_by_role("link", name="провайдеры", exact=True).click()
    page.get_by_role("link", name="Подключить интернет").click()
    page.get_by_role("link", name="рейтинг", exact=True).click()
    page.get_by_role("link", name="Подключить интернет").click()
    page.get_by_role("link", name="Тарифы", exact=True).click()
    page.get_by_role("link", name="Подключить интернет").click()
    page.locator('(//a[contains(text(), "Интернет в офис")])[1]').click()


@allure.step("Проверка футера")
def check_footer(page: Page):
    page.get_by_role("link", name="О нас").click()
    page.get_by_role("link", name="Подключить интернет").click()
    page.get_by_role("link", name="Оплата и гарантии").click()
    page.get_by_role("link", name="Подключить интернет").click()
    page.locator('//a[contains(text(), "Сотрудничество")]').click()
    page.goBack()
    page.get_by_role("link", name="Документы").click()
    page.get_by_role("contentinfo").locator("li").filter(has_text="Политика обработки персональных данных").click()
    page.get_by_role("link", name="Карта сайта").click()


@allure.step("Проверка раздела карьера в футере")
def check_footer_career(page: Page):
    page.goto('https://101internet.ru/abakan')
    page.get_by_role("link", name="Карьера").click()


@allure.step("Проверка раздела блог в футере")
def check_footer_blog(page: Page):
    page.goto('https://101internet.ru/abakan')
    page.get_by_role("link", name="Блог").click()


@allure.step("Проверка раздела отзывы о компании в футере")
def check_footer_rewievs(page: Page):
    page.goto('https://101internet.ru/abakan')
    page.get_by_role("link", name="Отзывы о компании").click()


@allure.step("Проверка верхнего футера")
def check_top_footer(page: Page):
    page.locator('//a[contains(text(), "Домашний интернет")]').click()
    page.get_by_role("link", name="Интернет+ТВ", exact=True).click()
    page.get_by_role("link", name="Интернет+ТВ+мобильная связь", exact=True).click()
    page.get_by_role("link", name="Интернет+мобильная связь").click()
    page.get_by_role("link", name="Онлайн-кинотеатры").click()
    page.locator('(//a[contains(text(), "Поиск по адресу")])[3]').click()
    page.get_by_text("Мобильная связь", exact=True).click()
    page.get_by_role("link", name="Безлимитный интернет").click()
    page.get_by_role("link", name="Роуминг за границей").click()
    page.get_by_role("link", name="Перенос номера").click()
    page.get_by_role("link", name="ESIM", exact=True).click()
    page.get_by_role("link", name="Все тарифы").click()
    page.get_by_role("link", name="МТС", exact=True).first.click()
    page.locator('(//a[contains(text(), "Ростелеком")])[2]').click()
    page.get_by_role("link", name="билайн").first.click()
    page.get_by_role("link", name="Дом.ру").click()
    page.get_by_role("link", name="МегаФон").nth(2).click()
    page.get_by_role("link", name="Все провайдеры").click()
    page.get_by_role("link", name="МТС").nth(3).click()
    page.get_by_role("link", name="Тинькофф Мобайл").click()
    page.get_by_role("link", name="Йота").click()
    page.get_by_role("link", name="билайн").nth(1).click()
    page.get_by_role("link", name="Теле2").click()
    page.get_by_role("link", name="СберМобайл").click()
    page.get_by_role("link", name="МегаФон").nth(1).click()
    page.get_by_role("link", name="Все операторы").click()
    page.get_by_role("link", name="Карта покрытия").click()
    page.get_by_role("link", name="Отзывы о провайдерах").click()
    page.get_by_role("link", name="Рейтинг провайдеров").click()
    page.get_by_role("link", name="Акции провайдеров").click()
    page.get_by_role("link", name="Бесплатные").click()
    page.get_by_role("link", name="Бронзовые").click()
    page.get_by_role("link", name="Серебряные").click()
    page.get_by_role("link", name="Золотые").click()
    page.get_by_role("link", name="Все номера").click()
    page.locator('(//a[contains(text(), "Интернет в офис")])[4]').click()
    page.locator('//a[contains(text(), "Интернет на дачу")]').click()


@allure.step("Проверка элементов на главной странице")
def check_maim_page(page: Page):
    page.locator('//div[@datatest="main_raitingprovider_button"]').click()
    page.locator('//span[contains(text(), "Подключить интернет")]').click()
    page.locator('//div[contains(text(), "Выгодные пакеты интернета")]').click()
    page.locator('//span[contains(text(), "Подключить интернет")]').click()
    page.locator('//div[@datatest="main_inflat_button"]').click()
    page.locator('//span[contains(text(), "Подключить интернет")]').click()
    page.locator('//div[@datatest="main_inhouse_button"]').click()
    page.locator("#HeaderMenu").get_by_role("link", name="/abakan").click()
    page.locator('//div[@datatest="main_inoffice_button"]').click()
    page.locator("#HeaderMenu").get_by_role("link", name="/abakan").click()
    page.get_by_role("link", name="Показать все").click()
    page.locator('//span[contains(text(), "Подключить интернет")]').click()
    page.locator('//span[contains(text(), "Согласие")]').click()
    page.get_by_text("Закрыть").click()
    page.locator('//span[contains(text(), "Политикой")]').click()
    page.get_by_text("Закрыть").click()
    page.get_by_role("link", name="оставить отзыв").click()
    page.locator('(//div[@class="container"]//span)[1]').click()
    page.get_by_role("link", name="все отзывы").click()
    page.locator('//span[contains(text(), "Подключить интернет")]').click()
    page.locator('(//span[contains(text(), "Ростелеком")])[1]').click()
    page.locator('//span[contains(text(), "Подключить интернет")]').click()


@allure.step("Проверка блока с тарифами и попапа на главной странице")
def check_tariff(page: Page):
    page.get_by_text("Подключить по акции").first.click()
    expect(page.locator('//input[@datatest="popup_tariff_order_input_tel"]')).to_be_visible()
    expect(page.locator('[data-test="popup_tariff_order_form_input_connect_button"]')).to_be_visible()
    expect(page.get_by_text("Телефон", exact=True)).to_be_visible()
    expect(page.get_by_text("Мобильный телефон")).to_be_visible()
    expect(page.get_by_text(
        'Нажимая на кнопку "Оставить заявку", вы даёте Согласие на обработку персональных')).to_be_visible()


@allure.step("Проверка блока с тарифами и попапа на странице поиск по адресу")
def check_tariff_to_home(page: Page):
    page.locator('[data-test="countRates"]').get_by_text("Подключить").first.click()
    expect(page.locator('//input[@datatest="popup_tariff_order_input_tel"]')).to_be_visible()
    expect(page.locator('[data-test="popup_tariff_order_form_input_connect_button"]')).to_be_visible()
    expect(page.get_by_text("Телефон", exact=True)).to_be_visible()
    expect(page.get_by_text("Мобильный телефон")).to_be_visible()
    expect(page.get_by_text(
        'Нажимая на кнопку "Оставить заявку", вы даёте Согласие на обработку персональных')).to_be_visible()
    page.locator('//*[@id="root"]/div/div[4]/div/div/div/div[2]/span').click()


@allure.step("Проверка кнопок сортировки на странице рейтинга")
def check_sorting_rating(page: Page):
    page.locator('//input[@datatest="raiting_input_filter_period"]').click()
    expect(page.get_by_text("3 месяца")).to_be_visible()
    expect(page.get_by_text("6 месяцев")).to_be_visible()
    expect(page.get_by_text("За всё время")).to_be_visible()
    page.get_by_text("12 месяцев").click()
    page.locator('//input[@datatest="raiting_input_filter_internet_type"]').click()
    expect(page.get_by_text("Мобильный доступ")).to_be_visible()
    expect(page.locator('//li[contains(text(), "Интернет в офис")]')).to_be_visible()
    page.get_by_text("Интернет в квартиру").click()


@allure.step("Проверка тегов на странице тарифов")
def check_tags_rates(page: Page):
    page.get_by_role("heading", name="Тарифы на домашний интернет в Абакане").click()
    page.get_by_role("link", name="интернет+тв+мобильная связь", exact=True).click()
    page.get_by_role("link", name="домашний интернет", exact=True).click()
    page.get_by_role("link", name="интернет+тв", exact=True).click()
    page.get_by_role("link", name="дешевый интернет").click()
    page.get_by_role("link", name="100 мб/с").click()
    page.get_by_role("link", name="300 мб/с").click()
    page.get_by_role("link", name="500 мб/с").click()
    page.get_by_role("link", name="онлайн-кинотеатр", exact=True).click()
    page.get_by_role("link", name="Все", exact=True).click()
    page.get_by_role("link", name="Белгород", exact=True).click()
    page.get_by_role("link", name=" Белгород").click()
    page.get_by_role("link", name="Владимир", exact=True).click()
    page.get_by_role("link", name=" Владимир").click()
    page.get_by_role("link", name="Астрахань").click()
    page.get_by_text("Астрахань+7 (800) 302-32-76БЕСПЛАТНАЯ КОНСУЛЬТАЦИЯ Войти").click()
    page.get_by_role("link", name=" Астрахань").click()
    page.get_by_role("link", name="Санкт-Петербург").click()
    page.get_by_role("link", name=" Санкт-Петербург").click()
    page.get_by_role("link", name="Москва").click()


@allure.step("Проверка страницы выбора региона")
def check_select_region(page: Page):
    page.get_by_role("link", name="Белгород", exact=True).click()
    page.locator('(//span[contains(text(), "Белгород")])[1]').click()
    page.get_by_role("link", name="Владимир", exact=True).click()
    page.locator('(//span[contains(text(), "Владимир")])[1]').click()
    page.get_by_role("link", name="Астрахань").click()
    page.locator('(//span[contains(text(), "Астрахань")])[1]').click()
    page.get_by_role("link", name="Санкт-Петербург").click()
    page.locator('(//span[contains(text(), "Санкт-Петербург")])[1]').click()
    page.get_by_role("link", name="Москва").click()


@allure.step("Проверка фильтров на странице отзывов")
def check_sorting_review(page: Page):
    page.locator('//input[@datatest="reviews_input_filter_provider"]').click()
    page.locator('//div[contains(text(), "2КОМ")]').click()
    page.locator('//input[@datatest="reviews_input-filter_reviews"]').click()
    expect(page.locator('//li[contains(text(), "Нейтральный")]')).to_be_visible()
    expect(page.locator('//li[contains(text(), "Негативный")]')).to_be_visible()
    page.locator('//li[contains(text(), "Положительный")]').click()
    page.locator('//input[@datatest="reviews_input_filter_service"]').click()
    expect(page.locator('//li[contains(text(), "Интернет в загородный дом")]')).to_be_visible()
    expect(page.locator('//li[contains(text(), "Интернет в офис")]')).to_be_visible()
    expect(page.locator('//li[contains(text(), "Мобильный доступ")]')).to_be_visible()
    page.locator('//li[contains(text(), "Интернет в квартиру ")]').click()
    page.locator('//input[@name="sort_reviews"]').click()
    expect(page.locator('//li[contains(text(), "Сначала старые отзывы")]')).to_be_visible()
    page.locator('//li[contains(text(), "Сначала новые отзывы")]').click()
    page.locator('(// a[contains(text(), "оставить отзыв")])[2]').click()
    page.locator('(//div[@class="container"]//span)[1]').click()



@allure.step("Проверка пангинации на странице отзывов")
def check_pangination_review(page: Page):
    for i in range(1, 6):
        page.locator(f'(//a[@aria-label="Переключить страницу"])[{i}]').click()
        expect(page.locator('(// a[contains(text(), "оставить отзыв")])[2]')).to_be_visible()














