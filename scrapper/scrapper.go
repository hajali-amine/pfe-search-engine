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
	defer service.Stop()

	driver, err := driver.GetChromeDriver()
	if err != nil {
		panic(err)
	}
	defer driver.Close()

	conn, channel := loader.GetChannel()
	defer conn.Close()
	defer channel.Close()
	
	scripts.ScrapOffers(driver, channel)
}
