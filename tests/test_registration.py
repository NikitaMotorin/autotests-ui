import pytest

from playwright.sync_api import Page, expect

@pytest.mark.regression  # Добавили маркировку regression
@pytest.mark.registration  # Добавили маркировку registration
def test_successful_registration(chromium_page: Page):
        # Переходим на страницу входа
        chromium_page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

        email_imput = chromium_page.get_by_test_id("registration-form-email-input").locator('input')
        email_imput.fill("user.name@gmail.com")

        # Заполняем поле username
        username_input = chromium_page.get_by_test_id("registration-form-username-input").locator('input')
        username_input.fill("username")

        # Заполняем поле password
        password_input = chromium_page.get_by_test_id("registration-form-password-input").locator('input')
        password_input.fill("password")

        regisration_button = chromium_page.get_by_test_id("registration-page-registration-button")
        regisration_button.click()

        dashboard_title = chromium_page.get_by_test_id("dashboard-toolbar-title-text")
        expect(dashboard_title).to_be_visible()