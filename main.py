import os
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from emoji import WhatsappEmoji
from utils import search_box, search_group_name, search_message_box, tag_clients, new_paragraph, send_attachment, click_back
import message

dir_path = os.getcwd()
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

profile = os.path.join(dir_path, "profile", "wpp") # RED Profile
# profile = os.path.join(dir_path, "profile2", "wpp2") # Main phone
options.add_argument(r"user-data-dir={}".format(profile))
driver = webdriver.Chrome(options=options)
driver.get("https://web.whatsapp.com")
wait=WebDriverWait(driver,100)

######################################## Variables ########################################
contact_dict = {}

with open("groupnames.txt") as f: # Change the file name accordingly
    for line in f:
        key, value = line.strip().split(', ') 
        contact_dict[key] = int(value) # Value is the number of clients in the group

# contact_list_2 = [f'"{item}"' for item in contact_list]

######################################## Sending message ########################################
for key, value in contact_dict.items():
    # Find the search box, click the search box, type the name of the group, click the group
    search_box(wait, key)
    search_group_name(wait, key)
    message_box = search_message_box(wait)
    emoji = WhatsappEmoji(message_box)

    # documents_path = '//input[@accept="*"]'
    # documents_box = wait.until(EC.presence_of_element_located((By.XPATH,documents_path)))

    ######################################## Message ########################################
    message_box.send_keys("Salam ")

    tag_clients(value, message_box)

    emoji.emoji_smiley()
    message_box.send_keys(",")

    message_box.send_keys(Keys.SHIFT + Keys.ENTER)
    message_box.send_keys(message.text_one)
    new_paragraph(message_box)
    message_box.send_keys(message.text_two)

    emoji.emoji_sheep()
    message_box.send_keys(" ")
    emoji.emoji_cow()

    new_paragraph(message_box)

    message_box.send_keys(message.text_three)

    new_paragraph(message_box)

    message_box.send_keys(message.text_four)

    new_paragraph(message_box)

    message_box.send_keys(message.text_five)
    emoji.emoji_pointdown()
    message_box.send_keys(Keys.SHIFT + Keys.ENTER)

    message_box.send_keys(message.text_six)

    send_attachment(wait, message_box, message.attachment_one)
    # send_attachment(wait, message_box, message.attachment_two)
    
    print('Message send to ' + key + ' successfully.')

    # Back icon
    click_back(wait)
