import logging
from dotenv import dotenv_values
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

ENV_FILE = 'tools/.env.email'

class NotifierEmail:
    __smtp = None

    def __init__(self) -> None:
        self.useSendMail()

    def useSendMail(self) -> None:
        self.__smtp = smtplib.SMTP('localhost')

    def send(self, title: str, content: str, contentType: str = 'plain') -> None:
        envs = dotenv_values(ENV_FILE)

        sender = envs['EMAIL_SENDER']
        recipients = envs['EMAIL_RECIPIENTS'].split(',')
        recipients = list(filter(None, recipients))

        if 0 == len(recipients):
            logging.warning('[SCRAPPY][NotifierEmail] Empty recipients list. Are you really want to send any e-mail?')
            return

        message = MIMEMultipart('alternative')
        message['Subject'] = title
        message['From'] = sender
        message['To'] = ','.join(recipients)
        message.attach(MIMEText(content, contentType))

        self.__smtp.sendmail(sender, recipients, message.as_string())
        self.__smtp.quit()
