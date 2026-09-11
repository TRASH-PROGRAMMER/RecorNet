import email
from abc import ABC, abstractmethod
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class EmailPort(ABC):
    @abstractmethod
    def send_email(self, to: str, subject: str, body: str) -> bool:
        raise NotImplementedError

class EmailConnection:
    def __init__(self):
        self.email_client = email.SMTP("smtp.gmail.com", 587)
        self.email_client.starttls()
        self.email_client.login("myemailaddress@gmail.com", "password")
    def send_email(self, to: str, subject: str, body: str) -> bool:
        self.email_client.sendmail("myemailaddress@gmail.com", to, f"Subject: {subject}\n\n{body}")
        return True

