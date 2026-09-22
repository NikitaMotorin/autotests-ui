import pytest
from playwright.sync_api import Playwright, Page

@pytest.fixture
def chromium_page(playwright:Playwright) -> Page:

        browser = playwright.chromium.launch(headless=False)
        yield browser.new_page()

@pytest.fixture(scope="session")
def initialize_browser_state(playwright: Playwright):
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

        email_imput = page.get_by_test_id("registration-form-email-input").locator('input')
        email_imput.fill("user.name@gmail.com")

                # Заполняем поле username
        username_input = page.get_by_test_id("registration-form-username-input").locator('input')
        username_input.fill("username")

                # Заполняем поле password
        password_input = page.get_by_test_id("registration-form-password-input").locator('input')
        password_input.fill("password")

        regisration_button = page.get_by_test_id("registration-page-registration-button")
        regisration_button.click()

        context.storage_state(path="browser-state.json")
        browser.close()

@pytest.fixture(scope="session")
def chromium_page_with_state(initialize_browser_state,playwright: Playwright) -> Page:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context(storage_state="browser-state.json")
        yield context.new_page()
        browser.close()