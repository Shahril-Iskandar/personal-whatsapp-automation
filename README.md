# WhatsApp Bulk Messaging Application
This Python application allows you to send a template message to multiple WhatsApp chats without requiring the recipients to save your number.

## Problem Statement
The existing WhatsApp broadcast feature necessitates that both parties save each other's contact numbers. For businesses with a large clientele, managing this can become cumbersome. This application simplifies the process by enabling administrators to send mass messages effortlessly.

## Features
* Send a template message to multiple recipients.
* No need for recipients to save the sender's number.
* Streamlined messaging for businesses with large client bases.

## Usage Instructions
### Step 1: Prepare Your Contact List
1. Create a text file containing the group names and number of people to tag. See example in `testgroup.txt`.

### Step 2: Customize Your Message
1. Open `message.py`.
2. Edit the file to include any attachment path and your desired message. Each new line in `message.py` should be a new variable string to form a paragraph.

### Step 3: Add New Emojis (Optional)
1. If you wish to include new emojis, add them to the `emoji.py` file.
2. Verify that the emojis work correctly by testing them in your messages.

### Step 4: Modify the Main Script
1. Open `main.py`.
2. Make necessary changes starting from line 41 to tailor the script to your specific needs.

### Step 5: Run the Application
1. Execute the main script to send the messages.