import os


def test_upload_download(page):
    # Переходим на страницу с формой загрузки файлов
    page.goto("https://practice-automation.com/file-upload/")
    # Загружаем файл 'text.txt' из папки 'files' в поле с id="file-upload"
    page.set_input_files("#file-upload", 'files/text.txt')
    # Обновляем страницу (перезагружаем)
    page.reload()

    # Настраиваем обработчик события выбора файла.
    # Когда появится диалог выбора файла, автоматически выберем 'files/text.txt'
    page.on('filechooser', lambda filechooser: filechooser.set_files('files/text.txt'))
    # Кликаем по элементу с id="file-upload", чтобы открыть диалог выбора файла
    page.locator('#file-upload').click()

    # Переходим на страницу, где можно скачать файл
    page.goto("https://practice-automation.com/file-download/")

    # Начинаем ожидать скачивание файла
    with page.expect_download() as download_info:
        # Кликаем по ссылке/кнопке скачивания
        page.get_by_role('link', name='Download').nth(2).click()

    # Получаем объект скачанного файла
    download = download_info.value
    # Получаем имя файла, которое предлагает браузер
    file_name = download.suggested_filename
    # Указываем папку, куда сохраним файл
    folder_path = "./files"
    # Собираем полный путь: папка + имя файла
    path_with_files = os.path.join(folder_path, file_name)
    # Сохраняем скачанный файл в указанную папку
    download.save_as(path_with_files)

    print('\nFile name: %s' % file_name)
    print('Folder path: %s' % folder_path)
    # Удаляем временный файл, который Playwright создал во время скачивания
    download.delete()
    # Удаляем сохраненный файл из папки 'files'
    os.remove(path_with_files)