FROM golang

# TODO: minimize the size of the image - yaay, optimization time
# ? Can I make it a multistage build where I take the chrome binary and the chrome driver to the final container?

# Install Chrome
RUN apt-get -y update
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list'
RUN apt-get -y update

# Install Chrome driver
RUN apt-get install -y google-chrome-stable
RUN apt-get install -yqq unzip curl
RUN wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`/chromedriver_linux64.zip
RUN unzip /tmp/chromedriver.zip chromedriver -d .

# Set path to Chrome driver
ENV CHROME_DRIVER_PATH=/go/chromedriver

# Copy scrapper and install dependencies
WORKDIR /app
COPY ./go.* /app/
RUN go mod download

ENV NB_PAGES_TO_SCRAP=5
ENV RABBITMQ_URL=localhost

ENV WAIT_VERSION 2.7.2
ADD https://github.com/ufoscout/docker-compose-wait/releases/download/$WAIT_VERSION/wait /wait
RUN chmod +x /wait

COPY . /app
CMD go run scrapper.go