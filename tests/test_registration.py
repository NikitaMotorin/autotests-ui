

import pytest

from playwright.sync_api import Page, expect
from pages.registration_page import RegistrationPage
from pages.dashboard_page import DashboardPage

@pytest.mark.regression  # Добавили маркировку regression
@pytest.mark.registration  # Добавили маркировку registration
@pytest.mark.parametrize("email, username, password", [("user.name@gmail.com", "username", "password")])
def test_successful_registration(registration_page: RegistrationPage, dashboard_page: DashboardPage, email: str, username: str, password: str):
        registration_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
        registration_page.fill_registration_form(email=email, username=username, password=password)
        registration_page.click_registration_button()
        dashboard_page.cheak_dashboard_title_to_be_visible()