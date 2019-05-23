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
import pandas as pd

driver = webdriver.Firefox(executable_path=os.path.join(os.getcwd(),'geckodriver'))

driver.set_page_load_timeout(200)
driver.get("https://results.chronotrack.com/event/results/event/event-49653")

#inputElement = driver.find_element_by_id("resultsResultsTab").click()
seconds1 = time.time()

while True:
    try:
        wait(driver, 100).until(EC.presence_of_element_located((By.ID, "resultsResultsTab"))).click()
        break
    except:
       print("no funciono en",(-seconds1+time.time()))
       time.sleep(5)
       #driver.quit()
time.sleep(4)  
Select(driver.find_element_by_id('bazu-full-results-races')).select_by_visible_text('42K')
#driver.find_element_by_id("bazu-full-results-races").click()

time.sleep(4)
Select(driver.find_element_by_id('bazu-full-results-paging')).select_by_visible_text('100')
time.sleep(4)
# select by visible text

table = driver.find_element_by_id("bazu-full-results-grid")

table_2=table.get_attribute('innerHTML')
soup = BeautifulSoup(table_2,"html.parser")

results = pd.DataFrame({'nombre':[],'tiempo':[]})

nombre = soup.find_all('td',{'class':"ui-widget-content bazu-name"})
time_runner = soup.find_all('td',{'class':"ui-widget-content bazu-time"})
hometown = soup.find_all('td',{'class':"ui-widget-content bazu-hometown"})
categoria_edad = soup.find_all('td',{'class':"ui-widget-content bazu-agroup"})
rank = soup.find_all('td',{'class':"ui-widget-content bazu-rank"})


for i in range(len(nombre)):
    new_runner = pd.DataFrame({'nombre':[nombre[i].get_text()],'tiempo':time_runner[i].get_text()},index=[int(rank[i].get_text())])
    results=results.append(new_runner)
pagina=0    

while True:
    pagina = pagina+1    
    print("siguiente página "+str(pagina))
    time.sleep(4)
    wait(driver, 100).until(EC.presence_of_element_located((By.ID, "bazu-full-results-grid_next"))).click()
    time.sleep(4)
    table = driver.find_element_by_id("bazu-full-results-grid")

    table_2=table.get_attribute('innerHTML')
    soup = BeautifulSoup(table_2,"html.parser")
    
    nombre = soup.find_all('td',{'class':"ui-widget-content bazu-name"})
    time_runner = soup.find_all('td',{'class':"ui-widget-content bazu-time"})
    hometown = soup.find_all('td',{'class':"ui-widget-content bazu-hometown"})
    categoria_edad = soup.find_all('td',{'class':"ui-widget-content bazu-agroup"})
    rank = soup.find_all('td',{'class':"ui-widget-content bazu-rank"})

    for i in range(len(nombre)):
        new_runner = pd.DataFrame({'nombre':[nombre[i].get_text()],'tiempo':time_runner[i].get_text()},index=[int(rank[i].get_text())])
        results=results.append(new_runner)
    
    if len(nombre)<100:
        break


time.sleep(5)
driver.quit()
print("hola1")
