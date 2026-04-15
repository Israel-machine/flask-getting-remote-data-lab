import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        #Query End-Point
        response = requests.get(self.url)
        if response.status_code==200:
            return self.load_json(response.text)
        else:
            return None
        
    #CONVERTS & RETURNS END POINT DATA TO JSON 
    def load_json(self, raw_data):
        data = json.loads(raw_data)
        return data
    

#EXECUTION AND TESTING:
test = GetRequester("https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json")

data = test.get_response_body()

print(data)



