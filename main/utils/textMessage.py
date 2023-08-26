import os

from dotenv import load_dotenv
load_dotenv()

from twilio.rest import Client

account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.get_env("TWILIO_AUTH_TOKEN")

client = Client(account_sid, auth_token)

def sendEmergencySMS():
    message = client.messages.create(
        to=os.getenv("MY_PHONE_NUMBER"),
        from_="+16692000743",
        body="ALERT!!! Potential emergency situation in the ride detected by rideCare.AI")

    print(message)