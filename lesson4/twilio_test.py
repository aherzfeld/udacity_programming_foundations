import os
from dotenv import load_dotenv
from twilio.rest import Client

# load env vars
basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

# Your Account SID from twilio.com/console
account_sid = os.environ.get('ACCOUNT_SID')
# Your Auth Token from twilio.com/console
auth_token = os.environ.get('AUTH_TOKEN')

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+61423064195",
    from_="+61423064195",
    body="Hello from Python!")

print(message.sid)
