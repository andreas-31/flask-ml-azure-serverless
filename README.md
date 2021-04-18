# flask-ml-azure-serverless
Deploy Flask Machine Learning Application on Azure App Services

## Purpose of Machine Learning Application
The application is implemented in Python by using the Flask framework. It uses a pre-built machine learning model to predict housing prices based on the [Bosten Housing Dataset](https://www.kaggle.com/prasadperera/the-boston-housing-dataset). The prediction functionality is made available as API endpoint "/predict". By sending a feature set formatted as JSON in an HTTP POST request, the predicted price is returned formatted as JSON. Example for querying the API endpoint:
```
curl -d '{
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
```
Note: the following bash scripts can be used to send these requests for yourself.
- ```make_predict.sh``` to query an app running on your local machine
- ```make_predict_azure_app.sh``` to query an app running remotly on another machine

## Architecture of Machine Learning Application

## Description of Using this Repo to Create a CI/CD Pipline with GitHub and Azure


