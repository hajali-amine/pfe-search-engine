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
        data = driver.find_elements_by_css_selector(".data-details > span")
        company = data[0].text
        location = data[1].text
        position = data[2].text

        skills_bubbles = driver.find_elements_by_class_name("check-bubble")
        skills_text = [skill.text for skill in skills_bubbles]
        skills = "-".join(skills_text)

        writer.writerow([title, company, location, position, skills])
