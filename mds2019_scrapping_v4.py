# -*- coding: utf-8 -*-
"""
Created on Tue May 14 12:01:29 2019

@author: carlos
"""

from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
import os

driver = webdriver.Firefox(executable_path=os.path.join(os.getcwd(),'geckodriver'))

driver.set_page_load_timeout(200)
driver.get("https://results.chronotrack.com/event/results/event/event-49653")

#inputElement = driver.find_element_by_id("resultsResultsTab").click()
seconds1 = time.time()

while True:
    try:
        element = wait(driver, 100).until(EC.presence_of_element_located((By.ID, "resultsResultsTab"))).click()
        print(element)
        break
    except:
       print("no funciono en",(-seconds1+time.time()))
       time.sleep(5)
       #driver.quit()
       
select = Select(driver.find_element_by_id('bazu-full-results-races'))

# select by visible text
select.select_by_visible_text('42K')
#driver.find_element_by_id("bazu-full-results-races").click()

select = Select(driver.find_element_by_id('bazu-full-results-paging'))

# select by visible text
select.select_by_visible_text('100')

table = driver.find_element_by_id("bazu-full-results-grid")

table_2=table.get_attribute('innerHTML')
soup = BeautifulSoup(table_2,"html.parser")

nombre = soup.find_all('td',{'class':"ui-widget-content bazu-name"})
for i in nombre:
    print(i.get_text())
    



time.sleep(5)
driver.quit()
print("hola1")
