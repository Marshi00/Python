from twilio.rest import Client
import smtplib

TWILIO_SID = ''
TWILIO_AUTH_TOKEN = ''
TWILIO_VIRTUAL_NUMBER = '+'
TWILIO_VERIFIED_NUMBER = '+'
MY_EMAIL = ""
MY_PASSWORD = ""
MAIL_PROVIDER_SMTP_ADDRESS = "smtp.gmail.com"


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)

    def send_emails(self, message, emails, link):
        with smtplib.SMTP(MAIL_PROVIDER_SMTP_ADDRESS, port=587) as connection:
            # make an app password in your Google account, and it is different from normal pass , 2 step must be active
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            for email in emails:
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=email,
                    msg=f"Subject:New Low Price !\n\n{message}\n{link}".encode('utf-8')
                )
