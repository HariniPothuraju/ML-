import pandas as pd
from sklearn import linear_model
from sklearn.neighbors import KNeighborsRegressor
df=pd.read_csv("Example1.CSV")
X=df[['Pattern1','Pattern2']]
Y=df['Target']
r=linear_model.LinearRegression()
r.fit(X.values,Y.values)
Y_P=r.predict([0.3,0.4])
print("predict values using linearRegressionis:",Y_P)
Knn_r=KNeighboursRegression(n_neighbours=5)
Knn_r=r.fit(X.values,Y.values)
Y_P_r=Knn_r.predict([0.3,0.4])
print("predicted values using Knn is:",Y_P_r)
