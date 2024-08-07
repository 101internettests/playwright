import pytest
from playwright.sync_api import Page, expect


def header_mol(page: Page):
    expect(page.locator('(//a[@aria-label="/"])[2]')).to_be_visible()
    expect(page.locator('(// span[contains(text(), "Москва")])[1]')).to_be_visible()


def review(page: Page):
    expect(
        page.locator('(//a[@datatest="main_allreviews_button"][contains(text(), "оставить отзыв")])[1]')).to_have_text(
        'оставить отзыв')
    expect(page.locator('(//a[@datatest="main_allreviews_button"][contains(text(), "все отзывы")])[1]')).to_have_text(
        'все отзывы')


def check_tags(page: Page):
    expect(page.locator('(//a[@href="/rates/internet-i-mobilnaya-svyaz"])[1]')).to_be_visible()
    expect(page.locator('(//a[@href="/rates/internet-tv-mobile"])[1]')).to_be_visible()
    expect(page.locator('(//a[@href="/rates/domashnij-internet"])[1]')).to_be_visible()
    expect(page.locator('(//a[@href="/rates/internet-i-tv"])[1]')).to_be_visible()
    expect(page.locator('(//a[@href="/rates/nedorogoj-domashnij-internet"])[1]')).to_be_visible()
    expect(page.locator('(//a[@href="/rates/internet-100-mbit"])[1]')).to_be_visible()
    expect(page.locator('(//a[@href="/rates/internet-300-mbit"])[1]')).to_be_visible()
    expect(page.locator('(//a[@href="/rates/internet-500-mbit"])[1]')).to_be_visible()
    expect(page.locator('(//a[@href="/rates/online-kinoteatr"])[1]')).to_be_visible()


def operatory_mts_main(page: Page):
    expect(page.get_by_role("link", name="Подключить интернет")).to_be_visible()
    expect(page.get_by_role("link", name="Мобильные операторы")).to_be_visible()
    expect(page.locator('//span[contains(text(), "МТС")]')).to_be_visible()
    expect(page.locator('//span[contains(text(), "Тарифы")]')).to_be_visible()
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