from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#scrap_user = input("Enter your username: ")
#scrap_link = "https://github.com/" + scrap_user

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://github.com/Samikmalhotra")

name=driver.find_element_by_tag_name("h1").text.split('\n')
name_of_user = name[0]
username = name[1]

no_of_repos = driver.find_element_by_class_name("Counter").text

contri_last_year = driver.find_element_by_xpath("//h2[@class='f4 text-normal mb-2']").text.split(" ")[0]

followings = driver.find_elements_by_xpath("//span[@class='text-bold color-text-primary']")
followers = followings[0].text
following = followings[1].text
star_repo = followings[2].text

web = driver.find_elements_by_xpath("//a[@class='Link--primary ']")

driver.quit()

startdate = input("Enter start date in YYYY-MM-DD format: ")
enddate = input("Enter end date in YYYY-MM-DD format: ")
link = "https://github.com/Samikmalhotra?tab=overview&from="+startdate+"&to="+enddate
print(link)