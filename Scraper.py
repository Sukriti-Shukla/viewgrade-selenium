from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
# Github credentials
username = "username"
password = "password"

def scraper(rollNumber:str=None, password:str=None)->str:
    if (rollNumber is None or password is None):
        raise KeyError("You must specify RollNumber and Password")
    try:
        driver = webdriver.Chrome("chromedriver")
        driver.get("https://www.iitm.ac.in/viewgrades/")
        driver.find_element_by_xpath('/html/body/div/div[1]/form/center/table[1]/tbody/tr[1]/td[2]/input').send_keys(username)
        password = driver.find_element_by_xpath('/html/body/div/div[1]/form/center/table[1]/tbody/tr[2]/td[2]/input').send_keys(password)
        submit = driver.find_element_by_xpath('/html/body/div/div[1]/form/center/table[2]/tbody/tr/td[1]/input').click()
        WebDriverWait(driver=driver, timeout=10).until(lambda x: x.execute_script("return document.readyState === 'complete'"))
        error_message = "Incorrect username or password."
        errors = driver.find_elements_by_class_name("flash-error")
        if any(error_message in e.text for e in errors):
            print("[!] Login failed")
        else:
            print("[+] Login successful")
        grade_html= driver.find_element_by_tag_name('html').get_attribute('innerHTML')
        return grade_html
    except:
        return 'server error'
