from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

username = input("Enter your user name: ")
startdate = input("Enter the start date in YYYY-MM-DD format: ")
enddate = input("Enter the end date in YYYY-MM-DD format: ")
link = "https://github.com/"+username+"?tab=overview&from="+startdate+"&to="+enddate

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get(link)

spec = driver.find_elements_by_xpath("//div[@class='TimelineItem']")

if not spec:
    print("------------------------------>")
    print("No activity in this period")
    print("------------------------------>")
else:
    print("------------------------------>")
    for i in range(len(spec)):
        print(spec[i].text)
        print("------------------------------>")