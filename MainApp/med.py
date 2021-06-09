import os
from twilio.rest import Client
#from twilio.http.http_client import TwilioHttpClient

#proxy_client = TwilioHttpClient(proxy={'http': os.environ['http_proxy'], 'https': os.environ['https_proxy']})

TWILIO_ACCOUNT_SID ='AC1b9671b12aae30d426e275106cd060f6'
TWILIO_AUTH_TOKEN = '85896c1e9da2b4eccfa4699da4b6947d'
account_sid = os.environ[TWILIO_ACCOUNT_SID]
auth_token = os.environ[TWILIO_AUTH_TOKEN]


client = Client(acc_sid, auth_token)
# data to be sent from api
message = client.messages.create(
    messaging_service_sid='TheElderly',
    body = 'Take your medicines!! Stay healthy and fit! Have a nice day!!',
    to = '+919561643273'
    )
print(message.sid)
