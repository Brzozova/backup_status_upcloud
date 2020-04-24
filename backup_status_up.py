from collections import OrderedDict, defaultdict
from requests.auth import HTTPBasicAuth
from collections import defaultdict
from socket import gethostname
import http.client
import base64
import json

class BaseAPI:
    api = "api.upcloud.com"
    api_v = "1.3"
    # Add username and password in place of API_ID and API_SECRET
    token = base64.b64encode('API_ID:API_SECRET'.encode())
    def get(self, endpoint):
        conn = http.client.HTTPSConnection(self.api)
        url = "/" + self.api_v + endpoint
        headers = {
            "Authorization": "Basic " + self.token.decode(),
            "Content-Type": "application/json"
        }
        conn.request("GET", url, None, headers)
        res = conn.getresponse()
        self.printresponse(res.read())
    def printresponse(self, res):
        data = res.decode(encoding="UTF-8")
        print(data)

class Account(BaseAPI):
    endpoint="/account"
    def do(self):
        self.get(self.endpoint)
# Get a list of servers
class Servers(BaseAPI):
    endpoint = "/server"
    def do(self):
        self.get(self.endpoint)
    def backups_list(self):
        for d in srvid['servers']['server']:
            srvtitle = d['title']
            srvid = d['uuid']
            print(srv)
    endpoint = "/server/" + srvid
    def Backup_List(self):
        self.get(self.endpoint)
        endpoint = "/server/" + srvid

if __name__ == "__main__":
    srvid = Servers().do()
