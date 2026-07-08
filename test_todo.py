from pydoc import pager

import pytest

# поиск локатора, который подходит по двум методам
@pytest.mark.twomethod
def test_two_method(page):
    page.goto(
        "https://zimaev.github.io/locatorand/")
    selector = page.get_by_role("button", name="Sing up").and_(page.get_by_title("Sing up today"))
    selector.click()
    page.pause()

@pytest.mark.navbar
def test_navbar(page):
    page.goto(
        "https://zimaev.github.io/navbar/")
    page.locator("#navbarNavDropdown >> li:has-text('Company')").click() #наследование
    page.wait_for_timeout(2000)
    page.get_by_role("button", name="Company").click()
    page.wait_for_timeout(2000)
    page.locator("li").filter(has_text='Company').click() #ФИЛЬТРАЦИЯ ПО ТЕКСТУ
    page.wait_for_timeout(2000)
    page.locator("li").filter(has=page.locator('.dropdown-toggle')).click() #ФИЛЬТРАЦИЯ ПО ЛОКАТОРУ
    # page.pause()


@pytest.mark.filter
def test_filter(page):
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


@pytest.mark.checkbox
def test_checkbox(page):
    page.goto('https://zimaev.github.io/checks-radios/')
    checkbox = page.locator('input')

    # Функция range() генерирует ряд чисел в рамках заданного диапазона
    for i in range(checkbox.count()):
        checkbox.nth(i).click()
    page.wait_for_timeout(2000)

    for checkbox in checkbox.all():
        checkbox.check() # check включает чекбокс, кнопку и т.д., если чекбокс уже включен, он не выключится
    page.wait_for_timeout(2000)


@pytest.mark.keyboard
def test_keyboard(page):
    page.goto('https://ya.ru/?npr=1')
    page.locator(".mini-suggest__control").type("собака", delay=300) #ввод символов с задержкой в 300мс
    page.wait_for_timeout(1000)
    page.locator(".mini-suggest__control").press("Enter") #нажатие на enter
    page.wait_for_timeout(5000)


# выбор элемента в выпадающих списках
@pytest.mark.select
def test_select(page):
    page.goto('https://zimaev.github.io/select/')

    page.select_option("#floatingSelect", value="3")
    page.wait_for_timeout(2000)

    page.select_option("#floatingSelect", index=1)
    page.wait_for_timeout(2000)

    page.select_option("#floatingSelect", label="Нашел и завел bug")
    page.wait_for_timeout(2000)

    page.select_option("#floatingSelect", "3") #value по умолчанию
    page.wait_for_timeout(2000)

    page.select_option("#skills", value=['linux', 'python'])
    page.wait_for_timeout(2000)

#drag and drop внутри страницы
@pytest.mark.draganddrop
def test_draganddrop(page):
    page.goto('https://zimaev.github.io/draganddrop/')
    page.drag_and_drop("#drag", "#drop")
    page.wait_for_timeout(2000)
    page.pause()

# непонятная тема с диалоговыми окнами, нужна практика
@pytest.mark.dialog
def test_dialog(page):
    page.goto('https://zimaev.github.io/dialog/')
    page.on('dialog', lambda dialog: dialog.accept())
    # page.on -  прослушивает события которые, происходит в приложении.
    # 'dialog'  -  указывает на тип события которое нужно обработать
    # lambda dialog: dialog.accept() - анонимная функция обрабатывающая событие.
    page.get_by_text("Диалог Alert").click()
    page.wait_for_timeout(2000)

    page.on('dialog', lambda dialog: dialog.dismiss())
    page.get_by_text("Диалог Confirmation").click()
    page.wait_for_timeout(2000)

    page.on('dialog', lambda dialog: dialog.dismiss())
    page.on('dialog', lambda dialog: print(dialog.message))
    page.get_by_text("Диалог Prompt").click()
    page.wait_for_timeout(2000)

# загрузка файлов
@pytest.mark.upload
def test_upload(page):
    page.goto('https://zimaev.github.io/upload/')
    page.set_input_files('#formFile', 'text.txt') # пишем метод, обращаемся к селектору и загружаем файл

    page.on('filechooser', lambda filechooser: filechooser.set_files('text.txt')) # второй способ загрузки фала, через событие
    page.locator('#formFile').click()
    page.locator('#file-submit').click()
