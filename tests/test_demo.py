from playwright.sync_api import Page, expect


def test_first(page: Page):
    page.goto('https://ru.wikipedia.org/')
    page.get_by_role('link', name='Содержание').click()
    page.locator('#ca-talk').click()
    expect(page.locator('#firstHeading')).to_have_text('Обсуждение Википедии:Содержание')


# Тест который отправляет заявку с попапа
def test_pag(page: Page):
    page.goto('https://www.moskvaonline.ru/')
    change_region = page.locator('(//a[@href="/select-region"])[1]')
    change_region.click()
    change_balashixa = page.locator('//input[@placeholder="Введите первые 3 буквы"]')
    change_balashixa.fill('Балашиха')
    choose_balashixa = page.locator('(//a[contains(text(), "Балашиха")])[1]')
    choose_balashixa.click()
    CHOOSE_THE_COVERAGE_MAP = page.locator("//a[contains(text(), 'Карта покрытия')]")
    CHOOSE_THE_COVERAGE_MAP.click()
    CHOOSE_ZONE = page.locator("//a[contains(text(), 'Балашиха')]")
    CHOOSE_ZONE.click()
    CHOSE_REGION = page.locator("(//a[contains(text(), 'Красный Текстильщик ул')])[1]")
    CHOSE_REGION.click()
    # STREET = page.locator("//a[contains(text(), 'Советская ул')]")
    # STREET.click()
    HOUSE = page.locator("//a[contains(text(), '3А')]")
    HOUSE.click()
    INPUT = page.locator("//input[@datatest='rates_popup1_from_quiz_input_tel']")
    INPUT.fill('1111111111')
    CHOW_RES = page.locator("//div[contains(text(), 'Показать результаты')]")
    CHOW_RES.click()
    CLOSE_POPUP = page.locator("//div[@datatest='close_popup1_from_quiz_input_tel']")
    CLOSE_POPUP.click()

