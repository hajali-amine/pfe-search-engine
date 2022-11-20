package scripts

import (
	"fmt"

	"github.com/tebeka/selenium"
)

func getTitle(offer selenium.WebDriver){
	
}

func ScrapOffers(driver selenium.WebDriver) {
    driver.Get("https://www.simplyhired.com/search?q=devops+internship&l=&job=WHoN7Js-7u7DphMDQnWutGqIk5Yqb5ACwjj4ERNs_QIc61EhAb9CUA")
	fmt.Println("Scrapping in progress...")
	jobOffers, err := driver.FindElements(selenium.ByClassName, "SerpJob-jobCard")
	if err != nil {
		panic(err)
	}
	for _, jobOffer := range jobOffers {
		title, err := jobOffer.FindElement(selenium.ByClassName, "jobposting-title")
		title, err := jobOffer.FindElement(selenium.ByClassName, "jobposting-title")
		title, err := jobOffer.FindElement(selenium.ByClassName, "jobposting-title")
		title, err := jobOffer.FindElement(selenium.ByClassName, "jobposting-title")

	}
	
	title, err := t[0].FindElement(selenium.ByClassName, "jobposting-title")
	fmt.Println(title.Text())

}