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

## Description How To Use CI/CD Pipline with GitHub and Azure
After setting up an [Azure account](https://azure.microsoft.com/en-us/free/), log into the Azure portal and start the [Azure Cloud Shell](https://docs.microsoft.com/en-us/azure/cloud-shell/overview). Clone the repository into Azure Cloud Shell via HTTPS or SSH. The following screenshot shows the command for cloning via SSH.

| ![Project cloned into Azure Cloud Shell](https://user-images.githubusercontent.com/20167788/115139793-3ef63b00-a034-11eb-9766-dbfe9cc983f1.PNG) | 
|:--:| 
| *Project cloned into Azure Cloud Shell* |

After having successfully cloned the repository, setup a Python virtual environment with required dependencies (modules) by running following commands.
```
make setup
source ~/.azure-devops/bin/activate
make all
```
A Python 3.7 virtual environment is created in a hidden subfolder in your home directory: ```~/.azure-devops``` and is activated. Required Python modules listed in ```requirements.txt``` are installed, Python files are linted and the ML app is tested.

| ![Passing tests after make all](https://user-images.githubusercontent.com/20167788/115149682-81843b80-a065-11eb-8e58-e7be4a368939.PNG) | 
|:--:| 
| *Passing tests that are displayed after running the ```make all``` command from the Makefile.* |

Unit tests are configured with pytest and can be run explicitly by executing the command ```make test```. These tests are defined in files ```tests/conftest.py``` and ```tests/unit/test_app.py```. Unit tests check the availability and responses of the Flask routes or URLs "/" and "/predict".

| ![Output of a test run](https://user-images.githubusercontent.com/20167788/115150446-b8a81c00-a068-11eb-8e4b-0eacd65aa881.PNG) | 
|:--:| 
| *Output of a test run started with ```make test```* |
