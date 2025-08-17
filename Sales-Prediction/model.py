import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

df=  pd.read_csv("advertising_sales_data_1000rows.csv")
X= df[["TV","Radio","Newspaper"]]
y= df["Sales"]
regressor_model = LinearRegression()

regressor_model.fit(X,y)

pickle.dump(regressor_model, open('regressor_model.pkl', 'wb'))



