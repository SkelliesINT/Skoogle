#Skoogle News Scraper
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
from selenium.webdriver.edge.options import Options as EdgeOptions
import pandas as pd
import time

# Settings Variables
NUMBER_OF_PAGES = 3
FILE_PATH_FOLDER = ('..')
HEADLESS = True
SEARCH_TERM = "cyber news"
VERSION = "0.0.4"
VERBOSE = False
WAIT_PER_SEARCH = 2
WAIT_PER_PAGE = 1

def get_google_news(driver,article_data_arrays):
	driver.get('https://google.com')
	ARTICLE_DIV_CLASS_NAME = "iRPxbe"
	TITLE_DIV_CLASS_NAME = "mCBkyc ynAwRc MBeuO nDgy9d"
	AGENCY_DIV_CLASS_NAME = "CEMjEf NUnG9d"
	DATE_DIV_CLASS_NAME = "OSrXXb ZE0LJd YsWzw"
	HREF_TAG_CLASS_NAME = "WlydOe"
	search_bar = driver.find_element(By.CLASS_NAME, 'gLFyf')
	search_bar.send_keys(SEARCH_TERM)
	search_bar.submit()
	time.sleep(WAIT_PER_SEARCH)
	news_tab = driver.find_element(By.XPATH, "//a[@data-hveid='CAEQAw']") or driver.find_element(By.XPATH, "//a[@data-hveid='CAMQAw']")
	news_tab.click()
	for pg_n in range(NUMBER_OF_PAGES):
		time.sleep(WAIT_PER_PAGE)
		n_articles = len(driver.find_elements(By.XPATH, f"//div[@class='{ARTICLE_DIV_CLASS_NAME}']"))

		print(f"Page {pg_n+1}: {n_articles} articles founds")
		
		for i in range(1,(n_articles+1)): # "i" is the article's top div
			article_title = driver.find_element(By.XPATH, f"//div[@class='MjjYud']/div[1]/div[{i}]//div[@class='{TITLE_DIV_CLASS_NAME}']")
			article_agency = driver.find_element(By.XPATH, f"//div[@class='MjjYud']/div[1]/div[{i}]//div[@class='{AGENCY_DIV_CLASS_NAME}']")
			article_date = driver.find_element(By.XPATH, f"//div[@class='MjjYud']/div[1]/div[{i}]//div[@class='{DATE_DIV_CLASS_NAME}']")
			article_link = driver.find_element(By.XPATH, f"//div[@class='MjjYud']/div[1]/div[{i}]//a[@class='{HREF_TAG_CLASS_NAME}']")
			article_data = [article_title.text,article_agency.text,article_date.text,article_link.get_attribute("href")]
			article_data_arrays.append(article_data)
			print(f"Article {i}: {article_title.text}")
		if NUMBER_OF_PAGES > 1:
			next_button = driver.find_element(By.ID, 'pnnext')
			next_button.click()

def get_bing_news(driver,article_data_arrays):
	driver.get("https://www.bing.com/news")
	search_bar = driver.find_element(By.XPATH, "//input[@class='b_searchbox']")
	search_bar.send_keys(SEARCH_TERM)
	search_bar.submit()
	time.sleep(0.5)
	time_sort_button = driver.find_element(By.XPATH, "//div[@id='newsFilterV5']//a[@role='button']")
	time_sort_button.click()
	time.sleep(0.25)
	last_24_hours_button = driver.find_element(By.XPATH, "//div[@id='newsFilterV5']//ul[@role='list']/li[2]/a[1]")
	last_24_hours_button.click()
	time.sleep(WAIT_PER_SEARCH)
	n_articles = NUMBER_OF_PAGES*10
	for i in range(1,n_articles+1):
		article = None
		while not article:
			try:
				article = driver.find_element(By.XPATH, f"//div[@class='algocore']/div[{i}]")
			except:
				driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
				time.sleep(WAIT_PER_PAGE)
		article_title = article.get_attribute("data-title")
		article_agency = article.get_attribute("data-author")
		article_date = driver.find_element(By.XPATH, f"//div[@class='algocore']/div[{i}]//span[@tabindex=0]")
		article_link = article.get_attribute("url")
		article_data = [article_title,article_agency,article_date.text,article_link]
		article_data_arrays.append(article_data)


def get_yandex_news(driver,article_data_arrays):
	pass

def get_ddg_news():
	pass

def get_yandex_news():
	pass

def get_hn_news():
	pass

def get_krebsonsec_news():
	pass

def remove_duplicates():
	pass

def sort_recent():
	pass

def main():
	article_data_arrays = []
	options = EdgeOptions()
	if HEADLESS:
		options.add_argument("--headless=new")

	driver = webdriver.Edge(options=options)

	get_google_news(driver,article_data_arrays)
	get_bing_news(driver,article_data_arrays)

	article_data_frame = pd.DataFrame(article_data_arrays)
	article_data_frame.columns = ['title', 'agency', 'text','link']
	article_data_frame.to_csv('articles.csv',  index=False)

	time.sleep(1)
	driver.quit()

if __name__ == "__main__":
	main()