# flask-ml-azure-serverless
[![Python application test with Github Actions](https://github.com/andreas-31/flask-ml-azure-serverless/actions/workflows/main.yml/badge.svg)](https://github.com/andreas-31/flask-ml-azure-serverless/actions/workflows/main.yml)

Deploy Flask Machine Learning Application on Azure App Services

## Overview of the Project
### Functionality and API of Machine Learning Application
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

### Architecture of Machine Learning Application
| ![Architectural Diagram of the Machine Learning application](https://user-images.githubusercontent.com/20167788/115421185-0acd7680-a1fc-11eb-8cde-47e7ea61d5c5.png) | 
|:--:| 
| *Architectural Diagram of the Machine Learning application* |

The architecture of the Machine Learning Application comprises the following elements and services:
- GitHub
    * Version Control: Git repository for application's source code and configuration files
    * CI/CD Pipeline: GitHub actions workflow for automated Continuous Integration and Continuous Delivery of the application
- Azure (Microsoft's Public Cloud)
    * [App Service](https://azure.microsoft.com/en-us/services/app-service/): managed platform for deploying and running web applications.
    * [App Service Plan](https://docs.microsoft.com/en-us/azure/app-service/overview-hosting-plans): defines a set of compute resources for a web app to run.
        + Region (West US, East US, etc.)
        + Number of VM instances
        + Size of VM instances (Small, Medium, Large)
        + Pricing tier (Free, Shared, Basic, Standard, Premium, PremiumV2, PremiumV3, Isolated)
    * [Resource Group](https://docs.microsoft.com/en-us/azure/azure-resource-manager/management/manage-resource-groups-portal): logical container that holds related Azure resources created for the application.
    * [Azure DNS](https://azure.microsoft.com/en-us/services/dns/): an Internet URL is assigned to the application for the clients to access the application over the Internet.
    * [Cloud Shell](https://docs.microsoft.com/en-us/azure/cloud-shell/overview): a command line interface (bash or PowerShell) that is available after login into the Azure Portal. It has persistent storage for files and provides a Linux environment that can be used for application development and Azure administration.
    * [Azure Active Directory](https://azure.microsoft.com/en-us/services/active-directory/): identity service providing authentication and authorization of users and services.

### Project Management

#### Trello Board
Link to Trello Board: [Task Board Udacity](https://trello.com/b/1wJA8THi/task-board-udacity)

#### Project Plan
Link to project plan on Google Sheets: [Udacity Project Plan](https://docs.google.com/spreadsheets/d/1ndce_5hmYX9DcHrf5YyK9V8OKs6JIFIIEpAznDf6vY8/edit?usp=sharing)

### Demo of Application with Screencast
Link to YouTube video: [Demo CI/CD Pipeline for Web Application](https://youtu.be/4LDal-ULovw)

## Description How To Use Project's CI/CD Pipline with GitHub and Azure
### Application Development and Testing in Azure Cloud Shell
#### Azure Cloud Shell Setup
After setting up an [Azure account](https://azure.microsoft.com/en-us/free/), log into the Azure portal and start the [Azure Cloud Shell](https://docs.microsoft.com/en-us/azure/cloud-shell/overview). Clone the repository into Azure Cloud Shell via HTTPS or SSH. The following screenshot shows the command for cloning via SSH.

| ![Project cloned into Azure Cloud Shell](https://user-images.githubusercontent.com/20167788/115139793-3ef63b00-a034-11eb-9766-dbfe9cc983f1.PNG) | 
|:--:| 
| *Project cloned into Azure Cloud Shell* |

#### Prepare Environment in Azure Cloud Shell
After having successfully cloned the repository, set up a Python virtual environment with required dependencies (modules) by running following commands.
```
$ make setup                          # Python virtual environment is created in a hidden subfolder in user's home directory
$ source ~/.azure-devops/bin/activate # Python virtual environment is activated
(.azure-devops)$ make all             # Required Python modules listed in "requirements.txt" are installed, Python files are linted and the ML app is tested
```

| ![Passing tests after make all](https://user-images.githubusercontent.com/20167788/115149682-81843b80-a065-11eb-8e58-e7be4a368939.PNG) | 
|:--:| 
| *Passing tests that are displayed after running the ```make all``` command from the Makefile.* |

#### Testing the Application
After making changes to the code or configuration files and before committing and pushing changes to the repository, run unit tests and load tests to make sure that the application is working as expected and without errors.
##### Unit Tests
Unit tests are configured with pytest and can be run explicitly by executing the command ```make test```. These tests are defined in files ```tests/conftest.py``` and ```tests/unit/test_app.py```. Unit tests check the availability and responses of the Flask routes or URLs "/" and "/predict".

| ![Output of a test run](https://user-images.githubusercontent.com/20167788/115150446-b8a81c00-a068-11eb-8e4b-0eacd65aa881.PNG) | 
|:--:| 
| *Output of a test run started with ```make test```* |

##### Load Tests
Load tests are configured and executed with locust and can be run explicitly by executing one of these commands:
- ```make loadlocalhost```: after starting the application by running ```python3 ./app.py``` on localhost (http://localhost:5000), load test the application 
- ```make load```: load test the application that is deployed on Azure App Services (in my case https://flask-ml-service-agaupmann.azurewebsites.net)
Generated traffic load is sent to Flask routes or URLs "/" and "/predict".

| ![Load testing ML app running on localhost, Page 1](https://user-images.githubusercontent.com/20167788/115356054-9246c580-a1bb-11eb-9e4b-10a2ca41dd31.png) | 
|:--:| 
| *Load testing ML app running on localhost with locust. Testing can also be started with command ```make loadlocalhost```, Page 1* |

| ![Load testing ML app running on localhost, Page 2](https://user-images.githubusercontent.com/20167788/115356065-9541b600-a1bb-11eb-8d7a-f5980fbc6409.png) | 
|:--:| 
| *Load testing ML app running on localhost with locust. Testing can also be started with command ```make loadlocalhost```, Page 2* |

As soon as the test runs in Azure Cloud Shell have been successfully passed, the changes in the application's code files can be pushed to the remote repository on GitHub.
```
(.azure-devops)$ git commit -am "Description of changes"
(.azure-devops)$ git push
```

#### GitHub Actions for Automated CI and CD
The GitHub Actions workflow for Continuous Integration and Continuous Delivery (CI/CD) is started automatically as soon as changes are committed to the GitHub repository. The CI/CD workflow is defined in the YAML file ```.github/workflows/main.yml``` in this repository and contains these stages:
- CI: Set up Python environment
- CI: Install dependencies
- CI: Lint Python source code with pylint
- CI: Run tests with pytest and locust
- CD: Login to Azure
- CD: Configure Azure App Services
- CD: Deploy app to Azure App Services
- CD: Logout from Azure
- CD: Run load tests against deployed app with locust

| ![GitHub Actions YAML file for CI and CD, Page 1](https://user-images.githubusercontent.com/20167788/115237132-7b04cb00-a11c-11eb-877a-1c0f1faf5823.png) | 
|:--:| 
| *GitHub Actions YAML file for CI and CD, Page 1* |

| ![GitHub Actions YAML file for CI and CD, Page 2](https://user-images.githubusercontent.com/20167788/115237153-822bd900-a11c-11eb-90d6-e74c61d5f5f7.png) | 
|:--:| 
| *GitHub Actions YAML file for CI and CD, Page 2* |

### Continuous Delivery
*Note: Microsoft made a change in Azure Pipelines Grant for Public Projects. It set the maximum number of build requests to 0. This means that nothing is built until you pay for it or you can get a free grant. Please [see this blog post](https://devblogs.microsoft.com/devops/change-in-azure-pipelines-grant-for-public-projects/).
According to Xiaodi from the Udacity Student Services Team it’s ok to use Github Actions instead of Azure Pipeline in the project.*

#### Deploy the application using GitHub Actions into Azure App Services
| ![Screenshot of Azure Azure App Service showing deployed ML application](https://user-images.githubusercontent.com/20167788/115397275-347ba300-a1e6-11eb-95d5-f07fde558c31.PNG) | 
|:--:| 
| *Screenshot of Azure Azure App Service showing deployed ML application* |

| ![Screenshot of a successful prediction in Azure Cloud Shell](https://user-images.githubusercontent.com/20167788/115397276-347ba300-a1e6-11eb-8a13-8f59395879ea.PNG) | 
|:--:| 
| *Screenshot of a successful prediction in Azure Cloud Shell* |

#### Use the Azure CLI to deploy and manage an application
The Azure CLI can be used for manual deployment of the application into Azure App Services. The following commands can be used to manage the application on the command line.
```
# Make a dryrun to see if deployment to Azure App Services would be successful
az webapp up -n flask-ml-service-agaupmann --location eastus --sku F1 --dryrun

# Deploy the application to Azure Web Services
az webapp up -n flask-ml-service-agaupmann --location eastus --sku F1

# List all deployed applications
az webapp list

# Redeploy of application, e.g. after implementing new functionality
az webapp up

# Get the details of a web app's logging configuration
az webapp log show

# Start live log tracing for a web app
az webapp log tail

# Remove the application's deployment from Azure App Services
az webapp delete --name flask-ml-service
```
These Azure CLI commands are also provided in the file ```commands.sh``` in this repository.

#### Test the application inside of GitHub Actions
| ![Test application inside of GitHub Actions workflow](https://user-images.githubusercontent.com/20167788/115404890-04d09900-a1ee-11eb-9450-dcc9a88023b3.PNG) | 
|:--:| 
| *Test application inside of GitHub Actions workflow: the testing steps are "Test with pytest" before deployment and "Run load tests" after deployment* |

| ![Test application inside of GitHub Actions workflow with pytest](https://user-images.githubusercontent.com/20167788/115404899-05692f80-a1ee-11eb-8154-00f0481e9fcb.PNG) | 
|:--:| 
| *Running unit tests inside of Github Actions with pytest in the workflow step "Test with pytest"* |

#### Load test the application using Locust
| ![Test application inside of GitHub Actions workflow with locust, Page 1](https://user-images.githubusercontent.com/20167788/115404650-d226a080-a1ed-11eb-8617-3fc6158260d7.PNG) | 
|:--:| 
| *Running load tests inside of Github Actions with locust in the workflow step "Run load tests", Page 1* |

| ![Test application inside of GitHub Actions workflow with locust, Page 2](https://user-images.githubusercontent.com/20167788/115404656-d2bf3700-a1ed-11eb-996f-a51048392876.PNG) | 
|:--:| 
| *Running load tests inside of Github Actions with locust in the workflow step "Run load tests", Page 2* |

## Possible Improvements of the Application in the Future
- Containerization: create a Docker image and publish it on DockerHub
- Run application on Kubernetes and pull container image from DockerHub
- Add authentication so that only known users are allowed to access the API
- A selection of multiple machine learning models could be provided for the user to select when calling the API endpoint
