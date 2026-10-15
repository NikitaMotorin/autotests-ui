import pytest
import allure
from allure_commons.types import Severity

from pages.authentication.registration_page import RegistrationPage
from pages.dashboard.dashboard_page import DashboardPage
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
from tools.allure.tags import AllureTag


@pytest.mark.regression
@pytest.mark.registration
@allure.tag(AllureTag.REGRESSION, AllureTag.REGISTRATION)
@allure.epic(AllureEpic.LMS) # Добавили epic
@allure.feature(AllureFeature.AUTHENTICATION) # Добавили feature
@allure.story(AllureStory.REGISTRATION) # Добавили story
class TestRegistration:
        @pytest.mark.parametrize(
                "email, username, password",
                [
                        ("user.name@gmail.com", "username", "password")
                ]
        )
        @allure.title('Registration with correct email, username and password')
        @allure.severity(Severity.CRITICAL)
        def test_successful_registration(self, registration_page: RegistrationPage, dashboard_page: DashboardPage, email: str,
                                         username: str, password: str):
                registration_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
                registration_page.registration_form.fill(email=email, username=username, password=password)
                registration_page.click_registration_button()
                dashboard_page.toolbar_view.check_visible()