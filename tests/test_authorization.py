import pytest
from playwright.sync_api import sync_playwright, expect, Page

@pytest.mark.regression  # Добавили маркировку regression
@pytest.mark.authorization # Добавили маркировку authorization
@pytest.mark.parametrize("email, password", [("user.name@gmail.com", "password"), ("user.name@gmail.com", "  "), ("  ", "password")])
def test_wrong_email_or_password_authorization(chromium_page: Page, email: str, password: str):
        # Переходим на страницу входа
        chromium_page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")

        # Заполняем поле email
        email_input = chromium_page.get_by_test_id('login-form-email-input').locator('input')
        email_input.fill(email)

        # Заполняем поле пароль
        password_input = chromium_page.get_by_test_id('login-form-password-input').locator('input')
        password_input.fill(password)

        # Нажимаем на кнопку Login
        login_button = chromium_page.get_by_test_id('login-page-login-button')
        login_button.click()

        # Проверяем, что появилось сообщение об ошибке
        wrong_email_or_password_alert = chromium_page.get_by_test_id('login-page-wrong-email-or-password-alert')
        expect(wrong_email_or_password_alert).to_be_visible()
        expect(wrong_email_or_password_alert).to_have_text("Wrong email or password")
