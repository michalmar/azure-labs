
# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------
import json
import pickle
import numpy as np
import pandas as pd
import azureml.train.automl
from sklearn.externals import joblib
from azureml.core.model import Model

from inference_schema.schema_decorators import input_schema, output_schema
from inference_schema.parameter_types.numpy_parameter_type import NumpyParameterType
from inference_schema.parameter_types.pandas_parameter_type import PandasParameterType


input_sample = pd.DataFrame({"vendorID": pd.Series(["2.0"], dtype="float64"), "passengerCount": pd.Series(["1.0"], dtype="float64"), "tripDistance": pd.Series(["1.45"], dtype="float64"), "month_num": pd.Series(["6.0"], dtype="float64"), "day_of_month": pd.Series(["3.0"], dtype="float64"), "day_of_week": pd.Series(["2.0"], dtype="float64"), "hour_of_day": pd.Series(["13.0"], dtype="float64")})
output_sample = np.array([0])


def init():
    global model
    # This name is model.id of model that we want to deploy deserialize the model file back
    # into a sklearn model
    model_path = Model.get_model_path(model_name = 'nyc_regression')
    model = joblib.load(model_path)


@input_schema('data', PandasParameterType(input_sample))
@output_schema(NumpyParameterType(output_sample))
def run(data):
    try:
        result = model.predict(data)
        return json.dumps({"result": result.tolist()})
    except Exception as e:
        result = str(e)
        return json.dumps({"error": result})
