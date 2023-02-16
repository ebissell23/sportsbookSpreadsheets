from selenium import webdriver
from selenium.webdriver.chrome.service import Service


#gets path from driverpath.txt
#keeps things private
with open('driverpath.txt','r') as f:
    driver_path = f.read()
    f.close()

# Start the ChromeDriver service
service = Service(driver_path)
service.start()

# Create a new instance of the Chrome browser
driver = webdriver.Chrome(service=service)

# Navigate to a web page
driver.get('https://oddsjam.com/bet-tracker')
print('before')
with open('loginCookie.txt','r') as f:
    loginCookieDict = {}
    for line in f:
        key, value = line.strip().split('=')
        loginCookieDict[key] = value
    loginCookie = f.read()
    f.close()

driver.add_cookie(loginCookieDict)
driver.refresh()
#element = driver.find_element_by_class_name('dkcss-1l4mw41')
#print(element)
print('after')
# Close the browser
input()
driver.quit()