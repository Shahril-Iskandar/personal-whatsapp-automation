import os
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

dir_path = os.getcwd()
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

profile = os.path.join(dir_path, "profile", "wpp")
options.add_argument(r"user-data-dir={}".format(profile))
driver = webdriver.Chrome(options=options)
driver.get("https://web.whatsapp.com")
wait=WebDriverWait(driver,100)

######################################## Variables ########################################

contact_dict = {}
with open('testgroup.txt') as f:
    for line in f:
        key, value = line.strip().split(', ') 
        contact_dict[key] = int(value) # Value is the number of clients in the group

# contact_list_2 = [f'"{item}"' for item in contact_list]
attachment_one = "C:\\Users\\14000\\Downloads\\FMZ\\EDM\\poster_braces.jpg"
attachment_two = ""

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
    message_box.send_keys(":good" + Keys.ENTER)
    time.sleep(.5)

# 🔥
def emoji_fire():
    message_box.send_keys(":fire" + Keys.ENTER)
    time.sleep(.5)

# 💡
def emoji_lightbulb():
    message_box.send_keys(":light bulb" + Keys.ENTER)
    time.sleep(.5)

# 🆕
def emoji_new():
    message_box.send_keys(":new" + Keys.ENTER)
    time.sleep(.5)

# 😳
def emoji_flushedFace():
    message_box.send_keys(":flushed" + Keys.ENTER)
    time.sleep(.5)

# 🤔
def emoji_thinking():
    message_box.send_keys(":thinking" + Keys.ENTER)
    time.sleep(.5)

# 🥺
def emoji_sad():
    message_box.send_keys(":sad" + Keys.ENTER)
    time.sleep(.5)

# 💎
def emoji_diamond():
    message_box.send_keys(":diamond")
    time.sleep(.5)
    message_box.send_keys(Keys.ARROW_RIGHT + Keys.ENTER) 
    time.sleep(.5)

# 🛡️
def emoji_shield():
    message_box.send_keys(":shield" + Keys.ENTER)
    time.sleep(.5)

# 😁
def emoji_bigsmile():
    message_box.send_keys(":teeth" + Keys.ENTER)
    time.sleep(.5)

# 🦷
def emoji_tooth():
    message_box.send_keys(":tooth" + Keys.ENTER)
    time.sleep(.5)

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
    message_one = "[15-May, Wed] Brace Yourself! The Ultimate Showdown - Traditional Braces VS Invisalign!"
    message_two = "Join us on World Orthodontics Day, May 15th, for an enlightening webinar tailored to young professionals contemplating orthodontic treatment. Delve into the realm of orthodontics with Dr Aaron Hoo, Clinical Director and Lead Dentist at Newlife Dental Practice. In this interactive session, we will cover:"
    message_three = "Unlock the secrets of a confident smile"
    message_four = "Demystify traditional braces"
    message_five = "Embrace the Invisalign revolution"
    message_six = "Make the perfect choice: Traditional braces vs Invisalign"
    message_seven = "Registration is now open."
    message_eight = "https://iammerlin.co/ipreciate/Mizi_khamsani"
    
    emoji_new()
    message_box.send_keys(" ")
    message_box.send_keys(message_one)
    message_box.send_keys(" ")
    emoji_bigsmile()
    message_box.send_keys(Keys.SHIFT + Keys.ENTER)
    message_box.send_keys(Keys.SHIFT + Keys.ENTER)
    message_box.send_keys(message_two)
    message_box.send_keys(Keys.SHIFT + Keys.ENTER)
    message_box.send_keys(Keys.SHIFT + Keys.ENTER)

    emoji_tooth()
    message_box.send_keys(" ")
    message_box.send_keys(message_three)
    message_box.send_keys(Keys.SHIFT + Keys.ENTER)

    emoji_tooth()
    message_box.send_keys(" ")
    message_box.send_keys(message_four)
    message_box.send_keys(Keys.SHIFT + Keys.ENTER)

    emoji_tooth()
    message_box.send_keys(" ")
    message_box.send_keys(message_five)
    message_box.send_keys(Keys.SHIFT + Keys.ENTER)

    emoji_tooth()
    message_box.send_keys(" ")
    message_box.send_keys(message_six)
    message_box.send_keys(Keys.SHIFT + Keys.ENTER)
    message_box.send_keys(Keys.SHIFT + Keys.ENTER)

    emoji_lightbulb()
    message_box.send_keys(" ")
    message_box.send_keys(message_seven)
    emoji_geek()
    message_box.send_keys(Keys.SHIFT + Keys.ENTER)
    message_box.send_keys(Keys.SHIFT + Keys.ENTER)

    message_box.send_keys(message_eight)

    if not attachment_one:
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
        images_box.send_keys(attachment_one)
        time.sleep(3)
        # sent_image_path = '//div[@class="g0rxnol2"]'
        sent_image_path = '//span[@data-icon="send"]'
        sent_image = wait.until(EC.presence_of_element_located((By.XPATH,sent_image_path)))
        sent_image.click()

    # Send another attachment
    if not attachment_two:
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
        images_box.send_keys(attachment_two)
        time.sleep(3)
        # sent_image_path = '//div[@class="g0rxnol2"]'
        sent_image_path = '//span[@data-icon="send"]'
        sent_image = wait.until(EC.presence_of_element_located((By.XPATH,sent_image_path)))
        sent_image.click()

    # message_box.send_keys("Here's the program outline and more details of the exclusive perks for attendees.")

    print('Message send to ' + key + ' successfully.')
    # Back icon
    back_path = '//span[@data-icon="search"]'
    back_icon = wait.until(EC.presence_of_element_located((By.XPATH,back_path)))
    back_icon.click()
    time.sleep(1)
