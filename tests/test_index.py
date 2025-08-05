import re 
from playwright.sync_api import Page, expect

def test_about_has_header(page: Page, test_web_address):
    page.goto(f"http://{test_web_address}/about")
    header = page.locator("h1")
    expect(header).to_have_text("About")

def test_has_header(page: Page, test_web_address):
    page.goto(f"http://{test_web_address}/")

    header = page.locator("h1")

    expect(header).to_have_text("Its Raining Cats and Dogs!")

def test_seven_days_display_as_grid(page: Page, test_web_address, db_connection):

    page.goto(f"http://{test_web_address}/")

    week_layout = page.locator(".week-layout")

    expect(week_layout).to_have_css("display", "grid")

def test_all_seven_days_load(page: Page, test_web_address, db_connection):

    page.goto(f"http://{test_web_address}/")

    days = page.locator(".day")

    assert days.count() == 7

