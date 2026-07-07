from pydoc import pager

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
    page.locator("li").filter(has_text='Company').click() #ФИЛЬТРАЦИЯ ПО ТЕКСТУ
    page.wait_for_timeout(2000)
    page.locator("li").filter(has=page.locator('.dropdown-toggle')).click() #ФИЛЬТРАЦИЯ ПО ЛОКАТОРУ
    page.pause()


@pytest.mark.filter
def test_locator_filter(page):
    page.goto('https://zimaev.github.io/filter/')

# фильтрация по отсутствию роли в элемента
    row_locator = page.locator('tr')
    total = row_locator.filter(has_not=page.get_by_role("button")).count()
    print(total)

#фильтрация по отсутствию текста
    row_locator_text = page.locator('tr')
    total2 = row_locator_text.filter(has_not_text="helicopter").count()
    print(total2)

#фильтрация по тексту и кнопки, в итоге найдется 1 элемент, который подходит по двум условиям
    row_locator_and = page.locator('tr')
    total4 = (row_locator_and
              .filter(has_text="QA")
              .filter(has=page.get_by_role('button')).count())
    print(total4)
    page.pause()


@pytest.mark.checkbox
def test_locator_checkbox(page):
    page.goto('https://zimaev.github.io/checks-radios/')
    checkbox = page.locator('input')

    # Функция range() генерирует ряд чисел в рамках заданного диапазона
    for i in range(checkbox.count()):
        checkbox.nth(i).click()
    page.wait_for_timeout(2000)

    for checkbox in checkbox.all():
        checkbox.check()
    page.wait_for_timeout(2000)
