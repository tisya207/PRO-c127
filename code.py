from bs4 import BeautifulSoup
from selenium import webdriver
import requests
import time
import csv

start_url= "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
browser= webdriver.Chrome("./chromedriver")

browser.get(start_url)
time.sleep(10)

def scrape():
    headers= ["Proper Name", "Distance", "Mass", "Radius"]
    star_data=[]
    soup= BeautifulSoup(browser.page_source,"html.parser")
    for tr_tag in soup.find_all("tr",attrs={"class","expo-planet"}):
        t_tags= tr_tag.find_all("tr")
        temp=[]
        for index, t_tags in enumerate(t_tags):
            if index==0:
                temp.append(t_tags.find_all("a")[0].contents[0])
            else:
                try:
                    temp.append(t_tags.contents[0])
                except:
                    temp.append("")
        star_data.append(temp)
    with open("scraper.csv","w") as f:
        csv_w= csv.writer(f)
        csv_w.writerow(headers)
        csv_w.writerows(star_data)

scrape()