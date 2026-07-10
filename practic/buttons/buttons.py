def test_button(page):
    page.goto('https://demoqa.com/buttons')

    page.locator('#rightClickBtn').click(button='right')
    page.locator('#doubleClickBtn').dblclick()
    page.get_by_role('button', name="Click Me", exact=True).click()


