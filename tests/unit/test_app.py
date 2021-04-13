import pytest

def test_predict(client):
    landing = client.get("/")
    html = landing.data.decode()
    print(html) # $ pytest -rP
    #assert input_value % 3 == 0
