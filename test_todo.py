import os
from colorama import init, Fore, Back, Style
from pydoc import pager
from traceback import print_exc

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

# имитация нажатий на клавиаутру (вызов событий кнопок)
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
    page.set_input_files('#formFile', 'files/text.txt') # пишем метод, обращаемся к селектору и загружаем файл

    page.on('filechooser', lambda filechooser: filechooser.set_files('files/text.txt')) # второй способ загрузки фала, через событие
    page.locator('#formFile').click()
    page.locator('#file-submit').click()

# загрузка файла
@pytest.mark.download
def test_download(page):
    page.goto('https://demoqa.com/upload-download')
    # page.on('download', lambda download: print(download.path()))
    # данный способ используется, если вы понятия не имеете, что инициирует загрузку

    with page.expect_download() as download_info:
        page.locator('#downloadButton').click()

    download = download_info.value # получение объекта скачивания
    file_name = download.suggested_filename # получение инфы о файле
    destination_folder_path = './files/' # сохраняем путь в переменной
    path_with_files = (os.path.join(destination_folder_path, file_name)) # сохраняем путь с именем файла в переменную
    download.save_as(path_with_files) # сохраняем файл в пути

    print(Fore.RED + "\nИмя файла: " + file_name)
    print(Fore.RED + "Файл сохранен в : " + destination_folder_path)

    download.delete() # удаление временного файла
    os.remove(path_with_files) # удаление файла с директории

# извлечение данных с веб странниц
@pytest.mark.table
def test_table(page):
    page.goto('https://zimaev.github.io/table/')
    row = page.locator('tr')
    print(f'\n {row.all_text_contents()}')

    print(f'\n {row.all_inner_texts()}')

# создание скриншотов
@pytest.mark.screen
def test_screen(page):
    page.goto('https://demoqa.com/automation-practice-form')

    page.screenshot(path='files/screen/screenshot.png', full_page=True) # скрин всей страницы
    page.locator('.practice-form-wrapper').screenshot(path='files/screen/screen_element.png') # скрин элемента

# Работа с несколькими вкладками
@pytest.mark.tabs
def test_tabs(page):
    page.goto('https://zimaev.github.io/tabs/')
    with page.context.expect_page() as tab: # Метод page.context.expect_page()  ожидает открытия новой вкладки.
        page.get_by_text("Переход к Dashboard").click()

    new_tab = tab.value
# проверка, что мы перешли на ту страницу, которую ожидали. проверка URL и элемента
    url_accept = new_tab.url == "https://zimaev.github.io/tabs/dashboard/index.html?"
    sign_out = new_tab.locator(".nav-link", has_text="Sign out")
    element_accept = sign_out.is_visible()
# проверка на наличие урл и элемента
    if url_accept is True:
        print(Fore.GREEN + "\nurl правильный")
    else:
        print(Fore.RED + "\nurl неправильный")

    if element_accept is True:
        print(Fore.GREEN + "Элемент присутствует")
    else:
        print(Fore.RED + "Элемент отсутствует")

# проверки можно было сделать по другому, через assert, но я не разобрался как выводить в консоль результаты
    # assert new_tab.url == "https://zimaev.github.io/tabs/dashboard/index.html?"
    # sign_out = new_tab.locator('.nav-link', has_text='Sign out')
    # assert sign_out.is_visible()