
import pickle
from sklearn.preprocessing import MinMaxScaler
import numpy
import joblib

data_dict = joblib.load(open("/app/tools/final_project_dataset.pkl", "rb"))
data_dict.pop("TOTAL", 0)

salary = []
ex_stok = []
for users in data_dict:
    val = data_dict[users]["salary"]
    if val == 'NaN':
        continue
    salary.append(float(val))
    val = data_dict[users]["exercised_stock_options"]
    if val == 'NaN':
        continue
    ex_stok.append(float(val))
    
salary = [min(salary),200000.0,max(salary)]
ex_stok = [min(ex_stok),1000000.0,max(ex_stok)]

print(salary)
print(ex_stok)

salary = numpy.array([[e] for e in salary])
ex_stok = numpy.array([[e] for e in ex_stok])

scaler_salary = MinMaxScaler()
scaler_stok = MinMaxScaler()

rescaled_salary = scaler_salary.fit_transform(salary)
rescaled_stock = scaler_salary.fit_transform(ex_stok)

print(rescaled_salary)
print(rescaled_stock)