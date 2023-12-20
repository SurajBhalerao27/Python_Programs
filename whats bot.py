from time import time, sleep
import pyautogui as pg
import webbrowser as wb
import pywhatkit as wt

# Open WhatsApp Web
wb.open('https://web.whatsapp.com/')

# Wait for WhatsApp Web to load (adjust the sleep duration as needed)
sleep(30)

# Send a message using pywhatkit
recipient_number = '+91-8830951567'  # Replace with the recipient's phone number
message = 'Your message goes here.'  # Replace with your message
current_time = time()
scheduled_time = current_time + 10  # Send the message after 10 seconds

wt.sendwhatmsg(recipient_number, message, int(scheduled_time/60), int(scheduled_time%60))
