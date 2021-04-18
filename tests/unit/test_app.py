# Definition of unit tests to be run by pylint
# https://pylint.org/ | https://pypi.org/project/pylint/

# Testing main URL of app by sending HTTP GET request
def test_html(client, my_html):
    landing = client.get("/")
    html = landing.data.decode()
    print(html) # $ pytest -rP
    #assert "<h3>Sklearn Prediction Home</h3>" in html
    assert my_html in html

# https://stackoverflow.com/questions/45703591/how-to-send-post-data-to-flask-using-pytest-flask
# Testing prediction URL of app by sending HTTP POST request
def test_predict(client, my_prediction):
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
    url = '/predict'

    response = client.post(url, json=data)
    print(response, "Prediction:", response.json['prediction'][0]) # $ pytest -rP

    assert response.content_type == 'application/json'
    assert response.json['prediction'][0] == my_prediction['prediction'][0]

