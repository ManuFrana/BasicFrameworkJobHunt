
import pytest
import unittest

from test.pages.careersPage import CareersPage

@pytest.mark.usefixtures("setup")
class TestApplyToJobOffer(unittest.TestCase):

    def test_assert_some_job_is_found_with_search(self):
        self.careerPage = CareersPage(self.driver, self.wait)
        self.careerPage.open()
        self.careerPage.close_cookies_banner()
        self.careerPage.search_for_job('QA', 'Quality Control', 'AR')
        self.careerPage.close_cookies_banner()
        self.careerPage.assert_some_job_is_found('Senior Test Automation Engineer (Anywhere)')