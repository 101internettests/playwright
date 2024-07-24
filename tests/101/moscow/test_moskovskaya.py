import allure
import pytest
from playwright.sync_api import Page, expect
from pages.main_page import sorting_providers_rates,tags_mobile, tags_for_operatory, nomera_page
from pages.main_page import check_footer, sorting, ooops_stub, operators_menu_block
from pages.main_page import check_header_operator_page, tags_nomera_mobile, cellular_network, sorting_second
from pages.main_site_pages.moscow_page import check_header_moscow_obl


@allure.title("Проверка страницы тарифов бещз абонентской платы в Моск. обл. 101")
def test_operatory_mts_ratesmobile_bez_platy(page: Page):
    page.goto('https://101internet.ru/moskovskaya-oblast/operatory/mts/ratesmobile/bez-abonentskoj-platy')
    check_header_operator_page(page)
    check_footer(page)
    check_header_moscow_obl(page)
    expect(page.get_by_role("link", name="Подключить интернет")).to_be_visible()
    expect(page.get_by_role("link", name="Мобильные операторы")).to_be_visible()
    expect(page.locator('//span[contains(text(), "МТС")]')).to_be_visible()
    expect(page.locator('//span[contains(text(), "Тарифы")]')).to_be_visible()
    expect(page.locator('//span[contains(text(), "Без абонентской платы")]')).to_be_visible()
    expect(page.get_by_role("heading", name="Без абонентской платы тарифы МТС в Московской области")).to_be_visible()
    expect(page.locator('//img[@itemprop="contentUrl"]')).to_be_visible()
    expect(page.locator("#operator_banner").get_by_text("Подключение")).to_be_visible()
    expect(page.locator("#operator_banner").get_by_text("Техподдержка")).to_be_visible()
    expect(page.locator('//a[contains(text(), "+7  (800)  250-08-90")]')).to_be_visible()
    expect(page.locator('//a[contains(text(), "+7 (800) 250-08-90")]')).to_be_visible()
    expect(page.get_by_role("link", name="Об операторе")).to_be_visible()
    expect(page.get_by_role("link", name="Тарифы").nth(1)).to_be_visible()
    expect(page.get_by_role("link", name="Номера")).to_be_visible()
    expect(page.get_by_role("link", name="акции", exact=True)).to_be_visible()
    expect(page.get_by_role("link", name="в 1")).to_be_visible()
    expect(page.locator('//p[contains(text(), "К сожалению, у нас нет информации о тарифах оператора в этом регионе.")]')).to_be_visible()
    expect(page.locator('//div[contains(text(), "Недавно подключенные тарифы в ")]')).to_be_visible()
    tags_mobile(page)
    for i in range(1, 7 ):
        expect(page.locator(f'(//div[contains(text(), "Выбрать")])[{i}]')).to_be_visible()


def test_operatory_mts_ratesmobile_bezlimitnaja(page: Page):
    page.goto('https://101internet.ru/moskovskaya-oblast/operatory/mts/ratesmobile/bezlimitnaja-svjaz')
    check_header_operator_page(page)
    check_footer(page)
    check_header_moscow_obl(page)
    expect(page.get_by_role("link", name="Подключить интернет")).to_be_visible()
    expect(page.get_by_role("link", name="Мобильные операторы")).to_be_visible()
    expect(page.locator('//span[contains(text(), "МТС")]')).to_be_visible()
    expect(page.locator('//span[contains(text(), "Тарифы")]')).to_be_visible()
    expect(page.locator('//span[contains(text(), "Безлимитная связь")]')).to_be_visible()
    expect(page.get_by_role("heading", name="Безлимитные звонки на все операторы от МТС в Московской области")).to_be_visible()
    expect(page.locator('//img[@itemprop="contentUrl"]')).to_be_visible()
    expect(page.locator("#operator_banner").get_by_text("Подключение")).to_be_visible()
    expect(page.locator("#operator_banner").get_by_text("Техподдержка")).to_be_visible()
    expect(page.locator('//a[contains(text(), "+7  (800)  250-08-90")]')).to_be_visible()
    expect(page.locator('//a[contains(text(), "+7 (800) 250-08-90")]')).to_be_visible()
    expect(page.get_by_role("link", name="Об операторе")).to_be_visible()
    expect(page.get_by_role("link", name="Тарифы").nth(1)).to_be_visible()
    expect(page.get_by_role("link", name="Номера")).to_be_visible()
    expect(page.get_by_role("link", name="акции", exact=True)).to_be_visible()
    expect(page.get_by_role("link", name="в 1")).to_be_visible()
    tags_for_operatory(page)
    tags_mobile(page)
    for i in range(1, 8):
        expect(page.locator(f'(//div[contains(text(), "Выбрать")])[{i}]')).to_be_visible()
    expect(page.locator('//h2')).to_be_visible()


def test_operatory_mts_ratesmobile_bezlimitniy_internet(page: Page):
    page.goto('https://101internet.ru/moskovskaya-oblast/operatory/mts/ratesmobile/bezlimitnyj-internet')
    check_header_operator_page(page)
    check_footer(page)
    check_header_moscow_obl(page)
    expect(page.get_by_role("link", name="Подключить интернет")).to_be_visible()
    expect(page.get_by_role("link", name="Мобильные операторы")).to_be_visible()
    expect(page.locator('//span[contains(text(), "МТС")]')).to_be_visible()
    expect(page.locator('//span[contains(text(), "Тарифы")]')).to_be_visible()
    expect(page.locator('//span[contains(text(), "Безлимитный интернет")]')).to_be_visible()
    expect(page.get_by_role("heading", name="Безлимитный интернет тарифы МТС в Московской области")).to_be_visible()
    expect(page.locator('//img[@itemprop="contentUrl"]')).to_be_visible()
    expect(page.locator("#operator_banner").get_by_text("Подключение")).to_be_visible()
    expect(page.locator("#operator_banner").get_by_text("Техподдержка")).to_be_visible()
    expect(page.locator('//a[contains(text(), "+7  (800)  250-08-90")]')).to_be_visible()
    expect(page.locator('//a[contains(text(), "+7 (800) 250-08-90")]')).to_be_visible()
    expect(page.get_by_role("link", name="Об операторе")).to_be_visible()
    expect(page.get_by_role("link", name="Тарифы").nth(1)).to_be_visible()
    expect(page.get_by_role("link", name="Номера")).to_be_visible()
    expect(page.get_by_role("link", name="акции", exact=True)).to_be_visible()
    expect(page.get_by_role("link", name="в 1")).to_be_visible()
    tags_mobile(page)
    for i in range(1, 13):
        expect(page.locator(f'(//div[contains(text(), "Выбрать")])[{i}]')).to_be_visible()
    expect(page.locator('//h2')).to_be_visible()


def test_operatory_mts_ratesmobile_bezlimitnaja_svjaz(page: Page):
    page.goto('https://101internet.ru/moskovskaya-oblast/operatory/mts/ratesmobile/bezlimitnaja-svjaz-po-rossii')
    check_header_operator_page(page)
    check_footer(page)
    check_header_moscow_obl(page)
    expect(page.get_by_role("link", name="Подключить интернет")).to_be_visible()
    expect(page.get_by_role("link", name="Мобильные операторы")).to_be_visible()
    expect(page.locator('//span[contains(text(), "МТС")]')).to_be_visible()
    expect(page.locator('//span[contains(text(), "Тарифы")]')).to_be_visible()
    expect(page.locator('//span[contains(text(), "Безлимитная связь по России")]')).to_be_visible()
    expect(page.get_by_role("heading", name="Безлимитные звонки по России от МТС в Московской области")).to_be_visible()
    expect(page.locator('//img[@itemprop="contentUrl"]')).to_be_visible()
    expect(page.locator("#operator_banner").get_by_text("Подключение")).to_be_visible()
    expect(page.locator("#operator_banner").get_by_text("Техподдержка")).to_be_visible()
    expect(page.locator('//a[contains(text(), "+7  (800)  250-08-90")]')).to_be_visible()
    expect(page.locator('//a[contains(text(), "+7 (800) 250-08-90")]')).to_be_visible()
    expect(page.get_by_role("link", name="Об операторе")).to_be_visible()
    expect(page.get_by_role("link", name="Тарифы").nth(1)).to_be_visible()
    expect(page.get_by_role("link", name="Номера")).to_be_visible()
    expect(page.get_by_role("link", name="акции", exact=True)).to_be_visible()
    expect(page.get_by_role("link", name="в 1")).to_be_visible()
    tags_mobile(page)
    expect(page.locator('//div[contains(text(), "Недавно подключенные тарифы в ")]')).to_be_visible()
    for i in range(1, 7):
        expect(page.locator(f'(//div[contains(text(), "Выбрать")])[{i}]')).to_be_visible()


def test_operatory_mts_ratesmobile_dlia_modema(page: Page):
    page.goto('https://101internet.ru/moskovskaya-oblast/operatory/mts/ratesmobile/dlja-modema')
    check_header_operator_page(page)
    check_footer(page)
    check_header_moscow_obl(page)
    expect(page.get_by_role("link", name="Подключить интернет")).to_be_visible()
    expect(page.get_by_role("link", name="Мобильные операторы")).to_be_visible()
    expect(page.locator('//span[contains(text(), "МТС")]')).to_be_visible()
    expect(page.locator('//span[contains(text(), "Тарифы")]')).to_be_visible()
    expect(page.locator('//span[contains(text(), "Для модема/роутера")]')).to_be_visible()
    expect(page.get_by_role("heading", name="Тарифы МТС для интернета через модем в Московской области")).to_be_visible()
    expect(page.locator('//img[@itemprop="contentUrl"]')).to_be_visible()
    expect(page.locator("#operator_banner").get_by_text("Подключение")).to_be_visible()
    expect(page.locator("#operator_banner").get_by_text("Техподдержка")).to_be_visible()
    expect(page.locator('//a[contains(text(), "+7  (800)  250-08-90")]')).to_be_visible()
    expect(page.locator('//a[contains(text(), "+7 (800) 250-08-90")]')).to_be_visible()
    expect(page.get_by_role("link", name="Об операторе")).to_be_visible()
    expect(page.get_by_role("link", name="Тарифы").nth(1)).to_be_visible()
    expect(page.get_by_role("link", name="Номера")).to_be_visible()
    expect(page.get_by_role("link", name="акции", exact=True)).to_be_visible()
    expect(page.get_by_role("link", name="в 1")).to_be_visible()
    tags_mobile(page)
    tags_for_operatory(page)
    for i in range(1, 5):
        expect(page.locator(f'(//div[contains(text(), "Выбрать")])[{i}]')).to_be_visible()


def test_operatory_mts_ratesmobile_dlia_plansheta(page: Page):
    page.goto('https://101internet.ru/moskovskaya-oblast/operatory/mts/ratesmobile/dlja-plansheta')
    check_header_operator_page(page)
    check_footer(page)
    check_header_moscow_obl(page)
    expect(page.get_by_role("link", name="Подключить интернет")).to_be_visible()
    expect(page.get_by_role("link", name="Мобильные операторы")).to_be_visible()
    expect(page.locator('//span[contains(text(), "МТС")]')).to_be_visible()
    expect(page.locator('//span[contains(text(), "Тарифы")]')).to_be_visible()
    expect(page.locator('//span[contains(text(), "Для планшета")]')).to_be_visible()
    expect(page.get_by_role("heading", name="Для планшета тарифы МТС в Московской области")).to_be_visible()
    expect(page.locator('//img[@itemprop="contentUrl"]')).to_be_visible()
    expect(page.locator("#operator_banner").get_by_text("Подключение")).to_be_visible()
    expect(page.locator("#operator_banner").get_by_text("Техподдержка")).to_be_visible()
    expect(page.locator('//a[contains(text(), "+7  (800)  250-08-90")]')).to_be_visible()
    expect(page.locator('//a[contains(text(), "+7 (800) 250-08-90")]')).to_be_visible()
    expect(page.get_by_role("link", name="Об операторе")).to_be_visible()
    expect(page.get_by_role("link", name="Тарифы").nth(1)).to_be_visible()
    expect(page.get_by_role("link", name="Номера")).to_be_visible()
    expect(page.get_by_role("link", name="акции", exact=True)).to_be_visible()
    expect(page.get_by_role("link", name="в 1")).to_be_visible()
    tags_mobile(page)
    tags_for_operatory(page)
    for i in range(1, 5):
        expect(page.locator(f'(//div[contains(text(), "Выбрать")])[{i}]')).to_be_visible()
    expect(page.locator('//h2')).to_be_visible()


def test_operatory_mts_ratesmobile_dlia_sng(page: Page):
    page.goto('https://101internet.ru/moskovskaya-oblast/operatory/mts/ratesmobile/dlja-sng')
    check_header_operator_page(page)
    check_footer(page)
    check_header_moscow_obl(page)
    expect(page.get_by_role("link", name="Подключить интернет")).to_be_visible()
    expect(page.get_by_role("link", name="Мобильные операторы")).to_be_visible()
    expect(page.locator('//span[contains(text(), "МТС")]')).to_be_visible()
    expect(page.locator('//span[contains(text(), "Тарифы")]')).to_be_visible()
    expect(page.locator('//span[contains(text(), "Для СНГ")]')).to_be_visible()
    expect(page.get_by_role("heading", name="Для СНГ тарифы МТС в Московской области")).to_be_visible()
    expect(page.locator('//img[@itemprop="contentUrl"]')).to_be_visible()
    expect(page.locator("#operator_banner").get_by_text("Подключение")).to_be_visible()
    expect(page.locator("#operator_banner").get_by_text("Техподдержка")).to_be_visible()
    expect(page.locator('//a[contains(text(), "+7  (800)  250-08-90")]')).to_be_visible()
    expect(page.locator('//a[contains(text(), "+7 (800) 250-08-90")]')).to_be_visible()
    expect(page.get_by_role("link", name="Об операторе")).to_be_visible()
    expect(page.get_by_role("link", name="Тарифы").nth(1)).to_be_visible()
    expect(page.get_by_role("link", name="Номера")).to_be_visible()
    expect(page.get_by_role("link", name="акции", exact=True)).to_be_visible()
    expect(page.get_by_role("link", name="в 1")).to_be_visible()
    expect(page.locator('//p[contains(text(), "К сожалению, у нас нет информации о тарифах оператора в этом регионе.")]')).to_be_visible()
    expect(page.locator('//div[contains(text(), "Недавно подключенные тарифы в ")]')).to_be_visible()
    tags_mobile(page)
    for i in range(1, 7):
        expect(page.locator(f'(//div[contains(text(), "Выбрать")])[{i}]')).to_be_visible()


def test_operatory_mts_ratesmobile_mezhdunarodnye(page: Page):
    page.goto('https://101internet.ru/moskovskaya-oblast/operatory/mts/ratesmobile/mezhdunarodnye')
    check_header_operator_page(page)
    check_footer(page)
    check_header_moscow_obl(page)
    expect(page.get_by_role("link", name="Подключить интернет")).to_be_visible()
    expect(page.get_by_role("link", name="Мобильные операторы")).to_be_visible()
    expect(page.locator('//span[contains(text(), "МТС")]')).to_be_visible()
    expect(page.locator('//span[contains(text(), "Тарифы")]')).to_be_visible()
    expect(page.locator('//span[contains(text(), "Роуминг за границей")]')).to_be_visible()
    expect(page.get_by_role("heading", name="Международные тарифы от МТС подключение в Московской области")).to_be_visible()
    expect(page.locator('//img[@itemprop="contentUrl"]')).to_be_visible()
    expect(page.get_by_text("Подключение", exact=True)).to_be_visible()
    expect(page.get_by_text("Техподдержка")).to_be_visible()
    expect(page.locator('//a[contains(text(), "+7  (800)  250-08-90")]')).to_be_visible()
    expect(page.locator('//a[contains(text(), "+7 (800) 250-08-90")]')).to_be_visible()
    expect(page.get_by_role("link", name="Об операторе")).to_be_visible()
    expect(page.get_by_role("link", name="Тарифы").nth(1)).to_be_visible()
    expect(page.get_by_role("link", name="Номера")).to_be_visible()
    expect(page.get_by_role("link", name="акции", exact=True)).to_be_visible()
    expect(page.get_by_role("link", name="в 1")).to_be_visible()
    tags_for_operatory(page)
    tags_mobile(page)
    for i in range(1, 3):
        expect(page.locator(f'(//div[contains(text(), "Выбрать")])[{i}]')).to_be_visible()
    expect(page.locator('//h2')).to_be_visible()


def test_operatory_mts_ratesmobile_optom(page: Page):
    page.goto('https://101internet.ru/moskovskaya-oblast/operatory/mts/ratesmobile/optom')
    check_header_operator_page(page)
    check_footer(page)
    check_header_moscow_obl(page)
    expect(page.get_by_role("link", name="Подключить интернет")).to_be_visible()
    expect(page.get_by_role("link", name="Мобильные операторы")).to_be_visible()
    expect(page.locator('//span[contains(text(), "МТС")]')).to_be_visible()
    expect(page.locator('//span[contains(text(), "Тарифы")]')).to_be_visible()
    expect(page.locator('//span[contains(text(), "Оптом")]')).to_be_visible()
    expect(page.get_by_role("heading", name="Оптом тарифы МТС в Московской области")).to_be_visible()
    expect(page.locator('//img[@itemprop="contentUrl"]')).to_be_visible()
    expect(page.get_by_text("Подключение", exact=True)).to_be_visible()
    expect(page.get_by_text("Техподдержка")).to_be_visible()
    expect(page.locator('//a[contains(text(), "+7  (800)  250-08-90")]')).to_be_visible()
    expect(page.locator('//a[contains(text(), "+7 (800) 250-08-90")]')).to_be_visible()
    expect(page.get_by_role("link", name="Об операторе")).to_be_visible()
    expect(page.get_by_role("link", name="Тарифы").nth(1)).to_be_visible()
    expect(page.get_by_role("link", name="Номера")).to_be_visible()
    expect(page.get_by_role("link", name="акции", exact=True)).to_be_visible()
    expect(page.get_by_role("link", name="в 1")).to_be_visible()
    expect(page.locator(
        '//p[contains(text(), "К сожалению, у нас нет информации о тарифах оператора в этом регионе.")]')).to_be_visible()
    expect(page.locator('//div[contains(text(), "Недавно подключенные тарифы в ")]')).to_be_visible()
    tags_mobile(page)
    for i in range(1, 7):
        expect(page.locator(f'(//div[contains(text(), "Выбрать")])[{i}]')).to_be_visible()


def test_operatory_mts_ratesmobile_unikalnye(page: Page):
    page.goto('https://101internet.ru/moskovskaya-oblast/operatory/mts/ratesmobile/unikalnye')
    check_header_operator_page(page)
    check_footer(page)
    check_header_moscow_obl(page)
    expect(page.get_by_role("link", name="Подключить интернет")).to_be_visible()
    expect(page.get_by_role("link", name="Мобильные операторы")).to_be_visible()
    expect(page.locator('//span[contains(text(), "МТС")]')).to_be_visible()
    expect(page.locator('//span[contains(text(), "Тарифы")]')).to_be_visible()
    expect(page.locator('//span[contains(text(), "Непубличные")]')).to_be_visible()
    expect(page.get_by_role("heading", name="Непубличные тарифы МТС в Московской области")).to_be_visible()
    expect(page.locator('//img[@itemprop="contentUrl"]')).to_be_visible()
    expect(page.get_by_text("Подключение", exact=True)).to_be_visible()
    expect(page.get_by_text("Техподдержка")).to_be_visible()
    expect(page.locator('//a[contains(text(), "+7  (800)  250-08-90")]')).to_be_visible()
    expect(page.locator('//a[contains(text(), "+7 (800) 250-08-90")]')).to_be_visible()
    expect(page.get_by_role("link", name="Об операторе")).to_be_visible()
    expect(page.get_by_role("link", name="Тарифы").nth(1)).to_be_visible()
    expect(page.get_by_role("link", name="Номера")).to_be_visible()
    expect(page.get_by_role("link", name="акции", exact=True)).to_be_visible()
    expect(page.get_by_role("link", name="в 1")).to_be_visible()
    tags_for_operatory(page)
    tags_mobile(page)
    for i in range(1, 10):
        expect(page.locator(f'(//div[contains(text(), "Выбрать")])[{i}]')).to_be_visible()
    expect(page.locator('//h2[contains(text(), "Частые вопросы")]')).to_be_visible()


def test_operatory_mts_operatory_nomera(page: Page):
    page.goto('https://101internet.ru/moskovskaya-oblast/operatory/mts/nomera')
    check_header_operator_page(page)
    check_footer(page)
    check_header_moscow_obl(page)
    expect(page.get_by_role("link", name="Подключить интернет")).to_be_visible()
    expect(page.get_by_role("link", name="Мобильные операторы")).to_be_visible()
    expect(page.locator('//span[contains(text(), "МТС")]')).to_be_visible()
    expect(page.locator('//span[contains(text(), "Номера")]')).to_be_visible()
    expect(page.get_by_role("heading", name="Выбрать номер МТС")).to_be_visible()
    expect(page.locator('//img[@itemprop="contentUrl"]')).to_be_visible()
    expect(page.get_by_text("Подключение", exact=True)).to_be_visible()
    expect(page.get_by_text("Техподдержка")).to_be_visible()
    expect(page.locator('//a[contains(text(), "+7  (800)  250-08-90")]')).to_be_visible()
    expect(page.locator('//a[contains(text(), "+7 (800) 250-08-90")]')).to_be_visible()
    expect(page.get_by_role("link", name="Об операторе")).to_be_visible()
    expect(page.get_by_role("link", name="Тарифы").nth(1)).to_be_visible()
    expect(page.get_by_role("link", name="Номера")).to_be_visible()
    expect(page.get_by_role("link", name="акции", exact=True)).to_be_visible()
    expect(page.get_by_role("link", name="в 1")).to_be_visible()
    tags_nomera_mobile(page)
    for i in range(1, 15):
        expect(page.locator(f'(//div[contains(text(), "Подключить На официальном сайте")])[{i}]')).to_be_visible()
    expect(page.locator('//div[contains(text(), "ПОКАЗАТЬ ЕЩЁ")]')).to_be_visible()
    expect(page.locator('//h2[contains(text(), "Частые вопросы")]')).to_be_visible()


def test_moskovskaya_oblast_operatory(page: Page):
    page.goto('https://101internet.ru/moskovskaya-oblast/operatory')
    check_header_operator_page(page)
    check_footer(page)
    check_header_moscow_obl(page)
    expect(page.get_by_role("link", name="Подключить интернет")).to_be_visible()
    expect(page.locator("span").filter(has_text="Мобильные операторы")).to_be_visible()
    expect(page.get_by_role("heading", name="Мобильные операторы")).to_be_visible()
    expect(page.get_by_role("heading", name="Операторы связи в Московской области")).to_be_visible()
    for i in range(1, 7):
        expect(page.locator(f'(//span[contains(text(), "Подробнее")])[{i}]')).to_be_visible()
    expect(page.get_by_text("МТС предоставляет широкий спектр тарифов, в том числе с поддержкой 4G")).to_be_visible()
    expect(page.get_by_text(
        "МегаФон помимо безлимитной связи по России может похвастаться отдельными тарифами для международного общения")).to_be_visible()
    expect(page.get_by_text(
        "У билайна хорошее качество связи и лучшее, среди прочих, качество подключения к сети в метро. Компания предоставляет удобный набор безлимитных опций и дополнительных услуг")).to_be_visible()
    expect(page.get_by_text(
        "Тинькофф Мобайл — оператор, предоставляющий единый тариф-конструктор, который позволяет самостоятельно выбрать число минут, СМС, Гб и подходящий размер абонплаты. За счет этого Тинькофф Мобайл является одним из самых выгодных операторов")).to_be_visible()
    expect(page.get_by_text(
        "Tele2 — оператор сотовой связи, который успел завоевать симпатии клиентов благодаря своей доступной ценовой политике")).to_be_visible()
    expect(page.get_by_text(
        "Yota — виртуальный оператор, работающий на сетях МегаФона и предоставляющий абонентам высокую скорость подключения к интернету и доступные цены")).to_be_visible()
    expect(page.get_by_text(
        "СберМобайл предоставляет стабильную связь по всей России, постоянные акции и возможность вернуть до 20% бонусами Спасибо, сим-карту можно забрать в любом отделении Сбера")).to_be_visible()


def test_operatory_mts_operatory_zolotoj(page: Page):
    page.goto('https://101internet.ru/moskovskaya-oblast/operatory/mts/nomera/zolotoj')
    check_header_operator_page(page)
    check_footer(page)
    check_header_moscow_obl(page)
    expect(page.get_by_role("link", name="Подключить интернет")).to_be_visible()
    expect(page.get_by_role("link", name="Мобильные операторы")).to_be_visible()
    expect(page.locator('//span[contains(text(), "МТС")]')).to_be_visible()
    expect(page.locator('//span[contains(text(), "Номера")]')).to_be_visible()
    expect(page.locator('//span[contains(text(), "Золотые")]')).to_be_visible()
    expect(page.get_by_role("heading", name="Золотые номера МТС на выбор в Московской области")).to_be_visible()
    expect(page.locator('//img[@itemprop="contentUrl"]')).to_be_visible()
    expect(page.get_by_text("Подключение", exact=True)).to_be_visible()
    expect(page.get_by_text("Техподдержка")).to_be_visible()
    expect(page.locator('//a[contains(text(), "+7  (800)  250-08-90")]')).to_be_visible()
    expect(page.locator('//a[contains(text(), "+7 (800) 250-08-90")]')).to_be_visible()
    operators_menu_block(page)
    expect(page.locator(
        '//span[contains(text(), "Информация носит справочный характер и не является публичной офертой.")]')).to_be_visible()
    tags_nomera_mobile(page)
    for i in range(1, 15):
        expect(page.locator(f'(//div[contains(text(), "Подключить На официальном сайте")])[{i}]')).to_be_visible()
    expect(page.locator('//div[contains(text(), "ПОКАЗАТЬ ЕЩЁ")]')).to_be_visible()
    expect(page.locator('//h2[contains(text(), "Частые вопросы")]')).to_be_visible()


def test_operatory_mts_operatory_bronzovyj(page: Page):
    page.goto('https://101internet.ru/moskovskaya-oblast/operatory/mts/nomera/bronzovyj')
    check_header_operator_page(page)
    check_footer(page)
    check_header_moscow_obl(page)
    expect(page.get_by_role("link", name="Подключить интернет")).to_be_visible()
    expect(page.get_by_role("link", name="Мобильные операторы")).to_be_visible()
    expect(page.locator('//span[contains(text(), "МТС")]')).to_be_visible()
    expect(page.locator('//span[contains(text(), "Номера")]')).to_be_visible()
    expect(page.locator('//span[contains(text(), "Бронзовые")]')).to_be_visible()
    expect(page.get_by_role("heading", name="Бронзовые номера МТС на выбор в Московской области")).to_be_visible()
    expect(page.locator('//img[@itemprop="contentUrl"]')).to_be_visible()
    expect(page.get_by_text("Подключение", exact=True)).to_be_visible()
    expect(page.get_by_text("Техподдержка")).to_be_visible()
    expect(page.locator('//a[contains(text(), "+7  (800)  250-08-90")]')).to_be_visible()
    expect(page.locator('//a[contains(text(), "+7 (800) 250-08-90")]')).to_be_visible()
    operators_menu_block(page)
    expect(page.locator(
        '//span[contains(text(), "Информация носит справочный характер и не является публичной офертой.")]')).to_be_visible()
    tags_nomera_mobile(page)
    for i in range(1, 15):
        expect(page.locator(f'(//div[contains(text(), "Подключить На официальном сайте")])[{i}]')).to_be_visible()
    expect(page.locator('//div[contains(text(), "ПОКАЗАТЬ ЕЩЁ")]')).to_be_visible()
    expect(page.locator('//h2[contains(text(), "Частые вопросы")]')).to_be_visible()


def test_operatory_mts_operatory_serebrjanyj(page: Page):
    page.goto('https://101internet.ru/moskovskaya-oblast/operatory/mts/nomera/serebrjanyj')
    check_header_operator_page(page)
    check_footer(page)
    check_header_moscow_obl(page)
    expect(page.get_by_role("link", name="Подключить интернет")).to_be_visible()
    expect(page.get_by_role("link", name="Мобильные операторы")).to_be_visible()
    expect(page.locator('//span[contains(text(), "МТС")]')).to_be_visible()
    expect(page.locator('//span[contains(text(), "Номера")]')).to_be_visible()
    expect(page.locator('//span[contains(text(), "Серебряные")]')).to_be_visible()
    expect(page.get_by_role("heading", name="Серебряные номера МТС на выбор в Московской области")).to_be_visible()
    expect(page.locator('//img[@itemprop="contentUrl"]')).to_be_visible()
    expect(page.get_by_text("Подключение", exact=True)).to_be_visible()
    expect(page.get_by_text("Техподдержка")).to_be_visible()
    expect(page.locator('//a[contains(text(), "+7  (800)  250-08-90")]')).to_be_visible()
    expect(page.locator('//a[contains(text(), "+7 (800) 250-08-90")]')).to_be_visible()
    operators_menu_block(page)
    expect(page.locator(
        '//span[contains(text(), "Информация носит справочный характер и не является публичной офертой.")]')).to_be_visible()
    tags_nomera_mobile(page)
    for i in range(1, 15):
        expect(page.locator(f'(//div[contains(text(), "Подключить На официальном сайте")])[{i}]')).to_be_visible()
    expect(page.locator('//div[contains(text(), "ПОКАЗАТЬ ЕЩЁ")]')).to_be_visible()
    expect(page.locator('//h2[contains(text(), "Частые вопросы")]')).to_be_visible()


def test_operatory_mts_operatory_platinovyj(page: Page):
    page.goto('https://101internet.ru/moskovskaya-oblast/operatory/mts/nomera/platinovyj')
    check_header_operator_page(page)
    check_footer(page)
    check_header_moscow_obl(page)
    expect(page.get_by_role("link", name="Подключить интернет")).to_be_visible()
    expect(page.get_by_role("link", name="Мобильные операторы")).to_be_visible()
    expect(page.locator('//span[contains(text(), "МТС")]')).to_be_visible()
    expect(page.locator('//span[contains(text(), "Номера")]')).to_be_visible()
    expect(page.locator('//span[contains(text(), "Платиновые")]')).to_be_visible()
    expect(page.get_by_role("heading", name="Платиновые номера МТС на выбор в Московской области")).to_be_visible()
    expect(page.locator('//img[@itemprop="contentUrl"]')).to_be_visible()
    expect(page.get_by_text("Подключение", exact=True)).to_be_visible()
    expect(page.get_by_text("Техподдержка")).to_be_visible()
    expect(page.locator('//a[contains(text(), "+7  (800)  250-08-90")]')).to_be_visible()
    expect(page.locator('//a[contains(text(), "+7 (800) 250-08-90")]')).to_be_visible()
    operators_menu_block(page)
    expect(page.locator(
        '//span[contains(text(), "Информация носит справочный характер и не является публичной офертой.")]')).to_be_visible()
    tags_nomera_mobile(page)
    for i in range(1, 15):
        expect(page.locator(f'(//div[contains(text(), "Подключить На официальном сайте")])[{i}]')).to_be_visible()
    expect(page.locator('//div[contains(text(), "ПОКАЗАТЬ ЕЩЁ")]')).to_be_visible()
    expect(page.locator('//h2[contains(text(), "Частые вопросы")]')).to_be_visible()


def test_operatory_mts_operatory_besplatnye(page: Page):
    page.goto('https://101internet.ru/moskovskaya-oblast/operatory/mts/nomera/besplatnye')
    check_header_operator_page(page)
    check_footer(page)
    check_header_moscow_obl(page)
    expect(page.get_by_role("link", name="Подключить интернет")).to_be_visible()
    expect(page.get_by_role("link", name="Мобильные операторы")).to_be_visible()
    expect(page.locator('//span[contains(text(), "МТС")]')).to_be_visible()
    expect(page.locator('//span[contains(text(), "Номера")]')).to_be_visible()
    expect(page.locator('//span[contains(text(), "Бесплатные")]')).to_be_visible()
    expect(page.get_by_role("heading", name="Бесплатные номера МТС на выбор в Московской области")).to_be_visible()
    expect(page.locator('//img[@itemprop="contentUrl"]')).to_be_visible()
    expect(page.get_by_text("Подключение", exact=True)).to_be_visible()
    expect(page.get_by_text("Техподдержка")).to_be_visible()
    expect(page.locator('//a[contains(text(), "+7  (800)  250-08-90")]')).to_be_visible()
    expect(page.locator('//a[contains(text(), "+7 (800) 250-08-90")]')).to_be_visible()
    operators_menu_block(page)
    expect(page.locator(
        '//span[contains(text(), "Информация носит справочный характер и не является публичной офертой.")]')).to_be_visible()
    tags_nomera_mobile(page)
    for i in range(1, 6):
        expect(page.locator(f'(//div[contains(text(), "Подключить На официальном сайте")])[{i}]')).to_be_visible()
    expect(page.locator('//h2[contains(text(), "Частые вопросы")]')).to_be_visible()


def test_operatory_mts_ratesmobile(page: Page):
    page.goto('https://101internet.ru/moskovskaya-oblast/ratesmobile')
    check_header_operator_page(page)
    check_footer(page)
    check_header_moscow_obl(page)
    expect(page.get_by_role("link", name="Подключить интернет")).to_be_visible()
    expect(page.get_by_text("Тарифы сотовой связи", exact=True)).to_be_visible()
    expect(page.get_by_text("КОНСТРУКТОР (new!)")).to_be_visible()
    expect(page.get_by_text("СПИСОК ТАРИФОВ")).to_be_visible()
    expect(page.get_by_text("оператор", exact=True)).to_be_visible()
    expect(page.locator("input[name=\"change_operators\"]")).to_be_visible()
    expect(page.get_by_role("heading", name="Тарифы сотовой связи для телефона в Московской области")).to_be_visible()
    tags_for_operatory(page)
    tags_mobile(page)
    sorting_second(page)
    for i in range(1, 15):
        expect(page.locator(f'(//div[contains(text(), "Выбрать")])[{i}]')).to_be_visible()
    expect(page.locator('//div[contains(text(), "ПОКАЗАТЬ ЕЩЁ")]')).to_be_visible()
    expect(page.get_by_role("heading", name="Отзывы жителей Московской области")).to_be_visible()
    expect(page.locator('//h2[contains(text(), "Частые вопросы")]')).to_be_visible()


def test_operatory_ratesmobile_modem(page: Page):
    page.goto('https://101internet.ru/moskovskaya-oblast/ratesmobile/dlja-modema')
    check_header_operator_page(page)
    check_footer(page)
    check_header_moscow_obl(page)
    cellular_network(page)
    expect(page.locator('//span[contains(text(), "Для модема/роутера")]')).to_be_visible()
    expect(page.locator('//h1[contains(text(), "Тарифы операторов для модема в Московской области")]')).to_be_visible()
    tags_mobile(page)
    tags_for_operatory(page)
    for i in range(1, 15):
        expect(page.locator(f'(//div[contains(text(), "Выбрать")])[{i}]')).to_be_visible()
    expect(page.locator('//h2[contains(text(), "Тарифы операторов для модема в Московской области")]')).to_be_visible()
    expect(page.locator('//div[contains(text(), "ПОКАЗАТЬ ЕЩЁ")]')).to_be_visible()


def test_operatory_ratesmobile_bez_platy(page: Page):
    page.goto('https://101internet.ru/moskovskaya-oblast/ratesmobile/bez-abonentskoj-platy')
    check_header_operator_page(page)
    check_footer(page)
    check_header_moscow_obl(page)
    expect(page.get_by_role("link", name="Подключить интернет")).to_be_visible()
    expect(page.get_by_role("link", name="Тарифы сотовой связи")).to_be_visible()
    expect(page.locator('//span[contains(text(), "Без абонентской платы")]')).to_be_visible()
    expect(page.locator('//h1[contains(text(), "Безлимитный интернет для телефона")]')).to_be_visible()
    expect(page.get_by_text("КОНСТРУКТОР (new!)")).to_be_visible()
    expect(page.get_by_text("СПИСОК ТАРИФОВ")).to_be_visible()
    tags_mobile(page)
    tags_for_operatory(page)
    sorting_second(page)
    expect(page.locator('//div[contains(text(), "Выбрать")]')).to_be_visible()


def test_operatory_ratesmobile_svjaz(page: Page):
    page.goto('https://101internet.ru/moskovskaya-oblast/ratesmobile/bezlimitnaja-svjaz')
    check_header_operator_page(page)
    check_footer(page)
    check_header_moscow_obl(page)
    cellular_network(page)
    expect(page.locator('//span[contains(text(), "Безлимитная связь")]')).to_be_visible()
    expect(page.locator('//h1[contains(text(), "Тарифы операторов с безлимитной связью в Московской области")]')).to_be_visible()
    tags_mobile(page)
    tags_for_operatory(page)
    for i in range(1, 15):
        expect(page.locator(f'(//div[contains(text(), "Выбрать")])[{i}]')).to_be_visible()
    expect(page.locator('//h2[contains(text(), "Тарифы операторов с безлимитными звонками в Московской области")]')).to_be_visible()
    expect(page.locator('//div[contains(text(), "ПОКАЗАТЬ ЕЩЁ")]')).to_be_visible()


def test_operatory_ratesmobile_bezlimitn_internet(page: Page):
    page.goto('https://101internet.ru/moskovskaya-oblast/ratesmobile/bezlimitnyj-internet')
    check_header_operator_page(page)
    check_footer(page)
    check_header_moscow_obl(page)
    cellular_network(page)
    expect(page.locator('//span[contains(text(), "Безлимитный интернет")]')).to_be_visible()
    expect(page.locator('//h1[contains(text(), "Тарифы с безлимитным интернетом")]')).to_be_visible()
    tags_mobile(page)
    tags_for_operatory(page)
    for i in range(1, 15):
        expect(page.locator(f'(//div[contains(text(), "Выбрать")])[{i}]')).to_be_visible()
    expect(page.locator('//div[contains(text(), "ПОКАЗАТЬ ЕЩЁ")]')).to_be_visible()


def test_operatory_ratesmobile_vygodnye(page: Page):
    page.goto('https://101internet.ru/moskovskaya-oblast/ratesmobile/vygodnye')
    check_header_operator_page(page)
    check_footer(page)
    check_header_moscow_obl(page)
    expect(page.get_by_role("link", name="Подключить интернет")).to_be_visible()
    expect(page.get_by_role("link", name="Тарифы сотовой связи")).to_be_visible()
    expect(page.locator('//span[contains(text(), "Выгодные")]')).to_be_visible()
    expect(page.locator('//h1[contains(text(), "Выгодные тарифы сотовых операторов в Московской области")]')).to_be_visible()
    expect(page.get_by_text("КОНСТРУКТОР (new!)")).to_be_visible()
    expect(page.get_by_text("СПИСОК ТАРИФОВ")).to_be_visible()
    tags_mobile(page)
    tags_for_operatory(page)
    sorting_second(page)
    for i in range(1, 15):
        expect(page.locator(f'(//div[contains(text(), "Выбрать")])[{i}]')).to_be_visible()
    expect(page.locator('//div[contains(text(), "ПОКАЗАТЬ ЕЩЁ")]')).to_be_visible()
    expect(page.locator(
        '//h2[contains(text(), "Тарифы операторов с выгодными предложениями в Московской области")]')).to_be_visible()


def test_operatory_ratesmobile_planshet(page: Page):
    page.goto('https://101internet.ru/moskovskaya-oblast/ratesmobile/dlja-plansheta')
    check_header_operator_page(page)
    check_footer(page)
    check_header_moscow_obl(page)
    cellular_network(page)
    expect(page.locator('//span[contains(text(), "Для планшета")]')).to_be_visible()
    expect(page.locator('//h1[contains(text(), "Тарифные планы на интернет для планшета")]')).to_be_visible()
    tags_mobile(page)
    tags_for_operatory(page)
    for i in range(1, 15):
        expect(page.locator(f'(//div[contains(text(), "Выбрать")])[{i}]')).to_be_visible()
    expect(page.locator('//div[contains(text(), "ПОКАЗАТЬ ЕЩЁ")]')).to_be_visible()


def test_operatory_ratesmobile_noutbuke1(page: Page):
    page.goto('https://101internet.ru/moskovskaya-oblast/ratesmobile/dlja-noutbuka')
    check_header_operator_page(page)
    check_footer(page)
    check_header_moscow_obl(page)
    cellular_network(page)
    expect(page.locator('//span[contains(text(), "Для ноутбука")]')).to_be_visible()
    expect(page.locator('//h1[contains(text(), "Тарифные планы для ноутбука")]')).to_be_visible()
    tags_mobile(page)
    tags_for_operatory(page)
    for i in range(1, 2):
        expect(page.locator(f'(//div[contains(text(), "Выбрать")])[{i}]')).to_be_visible()


def test_operatory_ratesmobile_mezhdunarodnye(page: Page):
    page.goto('https://101internet.ru/moskovskaya-oblast/ratesmobile/mezhdunarodnye')
    check_header_operator_page(page)
    check_footer(page)
    check_header_moscow_obl(page)
    expect(page.locator('//span[contains(text(), "Роуминг за границей")]')).to_be_visible()
    expect(page.locator('//h1[contains(text(), "Мобильные тарифы для связи за границей - подключить в Московской области")]')).to_be_visible()
    tags_mobile(page)
    tags_for_operatory(page)
    for i in range(1, 6):
        expect(page.locator(f'(//div[contains(text(), "Выбрать")])[{i}]')).to_be_visible()


def test_operatory_ratesmobile_po_rf(page: Page):
    page.goto('https://101internet.ru/moskovskaya-oblast/ratesmobile/po-rossii')
    check_header_operator_page(page)
    check_footer(page)
    check_header_moscow_obl(page)
    cellular_network(page)
    expect(page.locator('//span[contains(text(), "Связь по России")]')).to_be_visible()
    expect(page.locator('//h1[contains(text(), "Тарифы телефонных операторов в Московской области для связи по России")]')).to_be_visible()
    tags_mobile(page)
    tags_for_operatory(page)
    for i in range(1, 6):
        expect(page.locator(f'(//div[contains(text(), "Выбрать")])[{i}]')).to_be_visible()
    expect(page.locator('//div[contains(text(), "ПОКАЗАТЬ ЕЩЁ")]')).to_be_visible()


def test_operatory_ratesmobile_esim(page: Page):
    page.goto('https://101internet.ru/moskovskaya-oblast/ratesmobile/esim')
    check_header_operator_page(page)
    check_footer(page)
    check_header_moscow_obl(page)
    cellular_network(page)
    expect(page.locator('//span[contains(text(), "eSIM")]')).to_be_visible()
    expect(page.locator('//h1[contains(text(), "Тарифы eSIM для вашего устройства в Московской области")]')).to_be_visible()
    tags_mobile(page)
    tags_for_operatory(page)
    for i in range(1, 6):
        expect(page.locator(f'(//div[contains(text(), "Выбрать")])[{i}]')).to_be_visible()
    expect(page.locator('//div[contains(text(), "ПОКАЗАТЬ ЕЩЁ")]')).to_be_visible()
    expect(page.locator('//h2[contains(text(), "Тарифы eSIM в Московской области")]')).to_be_visible()


def test_operatory_ratesmobile_perenos_nomera(page: Page):
    page.goto('https://101internet.ru/moskovskaya-oblast/ratesmobile/perenos_nomera')
    check_header_operator_page(page)
    check_footer(page)
    check_header_moscow_obl(page)
    cellular_network(page)
    expect(page.locator('//span[contains(text(), "Перейти со своим номером")]')).to_be_visible()
    expect(page.locator('//h1[contains(text(), "Перейти на другого оператора с сохранением номера в Московской области")]')).to_be_visible()
    tags_mobile(page)
    tags_for_operatory(page)
    for i in range(1, 15):
        expect(page.locator(f'(//div[contains(text(), "Выбрать")])[{i}]')).to_be_visible()
    expect(page.locator('//div[contains(text(), "ПОКАЗАТЬ ЕЩЁ")]')).to_be_visible()


def test_operatory_ratesmobile_unikalnye(page: Page):
    page.goto('https://101internet.ru/moskovskaya-oblast/ratesmobile/unikalnye')
    check_header_operator_page(page)
    check_footer(page)
    check_header_moscow_obl(page)
    cellular_network(page)
    expect(page.locator('//span[contains(text(), "Непубличные")]')).to_be_visible()
    expect(page.locator('//h1[contains(text(), "Непубличные тарифы ")]')).to_be_visible()
    tags_mobile(page)
    tags_for_operatory(page)
    cellular_network(page)
    for i in range(1, 15):
        expect(page.locator(f'(//div[contains(text(), "Выбрать")])[{i}]')).to_be_visible()
    expect(page.locator('//div[contains(text(), "ПОКАЗАТЬ ЕЩЁ")]')).to_be_visible()


def test_operatory_nomera(page: Page):
    page.goto('https://101internet.ru/moskovskaya-oblast/nomera')
    check_header_operator_page(page)
    check_footer(page)
    check_header_moscow_obl(page)
    tags_nomera_mobile(page)
    expect(page.get_by_role("link", name="Подключить интернет")).to_be_visible()
    expect(page.locator('//span[contains(text(), "Номера")]')).to_be_visible()
    expect(page.locator('//h1[contains(text(), "Выбрать номер")]')).to_be_visible()
    expect(page.get_by_role("link", name="Федеральные")).to_be_visible()
    expect(page.get_by_role("link", name="VIP")).to_be_visible()
    for i in range(1, 15):
        expect(page.locator(f'(//div[contains(text(), "Подключить На официальном сайте")])[{i}]')).to_be_visible()
    expect(page.locator('//div[contains(text(), "ПОКАЗАТЬ ЕЩЁ")]')).to_be_visible()
    expect(page.locator('//h2[contains(text(), "Частые вопросы")]')).to_be_visible()


def test_operatory_nomera_zolotoj(page: Page):
    page.goto('https://101internet.ru/moskovskaya-oblast/nomera/zolotoj')
    check_header_operator_page(page)
    check_footer(page)
    check_header_moscow_obl(page)
    tags_nomera_mobile(page)
    nomera_page(page)
    expect(page.locator('//span[contains(text(), "Золотые")]')).to_be_visible()
    expect(page.locator('//h1[contains(text(), "Элитные номера телефонов")]')).to_be_visible()


def test_operatory_nomera_bronzovyj(page: Page):
    page.goto('https://101internet.ru/moskovskaya-oblast/nomera/bronzovyj')
    check_header_operator_page(page)
    check_footer(page)
    check_header_moscow_obl(page)
    tags_nomera_mobile(page)
    nomera_page(page)
    expect(page.locator('//span[contains(text(), "Бронзовые")]')).to_be_visible()
    expect(page.locator('//h1[contains(text(), "Бронзовый номер телефона")]')).to_be_visible()


def test_operatory_nomera_serebrjanyj(page: Page):
    page.goto('https://101internet.ru/moskovskaya-oblast/nomera/serebrjanyj')
    check_header_operator_page(page)
    check_footer(page)
    check_header_moscow_obl(page)
    tags_nomera_mobile(page)
    nomera_page(page)
    expect(page.locator('//span[contains(text(), "Серебряные")]')).to_be_visible()
    expect(page.locator('//h1[contains(text(), "Серебряный номер от российских операторов")]')).to_be_visible()


def test_operatory_nomera_platinovyj(page: Page):
    page.goto('https://101internet.ru/moskovskaya-oblast/nomera/platinovyj')
    check_header_operator_page(page)
    check_footer(page)
    check_header_moscow_obl(page)
    tags_nomera_mobile(page)
    nomera_page(page)
    expect(page.locator('//span[contains(text(), "Платиновые")]')).to_be_visible()
    expect(page.locator('//h1[contains(text(), "Платиновый номер телефона")]')).to_be_visible()


def test_operatory_nomera_vip(page: Page):
    page.goto('https://101internet.ru/moskovskaya-oblast/nomera/vip')
    check_header_operator_page(page)
    check_footer(page)
    check_header_moscow_obl(page)
    tags_nomera_mobile(page)
    nomera_page(page)
    expect(page.locator('//span[contains(text(), "VIP")]')).to_be_visible()
    expect(page.locator('//h1[contains(text(), "Вип номера телефонов")]')).to_be_visible()


def test_operatory_nomera_federalnye(page: Page):
    page.goto('https://101internet.ru/moskovskaya-oblast/nomera/federalnye')
    check_header_operator_page(page)
    check_footer(page)
    check_header_moscow_obl(page)
    tags_nomera_mobile(page)
    nomera_page(page)
    expect(page.locator('//span[contains(text(), "Федеральные")]')).to_be_visible()
    expect(page.locator('//h1[contains(text(), "Федеральный номер от российских операторов")]')).to_be_visible()


def test_operatory_nomera_besplatnye(page: Page):
    page.goto('https://101internet.ru/moskovskaya-oblast/nomera/besplatnye')
    check_header_operator_page(page)
    check_footer(page)
    check_header_moscow_obl(page)
    tags_nomera_mobile(page)
    expect(page.locator('//span[contains(text(), "Бесплатные")]')).to_be_visible()
    expect(page.locator('//h1[contains(text(), "Бесплатные номера телефонов")]')).to_be_visible()
    nomera_page(page)