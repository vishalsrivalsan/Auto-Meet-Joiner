from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pyautogui
import chromedriver_binary

options=webdriver.ChromeOptions()
options.add_argument("user-data-dir=C:\\Users\\VISHAL\\AppData\\Local\\Google\\Chrome\\User Data")
options.add_argument("profile-directiory= Profile 1")
#options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.get('https://meet.google.com/ttu-ammu-hsj?authuser=0&hs=179')
driver.implicitly_wait(10)
'''
element=driver.find_elements_by_xpath('.//span[contains(text(),"Dismiss")]')
element.click()
s=driver.find_element_by_css_selector("span[class='RveJvd snByac']")'''
# get the browser panel height
'''panel_height = driver.execute_script('return window.outerHeight - window.innerHeight;')
# get absolute x value
abs_x = s.location['x']

# get y value (this is relative y value - meaning y value with in browser)
y = s.location['y']
abs_y = y + panel_height
# print the absolute x and y values
print ("Absolute x : " + abs_x)
print ("Absolute y : " + abs_y)'''
pyautogui.PAUSE=5
pyautogui.moveTo(1159,653,duration=0.5)
pyautogui.pause=2
pyautogui.click()
pyautogui.moveTo(1270,632,duration=0.5)
pyautogui.pause=2
pyautogui.click()

profile=webdriver.FirefoxProfile('C:/Users/VISHAL/AppData/Roaming/Mozilla/Firefox/Profiles/tiwehmlc.Vishal')
driver2 = webdriver.Firefox(firefox_profile=profile)
driver2.maximize_window()
driver2.get('https://meet.google.com/ttu-ammu-hsj?authuser=0&hs=179')
driver2.implicitly_wait(10)
'''
element=driver.find_elements_by_xpath('.//span[contains(text(),"Dismiss")]')
element.click()'''
'''s=driver2.find_element_by_css_selector("span[class='RveJvd snByac']")
# get the browser panel height
panel_height = driver.execute_script('return window.outerHeight - window.innerHeight;')
# get absolute x value
abs_x = s.location['x']

# get y value (this is relative y value - meaning y value with in browser)
y = s.location['y']
abs_y = y + panel_height
# print the absolute x and y values
print ("Absolute x : " + abs_x)
print ("Absolute y : " + abs_y)'''
pyautogui.PAUSE=5
pyautogui.moveTo(1159,653,duration=0.5)
pyautogui.pause=2
pyautogui.click()
pyautogui.moveTo(1270,632,duration=0.5)
pyautogui.pause=2
pyautogui.click()
