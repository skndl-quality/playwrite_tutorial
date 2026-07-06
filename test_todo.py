import pytest


@pytest.mark.locator
def test_locator(page):
    page.goto(
        "https://zimaev.github.io/locatorand/")
    selector = page.get_by_role("button", name="Sing up").and_(page.get_by_title("Sing up today"))
    selector.click()
    page.pause()

@pytest.mark.navbar
def test_locator(page):
    page.goto(
        "https://zimaev.github.io/navbar/")
    page.locator("#navbarNavDropdown >> li:has-text('Company')").click()
    page.wait_for_timeout(2000)
    page.get_by_role("button", name="Company").click()
    page.wait_for_timeout(2000)

    page.pause()
