import os
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from webdriver_manager.chrome import ChromeDriverManager

# options = Options()
# options.add_experimental_option("detach", True)
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
#                           options=options)

# driver.get("https://web.whatsapp.com/")

# Method 2:
# options=webdriver.ChromeOptions()
# options.add_experimental_option("detach", True)
# options.add_argument("--user-data-dir=C:\\Users\\14000\\AppData\\Local\\Google\\Chrome\\User Data")
# ser = Service("./chromedriver.exe")
# driver = webdriver.Chrome(service=ser,options=options)

# # driver.get("https://web.whatsapp.com/")

dir_path = os.getcwd()
profile = os.path.join(dir_path, "profile", "wpp")
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument(
    r"user-data-dir={}".format(profile))
driver = webdriver.Chrome(options=options)
driver.get("https://web.whatsapp.com")
wait=WebDriverWait(driver,100)

######################################## Variables ########################################
target='Group test' # Name of the contact or group
target2='"Group test"'
person = "FMZ Shahril"
tag_person = f"Hi @{person}"

# with open('message.txt', 'r', encoding='utf8') as f:
#     text_message = f.read()
text_message = "This is a test message."
emoji = "👍🏼🤗💪🏽😊✨👇🏼"

######################################## Search box ########################################
# Find the search box, click the search box, type the name of the group, click the group
search_box_path='//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div[1]/p' # Find the search box element
search_box = wait.until(EC.presence_of_element_located((By.XPATH, search_box_path)))
search_box.click() # Click on search box
search_box.send_keys(target) # Type the chat name

chat_name_path = '//span[contains(@title,'+ target2 + ')]' # Find the chat name element, have to have ""
chat_name = wait.until(EC.presence_of_element_located((By.XPATH, chat_name_path)))
chat_name.click()

######################################## In group message ########################################
message_box_path='//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p' # Search for message box element
message_box=wait.until(EC.presence_of_element_located((By.XPATH,message_box_path)))
message_box.click() # Click on message box
# text_element = driver_trader.find_element_by_xpath(message_box_path)
# Message
message_box.send_keys("@" + Keys.ARROW_DOWN + Keys.ENTER) # For one person other than Mizi
message_box.send_keys(":bodybuilder" + Keys.ARROW_RIGHT + Keys.ARROW_RIGHT + Keys.ENTER) # bodybuilder
message_box.send_keys(":backhand" + Keys.ARROW_RIGHT + Keys.ARROW_RIGHT + Keys.ARROW_RIGHT + Keys.ENTER) # backhand index pointing down
message_box.send_keys(Keys.ENTER) # Submit 

# driver.execute_script("arguments[0].innerHTML = '{}'".format(emoji),text_element)
# text_element.send_keys('.')
# text_element.send_keys(Keys.BACKSPACE)

# message_box.send_keys(tag_person + Keys.ENTER) # Enter message
# message_box.click() # Click on message box
# message_box.send_keys(Keys.SHIFT, Keys.ENTER) # New line
# message_box.send_keys(Keys.SHIFT, Keys.ENTER) # New line
# message_box.send_keys(text_message, Keys.ENTER) # Send message


# Method 3:
# import pywhatkit as pwk
# pwk.sendwhatmsg("+6596561830", "Test", 19, 51)

# Method 4:
# ## IMPORTS ##
# from selenium import webdriver
# from selenium.webdriver.edge.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from urllib.parse import quote
# from re import fullmatch
# import time

# # Driver Managers
# from webdriver_manager.microsoft import EdgeChromiumDriverManager
# from webdriver_manager.chrome import ChromeDriverManager
# from webdriver_manager.firefox import GeckoDriverManager
# from webdriver_manager.opera import OperaDriverManager
# from webdriver_manager.core.os_manager import ChromeType

# ## RUNTIME VARIABLES ##
# """
# Place the associated driver manager above depending on the browser you want to launch.
# Selenium supports the following:
# - Chrome
# - Edge
# - Firefox
# - Opera
# - Brave

# Below the script is configured set to use an Edge browser. Be sure to change it according to the browser you use.
# """
# browser = "Chrome"

# ## INPUT ##
# """
# Takes input related to sending a text from the recipient phone number and message.
# """
# print("\n")
# print("Write recipient phone number in format +[Country Code][Area Code][Rest]:")
# phone_no = str(input())
# print("\nWrite message:")
# message = str(input())

# ## HELPERS ##
# """
# Functions that do self explanatory tasks
# """
# def modify_number(phone_no):
#     phone_no = phone_no.replace(" ", "").replace("-", "").replace("(", "").replace(")", "")
#     return phone_no

# def validate_number(phone_no):
#     def check_number(number):
#         return "+" in number or "_" in number

#     if not check_number(number=phone_no):
#         raise Exception("Country Code Missing in Phone Number!")

#     if not fullmatch(r"^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$", phone_no):
#         raise Exception("Invalid Phone Number.")
#     return True

# def set_browser(browser):
#     install = lambda dm : dm.install()
#     try:
#         if (browser == "Edge"):
#             bm = EdgeChromiumDriverManager()
#             return webdriver.Edge(service=Service(install(bm)))
#         elif (browser == "Chrome"):
#             bm = ChromeDriverManager()
#             return webdriver.Chrome(service=Service(install(bm)))
#         elif (browser == "Firefox"):
#             bm = GeckoDriverManager()
#             return webdriver.Firefox(service=Service(install(bm)))
#         elif (browser == "Opera"):
#             bm = OperaDriverManager()
#             return webdriver.Opera(service=Service(install(bm)))
#         elif (browser == "Brave"):
#             bm = ChromeDriverManager(chrome_type=ChromeType.BRAVE)
#             return webdriver.Chrome(service=Service(install(bm)))
#     except:
#         raise Exception("Browser not found")

# ## SCRIPT ##
# """
# Uses Selenium to send a text
# """
# phone_no = modify_number(phone_no)
# if (validate_number(phone_no)):

#     # Loads browser
#     driver = set_browser(browser)
    
#     # Goes to site
#     site = f"https://web.whatsapp.com/send?phone={phone_no}&text={quote(message)}"
#     driver.get(site)
    
#     # Uses XPATH to find a send button
#     element = lambda d : d.find_elements(by=By.XPATH, value="//div//button/span[@data-icon='send']")
    
#     # Waits until send is found (in case of login)
#     loaded = WebDriverWait(driver, 1000).until(method=element, message="User never signed in")
    
#     # Loads a send button
#     driver.implicitly_wait(10)
#     send = element(driver)[0]
    
#     # Clicks the send button
#     send.click()
    
#     # Sleeps for 5 secs to allow time for text to send before closing window
#     time.sleep(5) 
    
#     # Closes window
#     driver.close()
