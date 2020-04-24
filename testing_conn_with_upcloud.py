import http.client
import base64
import json

class BaseAPI:
    api = "api.upcloud.com"
    api_v = "1.3"
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
        
if __name__ == "__main__":
    Account().do()
