import pytest
from pages.courses_list_page import CoursesListPage
from pages.create_course_page import CreateCoursePage

@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(initialize_browser_state, courses_list_page: CoursesListPage):
        courses_list_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")
        courses_list_page.navbar.check_visible("username")
        courses_list_page.sidebar.check_visible()
        courses_list_page.check_visible_empty_view()
        courses_list_page.toolbar_view.check_visible()

@pytest.mark.courses
@pytest.mark.regression
def test_create_course(initialize_browser_state, create_course_page: CreateCoursePage, courses_list_page: CoursesListPage):
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




