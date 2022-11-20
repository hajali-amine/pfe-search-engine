package main

import (
	"os"
	"searchengine/scrapper/scripts"

	"github.com/tebeka/selenium"
	"github.com/tebeka/selenium/chrome"
)

func main() {
	// Run Chrome browser
	service, err := selenium.NewChromeDriverService(os.Getenv("CHROME_DRIVER_PATH"), 4444)
	if err != nil {
		panic(err)
	}
	defer service.Stop()

	caps := selenium.Capabilities{}
	caps.AddChrome(chrome.Capabilities{Args: []string{
		"window-size=1920x1080",
		"--no-sandbox",
		"--disable-dev-shm-usage",
		"disable-gpu",
		"--headless",
	}})

	driver, err := selenium.NewRemote(caps, "")
	if err != nil {
		panic(err)
	}
	scripts.ScrapOffers(driver)
}
