import os
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.utils import formatdate
from dotenv import load_dotenv

load_dotenv()


def send_mail(_to_main: str, message_info: str, takeaway: str) -> None:
    from_mail = os.getenv("FROM_MAIL")
    from_passwd = os.getenv('FROM_PASSWORD')
    server_adr = os.getenv('SERVER_ADR')
    to_mail = _to_main

    msg = MIMEMultipart()
    msg["From"] = from_mail
    msg["TO"] = to_mail
    msg["Subject"] = Header("vinyl", "utf-8")
    msg["Date"] = formatdate(localtime=True)
    formatted_message = f"{message_info}<br><br>Takeaway: {takeaway}"
    msg.attach(MIMEText(formatted_message, "html", "utf-8"))

    smtp = smtplib.SMTP(server_adr, 25)
    smtp.starttls()
    smtp.ehlo()
    smtp.login(from_mail, from_passwd)
    smtp.sendmail(from_mail, to_mail, msg.as_string())
    smtp.quit()
