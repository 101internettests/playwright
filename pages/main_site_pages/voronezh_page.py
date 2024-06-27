import pytest
from playwright.sync_api import Page, expect


def check_header_voronezh(page: Page):
    expect(page.locator('(//a[@aria-label="/voronezh"] )[2]')).to_be_visible()
    expect(page.locator('(//div[contains(text(), "+7 (473) 202-92-95")])[1]')).to_be_visible()
    expect(page.locator('(// span[contains(text(), "Воронеж")])[1]')).to_be_visible()


def review(page: Page):
    expect(page.locator('//h2[contains(text(), "Отзывы о провайдерах домашнего интернета в Рязани")]')).to_have_text(
        'Отзывы о провайдерах домашнего интернета в Рязани')
    expect(
        page.locator('(//a[@datatest="main_allreviews_button"][contains(text(), "оставить отзыв")])[1]')).to_have_text(
        'оставить отзыв')
    expect(page.locator('(//a[@datatest="main_allreviews_button"][contains(text(), "все отзывы")])[1]')).to_have_text(
        'все отзывы')


def check_tags(page: Page):
    expect(page.locator('(//a[@href="/voronezh/rates/internet-i-mobilnaya-svyaz"])[1]')).to_be_visible()
    expect(page.locator('(//a[@href="/voronezh/rates/internet-tv-mobile"])[1]')).to_be_visible()
    expect(page.locator('(//a[@href="/voronezh/rates/domashnij-internet"])[1]')).to_be_visible()
    expect(page.locator('(//a[@href="/voronezh/rates/internet-i-tv"])[1]')).to_be_visible()
    expect(page.locator('(//a[@href="/voronezh/rates/nedorogoj-domashnij-internet"])[1]')).to_be_visible()
    expect(page.locator('(//a[@href="/voronezh/rates/internet-100-mbit"])[1]')).to_be_visible()
    expect(page.locator('(//a[@href="/voronezh/rates/internet-300-mbit"])[1]')).to_be_visible()
    expect(page.locator('(//a[@href="/voronezh/rates/internet-500-mbit"])[1]')).to_be_visible()
    expect(page.locator('(//a[@href="/voronezh/rates/online-kinoteatr"])[1]')).to_be_visible()
