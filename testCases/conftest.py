from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
import pytest
from selenium.webdriver.chrome.options import Options as ChromeOptions
from Configurations.Config import testdata
@pytest.fixture(params=["chrome"], scope='class')
def setup(request):
    if request.param=="chrome":

        chrome_options = ChromeOptions()
        chrome_options.add_argument("user-data-dir=F:\\testing\\KT")
        # chrome_options.add_extension("meta.crx")
        web_driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
        web_driver.get(testdata.app_url)
        web_driver.maximize_window()

    #if request.param=="firefox":
     #   web_driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    request.cls.driver = web_driver
    yield
    web_driver.close()