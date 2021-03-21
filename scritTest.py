from datetime import datetime
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\Users\\DELL\\Downloads\\chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(10)
listOfCities = ['Milford', 'Trumbull', 'Norwalk', 'Stamford', 'Sharon', 'Fairfield']


def checkDate():
    dateText = driver.find_element_by_id("ctl00_cphBody_GridView1_ctl02_Label1").text[0:10]
    today = datetime.now()
    date1 = datetime.strptime(dateText, "%m/%d/%Y")
    print(type(date1))
    if (today - date1).days < 7 or today == date1:
        return True
    else:
        print('Date is so older')
    return False


def executeScript():
    sleep(5)
    if checkDate():
        driver.find_element_by_link_text("View Full Notice").send_keys(Keys.CONTROL + Keys.RETURN)
        driver.execute_script("window.history.go(-1)")
    else:
        print('ERROR')


for i in listOfCities:
    print(i)
    driver = webdriver.Chrome(executable_path="C:\\Users\\DELL\\Downloads\\chromedriver.exe")
    driver.get("https://sso.eservices.jud.ct.gov/Foreclosures/Public/PendPostbyTownList.aspx")
    driver.maximize_window()
    sleep(10)
    driver.find_element_by_link_text(str(i)).click()
    executeScript()

