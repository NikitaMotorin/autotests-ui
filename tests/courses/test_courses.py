import pytest
import allure
from allure_commons.types import Severity

from pages.courses.courses_list_page import CoursesListPage
from pages.courses.create_course_page import CreateCoursePage
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
from tools.allure.tags import AllureTag


@pytest.mark.courses
@pytest.mark.regression
@allure.tag(AllureTag.REGRESSION, AllureTag.COURSES)
@allure.epic(AllureEpic.LMS) # Добавили epic
@allure.feature(AllureFeature.COURSES) # Добавили feature
@allure.story(AllureStory.COURSES) # Добавили story
class TestCourse:
    @allure.title("Check displaying of empty courses list")
    @allure.severity(Severity.NORMAL)
    def test_empty_courses_list(self, initialize_browser_state, courses_list_page: CoursesListPage):
        courses_list_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")
        courses_list_page.navbar.check_visible("username")
        courses_list_page.sidebar.check_visible()
        courses_list_page.check_visible_empty_view()
        courses_list_page.toolbar_view.check_visible()

    @allure.title("Create course")
    @allure.severity(Severity.CRITICAL)
    def test_create_course(self, initialize_browser_state, create_course_page: CreateCoursePage,
                           courses_list_page: CoursesListPage):
        create_course_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create")

        create_course_page.toolbar_view.check_visible()
        create_course_page.toolbar_view.check_disabled()
        create_course_page.image_upload_widget.check_visible(is_image_uploaded=False)
        create_course_page.create_course.check_visible(
            "",
            "",
            "",
            "0",
            "0"
        )
        create_course_page.exercise_toolbar_view.check_visible()
        create_course_page.check_visible_exercises_empty_view()
        create_course_page.image_upload_widget.upload_preview_image("./testdata/files/image.png")
        create_course_page.image_upload_widget.check_visible(is_image_uploaded=True)
        create_course_page.create_course.fill(
            "Playwright",
            "2 week",
            "Playwright",
            "100",
            "10"
        )
        create_course_page.toolbar_view.click_create_course_button()
        courses_list_page.toolbar_view.check_visible()
        courses_list_page.course_view.check_visible(
            0,
            "Playwright",
            "100",
            "10",
            "2 week"
        )

    @allure.title("Check correct edit course")
    @allure.severity(Severity.CRITICAL)
    def test_edit_course(self, initialize_browser_state, create_course_page: CreateCoursePage, courses_list_page: CoursesListPage):

        create_course_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create")
        create_course_page.image_upload_widget.upload_preview_image("./testdata/files/image.png")
        create_course_page.create_course.fill(
            "Playwright",
            "2 week",
            "Playwright",
            "100",
            "10"
        )
        create_course_page.toolbar_view.click_create_course_button()
        courses_list_page.course_view.check_visible(
            0,
            "Playwright",
            "100",
            "10",
            "2 week"
        )
        courses_list_page.course_view.menu.click_edit(0)
        create_course_page.create_course.fill(
            "Playwright111",
            "2 week",
            "Playwright",
            "100",
            "10"
        )
        create_course_page.toolbar_view.click_create_course_button()
        courses_list_page.toolbar_view.check_visible()
        courses_list_page.course_view.check_visible(
            0,
            "Playwright111",
            "100",
            "10",
            "2 week"
        )










