import pandas as pd
import requests
from bs4 import BeautifulSoup as soup 
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager
from flask_pymongo import PyMongo
from flask import Flask, render_template, redirect


def scrape():
    return_dict  = {}

    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
    url = 'https://redplanetscience.com/'
    browser.visit(url)
    
    html = browser.html
    red_planet =soup(html,"html.parser") 

    news = red_planet.select_one("div.list_text")

    news_title  = news.find("div", class_= "content_title").get_text()
    return_dict["news_title"] = news_title

    news_p = news.find("div", class_= "article_teaser_body").get_text()
    return_dict["news_p"] = news_p

    news_date = news.find("div", class_= "list_date").get_text()
    return_dict["news_date"] = news_date

    url = 'https://spaceimages-mars.com/'
    browser.visit(url)

    html = browser.html
    space_image =soup(html,"html.parser") 

    image_element = space_image.select_one("img.headerimage.fade-in")
   
    featured_image_url = url + image_element["src"]
    return_dict["featured_image_url"] = featured_image_url
    
    url = 'https://galaxyfacts-mars.com/'
    Mars_facts_tables = pd.read_html(url)

    Mars_facts = Mars_facts_tables[0]

    Mars_facts.columns=['Description', 'Mars', 'Earth']
    Mars_facts.set_index('Description', inplace=True)

    html_Mars_facts = Mars_facts.to_html(classes="table")
    return_dict["html_Mars_facts"] = html_Mars_facts


    url = 'https://marshemispheres.com/'
    browser.visit(url)

    links = browser.find_by_css("a.product-item img")
    number_of_links = range(len(links))
    mars_hemispheres = []


    for index in number_of_links:
        hemispheres = {}
        browser.find_by_css("a.product-item img")[index].click()
        title_text = browser.find_by_css("h2.title").text
        mars_image = browser.links.find_by_text("Sample").first["href"]
        hemispheres["title"] = title_text
        hemispheres["img_url"] = mars_image
        mars_hemispheres.append(hemispheres)
        browser.back()

    return_dict["mars_hemispheres"]  = mars_hemispheres              
    browser.quit()

    return (return_dict)


    