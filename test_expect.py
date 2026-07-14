from itertools import count

from playwright.sync_api import expect


def test_expect(page):
    page.goto("https://demo.playwright.dev/todomvc/")
    expect((page), "Не тот урл").to_have_url('https://demo.playwright.dev/todomvc/#/')
    expect((page.locator('.new-todo')), "Поле заполнено").to_be_empty()

    for i in range(5):
        page.locator('.new-todo').fill(str(i))
        page.locator('.new-todo').press("Enter")
    expect(page.get_by_test_id('todo-title'), 'Не равно пяти').to_have_count(5)

    page.locator('.toggle').nth(3).click()
    expect(page.locator('.toggle').nth(2), "Чек-бокс выключен").to_be_checked()