import json
from playwright.sync_api import Page, expect

def test_modified_filter(page: Page):

    page.goto("https://business.test01.russpass.dev/analytical-materials")

    def test_filter(route):
        modified_filter_data = {
            "filters": {
                "tags": ["luchshij_teg2"],
                "count": 12
            },
            "samplingOption": "LARGE"
        }
        route.continue_(post_data=json.dumps(modified_filter_data))

    page.route("**/cms/business/v2/analytics/filters", test_filter)

    page.get_by_role("button", name="Показать").click()
    page.get_by_role("dialog").locator("label").filter(has_text="успех").click()
    page.get_by_role("button", name="Применить").click()

