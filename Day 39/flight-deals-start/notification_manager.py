from twilio.rest import Client

TWILIO_SID = 'AC79bbcb586907bdaf95747e945d38e169'
TWILIO_AUTH_TOKEN = '712b5db344c175e07a85c4dca1061cce'
TWILIO_VIRTUAL_NUMBER = '+19897122708'
TWILIO_VERIFIED_NUMBER = '+15194041210'


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