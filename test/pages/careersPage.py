
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class CareersPage():

    URL = "https://career.globant.com/"
    COOKIE_CLOSE = "cookie-close"
    JOB_ALERT_FORM = "//form[contains(@class, 'jobAlertsSearchForm')]"
    INPUT_JOB_SEARCH = JOB_ALERT_FORM + "//input[@type='text']" # It has an id, but just to show xpath selectors :)
    AREA_SELECT = JOB_ALERT_FORM + "//select[@name='optionsFacetsDD_department']"
    COUNTRY = JOB_ALERT_FORM + "//select[@name='optionsFacetsDD_country']"
    JOB_SEARCH_BUTTON = "//input[contains(@class, 'keywordsearch-button')]"
    TITLE_ON_SEARCH = "Careers Search | Globant Careers"

    def __init__(self, driver: webdriver, wait: WebDriverWait):
        self.driver = driver
        self.wait = wait

    def get_title(self):
        return self.driver.title

    def open(self):
        self.driver.get(self.URL)

    def close_cookies_banner(self):
        self.wait.until(expected_conditions.visibility_of_element_located([By.ID, self.COOKIE_CLOSE]))
        cookie_btn = self.driver.find_element(By.ID, self.COOKIE_CLOSE)
        cookie_btn.click()

    def search_for_job(self, keyword, area = '', country = ''):
        self.wait.until(expected_conditions.visibility_of_element_located([By.XPATH, self.INPUT_JOB_SEARCH]))
        keyword_input = self.driver.find_element(By.XPATH, self.INPUT_JOB_SEARCH)
        keyword_input.send_keys(keyword)
        self._click_job_form_select_option(area, self.AREA_SELECT, 'All Areas')
        self._click_job_form_select_option(country, self.COUNTRY, 'All Countries')
        self.driver.find_element(By.XPATH, self.JOB_SEARCH_BUTTON).click()
        self.wait.until(expected_conditions.title_is(self.TITLE_ON_SEARCH))

    def assert_some_job_is_found(self, some_job):
        self.wait.until(expected_conditions.invisibility_of_element_located([By.ID, 'noresults']))
        all_job_results = self.driver.find_elements(By.XPATH, "//div//a[contains(@class, 'jobTitle-link')]")
        jobs_found = {}
        for job in all_job_results:
            jobs_found[job.text] = True
        if (some_job not in jobs_found):
            raise Exception(some_job + ' was not found within the search results')

    def _click_job_form_select_option(self, option_to_select, selectXpath, type_of_select):
        allOptionsElements = self.driver.find_elements(By.XPATH, selectXpath + '//option')
        actualOptions = {}
        for id, option in enumerate(allOptionsElements):
            actualOptions[option.get_attribute('value')] = id
        if (not option_to_select in actualOptions):
            raise Exception(option_to_select + ' was not found withing actual options')
        areas_select = self.driver.find_element(By.XPATH, self.JOB_ALERT_FORM + "//span[text()='" + type_of_select + "']")
        areas_select.click()
        area_to_select = self.driver.find_element(By.XPATH, self.JOB_ALERT_FORM + "//ul//li[@data-value='" + option_to_select + "']")
        area_to_select.click()