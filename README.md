# flask-ml-azure-serverless
[![Python application test with Github Actions](https://github.com/andreas-31/flask-ml-azure-serverless/actions/workflows/main.yml/badge.svg)](https://github.com/andreas-31/flask-ml-azure-serverless/actions/workflows/main.yml)

Deploy Flask Machine Learning Application on Azure App Services

## API of Machine Learning Application
The application is implemented in Python by using the Flask framework. It uses a pre-built machine learning model to predict housing prices based on the [Bosten Housing Dataset](https://www.kaggle.com/prasadperera/the-boston-housing-dataset). The prediction functionality is made available as API endpoint "/predict". By sending a feature set formatted as JSON in an HTTP POST request, the predicted price is returned formatted as JSON. Example for querying the API endpoint:
```
$ curl -d '{
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
}'\
     -H "Content-Type: application/json" \
     -X POST "https://flask-ml-service-agaupmann.azurewebsites.net/predict"

{"prediction":[20.35373177134412]}
```
Note: the following bash scripts can be used to send these requests for yourself.
- ```make_predict.sh``` to query an app running on your local machine
- ```make_predict_azure_app.sh``` to query an app running remotly on another machine

## Architecture of Machine Learning Application

## Description of Using this Repo to Create a CI/CD Pipline with GitHub and Azure
After seeting up an Azure account you can log into the Azure portal and start a cloud shell. In the cloud shell you can clone the repository with the command
```
$ git clone git@github.com:andreas-31/flask-ml-azure-serverless.git
```

| ![Project cloned into Azure Cloud Shell](https://user-images.githubusercontent.com/20167788/115139793-3ef63b00-a034-11eb-9766-dbfe9cc983f1.PNG) | 
|:--:| 
| *Project cloned into Azure Cloud Shell* |
