from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

SERVICE_PATH = "C:\\Program Files (x86)\\chromedriver.exe"
service = Service(SERVICE_PATH)
driver = webdriver.Chrome(service=service)

driver.get('https://www.amazon.ca/')
driver.implicitly_wait(10)

driver.find_element(By.ID, 'twotabsearchtextbox').send_keys('monitor')
driver.find_element(By.ID, 'nav-search-submit-button').click()

search_results = driver.find_elements(By.XPATH, '//div[@data-component-type="s-search-result"]')

print("Items that will arrive before christmas:")
for result in search_results:
    has_christmas_tag = driver.execute_script(
        "return arguments[0].querySelector('[aria-label=\"Arrives before Christmas\"]')",
        result
    )
    if has_christmas_tag:
        try:
            item_name = driver.execute_script(
                "return arguments[0].querySelector('div[data-cy=\"title-recipe\"]').innerText",
                result
            )
        except:
            item_name = "No Name Found"

        try:
            item_price = driver.execute_script(
                "return arguments[0].querySelector('span[class=\"a-price-whole\"]').innerText",
                result
            )
        except:
            item_price = "Price Unavailable"

        try:
            item_url = driver.execute_script(
                "return arguments[0].querySelector('.a-link-normal').href",
                result
            )
        except:
            item_url = "URL Unavailable"

        print(f"Item Name: {item_name}\nPrice: ${item_price}\nURL: {item_url}\n")

driver.quit()