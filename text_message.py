from dotenv import load_dotenv
from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException
import os

load_dotenv()

ACCOUNT_SID = os.environ["TWILIO_ACCOUNT_SID"]
AUTH_TOKEN = os.environ["TWILIO_AUTH_TOKEN"]
MESSAGING_SERVICE_SID = os.environ["MESSAGING_SERVICE_SID"]


class TextMessage:
    def __init__(self):
        """
        Initialize the Twilio client for sending messages.

        """
        self.client = Client(ACCOUNT_SID, AUTH_TOKEN)

    def send(self, recipient: str, message: str):
        """
        Send the text message to the recipient using Twilio's API.

        Raises:
            ValueError - If the message exceeds 160 characters
            TwilioRestException - If there's error with twilio
        """
        if len(message) > 160:
            raise ValueError("The message exceeds 160 characters!")

        try:
            # Create and send the text message
            message = self.client.messages.create(
                messaging_service_sid=MESSAGING_SERVICE_SID,
                body=message,
                to=recipient,
            )
            return True

        except TwilioRestException:
            raise
