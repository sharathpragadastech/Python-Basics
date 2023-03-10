# -*- coding: utf-8 -*-
"""Linear_Regression(Insurance).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zS-sm8vomi4eBWHwD9dea-AbznvI1_l_

Step 1 : Gathering the Data1
"""

import numpy as np
import pandas as pd
data = pd.read_csv('/content/insurance.csv')
data.head()

"""Step2 : Data cleaning /Data preprocesing"""

#one hot encoding will be done to convert categorical variables to numerical variables
data['sex'] = data['sex'].apply({'male':0,'female':1}.get)
data['smoker'] = data['smoker'].apply({'no':0,'yes':1}.get)
data['region'] = data['region'].apply({'southeast':0,'southwest':1,'northeast':2,'northwest':3}.get)
data.head()

"""Step3 : Divide the data into independant(x) and dependant(y) variables."""

x = data[['age','sex','bmi','children','smoker','region']] # independant columns
y = data['charges'] # dependant column
x.head()

y.head()

"""Step4 : Split the data into two parts for testing and training"""

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2) # 0.2 means 20% data for testing

x_train.shape

x_test.shape

"""# Creating machine learning model for Linear Regression algorithum"""

from sklearn.linear_model import LinearRegression # importing the linear regression model
regression = LinearRegression() # creating the variable for model

regression.fit(x_train,y_train) #fit() is used to train the machine learning model by providing x_train and y_train as input variables

predictions = regression.predict(x_test) #predict() is used to predict the output from machine learning model which then gets compared to y_test 
print(predictions.size)
print(predictions) # charges produced by the machine learning model for x_test

regression.score(x,y) # score shows the accurasy of the machine rearning model

"""For the new customer how much should be the insurance cost(charges)?"""

new = {'age':23,'sex':0,'bmi':27,'children':0,'smoker':0,'region':1} # dictionary for the new customer data
index=[1]
newdata = pd.DataFrame(new,index) # convert into the dataframe
print(newdata)

prediction = regression.predict(newdata)
print(prediction)
