from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:

    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    regisration_button = page.get_by_test_id("registration-page-registration-button")
    expect(regisration_button).to_be_disabled()

    email_imput = page.get_by_test_id("registration-form-email-input").locator('input')
    email_imput.fill("user.name@gmail.com")

    # Заполняем поле username
    username_input = page.get_by_test_id("registration-form-username-input").locator('input')
    username_input.fill("username")

    # Заполняем поле password
    password_input = page.get_by_test_id("registration-form-password-input").locator('input')
    password_input.fill("password")

    regisration_button = page.get_by_test_id("registration-page-registration-button")
    expect(regisration_button).to_be_visible()

