import pytest
from playwright.sync_api import Page, expect


def header(page: Page):
    expect(page.locator('(//a[@aria-label="/leningradskaya-oblast"])[2]')).to_be_visible()
    expect(page.locator('(// span[contains(text(), "Ленинградская область")])[1]')).to_be_visible()


def rewiew(page: Page):
    expect(
        page.locator('(//a[@datatest="main_allreviews_button"][contains(text(), "оставить отзыв")])[1]')).to_have_text(
        'оставить отзыв')
    expect(page.locator('(//a[@datatest="main_allreviews_button"][contains(text(), "все отзывы")])[1]')).to_have_text(
        'все отзывы')


def tags(page: Page):
    expect(page.locator('(//a[@href="/leningradskaya-oblast/rates/internet-i-mobilnaya-svyaz"])[1]')).to_be_visible()
    expect(page.locator('(//a[@href="/leningradskaya-oblast/rates/internet-tv-mobile"])[1]')).to_be_visible()
    expect(page.locator('(//a[@href="/leningradskaya-oblast/rates/domashnij-internet"])[1]')).to_be_visible()
    expect(page.locator('(//a[@href="/leningradskaya-oblast/rates/internet-i-tv"])[1]')).to_be_visible()
    expect(page.locator('(//a[@href="/leningradskaya-oblast/rates/nedorogoj-domashnij-internet"])[1]')).to_be_visible()
    expect(page.locator('(//a[@href="/leningradskaya-oblast/rates/internet-100-mbit"])[1]')).to_be_visible()
    expect(page.locator('(//a[@href="/leningradskaya-oblast/rates/internet-300-mbit"])[1]')).to_be_visible()
    expect(page.locator('(//a[@href="/leningradskaya-oblast/rates/internet-500-mbit"])[1]')).to_be_visible()
    expect(page.locator('(//a[@href="/leningradskaya-oblast/rates/online-kinoteatr"])[1]')).to_be_visible()