package main

import (
	"os"
	webDriver "searchengine/scrapper/driver"
	loader "searchengine/scrapper/loader"
	log "searchengine/scrapper/logger"
	scripts "searchengine/scrapper/scripts"
)

func main() {
	logger := log.BuildLogger()

	service, err := webDriver.GetChromeService()
	if err != nil {
		logger.Errorw("Failed to run Chrome", "error", err)
		os.Exit(1)
	}
	logger.Infow("Run Chrome service successfully")
	defer service.Stop()

	driver, err := webDriver.GetChromeDriver()
	if err != nil {
		logger.Errorw("Failed to acquire Selenium Driver", "error", err)
		os.Exit(1)
	}
	logger.Infow("Instantiated Selenium's WebDriver")
	defer driver.Close()

	conn, channel, err := loader.GetChannel()
	if err != nil {
		logger.Errorw("Failed to connect to RabbitMQ", "error", err)
		os.Exit(1)
	}
	logger.Infow("Connected to RabbitMQ")
	defer conn.Close()
	defer channel.Close()

	scriptLogger := logger.With("Component", "Scrapper.ScriptLogger")
	scripts.ScrapOffers(driver, channel, scriptLogger)
}
