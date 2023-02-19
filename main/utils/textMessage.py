import os

from twilio.rest import Client

account_sid = ""
auth_token = ""

client = Client(account_sid, auth_token)

def sendEmergencySMS():
    message = client.messages.create(
        to="+16692924191",
        from_="+16692000743",
        body="ALERT!!! Potential emergency situation in the ride detected by rideCare.AI")

    print(message)