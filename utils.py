from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def search_box(wait, key):
    '''
    Search for the search box using xpath.
    '''
    search_box_path='//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div[1]/p' # Find the search box element
    search_box = wait.until(EC.presence_of_element_located((By.XPATH, search_box_path)))
    search_box.click() # Click on search box
    search_box.send_keys(key) # Type the group name in the search box, without quotes
    time.sleep(1)

def search_group_name(wait, key):
    '''
    Search for the group name in the search box using xpath.
    '''
    group_name = f'"{key}"' # Put quotes around the group name
    chat_name_path = '//span[contains(@title,'+ group_name + ')]' # Find the chat name element, need to have "" around the group name
    chat_name = wait.until(EC.presence_of_element_located((By.XPATH, chat_name_path)))
    chat_name.click()
    time.sleep(1)

def search_message_box(wait):
    '''
    Search for the message box in after clicking the group, using xpath and return the message box element to use further.
    '''
    message_box_path = '//div[@aria-label="Type a message"]' # Alternatively = '//div[@title="Type a message"]'
    message_box = wait.until(EC.presence_of_element_located((By.XPATH,message_box_path)))
    message_box.click() # Click on message box
    return message_box

def tag_clients(value, message_box):
    '''
    Count number of clients in group excluding Mizi and you, then tag them.

    Client number should not be save to work.
    '''
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

def new_paragraph(message_box):
    message_box.send_keys(Keys.SHIFT + Keys.ENTER)
    message_box.send_keys(Keys.SHIFT + Keys.ENTER)

def send_attachment(wait, message_box, attachment):
    '''
    Send attachment if there is any, else submit the message.
    '''
    if not attachment:
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
        images_box.send_keys(attachment)
        time.sleep(3)
        # sent_image_path = '//div[@class="g0rxnol2"]'
        sent_image_path = '//span[@data-icon="send"]'
        sent_image = wait.until(EC.presence_of_element_located((By.XPATH,sent_image_path)))
        sent_image.click()