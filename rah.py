import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from xgboost import XGBClassifier
import pickle
import warnings
warnings.filterwarnings("ignore")

data=pd.read_csv('parkinsons.csv')
X= data.drop(['status','name'],axis=1)
y=data['status']

X_train, X_test, y_train, y_test= train_test_split(X, y, random_state=7)
model = XGBClassifier()
model.fit(X_train, y_train)
pickle.dump(model,open('model.pkl','wb'))


