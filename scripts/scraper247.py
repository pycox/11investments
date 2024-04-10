from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
# from utils import readUrl, updateDB
import time


def main():
    key = 247
    com, url = "", "https://www.bjss.com/careers/search"
        # com, url = readUrl(key)
    options = Options()
    options.add_argument("--log-level=3")
    driver = webdriver.Chrome(options=options)
    driver.get(url)

    flag = True
    data = []

    while flag:
        time.sleep(4)
        items = driver.find_elements(By.CSS_SELECTOR, "div.border.p-6.md:p-8.md:flex.md:flex-row.justify-between.items-center.featured-positions-position.relative")
        for item in items:
            link = item.find_element(By.CSS_SELECTOR, "a").get_attribute("href").strip()
            location = item.find_element(By.CSS_SELECTOR, 'div').text.strip()

            print(location)

            for str in ['London', 'New York', 'San Francisco', 'United States', 'United Kingdom', 'UK', 'USA', 'US']:
                if (str in location):
                    data.append(
                        [
                            item.find_element(By.CSS_SELECTOR, "h4").text.strip(),
                            com,
                            location,
                            link,
                        ]
                    )
                    break

        try:
          driver.find_element(By.CSS_SELECTOR, "a[text='Next >']").click()
          time.sleep(4)
        except:
          flag = False
          print("No More Jobs")


    driver.quit()
    print(data)
    # updateDB(key, data)


if __name__ == "__main__":
    main()
