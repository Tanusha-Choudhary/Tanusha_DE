#Rain Alert
#How to Authentication-> using API key
#Using thie API provider monitor how someone is using and if have to charge or not (Free or For company
https://openweathermap.org/api/forecast5?collection=current_forecast
https://www.latlong.net/
long: 52.370216
lat: 4.895168
1)Twilio: Account creation: https://console.twilio.com/us1/develop/
Account_id and Auth_token
login ang get both the deails from that site
from twilio.rest import Client
2) Pythonanywhere account to schdeule the job :
-Add two commands : proxy_client = TwilioHttpClient()
                    proxy_client.session.proxies={'https':os.environ['https_proxy]'}
                    client = Client(account_id,auth_token,http_client=proxy_client)


