#!/usr/bin/env bash

PORT=443
app_name="flask-ml-service-agaupmann"
URL="https://${app_name}.azurewebsites.net:$PORT/predict"

echo "Getting prediction from URL: $URL"

# POST method predict
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
     -X POST "$URL" 

curl -d '{
   "CHAS":{
      "0":1
   },
   "RM":{
      "0":6.421
   },
   "TAX":{
      "0":242.0
   },
   "PTRATIO":{
      "0":17.8
   },
   "B":{
      "0":396.90
   },
   "LSTAT":{
      "0":9.14
   }
}'\
     -H "Content-Type: application/json" \
     -X POST "$URL" 

