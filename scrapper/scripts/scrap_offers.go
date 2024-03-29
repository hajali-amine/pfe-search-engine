package scripts

import (
	"os"
	"regexp"
	"searchengine/scrapper/constants"
	"searchengine/scrapper/loader"
	"searchengine/scrapper/types"
	"strconv"
	"time"

	amqp "github.com/rabbitmq/amqp091-go"
	"github.com/tebeka/selenium"
	"go.uber.org/zap"
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

// * Support logos in future versions
func getLogo(offer selenium.WebElement) string {
	return "to be supported"
}

// * Support links in future versions
func getLink(offer selenium.WebElement) string {
	return "to be supported"
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

func getSkills(driver selenium.WebDriver, offer selenium.WebElement) []*types.Job_Skills {
	skills := []*types.Job_Skills{}

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
			skills = append(skills, &types.Job_Skills{Skill: skill, Theme: theme})
		}
	}
	return skills
}

func ScrapOffers(driver selenium.WebDriver, channel *amqp.Channel, logger *zap.SugaredLogger) {
	err := driver.Get(INTERNSHIPS_WEBSITE_URL)
	if err != nil {
		logger.Errorw("Couldn't get website to scrap", "error", err)
	}

	logger.Infow("Scrapping in progress...")
	nbPages, _ := strconv.Atoi(os.Getenv("NB_PAGES_TO_SCRAP"))

	for i := 0; i < nbPages; i++ {
		jobOffers, err := driver.FindElements(selenium.ByClassName, OFFERS_CLASSNAME)
		if err != nil {
			logger.Errorw("Couldn't get offer", "error", err)
		}

		for _, jobOffer := range jobOffers {
			job := types.Job{
				Title:       getTitle(jobOffer),
				Description: getDescription(jobOffer),
				Location:    getLocation(jobOffer),
				Company:     getCompany(jobOffer),
				Logo:        getLogo(jobOffer),
				Link:        getLink(jobOffer),
				Skills:      getSkills(driver, jobOffer),
			}
			logger.Infow("Scrapped a new offer", "offer", job)
			err := loader.PublishMsg(channel, &job)
			if err != nil {
				logger.Errorw("Message failed to publish", "error", err)
			}
		}
		next, err := driver.FindElement(selenium.ByClassName, NEXT_PAGE_CLASSNAME)
		if err != nil {
			logger.Errorw("Couldn't change page", "error", err)
		}
		next.Click()
		time.Sleep(time.Second)
		logger.Infow("Next page", "pageNumber", i+1)
	}
}
