# The Azure CLI can be used for manual deployment of the application into Azure App Services.
# The following commands can be used to manage the application on the command line.

# Make a dryrun to see if deployment to Azure App Services would be successful
az webapp up -n flask-ml-service-agaupmann --location eastus --sku F1 --dryrun

# Deploy the application to Azure Web Services
az webapp up -n flask-ml-service-agaupmann --location eastus --sku F1

# List all deployed applications
az webapp list

# Redeploy of application, e.g. after implmenting new functionality
az webapp up

# Get the details of a web app's logging configuration
az webapp log show

# Start live log tracing for a web app
az webapp log tail

# Remove the application's deployment from Azure App Services
az webapp delete --name flask-ml-service
