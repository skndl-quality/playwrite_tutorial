import json
from playwright.sync_api import Page, expect

def test_modified_login(page: Page):
    # Функция перехвата запроса
    def inercept_login(route):
        # Данные, которые реально уйдет на сервер, подменные
        modified_data = {
            "login": "p.grinev+68@notamedia.com.ru",
            "password": "p.grinev+68@notamedia.com.ru1"
        }
        # json.dumps() превращает словарь в JSON-строку
        # post_data - аргумент, который подменяет тело запроса
        route.continue_(post_data=json.dumps(modified_data))

    # "**/api/auth/login?locale=ru" - шаблон URL для перехвата
    # intercept_login - функция, которая будет вызвана при совпадении
    page.route("**/api/auth/login?locale=ru", inercept_login)

    page.goto('https://business.test01.russpass.dev/signin')

    page.locator('[data-test="email"]').fill("p.grinev+1@notamedia.com.ru")
    page.locator('[data-test="password"]').fill("p.grinev+1@notamedia.com.ru1")
    page.locator('[data-test="signIn"]').click()

    expect(page).to_have_url('https://business.test01.russpass.dev/', timeout=10000)