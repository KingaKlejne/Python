import os
import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver

google_url = "https://docs.google.com/forms/d/e/1FAIpQLScj1VHPre_" \
             "zZsjM2VtsyjEZJQvYFdkPkDwYO4C2-Yez5mwzug/viewform?usp=sf_link"

zillow_url = "https://www.zillow.com/homes/for_rent/1-_beds/?search" \
             "QueryState=%7B%22pagination%22%3A%7B%7D%2C%22users" \
             "SearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%" \
             "3A-122.56276167822266%2C%22east%22%3A-122.30389632177734%" \
             "2C%22south%22%3A37.69261345230467%2C%22north%22%3A37.85787" \
             "7098316834%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState" \
             "%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3" \
             "A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3A" \
             "false%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%" \
             "3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3A" \
             "false%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%" \
             "3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3A" \
             "false%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%" \
             "7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%" \
             "2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D"
header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/107.0.0.0 Safari/537.36",
    "Accept-Language": "pl-PL,pl;q=0.9,en-US;q=0.8,en;q=0.7",
}

response = requests.get(zillow_url, headers=header)
zillow = response.text
soup = BeautifulSoup(zillow, "html.parser")
divs = soup.find_all(name="div", class_="property-card-data")
links = soup.find_all(name="a", class_="property-card-link")
addresses_list = [div.get_text().split("$")[0] for div in divs]
prices_list = [
    div.get_text().split("$")[1].split("+")[0].replace(",", "")
    if "+" in div.get_text().split("$")[1]
    else div.get_text().split("$")[1].split("/")[0].replace(",", "")
    for div in divs
]
links_list = [
    link.get("href")
    if "https" in link.get("href")
    else "https://www.zillow.com/" + link.get("href")
    for link in links
]


chrome_driver_path = os.getenv("CHROME_DRIVER_PATH")
driver = webdriver.Chrome(executable_path=chrome_driver_path)

for i in range(len(addresses_list)):
    driver.get(google_url)
    time.sleep(2)
    address_box = driver.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]'
        '/div/div/div[2]/div/div[1]/div/div[1]/input'
    )
    price_box = driver.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]'
        '/div/div/div[2]/div/div[1]/div/div[1]/input'
    )
    link_box = driver.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]'
        '/div/div/div[2]/div/div[1]/div/div[1]/input'
    )
    submit_button = driver.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]'
        '/div[1]/div/span/span'
    )
    address_box.send_keys(addresses_list[i])
    price_box.send_keys(prices_list[i])
    link_box.send_keys(links_list[i])
    submit_button.click()


driver.close()
driver.quit()
