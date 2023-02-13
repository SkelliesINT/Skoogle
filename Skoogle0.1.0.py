#Skoogle | Version: 0.1.0
#An automated google cyber news scraper utilizing the Selenium webdriver on Microsoft Edge and Pandas for report generating.
#By: SkelliesINT
#Collaborators: Jack Sledge

# Copyright (C) 2023 Devon Hughes
#
#  skelsec@proton.me
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>. 

from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time

FILE_PATH_FOLDER = ('..')
article_data_arrays = []
NUMBER_OF_PAGES = 10

driver = webdriver.Edge()

driver.get('https://google.com')

search_bar = driver.find_element(By.CLASS_NAME, 'gLFyf')
search_bar.send_keys('Cyber news')
search_bar.submit()
time.sleep(2)
news_tab = driver.find_element(By.XPATH, "//a[@data-hveid='CAEQAw']") or driver.find_element(By.XPATH, "//a[@data-hveid='CAMQAw']")
news_tab.click()

ARTICLE_DIV_CLASS_NAME = "iRPxbe"
TITLE_DIV_CLASS_NAME = "mCBkyc ynAwRc MBeuO nDgy9d"
AGENCY_DIV_CLASS_NAME = "CEMjEf NUnG9d"
DATE_DIV_CLASS_NAME = "OSrXXb ZE0LJd YsWzw"

for pg_n in range(NUMBER_OF_PAGES):
	time.sleep(1)
	n_articles = len(driver.find_elements(By.XPATH, "//div[@class='iRPxbe']"))
	print(f"Page {pg_n+1}: {n_articles} articles founds")
	for i in range(1,(n_articles+1)): # "i" is the article's top div
		article_title = driver.find_element(By.XPATH, f"//div[@class='MjjYud']/div[1]/div[{i}]/div[1]/div[1]/a[1]/div[1]/div[@class='{ARTICLE_DIV_CLASS_NAME}']/div[@class='{TITLE_DIV_CLASS_NAME}']")
		article_agency = driver.find_element(By.XPATH, f"//div[@class='MjjYud']/div[1]/div[{i}]/div[1]/div[1]/a[1]/div[1]/div[@class='{ARTICLE_DIV_CLASS_NAME}']/div[@class='{AGENCY_DIV_CLASS_NAME}']")
		article_date = driver.find_element(By.XPATH, f"//div[@class='MjjYud']/div[1]/div[{i}]/div[1]/div[1]/a[1]/div[1]/div[@class='{ARTICLE_DIV_CLASS_NAME}']/div[@class='{DATE_DIV_CLASS_NAME}']")
		article_data = [article_title.text,article_agency.text,article_date.text]
		article_data_arrays.append(article_data)
		print(f"Article {i}: {article_title.text}")
	if NUMBER_OF_PAGES > 1:
		next_button = driver.find_element(By.ID, 'pnnext')
		next_button.click()

article_data_frame = pd.DataFrame(article_data_arrays)
article_data_frame.columns = ['title', 'agency', 'text']
article_data_frame.to_csv('article_stuff.csv',  index=False)

time.sleep(1)
driver.quit()

