import time
from selenium.webdriver.common.keys import Keys

class WhatsappEmoji:
    def __init__(self, message_box):
        self.message_box = message_box

    # 💪🏽
    def emoji_muscle(self):
        self.message_box.send_keys(":bodybuilder" + Keys.ENTER)
        time.sleep(.5)
        
    # 👇🏼
    def emoji_pointdown(self):
        self.message_box.send_keys(":backhand")
        time.sleep(.5)
        self.message_box.send_keys(Keys.ARROW_RIGHT*3 + Keys.ENTER) # backhand index pointing down
        time.sleep(.5)

    # 🤗
    def emoji_hugging(self):
        self.message_box.send_keys(":hugging" + Keys.ENTER)
        time.sleep(.5)

    # 😊
    def emoji_smiley(self):
        self.message_box.send_keys(":happy")
        time.sleep(.5)
        self.message_box.send_keys(Keys.ARROW_RIGHT*5 + Keys.ENTER) 
        time.sleep(.5)

    # 🤓
    def emoji_geek(self):
        self.message_box.send_keys(":geek" + Keys.ENTER)
        time.sleep(.5)

    # 👩‍💻
    def emoji_girlcomputer(self):
        self.message_box.send_keys(":computer" + Keys.ENTER)
        time.sleep(.5)

    # ✨
    def emoji_sparkles(self):
        self.message_box.send_keys(":sparkles" + Keys.ENTER)
        time.sleep(.5)

    # 👍🏼
    def emoji_thumbsup(self):
        self.message_box.send_keys(":good" + Keys.ENTER)
        time.sleep(.5)

    # 🔥
    def emoji_fire(self):
        self.message_box.send_keys(":fire" + Keys.ENTER)
        time.sleep(.5)

    # 💡
    def emoji_lightbulb(self):
        self.message_box.send_keys(":light bulb" + Keys.ENTER)
        time.sleep(.5)

    # 🆕
    def emoji_new(self):
        self.message_box.send_keys(":new" + Keys.ENTER)
        time.sleep(.5)

    # 😳
    def emoji_flushedFace(self):
        self.message_box.send_keys(":flushed" + Keys.ENTER)
        time.sleep(.5)

    # 🤔
    def emoji_thinking(self):
        self.message_box.send_keys(":thinking" + Keys.ENTER)
        time.sleep(.5)

    # 🥺
    def emoji_sad(self):
        self.message_box.send_keys(":sad" + Keys.ENTER)
        time.sleep(.5)

    # 💎
    def emoji_diamond(self):
        self.message_box.send_keys(":diamond")
        time.sleep(.5)
        self.message_box.send_keys(Keys.ARROW_RIGHT + Keys.ENTER) 
        time.sleep(.5)

    # 🛡️
    def emoji_shield(self):
        self.message_box.send_keys(":shield" + Keys.ENTER)
        time.sleep(.5)

    # 😁
    def emoji_bigsmile(self):
        self.message_box.send_keys(":teeth" + Keys.ENTER)
        time.sleep(.5)

    # 🦷
    def emoji_tooth(self):
        self.message_box.send_keys(":tooth" + Keys.ENTER)
        time.sleep(.5)