package scripts

import (
	"fmt"
	"os"
	"regexp"
	"searchengine/scrapper/constants"
	"searchengine/scrapper/types"
	"strconv"
	"time"

	"github.com/tebeka/selenium"
)

const (
	INTERNSHIPS_WEBSITE_URL string = "https://www.simplyhired.com/search?q=devops+internship&l=&job=WHoN7Js-7u7DphMDQnWutGqIk5Yqb5ACwjj4ERNs_QIc61EhAb9CUA"
	OFFERS_CLASSNAME               = "SerpJob-jobCard"
	OFFERS_CSS                     = "#job-list > li > article"
	TITLE_CLASSNAME                = "jobposting-title"
	COMPANY_CLASSNAME              = "jobposting-company"
	LOCATION_CLASSNAME             = "jobposting-location"
	DESCRIPTION_CLASSNAME          = "jobposting-snippet"
	SKILLS_CLASSNAME               = "viewjob-qualification"
	NEXT_PAGE_CLASSNAME            = "next-pagination"
)

func getTitle(offer selenium.WebElement) string {
	titleElement, err := offer.FindElement(selenium.ByClassName, TITLE_CLASSNAME)
	if err != nil {
		panic(err)
	}
	title, err := titleElement.Text()

	return title
}

func getCompany(offer selenium.WebElement) string {
	companyElement, err := offer.FindElement(selenium.ByClassName, COMPANY_CLASSNAME)
	if err != nil {
		panic(err)
	}
	company, err := companyElement.Text()

	return company
}

func getLocation(offer selenium.WebElement) string {
	locationElement, err := offer.FindElement(selenium.ByClassName, LOCATION_CLASSNAME)
	if err != nil {
		panic(err)
	}
	location, err := locationElement.Text()

	re := regexp.MustCompile(", [A-Z]*")
	location = re.ReplaceAllString(location, "")

	return location
}

func getDescription(offer selenium.WebElement) string {
	descriptionElement, err := offer.FindElement(selenium.ByClassName, DESCRIPTION_CLASSNAME)
	if err != nil {
		panic(err)
	}
	description, err := descriptionElement.Text()

	return description
}

func getSkills(driver selenium.WebDriver, offer selenium.WebElement) []map[string]string {
	skills := []map[string]string{}

	offer.Click()
	// TODO: Find a better solution to wait for the page
	time.Sleep(2 * time.Second)

	skillsElements, err := driver.FindElements(selenium.ByClassName, SKILLS_CLASSNAME)
	if err != nil {
		panic(err)
	}

	for _, skillElement := range skillsElements {
		skill, _ := skillElement.Text()
		if theme, exists := constants.SkillsThemes[skill]; exists {
			skills = append(skills, map[string]string{skill: theme})
		}
	}
	return skills
}

func ScrapOffers(driver selenium.WebDriver) {
	driver.Get(INTERNSHIPS_WEBSITE_URL)

	fmt.Println("Scrapping in progress...")
	jobs := []types.Job{}
	nbPages, _ := strconv.Atoi(os.Getenv("NB_PAGES_TO_SCRAP"))

	for i := 0; i < nbPages; i++ {
		jobOffers, err := driver.FindElements(selenium.ByClassName, OFFERS_CLASSNAME)
		if err != nil {
			panic(err)
		}

		for _, jobOffer := range jobOffers {
			job := types.Job{
				Title:       getTitle(jobOffer),
				Description: getDescription(jobOffer),
				Location:    getLocation(jobOffer),
				Company:     getCompany(jobOffer),
				Skills:      getSkills(driver, jobOffer),
			}
			// ! This will be sent in RabbitMQ to the data loader
			jobs = append(jobs, job)
		}

		next, err := driver.FindElement(selenium.ByClassName, NEXT_PAGE_CLASSNAME)
		if err != nil {
			break
		}
		next.Click()
		time.Sleep(time.Second)
	}
	fmt.Println(jobs)
}
