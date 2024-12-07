from text_message import TextMessage
from twilio.base.exceptions import TwilioRestException
import os

MY_PHONE_NUMBER = os.environ["MY_PHONE_NUMBER"]

if __name__ == "__main__":
    text_message = TextMessage()
    text = "Hey there, what you're doing is amazing!"

    try:
        text_message.send(
            recipient=MY_PHONE_NUMBER,
            message=text,
        )
        print(f"Successfully sent the message to {MY_PHONE_NUMBER}")

    except ValueError as e:
        print(e)

    except TwilioRestException as e:
        print(e)
