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

time.sleep(3)
Select(driver.find_element_by_id('bazu-full-results-races')).select_by_visible_text('42K')
time.sleep(3)
#driver.find_element_by_id("bazu-full-results-races").click()
Select(driver.find_element_by_id('bazu-full-results-paging')).select_by_visible_text('100')
time.sleep(3)


result =  pd.DataFrame({'Rank':[] , 'Nombre':[],'Número':[] , 'Tiempo':[],'Ritmo':[] , 'Ciudad de Residencia':[],'Division':[] , 'Rango en Division':[]})

table = driver.find_element_by_id("bazu-full-results-grid")
table_2=table.get_attribute('innerHTML')
soup = BeautifulSoup(table_2,"html.parser")
rank = soup.find_all('td',{'class':"ui-widget-content bazu-rank"})
nombre = soup.find_all('td',{'class':"ui-widget-content bazu-name"})
numero= soup.find_all('td',{'class':"ui-widget-content bazu-bib"})
tiempo= soup.find_all('td',{'class':"ui-widget-content bazu-time"})
ritmo= soup.find_all('td',{'class':"ui-widget-content bazu-pace"})
ciudad= soup.find_all('td',{'class':"ui-widget-content bazu-hometown"})
division= soup.find_all('td',{'class':"ui-widget-content bazu-agroup"})
rango= soup.find_all('td',{'class':"ui-widget-content bazu-agrank"})

for i in range(len(nombre)):
    new_runner = pd.DataFrame({'Rank':[rank[i].get_text()] , 'Nombre':[nombre[i].get_text()],'Número':[numero[i].get_text()], 'Tiempo':[tiempo[i].get_text()],'Ritmo':[ritmo[i].get_text()] , 'Ciudad de Residencia':[ciudad[i].get_text()],'Division':[division[i].get_text()] , 'Rango en Division':[rango[i].get_text()]},index=[int(rank[i].get_text())] )
    result = result.append(new_runner)
nombre2=nombre

Pagina=1
while True:
    Pagina=Pagina+1
    print("Estamos en la Pagina: "+ str(Pagina))
    wait(driver, 100).until(EC.presence_of_element_located((By.ID, 'bazu-full-results-grid_next'))).click()
    time.sleep(6)
    table = driver.find_element_by_id("bazu-full-results-grid")
    table_2=table.get_attribute('innerHTML')
    soup = BeautifulSoup(table_2,"html.parser")
    rank = soup.find_all('td',{'class':"ui-widget-content bazu-rank"})
    nombre = soup.find_all('td',{'class':"ui-widget-content bazu-name"})
    numero= soup.find_all('td',{'class':"ui-widget-content bazu-bib"})
    tiempo= soup.find_all('td',{'class':"ui-widget-content bazu-time"})
    ritmo= soup.find_all('td',{'class':"ui-widget-content bazu-pace"})
    ciudad= soup.find_all('td',{'class':"ui-widget-content bazu-hometown"})
    division= soup.find_all('td',{'class':"ui-widget-content bazu-agroup"})
    rango= soup.find_all('td',{'class':"ui-widget-content bazu-agrank"})

    if nombre2==nombre:
        print("No existe más next")
        break 

    for i in range(len(nombre)):
        new_runner = pd.DataFrame({'Rank':[rank[i].get_text()] , 'Nombre':[nombre[i].get_text()],'Número':[numero[i].get_text()], 'Tiempo':[tiempo[i].get_text()],'Ritmo':[ritmo[i].get_text()] , 'Ciudad de Residencia':[ciudad[i].get_text()],'Division':[division[i].get_text()] , 'Rango en Division':[rango[i].get_text()]},index=[int(rank[i].get_text())] )
        result = result.append(new_runner)


    nombre2=nombre

time.sleep(20)
result.to_csv("file_name.csv",encoding='utf-8-sig', index=False)
driver.quit()
print("hola1")
