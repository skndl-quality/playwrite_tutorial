import json
from playwright.sync_api import Page, expect

def test_modified_response(page: Page):

    def handle_route(route):
        response = route.fetch()
        json = response.json()
        json['tags'] = [
            {"name": "Тест 1", "slug": "test_1"},
            {"name": "Тест 2", "slug": "test_2"},
            {"name": "Тест 3", "slug": "test_3"},
            {"name": "Тест 4", "slug": "test_4"},
            {"name": "Тест 5", "slug": "test_5"},
            {"name": "Тест 6", "slug": "test_6"},
            {"name": "Тест 7", "slug": "test_7"},
            {"name": "Тест 8", "slug": "test_8"},
            {"name": "Тест 9", "slug": "test_9"},
            {"name": "Тест 10", "slug": "test_10"}
        ]
        route.fulfill(json=json)

    page.route("**/cms/business/v2/analytics/filters", handle_route)
    page.goto("https://business.test01.russpass.dev/analytical-materials")