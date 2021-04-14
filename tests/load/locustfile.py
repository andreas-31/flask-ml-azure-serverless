# Definition of load tests to be run by locust
# https://locust.io/ | https://pypi.org/project/locust/

from locust import HttpUser, between, task


class WebsiteUser(HttpUser):
    wait_time = between(5, 15)
    
    @task
    def index(self):
        self.client.get("/")
    
    @task
    def predict(self):
        data = {
            "CHAS":{
                "0":0
            },
            "RM":{
                "0":6.575
            },
            "TAX":{
                "0":296.0
            },
            "PTRATIO":{
                "0":15.3
            },
            "B":{
                "0":396.9
            },
            "LSTAT":{
                "0":4.98
            }
        }
        response = self.client.post("/predict", json=data)

        # extract the prediction value from the JSON response
        json_var = response.json()
        print("Prediction:", json_var['prediction'][0])

# $ locust -f locustfile.py
