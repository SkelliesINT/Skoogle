# Skoogle

An automated Python based news scraper that takes the data collected and formats into a csv file for analysis. Utilizing Selenium for webdriving and Pandas for report formatting.

Purpose: 

Intended to be used as a cronjob/scheduled task script to automate the daily gathering of current news, specific to the user's interest, in a concise manner.

Dependencies:

- Microsoft Edge
- Python
- Selenium
- Pandas

Current capabilities:

* Google, Bing, DuckDuckGo:
	- Gathers  Article title
	- Gathers time since posted
	- Gathers news agency
	- Gathers URL link 
- Formats to CSV (Title, Agency, Time, Link)
- Ability to run headless or not

##Example Output
![image](https://user-images.githubusercontent.com/125293641/219120540-0014ca42-73a4-412a-85fa-6da1daa87a0a.png)
