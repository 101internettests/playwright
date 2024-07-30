import pytest
from playwright.sync_api import Page, expect


def check_header_balashixa(page: Page):
    expect(page.locator('(//a[@aria-label="/balashiha"])[2]')).to_be_visible()
    expect(page.locator('(// span[contains(text(), "Балашиха")])[1]')).to_be_visible()


def review(page: Page):
    expect(
        page.locator('(//a[@datatest="main_allreviews_button"][contains(text(), "оставить отзыв")])[1]')).to_have_text(
        'оставить отзыв')
    expect(page.locator('(//a[@datatest="main_allreviews_button"][contains(text(), "все отзывы")])[1]')).to_have_text(
        'все отзывы')

def tags_yota(page: Page):
    expect(page.get_by_role("link", name="Все", exact=True)).to_be_visible()
    expect(page.get_by_role("link", name="eSIM")).to_be_visible()
    expect(page.get_by_role("link", name="Для модема/роутера")).to_be_visible()
    expect(page.get_by_role("link", name="Выгодные")).to_be_visible()
    expect(page.get_by_role("link", name="Для планшета")).to_be_visible()
    expect(page.get_by_role("link", name="Связь по России")).to_be_visible()
    expect(page.get_by_role("link", name="Безлимитный интернет")).to_be_visible()
    expect(page.get_by_role("link", name="Перейти со своим номером")).to_be_visible()

def check_tags(page: Page):
    expect(page.locator('(//a[@href="/balashiha/rates/internet-i-mobilnaya-svyaz"])[1]')).to_be_visible()
    expect(page.locator('(//a[@href="/balashiha/rates/internet-tv-mobile"])[1]')).to_be_visible()
    expect(page.locator('(//a[@href="/balashiha/rates/domashnij-internet"])[1]')).to_be_visible()
    expect(page.locator('(//a[@href="/balashiha/rates/internet-i-tv"])[1]')).to_be_visible()
    expect(page.locator('(//a[@href="/balashiha/rates/nedorogoj-domashnij-internet"])[1]')).to_be_visible()
    expect(page.locator('(//a[@href="/balashiha/rates/internet-100-mbit"])[1]')).to_be_visible()
    expect(page.locator('(//a[@href="/balashiha/rates/internet-300-mbit"])[1]')).to_be_visible()
    expect(page.locator('(//a[@href="/balashiha/rates/internet-500-mbit"])[1]')).to_be_visible()
    expect(page.locator('(//a[@href="/balashiha/rates/online-kinoteatr"])[1]')).to_be_visible()


def page_nomera(page: Page):
    expect(page.get_by_role("link", name="Подключить интернет")).to_be_visible()
    expect(page.locator('//span[contains(text(), "Тарифы сотовой связи")]')).to_be_visible()
    expect(page.get_by_text("КОНСТРУКТОР (new!)")).to_be_visible()
    expect(page.get_by_text("СПИСОК ТАРИФОВ")).to_be_visible()
    expect(page.locator('//div[contains(text(), "Сортировка")]')).to_be_visible()
    expect(page.locator('//input[@value="Сначала популярные "]')).to_be_visible()
    expect(page.locator('(//h1)[1]')).to_be_visible()
