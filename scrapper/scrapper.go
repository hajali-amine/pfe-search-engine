package main

import (
	"searchengine/scrapper/driver"
	"searchengine/scrapper/loader"
	"searchengine/scrapper/scripts"
)

func main() {
	service, err := driver.GetChromeService()
	if err != nil {
		panic(err)
	}

	driver, err := driver.GetChromeDriver()
	if err != nil {
		panic(err)
	}

	conn, channel := loader.GetChannel()

	scripts.ScrapOffers(driver, channel)

	defer service.Stop()
	defer driver.Close()
	defer conn.Close()
	defer channel.Close()
}
