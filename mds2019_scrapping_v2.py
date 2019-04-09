from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support.ui import Select

driver = webdriver.Firefox(executable_path=r'C:\Users\carlos\Documents\Semestre 13\TICS\Trabajo\trabajo\geckodriver')

driver.set_page_load_timeout(10)
driver.get("https://results.chronotrack.com/event/results/event/event-49653")

#inputElement = driver.find_element_by_id("resultsResultsTab").click()

element = wait(driver, 20).until(EC.presence_of_element_located((By.ID, "resultsResultsTab")))
element.click()

select = Select(driver.find_element_by_id('bazu-full-results-races'))

# select by visible text
select.select_by_visible_text('42K')
#driver.find_element_by_id("bazu-full-results-races").click()

select = Select(driver.find_element_by_id('bazu-full-results-paging'))

# select by visible text
select.select_by_visible_text('100')

table = driver.find_element_by_id("bazu-full-results-grid")
rows = table.find_elements(By.TAG_NAME, "tr") # get all of the rows in the table

table_id = wait(driver, 10).until(EC.presence_of_element_located((By.ID, 'bazu-full-results-grid')))
rows = table_id.find_elements(By.TAG_NAME, "tr") # get all of the rows in the table
for row in rows:
    hola = row.get_attribute('innerHTML')
    print(hola)
'''
for row in rows:
    # Get the columns (all the column 2)        
    print(row)
    #col = row.find_elements(By.TAG_NAME, "td") #note: index start from 0, 1 is col 2
    #print(col) #prints text from the elementtable)
'''
time.sleep(5)
driver.quit()