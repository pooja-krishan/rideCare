import os

from twilio.rest import Client

account_sid = "ACead014df8c6300f40ed0c115dacb72d3"
auth_token = "3c128706ac2c8c5078c23bc61a067ba6"

client = Client(account_sid, auth_token)

def sendEmergencySMS():
    message = client.messages.create(
        to="+16692924191",
        from_="+16692000743",
        body="ALERT!!! Potential emergency situation in the ride detected by rideCare.AI")

    print(message)