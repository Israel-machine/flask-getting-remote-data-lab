import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            data = self.load_json(response.text)
            
            return json.dumps(data, indent=2).encode('utf-8')
        else:
            return None
        
    @staticmethod
    def load_json(raw_data):
        return json.loads(raw_data)



