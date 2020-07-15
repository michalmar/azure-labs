import os
import pandas as pd
import azureml.core
from azureml.core import Dataset, Run

from sklearn.linear_model import Ridge
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
# from sklearn.externals import joblib
import joblib

import lightgbm as lgb


print(azureml.core.VERSION)

os.makedirs('./outputs', exist_ok=True)

run = Run.get_context()

# get input dataset by name
base_path = run.input_datasets['taxi_data']
# print(base_path)

final_df = pd.read_csv(base_path)

y_df = final_df.pop("totalAmount")
x_df = final_df

x_train, x_test, y_train, y_test = train_test_split(x_df, y_df, test_size=0.2, random_state=223)

# Log the algorithm parameters to the run
run.log('num_leaves', 31)
run.log('learning_rate', 0.05)
run.log('n_estimators', 20)

# setup model, train and test
gbm = lgb.LGBMRegressor(num_leaves=31,
                        learning_rate=0.05,
                        n_estimators=20)
model_gbm = gbm.fit(x_train, y_train,
        eval_set=[(x_test, y_test)],
        eval_metric='l1',
        early_stopping_rounds=5)

preds = model_gbm.predict(x_test)

# Output the Mean Squared Error to the notebook and to the run
print('Mean Squared Error is', mean_squared_error(y_test, preds))
run.log('mse', mean_squared_error(y_test, preds))

# Save the model to the outputs directory for capture
model_file_name = './outputs/model.pkl'

joblib.dump(value = model_gbm, filename = model_file_name)

# upload the model file explicitly into artifacts 
run.upload_file(name = model_file_name, path_or_stream = model_file_name)
