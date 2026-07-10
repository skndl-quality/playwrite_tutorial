import pytest

def test_checkbox(page):
    page.goto('https://webdriveruniversity.com/Dropdown-Checkboxes-RadioButtons/index.html')


    page.select_option('#dropdowm-menu-1', value='C#') # Выбирает один или несколько параметров в <select> элементе
    page.locator('#dropdowm-menu-2').select_option(label='Maven') # Так же можно сначала выбрать селектор, а потом доставить метод

    checkbox = page.get_by_role('checkbox')
    page.get_by_role('checkbox', name='Option 1').click()
    page.get_by_role('checkbox', name='Option 2').check() # включит чекбокс
    page.get_by_role('checkbox', name='Option 3').check() # чекбокс останется включенным

    # клик по всем чекбоксам
    for i in range(checkbox.count()):
        checkbox.nth(i).click()

# радио-кноппка
    page.get_by_role('radio').nth(2).check()