from time import sleep
from selenium import webdriver 
import csv

driver = webdriver.Firefox() 
driver.get("https://www.careerbuilder.com/jobs?keywords=engineer&location=") 

elements = driver.find_elements_by_class_name("data-results-content-parent")

with open('output/internships.csv', 'w') as f:
    writer = csv.writer(f)
    for element in elements:
        element.click()
        title = driver.find_element_by_class_name("jdp_title_header").text
        data = driver.find_elements_by_css_selector("#jdp-data > div.apply-top-anchor.data-display-header > div.data-display-header_content > div > div.data-display-header_info-content.dib-m > div.data-details > span")
    
        company = data[0].text if len(data) == 3 else ""
        location = data[1].text if len(data) == 3 else ""
        position = data[2].text if len(data) == 3 else ""

        skills_bubbles = driver.find_elements_by_class_name("check-bubble")
        skills_text = [skill.text for skill in skills_bubbles]
        skills = "-".join(skills_text)

        writer.writerow([title, company, location, position, skills])
#jdp-data > div.apply-top-anchor.data-display-header > div.data-display-header_content > div > div.data-display-header_info-content.dib-m > div.data-details > span:nth-child(1)