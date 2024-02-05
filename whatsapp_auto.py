import os
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from webdriver_manager.chrome import ChromeDriverManager
import time

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
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

profile = os.path.join(dir_path, "profile", "wpp")
options.add_argument(r"user-data-dir={}".format(profile))
driver = webdriver.Chrome(options=options)
driver.get("https://web.whatsapp.com")
wait=WebDriverWait(driver,100)

######################################## Variables ########################################

# group_names = []
# with open('groupnames.txt', 'r') as file:
#     # Iterate through each line in the file
#     for line in file:
#         # Print each name (assuming each name is on a separate line)
#         group_names.append(line.strip())
#         # print(line.strip())

contact_dict = {}
with open('testgroup.txt') as f:
    for line in f:
        key, value = line.strip().split(', ') 
        contact_dict[key] = int(value) # Value is the number of clients in the group

# contact_list_2 = [f'"{item}"' for item in contact_list]
filepath_to_sent = "C:\\Users\\14000\\Downloads\\FMZ\\EDM\\poster_investinginAI.jpeg"

######################################## Functions ########################################
# 💪🏽
def emoji_muscle():
    message_box.send_keys(":bodybuilder" + Keys.ENTER)
    time.sleep(.5)
    
# 👇🏼
def emoji_pointdown():
    message_box.send_keys(":backhand")
    time.sleep(.5)
    message_box.send_keys(Keys.ARROW_RIGHT*3 + Keys.ENTER) # backhand index pointing down
    time.sleep(.5)

# 🤗
def emoji_hugging():
    message_box.send_keys(":hugging" + Keys.ENTER)
    time.sleep(.5)

# 😊
def emoji_smiley():
    message_box.send_keys(":happy")
    time.sleep(.5)
    message_box.send_keys(Keys.ARROW_RIGHT*5 + Keys.ENTER) 
    time.sleep(.5)

# 🤓
def emoji_geek():
    message_box.send_keys(":geek" + Keys.ENTER)
    time.sleep(.5)

# 👩‍💻
def emoji_girlcomputer():
    message_box.send_keys(":computer" + Keys.ENTER)
    time.sleep(.5)

# ✨
def emoji_sparkles():
    message_box.send_keys(":sparkles" + Keys.ENTER)
    time.sleep(.5)

# 👍🏼
def emoji_thumbsup():
    message_box.send_keys(":thumbs up" + Keys.ENTER)
    time.sleep(.5)

# 🔥
def emoji_fire():
    message_box.send_keys(":fire" + Keys.ENTER)
    time.sleep(.5)

# 💡
def emoji_lightbulb():
    message_box.send_keys(":light bulb" + Keys.ENTER)
    time.sleep(.5)

def emoji_new():
    message_box.send_keys(":new" + Keys.ENTER)
    time.sleep(.5)

# Another method to add emoji   :
# emoji_icon_path = '//span[@data-icon="smiley"]'
# emoji_icon = wait.until(EC.presence_of_element_located((By.XPATH,emoji_icon_path)))
# emoji_icon.click()

# emoji_search_path = '//input[@title="Search Emoji"]'
# emoji_search = wait.until(EC.presence_of_element_located((By.XPATH,emoji_search_path)))
# emoji_search.click()
# # driver.implicitly_wait(2)
# emoji_search.send_keys('bodybuilder' + Keys.ENTER)
# # emoji_search.send_keys(Keys.ENTER)

# close_emoji_path = '//span[@data-icon="x"]'
# close_emoji = wait.until(EC.presence_of_element_located((By.XPATH,close_emoji_path)))
# close_emoji.click()
# message_box.click() # Click on message box
# message_box.send_keys(Keys.ENTER) # New line

######################################## Sending message ########################################
for key, value in contact_dict.items():
    # Find the search box, click the search box, type the name of the group, click the group
    search_box_path='//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div[1]/p' # Find the search box element
    search_box = wait.until(EC.presence_of_element_located((By.XPATH, search_box_path)))
    search_box.click() # Click on search box
    search_box.send_keys(key) # Type the group name in the search box, without quotes
    time.sleep(1)

    group_name = f'"{key}"' # Put quotes around the group name
    chat_name_path = '//span[contains(@title,'+ group_name + ')]' # Find the chat name element, need to have "" around the group name
    chat_name = wait.until(EC.presence_of_element_located((By.XPATH, chat_name_path)))
    chat_name.click()
    time.sleep(1)

    message_box_path = '//div[@title="Type a message"]'
    message_box = wait.until(EC.presence_of_element_located((By.XPATH,message_box_path)))

    # documents_path = '//input[@accept="*"]'
    # documents_box = wait.until(EC.presence_of_element_located((By.XPATH,documents_path)))

    message_box.click() # Click on message box
    message_box.send_keys("Hi ")
    # message_box.send_keys("Hi " + "@" + Keys.ARROW_DOWN + Keys.ENTER) # Tag person: For one person other than Mizi
    # message_box.send_keys(Keys.SHIFT + Keys.ENTER)
    # message_box.send_keys(Keys.SHIFT + Keys.ENTER)

    if value == 1:
        message_box.send_keys("@")
        message_box.send_keys(Keys.ARROW_DOWN + Keys.ENTER)
    elif value == 2: # (2 clients in group excluding Mizi and you)
        message_box.send_keys("@")
        message_box.send_keys(Keys.ARROW_DOWN + Keys.ENTER)
        message_box.send_keys("@")
        message_box.send_keys(Keys.ARROW_DOWN + Keys.ARROW_DOWN + Keys.ENTER)
    elif value == 3:
        message_box.send_keys("@")
        message_box.send_keys(Keys.ARROW_DOWN + Keys.ENTER)
        message_box.send_keys("@")
        message_box.send_keys(Keys.ARROW_DOWN + Keys.ARROW_DOWN + Keys.ENTER)    
        message_box.send_keys("@")
        message_box.send_keys(Keys.ARROW_DOWN + Keys.ARROW_DOWN + Keys.ARROW_DOWN + Keys.ENTER)   

    message_box.send_keys(Keys.SHIFT + Keys.ENTER)
    message_box.send_keys(Keys.SHIFT + Keys.ENTER)
    ######################################## Message ########################################
    message_one = "Financial Symposium: Investing In Artificial Intelligence, presented by Allianz Global Investors on 22 Feb"
    message_two = " Proud to present you this premier launch* to explore the investing opportunities in the Artificial Intelligence with an **onboarding global fund house Allianz GI** in late Feb."
    message_three = "2023 proved to be a pivotal year for artificial intelligence companies. A better-than-expected economic backdrop was conducive to stock returns across the Al investment universe. The key catalyst was the rapid adoption of ChatGPT, creating a tailwind for companies across the Al value chain. Al's impact on every industry is starting to take hold."
    message_four = "Registration is now open with the full synopsis in the link, start inviting your prospective clients today with your affiliate RSVP link (retrieve from Merlin chatbot)!"

    emoji_girlcomputer()
    emoji_new()
    message_box.send_keys(" ")
    message_box.send_keys(message_one)
    message_box.send_keys(" ")
    emoji_sparkles()
    message_box.send_keys(Keys.SHIFT + Keys.ENTER)
    message_box.send_keys(Keys.SHIFT + Keys.ENTER)
    emoji_geek()
    message_box.send_keys(" ")
    message_box.send_keys(message_two)
    message_box.send_keys(Keys.SHIFT + Keys.ENTER)
    message_box.send_keys(Keys.SHIFT + Keys.ENTER)
    message_box.send_keys(message_three)
    emoji_fire()
    message_box.send_keys(Keys.SHIFT + Keys.ENTER)
    message_box.send_keys(Keys.SHIFT + Keys.ENTER)
    emoji_lightbulb()
    message_box.send_keys(" ")
    message_box.send_keys(message_four)
    message_box.send_keys(" ")
    emoji_hugging()

    if not filepath_to_sent:
        print("No file to sent")
        message_box.send_keys(Keys.ENTER) # Submit
    else:
        # Add attachment
        attachment_path = '//span[@data-icon="attach-menu-plus"]'
        attachment_box = wait.until(EC.presence_of_element_located((By.XPATH,attachment_path)))
        attachment_box.click()
        time.sleep(1)
        # Add image
        images_path = '//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]'
        # images_path = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/span/div/ul/div/div[2]/li/div/input'
        images_box = wait.until(EC.presence_of_element_located((By.XPATH,images_path)))
        images_box.send_keys(filepath_to_sent)
        time.sleep(5)
        # sent_image_path = '//div[@class="g0rxnol2"]'
        sent_image_path = '//span[@data-icon="send"]'
        sent_image = wait.until(EC.presence_of_element_located((By.XPATH,sent_image_path)))
        sent_image.click()

    print('Message send to ' + key + ' successfully.')
    # Back icon
    back_path = '//span[@data-icon="search"]'
    back_icon = wait.until(EC.presence_of_element_located((By.XPATH,back_path)))
    back_icon.click()
    time.sleep(1)

# message_box_path = '//span[@class="selectable-text copyable-text"]' 
# message_box = wait.until(EC.presence_of_element_located((By.XPATH,message_box_path)))
# message_box.click()
# message_box.send_keys(Keys.ENTER)
