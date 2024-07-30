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


@allure.step("Проверка кнопки проверить покрытие на странице провайдеры")
def check_button_coverage_providers(page: Page):
    page.locator('(//div[@data-test="providers_provider_connect_button"])[1]').click()
    expect(page.locator('(//input[@datatest="main_input_street_home_new"])[9]')).to_be_visible()
    expect(page.locator('(//input[@datatest="main_input_street_home_new"])[10]')).to_be_visible()
    page.locator('(//input[@aria-labelledby="label"])[13]').click()
    expect(page.get_by_text("В квартиру").nth(3)).to_be_visible()
    expect(page.get_by_text("В офис", exact=True).nth(2)).to_be_visible()
    page.get_by_text("На дачу").nth(3).click()
    expect(page.locator('[data-test="find_tohome_button_popup"]')).to_be_visible()
    expect(page.get_by_text(
        "Введите ваш адрес и сравните всех провайдеров своего дома в одной удобной таблице. В ней есть вся информация, необходимая для выбора провайдера: тарифы, сведения о прочих опциях, народный рейтинг провайдеров").nth(
        1)).to_be_visible()
