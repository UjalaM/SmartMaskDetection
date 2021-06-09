import smtplib
import ssl
from email.mime.text import MIMEText
from email.utils import formataddr
from email.mime.multipart import MIMEMultipart  # New line
from email.mime.base import MIMEBase  # New line
from email import encoders  # New line
import pyautogui 

myScreenshot = pyautogui.screenshot()
myScreenshot.save(r'E:/Ujala_folder/sem 6/ml/Sem6_FD/SmartMaskDetector/dataset/ss.png')
#[12:14, 5/14/2021] Yogita: # User configuration
sender_email = 'ujalamaurya.um@gmail.com'
sender_name = 'Ujala Maurya'
password = input('Please, type your password: ')

receiver_emails = 'anchallsm2000@gmail.com'
receiver_names = 'YogitaLikhi'

email_body = 'Python screenshot'
filename = 'E:/Ujala_folder/sem 6/ml/Sem6_FD/SmartMaskDetector/dataset/ss.png'


print("Sending the email...")
# Configurating user's info
msg = MIMEMultipart()
msg['To'] = formataddr((receiver_names, receiver_emails))
msg['From'] = formataddr((sender_name, sender_email))
msg['Subject'] = 'Hello, my friend ' + receiver_names
msg.attach(MIMEText(email_body))
msg.send()
