import json
import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from general import get_driver, get_company, get_location, get_page_offers, get_title, load_skills, get_description, get_logo


def parse_offers(site, driver):
    offers_data = []
    OFFER_DIV_TAG = site["OFFER_DIV_TAG"]

    while True:
        try:
            offers = get_page_offers(driver, OFFER_DIV_TAG)
            nextPage_offers_data = [get_offer_data(
                site, driver, offer) for offer in offers]
            offers_data.extend(nextPage_offers_data)
            nextPage = driver.find_elements(By.CLASS_NAME, 'next-pagination')
            nextPage[0].click()
        except:
            break

    return(offers_data)


def get_skills(driver, offer):
    skills_array = load_skills()

    skills = []

    DETAILS_TAG_NAME = 'card'
    openDetails = WebDriverWait(offer, 10).until(
        EC.presence_of_element_located(
            (By.CLASS_NAME, DETAILS_TAG_NAME))
    )
    openDetails.click()
    QUALIFICATIONS_TAG_NAME = 'viewjob-qualification'
    qualifications = []
    while qualifications == []:

        qualifications = driver.find_elements(
            By.CLASS_NAME, QUALIFICATIONS_TAG_NAME)

    # for qualification in qualifications:
    #     if(not (qualification.text in skills_array)):
    #         with open("skills.txt", "a") as file_object:
    #             file_object.write('\n' + qualification.text)

    #     skills.append(qualification.text)

    for qualification in qualifications:
        if (qualification.text in skills_array):
            item = {
                qualification.text: skills_array[qualification.text]
            }
            skills.append(item)

    DESCRIPTION_TAG_NAME = 'viewjob-jobDescription'

    description_div = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located(
            (By.CLASS_NAME, DESCRIPTION_TAG_NAME))
    )

    description_p = description_div.find_element(By.CLASS_NAME, 'p')
    description = description_p.text

    for item in skills_array:
        skill = description.find(item)
        skill_tuple = {
            item: skills_array[item]
        }
        skill_exists_already = skill_tuple in skills
        if((skill >= 0) and not (skill_exists_already)):
            skills.append(skill_tuple)

    return skills


def get_offer_data(site, driver, offer):

    # GET TITLE
    TITLE_TAG_NAME = site["TITLE_TAG_NAME"]
    TITLE_SEARCH_TAG = site["TITLE_SEARCH_TAG"]
    title = get_title(offer, TITLE_TAG_NAME, TITLE_SEARCH_TAG)
    print(title)

    # GET COMPANY
    COMPANY_TAG_NAME = site["COMPANY_TAG_NAME"]
    COMPANY_SEARCH_TAG = site["COMPANY_SEARCH_TAG"]
    company = get_company(offer, COMPANY_TAG_NAME, COMPANY_SEARCH_TAG)

    # GET LOCATION
    LOCATION_TAG_NAME = site["LOCATION_TAG_NAME"]
    LOCATION_SEARCH_TAG = site["LOCATION_SEARCH_TAG"]
    location = get_location(offer, LOCATION_TAG_NAME, LOCATION_SEARCH_TAG)
    
    
    # GET DESCRIPTION
    DESCRIPTION_TAG_NAME = site["DESCRIPTION_TAG_NAME"]
    DESCRIPTION_SEARCH_TAG = site["DESCRIPTION_SEARCH_TAG"]
    description = get_description(offer, DESCRIPTION_TAG_NAME, DESCRIPTION_SEARCH_TAG)
    
    
    # GET SKILLS
    skills = get_skills(driver, offer)
    
    # # GET LOGO
    # DETAILS_TAG_NAME = 'card'
    # openDetails = WebDriverWait(offer, 10).until(
    #     EC.presence_of_element_located(
    #         (By.CLASS_NAME, DETAILS_TAG_NAME))
    # )
    # openDetails.click()
    # LOGO_TAG_NAME = site["LOGO_TAG_NAME"]
    # LOGO_SEARCH_TAG = site["LOGO_SEARCH_TAG"]
    # logo = get_logo(driver, LOGO_TAG_NAME, LOGO_SEARCH_TAG)
    logo=''

    return {
        'title': title,
        'description':description,
        "logo":logo,
        'company': company,
        'location': location,
        'skills': skills,
    }



def scrap_data_to_load(url, event):
    # site = json.loads(event['body'])
    site=event

    SITE_URL =site["SITE_URL"]
    # Creating driver
    driver = get_driver(SITE_URL)
   
    # get the offers
    print('Parsing the offres ...')
    OFFER_DIV_TAG = site["OFFER_DIV_TAG"]
    offers = get_page_offers(driver, OFFER_DIV_TAG)
    # offers_data = [get_offer_data(site, driver, offer) for offer in offers]
    for offer in offers:
        data = get_offer_data(site, driver, offer)
        # offers_data = parse_offers(site, driver)
        print(data)
        _ = requests.post(url, json=data)

    driver.close();
    driver.quit();
