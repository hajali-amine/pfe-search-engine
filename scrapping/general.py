from selenium.webdriver.firefox.options import Options

from selenium import webdriver
from selenium.webdriver.common.by import By
import re
import json


def get_driver(SITE_URL):
    options = Options()
    options.headless = True
    driver = webdriver.Firefox(options=options)
    driver.get(SITE_URL)
    return driver



def get_page_offers(driver, OFFER_DIV_TAG):
    offers = driver.find_elements(By.TAG_NAME, OFFER_DIV_TAG)
    return offers


def load_skills():
    f = open('scrapping/skills.json')
    skills = json.load(f)
    return skills


def get_title(offer, TITLE_TAG_NAME, SEARCH_TAG):
    if SEARCH_TAG == 'TAG_NAME':
        title_tag = offer.find_element(By.TAG_NAME, TITLE_TAG_NAME)

    elif SEARCH_TAG == 'CLASS_NAME':
        title_tag = offer.find_element(By.CLASS_NAME, TITLE_TAG_NAME)

    title = title_tag.text
    title = title.replace('Intern, ', '')
    title = title.replace('Intern', '')
    return title


def get_company(offer, COMPANY_TAG_NAME, COMPANY_SEARCH_TAG):
    if COMPANY_SEARCH_TAG == 'TAG_NAME':
        company_div = offer.find_element(By.TAG_NAME, COMPANY_TAG_NAME)

    elif COMPANY_SEARCH_TAG == 'CLASS_NAME':
        company_div = offer.find_element(By.CLASS_NAME, COMPANY_TAG_NAME)

    company = company_div.text
    return company


def get_location(offer, LOCATION_TAG_NAME, LOCATION_SEARCH_TAG):
    if LOCATION_SEARCH_TAG == 'TAG_NAME':
        location_div = offer.find_element(By.TAG_NAME, LOCATION_TAG_NAME)

    elif LOCATION_SEARCH_TAG == 'CLASS_NAME':
        location_div = offer.find_element(By.CLASS_NAME, LOCATION_TAG_NAME)
    location_name = location_div.text
    location = re.sub(', [A-Z]*', '', location_name)
    return location


def get_description(offer, DESCRIPTION_TAG_NAME, DESCRIPTION_SEARCH_TAG):
    if DESCRIPTION_SEARCH_TAG == 'TAG_NAME':
        description_div = offer.find_element(By.TAG_NAME, DESCRIPTION_TAG_NAME)

    elif DESCRIPTION_SEARCH_TAG == 'CLASS_NAME':
        description_div = offer.find_element(By.CLASS_NAME, DESCRIPTION_TAG_NAME)
    description = description_div.text

    return description


def get_logo(offer, LOGO_TAG_NAME, LOGO_SEARCH_TAG):
    if LOGO_SEARCH_TAG == 'TAG_NAME':
        logo_div = offer.find_element(By.TAG_NAME, LOGO_TAG_NAME)

    elif LOGO_SEARCH_TAG == 'CLASS_NAME':
        logo_div = offer.find_element(By.CLASS_NAME, LOGO_TAG_NAME)
    # logo = "https://www.simplyhired.com/" + logo_div.get_attribute('src')
    logo = logo_div.get_attribute('src')
    

    return logo