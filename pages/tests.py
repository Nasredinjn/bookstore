
from django.test import SimpleTestCase  # herer we use SimpleTestCase because this test is not attach to database model

# Create your tests here.
from django.urls import reverse, resolve

from pages.views import *


class HomePageTest(SimpleTestCase):
    def test_url_exists_at_correct_location(self):  # checking the routing of the page
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_homepage_url_name(self):  # test if the name of the path is correct
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_homepage_template(self):  # test if the page use the correct template which's here home.html
        response = self.client.get('/')
        self.assertTemplateUsed(response, "home.html")
        # assertTemplateUsed checks if the rendered template within response is the one passed as second parameter home.html

    def test_homepage_contains_correct_html(self):  # test if the rendered template contains the correct html content
        response = self.client.get("/")
        self.assertContains(response, "Welcome")

    def test_homepage_does_not_contain_incorrect_html(
            self):  # test if the rendered template does not contains a wrong content
        response = self.client.get("/")
        self.assertNotContains(response, "Hi there! I should not be on the page.")

    def test_homepage_url_resolves_homepageview(self):
        view = resolve("/")
        self.assertEqual(view.func.__name__, HomePageView.as_view().__name__)

# diff between reverse & resolve :
# reverse takes pattern name to access the url
# resolve takes path to access the url

    class AboutPageTests(SimpleTestCase):
        def setup(self):
            self.response = self.client.get(reverse("about"))

        def test_about_template(self):
            self.assertEqual(self.response.status_code, 200)
            self.assertTemplateUsed(self.response, "about.html")
            self.assertContains(self.response, "about page")

        def test_about_view(self):
            view = reverse("about")
            self.assertEqual(view.func.__name__, AboutPageView.as_view().__name__)