from playwright.sync_api import Page, expect


def test_first(page: Page):
    page.goto('https://ru.wikipedia.org/')
    page.get_by_role('link', name='Содержание').click()
    page.locator('#ca-talk').click()
    expect(page.locator('#firstHeading')).to_have_text('Обсуждение Википедии:Содержание')

