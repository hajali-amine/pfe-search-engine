package driver

import (
	"os"

	"github.com/tebeka/selenium"
)

func GetChromeService() (*selenium.Service, error) {
	// Run Chrome browser
	service, err := selenium.NewChromeDriverService(os.Getenv("CHROME_DRIVER_PATH"), 4444)
	if err != nil {
		panic(err)
	}

	return service, err
}
