import os
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from emoji import WhatsappEmoji
from utils import search_box, search_group_name, search_message_box, tag_clients, new_paragraph, send_attachment

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

######################################## Sending message ########################################
for key, value in contact_dict.items():
    # Find the search box, click the search box, type the name of the group, click the group
    search_box(wait, key)
    search_group_name(wait, key)
    message_box = search_message_box(wait)

    emoji = WhatsappEmoji(message_box)

    # documents_path = '//input[@accept="*"]'
    # documents_box = wait.until(EC.presence_of_element_located((By.XPATH,documents_path)))

    message_box.send_keys("Hi ")

    tag_clients(value, message_box)

    new_paragraph(message_box)
    ######################################## Message ########################################
    message_one = "[15-May, Wed] Brace Yourself! The Ultimate Showdown - Traditional Braces VS Invisalign!"
    message_two = "Join us on World Orthodontics Day, May 15th, for an enlightening webinar tailored to young professionals contemplating orthodontic treatment."
    
    emoji.emoji_new()
    message_box.send_keys(" ")
    message_box.send_keys(message_one)
    message_box.send_keys(" ")
    emoji.emoji_bigsmile()
    new_paragraph(message_box)
    message_box.send_keys(message_two)
    new_paragraph(message_box)

    send_attachment(wait, message_box, attachment_one)
    send_attachment(wait, message_box, attachment_two)
    
    print('Message send to ' + key + ' successfully.')

    # Back icon
    back_path = '//span[@data-icon="search"]'
    back_icon = wait.until(EC.presence_of_element_located((By.XPATH,back_path)))
    back_icon.click()
    time.sleep(1)
