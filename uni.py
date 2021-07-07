from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import pyautogui
import chromedriver_binary

options=webdriver.ChromeOptions()
options.add_argument("user-data-dir=C:\\Users\\VISHAL\\AppData\\Local\\Google\\Chrome\\User Data")
options.add_argument("profile-directiory= Profile 1")
#options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.get('https://meet.google.com/lookup/akvsy7bcyp?authuser=0&hs=179')
time.sleep(6)
while(1):
    if pyautogui.locateOnScreen('meet_dismiss_button.png'):
        dismiss_pos=pyautogui.locateOnScreen('meet_dismiss_button.png')
        x,y=pyautogui.center(dismiss_pos)
        pyautogui.click(x,y)
        break
while(1):
    print("Looking for join")
    time.sleep(0.5)
    if pyautogui.locateOnScreen('meet_join_button.png'):
        print('found')
        join_pos=pyautogui.locateOnScreen('meet_join_button.png')
        x,y=pyautogui.center(join_pos)
        pyautogui.click(x,y)
        break

profile=webdriver.FirefoxProfile('C:/Users/VISHAL/AppData/Roaming/Mozilla/Firefox/Profiles/tiwehmlc.Vishal')
driver2 = webdriver.Firefox(firefox_profile=profile)
driver2.maximize_window()
driver2.get('https://meet.google.com/lookup/akvsy7bcyp?authuser=0&hs=179')
time.sleep(6)
'''
element=driver.find_elements_by_xpath('.//span[contains(text(),"Dismiss")]')
element.click()
s=driver2.find_element_by_css_selector("span[class='RveJvd snByac']")
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

while(1):
    print("Looking for join")
    time.sleep(0.5)
    if pyautogui.locateOnScreen('meet_join_button_firefox.png'):
        print('found')
        join_pos=pyautogui.locateOnScreen('meet_join_button_firefox.png')
        x,y=pyautogui.center(join_pos)
        pyautogui.click(x,y)
        break
