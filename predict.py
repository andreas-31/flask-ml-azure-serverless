import pandas as pd
from sklearn.externals import joblib
from sklearn.preprocessing import StandardScaler
import json

def scale(payload):
    """Scales Payload"""

    print("Scaling Payload:", payload)
    scaler = StandardScaler().fit(payload)
    scaled_adhoc_predict = scaler.transform(payload)
    return scaled_adhoc_predict

def predict():
    """Performs an sklearn prediction
       result looks like:
    { "prediction": [ 20.35373177134412 ] }
    
    The Boston Housing Dataset
    https://www.cs.toronto.edu/~delve/data/boston/bostonDetail.html
    There are 14 attributes in each case of the dataset. They are:
        CRIM - per capita crime rate by town
        ZN - proportion of residential land zoned for lots over 25,000 sq.ft.
        INDUS - proportion of non-retail business acres per town.
        CHAS - Charles River dummy variable (1 if tract bounds river; 0 otherwise)
        NOX - nitric oxides concentration (parts per 10 million)
        RM - average number of rooms per dwelling
        AGE - proportion of owner-occupied units built prior to 1940
        DIS - weighted distances to five Boston employment centres
        RAD - index of accessibility to radial highways
        TAX - full-value property-tax rate per $10,000
        PTRATIO - pupil-teacher ratio by town
        B - 1000(Bk - 0.63)^2 where Bk is the proportion of blacks by town
        LSTAT - % lower status of the population
        MEDV - Median value of owner-occupied homes in $1000's
    """

    json_payload = {
        "CHAS":{
            "0":1
        },
        "RM":{
            "0":3000.5
        },
        "TAX":{
            "0":296.0
        },
        "PTRATIO":{
            "0":15.3
        },
        "B":{
            "0":100000000
        },
        "LSTAT":{
            "0":4.98
        }
    }

    try:
        clf = joblib.load("boston_housing_prediction.joblib")
    except:
        print("JSON payload:", json_payload)
        return "Model not loaded"

    print("JSON payload:", json_payload)
    inference_payload = pd.DataFrame(json_payload)
    print("inference payload DataFrame:", inference_payload)
    scaled_payload = scale(inference_payload)
    print("Scaled Payload:", scaled_payload) # FIX: scaled payload is always [[0. 0. 0. 0. 0. 0.]]
    #scaled_payload = [[0.1, 0.1, 0.1, 0.1, 0.1, 0.1]] # {"prediction": [19.859930839357617]}
    prediction = list(clf.predict(scaled_payload))
    return json.dumps({'prediction': prediction})

if __name__ == "__main__":
    print(predict())
