#attribute selection
import pandas as pd
from sklearn.datasets import load_iris,load_diabetes,load_wine
from sklearn.feature_selection import selectkbest,f_classify
#load iris dataset
d=load_iris()
x=pd.dataframe(d.data,columns=d.feature_names)
y=pd.series(d.target)
#select the top 2 features
selector=selectkbest(score_func=f_classify,k=2)
x_selected.fit_transform(x,y)
print("selected features of iris dataset:\n",x.column[selector.get_support()])
#load diabeties dataset
d=load_diabeties()
x=pd.dataframe(d.data,columns=d.feature_names)
y=pd.series(d.target)
#select the top 3 features
selector=selectkbest(score_func=f_classify,k=3)
x_selected.fit_transform(x,y)
print("selected features of diabeties dataset:\n",x.column[selector.get_support()])
#load wine dataset
d=load_wine()
x=pd.dataframe(d.data,columns=d.feature_names)
y=pd.series(d.target)
#select the top 4 features
selector=selectkbest(score_func=f_classify,k=4)
x_selected.fit_transform(x,y)
print("selected features of wine dataset:\n",x.column[selector.get_support()])

