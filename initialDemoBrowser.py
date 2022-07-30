from selenium import webdriver
from selenium.webdriver.chrome.service import Service


# Create service object and call Chrome Driver object
service_obj = Service("C:\\Users\\Ivan\\Desktop\\QA Path\\SeleniumPython\\Drivers\\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

# Create service object and call Firefox object
# service_obj = Service("C:\\Users\\Ivan\\Desktop\\QA Path\\SeleniumPython\\Drivers\\geckodriver.exe")
# driver = webdriver.Firefox(service=service_obj)

# Create service object and call Edge object
# service_obj = Service("C:\\Users\\Ivan\\Desktop\\QA Path\\SeleniumPython\\Drivers\\msedgedriver.exe")
# driver = webdriver.Edge(service=service_obj)

# Max browser
driver.maximize_window()

# Hit url
driver.get("https://www.rahulshettyacademy.com")

# Get Title and Link
print(driver.title)
print(driver.current_url)

# Go to Section
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

# Minimize
driver.minimize_window()
driver.maximize_window()

# go Back, refresh, forward
driver.back()
driver.refresh()
driver.forward()

driver.close()