package driver

import (
	"github.com/tebeka/selenium"
	"github.com/tebeka/selenium/chrome"
)

func GetChromeDriver() (selenium.WebDriver, error) {
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

	return driver, err
}
