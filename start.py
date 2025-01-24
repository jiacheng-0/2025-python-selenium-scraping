import time

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4.element import ResultSet, Tag

option = webdriver.ChromeOptions()
option.add_argument("--no-sandbox") # Bypass OS security
option.add_argument("--headless")  # Run in background
option.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems
# option.add_argument("start-maximized")

driver: webdriver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()), options=option
)

driver.get("https://www.neuralnine.com/books")

soup = BeautifulSoup(driver.page_source, "lxml")

headings: ResultSet = soup.find_all("h2", {"class": "elementor-heading-title"})

for heading in headings:  # type: Tag
    print(heading.getText())

time.sleep(30)

driver.quit()
