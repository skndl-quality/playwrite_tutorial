import json
from playwright.sync_api import Page, expect

def test_service_mode(page):
    page.goto('https://business.test01.russpass.dev')
    response = page.request.get('https://api.test01.russpass.dev/cms/business/service_mode')
    print(response.status)
    print(response.json())


def test_filter_photo(page):
    data = {
        "page": 1,
        "limit": 50,
        "samplingOption": "LARGE",
        "dataPhoto": {
            "fileType": ["webp"]
        }
    }
    header = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'ru',
        'content-type': 'application/json',
        'origin': 'https://business.test01.russpass.dev',
        'referer': 'https://business.test01.russpass.dev/',
        'source': 'front',
        'x-gravitee-api-key': '61360fd3-7803-4c1e-be9b-a740af497e55',
        'x-platform-version': 'web 1.2.5',
        'rqid': '1707b374-8f29-4804-95cf-db0ad0bc69f3'
    }
    response = page.request.post('https://api.test01.russpass.dev/cms/business/v2/mediabank/photos/filter', data=data, headers=header)
    print(response.status)
    print(response.json())
    print(response.body())