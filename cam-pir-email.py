import os
import glob
import picamera
import RPi.GPIO as GPIO
import smtplib
from time import sleep

# Importing modules for sending mail
from email.mime.multipart import MIMEMultipart
#from email.MIMEMultipart import MIMEMultipart
from email.mime.text import MIMEText
#from email.MIMEText import MIMEText
from email.mime.base import MIMEBase
#from email.MIMEBase import MIMEBase
from email import encoders

sender = 'my_name@domain.net'
password = 'My-pass'
receiver = 'sender@domain.net'

DIR = './Database/'  # Imported picture folder name
FILE_PREFIX = 'image'
            
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.IN)  # Read output from PIR motion sensor

def send_mail():
    print ('Sending E-Mail')
    # Create the directory if not exists
    if not os.path.exists(DIR):
        os.makedirs(DIR)
    # Find the largest ID of existing images.
    # Start new images after this ID value.
    files = sorted(glob.glob(os.path.join(DIR, FILE_PREFIX + '[0-9][0-9][0-9].jpg')))
    count = 0
    
    if len(files) > 0:
        # Grab the count from the last filename.
        count = int(files[-1][-7:-4])+1

    # Save image to file
    filename = os.path.join(DIR, FILE_PREFIX + '%03d.jpg' % count)
    # Capture the face
    with picamera.PiCamera() as camera:  # Or with picamera.UsbCamera() as camera:
        pic = camera.capture(filename)
    # Sending mail
    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = receiver
    msg['Subject'] = 'Movement Detected'
    
    body = ('Picture is Attached.')
    msg.attach(MIMEText(body, 'plain'))
    attachment = open(filename, 'rb')
    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename= %s' % filename)
    msg.attach(part)
    server = smtplib.SMTP('mail.domain.net', 587)
    server.starttls()
    server.login(sender, password)
    text = msg.as_string()
    server.sendmail(sender, receiver, text)
    server.quit()

while True:
    i = GPIO.input(11)
    if i == 0:  # When output from motion sensor is LOW
        print ("No intruders"), i
        sleep(0.3)
    elif i == 1:  # When output from motion sensor is HIGH
        print ("Intruder detected"), i
        send_mail()
