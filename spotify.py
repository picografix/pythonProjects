import datetime
import requests
from urllib.parse import urlencode
import base64
client_id = '913e8eccae4e44dd90c3ce3ff8933be2'
client_secret = 'eec2117dcbf84d5498608a1259059d27'
class SpotifyAPI(object):
    access_token = None
    access_token_expires = datetime.datetime.now()
    client_id  = None
    client_secret = None
    token_url = "https://accounts.spotify.com/api/token"
    access_token_did_expires = True
    def __init__(self,client_id,client_secret,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.client_id = client_id
        self.client_secret = client_secret
    def get_client_credentials(self):
        #returns base64 credentials
        client_id=self.client_id
        client_secret = self.client_secret
        client_creds =  f"{client_id}:{client_secret}"
        client_creds_b64 = base64.b64encode(client_creds.encode())
        return client_creds_b64.decode()
    def get_token_header(self):
        client_creds_b64 = self.get_client_credentials()
        token_header = {
        "Authorization" : f"Basic {client_creds_b64}"
        }
        return token_header
    def get_token_data(self):
        token_data = {
        "grant_type":"client_credentials"
        }
        return token_data

    def performAuth(self):
        token_url = self.token_url
        token_data  = self.get_token_data()
        token_header = self.get_token_header()
        r = requests.post(token_url,data=token_data,headers=token_header)
        valid_request = r.status_code in range(200,299)
        if not valid_request:
            return False
        data = r.json()
        now = datetime.datetime.now()
        access_token  = data['access_token']
        self.access_token = access_token
        expires_in = data['expires_in']
        expires = now+datetime.timedelta(seconds=expires_in)
        self.access_token_expires = expires
        self.access_token_did_expires = expires<now
        did_expire = expires < now
        return True
client = SpotifyAPI(client_id,client_secret)
client.performAuth()
access_token = client.access_token
header = {
    "Authorization":f"Bearer {access_token}"
}
endpoint = "https://api.spotify.com/v1/search"
data = urlencode({"q":"Time","type":"track"})
lookup_url = f"{endpoint}?{data}"
r = requests.get(lookup_url,headers = header)
print(r.status_code)
print(r.json())