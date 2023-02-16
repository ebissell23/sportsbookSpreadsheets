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
driver.get('https://www.example.com')

# Close the browser
driver.quit()