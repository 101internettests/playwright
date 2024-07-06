import pytest
from playwright.sync_api import Page, expect


def check_header_moscow(page: Page):
    expect(page.locator('(//a[@href="tel:+74954874372"])[1]')).to_be_visible()
    expect(page.locator('(//a[@aria-label="/moskva"])[2]')).to_be_visible()
    expect(page.locator('(// span[contains(text(), "Москва")])[1]')).to_be_visible()


def check_tags(page: Page):
    expect(page.locator('(//a[@href="/moskva/rates/internet-i-mobilnaya-svyaz"])[1]')).to_be_visible()
    expect(page.locator('(//a[@href="/moskva/rates/internet-tv-mobile"])[1]')).to_be_visible()
    expect(page.locator('(//a[@href="/moskva/rates/domashnij-internet"])[1]')).to_be_visible()
    expect(page.locator('(//a[@href="/moskva/rates/internet-i-tv"])[1]')).to_be_visible()
    expect(page.locator('(//a[@href="/moskva/rates/nedorogoj-domashnij-internet"])[1]')).to_be_visible()
    expect(page.locator('(//a[@href="/moskva/rates/internet-100-mbit"])[1]')).to_be_visible()
    expect(page.locator('(//a[@href="/moskva/rates/internet-300-mbit"])[1]')).to_be_visible()
    expect(page.locator('(//a[@href="/moskva/rates/internet-500-mbit"])[1]')).to_be_visible()
    expect(page.locator('(//a[@href="/moskva/rates/online-kinoteatr"])[1]')).to_be_visible()


def check_provider_rostel_tags(page: Page):
    expect(page.locator('(//a[@href="/moskva/providers/rostelecom/rates/internet-i-mobilnaya-svyaz"])[1]')).to_be_visible()
    expect(page.locator('(//a[@href="/moskva/providers/rostelecom/rates/internet-tv-mobile"])[1]')).to_be_visible()
    expect(page.locator('(//a[@href="/moskva/providers/rostelecom/rates/domashnij-internet"])[1]')).to_be_visible()
    expect(page.locator('(//a[@href="/moskva/providers/rostelecom/rates/internet-i-tv"])[1]')).to_be_visible()
    expect(page.locator('(//a[@href="/moskva/providers/rostelecom/rates/nedorogoj-domashnij-internet"])[1]')).to_be_visible()
    expect(page.locator('(//a[@href="/moskva/providers/rostelecom/rates/online-kinoteatr"])[1]')).to_be_visible()


def check_provider_onlime_tags(page: Page):
    expect(page.locator('(//a[@href="/moskva/providers/onlime/rates/internet-i-mobilnaya-svyaz"])[1]')).to_be_visible()
    expect(page.locator('(//a[@href="/moskva/providers/onlime/rates/internet-tv-mobile"])[1]')).to_be_visible()
    expect(page.locator('(//a[@href="/moskva/providers/onlime/rates/domashnij-internet"])[1]')).to_be_visible()
    expect(page.locator('(//a[@href="/moskva/providers/onlime/rates/internet-i-tv"])[1]')).to_be_visible()
    expect(page.locator('(//a[@href="/moskva/providers/onlime/rates/nedorogoj-domashnij-internet"])[1]')).to_be_visible()
    expect(page.locator('(//a[@href="/moskva/providers/onlime/rates/online-kinoteatr"])[1]')).to_be_visible()