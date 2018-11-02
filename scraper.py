import requests
from bs4 import BeautifulSoup
import time
import smtplib


def check_color():
    if red_percent_box is None:
        send_positive_email()
    else:
        send_negative_email()


def send_positive_email():
    msg = 'Subject: EXL Stock has risen by 10 or more percent.'
    fromaddr = 'reed.scripts@gmail.com'
    toaddrs = ['reed.burdick@gmail.com']

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login("reed.scripts@gmail.com", "redburd01")

    print("From: " + fromaddr)
    print("To: " + str(toaddrs))
    print("Message: " + msg)

    server.sendmail(fromaddr, toaddrs, msg)
    server.quit()


def send_negative_email():
    msg = 'Subject: EXL Stock has fallen by 10 or more percent.'
    fromaddr = 'reed.scripts@gmail.com'
    toaddrs = ['reed.burdick@gmail.com']

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login("reed.scripts@gmail.com", "redburd01")

    print("From: " + fromaddr)
    print("To: " + str(toaddrs))
    print("Message: " + msg)

    server.sendmail(fromaddr, toaddrs, msg)
    server.quit()


while True:
    url = "https://www.nasdaq.com/symbol/exls"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    percent_box = soup.find("div", {"id": "qwidget_percent"})
    red_percent_box = soup.find("div", {"class": "qwidget-percent qwidget-Red"})
    green_percent_box = soup.find("div", {"class": "qwidget-percent qwidget-Green"})
    percent_text = percent_box.text.strip()
    percent = float(percent_text.replace("%", ""))
    print(percent)
    if percent >= 5:
        check_color()
        time.sleep(120)
    else:
        time.sleep(120)
