import numpy as np
import pandas as pd

from split import split_data

data=pd.read_excel('./data/data.xlsx')

#Split the data using the function split in split.py
def feature_standard(data):
  ######## write your code #########
  mu=np.mean(data,axis=0)
  std=np.std(data,axis=0)
  data_scaled= (data- mu )/std

  return data_scaled
#call the function feature_standart
data.iloc[:,:-1] = feature_standard(data.iloc[:,:-1])

X_train,X_test,Y_train,Y_test=split_data(data,0.8)