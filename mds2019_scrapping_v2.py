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

element = wait(driver, 10).until(EC.presence_of_element_located((By.ID, "resultsResultsTab")))
element.click()

select = Select(driver.find_element_by_id('bazu-full-results-races'))

# select by visible text
select.select_by_visible_text('42K')
#driver.find_element_by_id("bazu-full-results-races").click()


time.sleep(5)
driver.quit()