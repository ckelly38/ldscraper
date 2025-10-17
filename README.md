# ldscraper
Web Scraper that builds that stores a lot of info in some sort of DB or file.

## Selenium Notes:
This is the first web scraper that I have built that needed to use Selenium.
Technically you can use the requests library with BeautifulSoup, but for my needs it was not getting the job done.

For requests and the import:

import requests;
from bs4 import BeautifulSoup;
doc = BeautifulSoup(requests.get(murl).text, "html.parser");

I had to import it with:

from selenium import webdriver;
from selenium.webdriver.chrome.service import Service;

I had to configure it as:

opts = webdriver.ChromeOptions();
opts.add_argument("--headless");
opts.add_argument("--no-sandbox");
opts.add_argument("--disable-dev-shm-usage");
opts.add_argument("--remote-debugging-pipe");
driver = webdriver.Chrome(options=opts);

To get the web page that you want you need to call driver.get method with that url:
so murl can be https://www.google.com if you wanted...

tmpg = driver.get(murl);

The next line to work with the Beautiful Soup library you need this line.

doc = BeautifulSoup(driver.page_source, "html.parser");

Lastly, you need to close the driver because now Soup can handle it.

driver.quit();

FOR INSTALATION:

I also had to make sure the driver is for the Browser and the versions match.

I had to install Selenium with the following command:

pipenv install selenium

I also had to install chrome for linux Ubuntu:

wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | sudo apt-key add -
echo 'deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main' | sudo tee /etc/apt/sources.list.d/google-chrome.list
sudo apt-get update
sudo apt-get install -y libglib2.0 libnss3 libgconf-2-4 libfontconfig1 chromium-driver

I also had to install unzip

sudo apt install unzip

I also had to install the chromedriver for testing chrome with Selenium:

wget -N https://storage.googleapis.com/chrome-for-testing-public/141.0.7390.78/linux64/chromedriver-linux64.zip
unzip chromedriver-linux64.zip
sudo mv chromedriver-linux64/chromedriver /usr/local/bin/chromedriver 
sudo chmod +x /usr/local/bin/chromedriver

After that it was recommended to link up said chrome driver:

sudo ln -s /usr/local/share/chromedriver /usr/local/bin/chromedriver
sudo ln -s /usr/local/share/chromedriver /usr/bin/chromedriver

At this point a reboot of the terminal was a good idea.
