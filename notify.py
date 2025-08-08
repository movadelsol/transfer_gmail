import smtplib
import time
import socket
from icecream import ic
from my_gmail_account import APPLICATION_SPECIFIC_PASSWORD
from email.message import EmailMessage


def notify0(_strs=[]):
    hostname = socket.gethostname()
    ic(hostname)
    smtp_obj = smtplib.SMTP("smtp.gmail.com", 587)
    r1 = smtp_obj.ehlo()
    r2 = smtp_obj.starttls()
    r3 = smtp_obj.login("movadelsol@gmail.com", APPLICATION_SPECIFIC_PASSWORD)
    ic(r3)
    msg = "Subject:LOOK GMAIL FOR ASAHI SHIMBUN!!\n"
    # msg = "Subject:【新聞広告調査】アンケートのお願い!!\n"
    msg += f"Message from {hostname}\n"
    msg += f"{time.asctime()}\n"
    msg += "Mova del Sol"
    msg += "\n\nPlease check your inbox for the latest updates."

    for _str in _strs:
        msg += _str
    to_address = []
    to_address.append("movadelsol@gmail.com")
    to_address.append("osawa@imed-tech.co.jp")
    smtp_obj.sendmail("movadelsol@gmail.com", to_address, msg)
    smtp_obj.quit()


def notify(_strs=[]):
    hostname = socket.gethostname()
    ic(hostname)
    msg = EmailMessage()
    msg["Subject"] = "朝日新聞に関するアンケートのお願い"
    msg["From"] = "movadelsol@gmail.com"
    msg["To"] = "movadelsol@gmail.com,osawa@imed-tech.co.jp"
    body = f"Message from {hostname}\n{time.asctime()}\nMova del Sol\n\n"
    for _str in _strs:
        body += _str
    msg.set_content(body)

    smtp_obj = smtplib.SMTP("smtp.gmail.com", 587)
    smtp_obj.ehlo()
    smtp_obj.starttls()
    smtp_obj.login("movadelsol@gmail.com", APPLICATION_SPECIFIC_PASSWORD)
    smtp_obj.send_message(msg)
    smtp_obj.quit()


if __name__ == "__main__":
    notify(["New email received", "日本語字幕のテストです。"])
    ic("Notification sent.")
