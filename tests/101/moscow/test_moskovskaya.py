from playwright.sync_api import Page, expect
from pages.main_page import check_header, search_tariffs, one_click_form, tariffs_block, blue_form, feedback_page, sorting_providers_rates, contact_feedback, contact_page, tags_mobile, tags_for_operatory
from pages.main_page import check_footer, blue_form_second, search_tariffs_second, sorting, page_internet_in_office, ooops_stub, terms_of_use, personal_data, check_header_operator_page
from pages.main_site_pages.moscow_page import check_header_moscow, check_tags, check_provider_rostel_tags, check_provider_onlime_tags, check_header_moscow_obl


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