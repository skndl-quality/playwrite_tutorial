import json
from playwright.sync_api import Page, expect


def test_modified_response(page: Page):
    def handle_route(route):
        # 1. Получаем реальный ответ от сервера
        response = route.fetch()
        data = response.json()

        # 2. Меняем ТОЛЬКО теги в фильтрах
        # Все остальные поля (items, page, totalCards, totalPages и т.д.) сохраняются
        data['filters']['tags'] = [
            {"name": f"Тест {i}", "slug": f"test_{i}"}
            for i in range(1, 20)
        ]

        # 3. Отправляем измененный ответ
        route.fulfill(json=data)

    page.route("**/api.test01.russpass.dev/cms/business/v2/analytics/filters", handle_route)
    page.goto("https://business.test01.russpass.dev/analytical-materials")

    page.wait_for_load_state("networkidle")
    page.wait_for_timeout(8000)