# Taking photos with motion detection and sending to email address
# Hareket algılama ile fotoğraf çekme ve email adresine yollamak

Türkçe:
========
Raspberrypi 4 Model B ile Hareket Algılama ile Fotoğraf Çekerek Email Adresine Yollama

Kullanılan Kütüphaneler / Libraries Used of Python
- import os
- import glob
- import picamera
- import RPi.GPIO as GPIO
- import smtplib from time
- import sleep

- Raspberrypi 4 Model B
- Raspberrypi 4 Model B uyumlu Pır(Hareket Sensörü Örneğin: HC-SR501)
- Pi configürasyondan Kamerayı Açık konuma getirin.
- Cam-pi-email.py dosyası ile Database klasörünü ayni kalasör içinde bulundurun(Ör: /home/pi/Desktop içinde)

Ardından;
Cam-pi-email.py içinden;
- Alacak olanın email adresini ve yollayan mailin sunucu ayarları ile şifresini düzeltin.

Ve İster;
- Uç birimden(SSH) ile ister;
- Thony Python Ide(Python Editör) ile Cam-pi-email.py dosyasını çalıştırın.
- İhtiyaç halinde PIR sensörün kalibrasyonunu PIR üzerinden ayarlayın.

==============================================================================

English:
=========
Taking Pictures with Motion Detection with Raspberrypi 4 Model B and Sending to E-mail Address

Libraries Used of Python
- import os
- import glob
- import picamera
- import RPi.GPIO as GPIO
- import smtplib from time
- import sleep

- Raspberrypi 4 Model B
- Raspberrypi 4 Model B compatible Pır (Movement Shield For example: HC-SR501)
- Turn Camera On from Pi config.
- Place the Cam-pi-email.py file and the Database folder in the same folder (Ex: in /home/pi/Desktop)
Next;
Through Cam-pi-email.py;
- Correct the email address of the recipient and the server settings and password of the sending mail.
And Whether;
- Asks via SSH;
- Run Cam-pi-email.py file with Thony Python Ide (Python Editor).
- Adjust the calibration of the PIR sensor via PIR if needed.
