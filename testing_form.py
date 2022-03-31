import time

import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()
def setUp():
    global movieName, release, director, producer, language,driver
    movieName = input("Enter movie name:")
    release = input("Enter movie realease data")
    director = input("Enter movie director name")
    producer = input("Enter movie producer name")
    language = input("Enter movie language name")
    distributor = input("Enter movie distrubutor ")
    driver=webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    yield
    time.sleep(5)
    driver.close()
def test_form(setUp):
    driver.get("https://iprimedtraining.herokuapp.com/movie.php")
    driver.find_element_by_name("mname").send_keys(movieName)
    driver.find_element_by_name("myear").send_keys(release)
    driver.find_element_by_name("mdirector").send_keys(director)
    driver.find_element_by_name("mdist").send_keys(distributor)
    driver.find_element_by_name("mproducer").send_keys(producer)
    driver.find_element_by_name("mlang").send_keys(language)
    driver.find_element_by_name("subbtn").click()
    time.sleep(1)



