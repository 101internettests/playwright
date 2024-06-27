import pytest
from playwright.sync_api import Page, expect


def check_header_abakan(page: Page):
    expect(page.locator('(//a[@href="tel:+78003023276"])[1]')).to_be_visible()
    expect(page.locator('(//a[@aria-label="/abakan"])[2]')).to_be_visible()
    expect(page.locator('(// span[contains(text(), "Абакан")])[1]')).to_be_visible()


def review(page: Page):
    expect(page.locator('//h2[contains(text(), "Отзывы о провайдерах домашнего интернета в Абакане")]')).to_have_text(
        'Отзывы о провайдерах домашнего интернета в Абакане')
    expect(
        page.locator('(//a[@datatest="main_allreviews_button"][contains(text(), "оставить отзыв")])[1]')).to_have_text(
        'оставить отзыв')
    expect(page.locator('(//a[@datatest="main_allreviews_button"][contains(text(), "все отзывы")])[1]')).to_have_text(
        'все отзывы')


def check_tags(page: Page):
    expect(page.locator('(//a[@href="/abakan/rates/internet-i-mobilnaya-svyaz"])[1]')).to_be_visible()
    expect(page.locator('(//a[@href="/abakan/rates/internet-tv-mobile"])[1]')).to_be_visible()
    expect(page.locator('(//a[@href="/abakan/rates/domashnij-internet"])[1]')).to_be_visible()
    expect(page.locator('(//a[@href="/abakan/rates/internet-i-tv"])[1]')).to_be_visible()
    expect(page.locator('(//a[@href="/abakan/rates/nedorogoj-domashnij-internet"])[1]')).to_be_visible()
    expect(page.locator('(//a[@href="/abakan/rates/internet-100-mbit"])[1]')).to_be_visible()
    expect(page.locator('(//a[@href="/abakan/rates/internet-300-mbit"])[1]')).to_be_visible()
    expect(page.locator('(//a[@href="/abakan/rates/internet-500-mbit"])[1]')).to_be_visible()
    expect(page.locator('(//a[@href="/abakan/rates/online-kinoteatr"])[1]')).to_be_visible()
