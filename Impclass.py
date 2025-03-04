import pandas as pd
from SKlearn.tree import decisiontreeclassifier
import matplotlibpyplot as plt
df=pd.read_CSV("example1.CSV")
#print(df)
#specifying features and classses
features=['feature1','feature2']
X=df[features]
Y=['class']
#classsification based on decision tree
dtree=decisiontree(classifier)
model=dtree.fit(X,Y)
tree.plot=tree(model,feature_names=features)
#text represntation of decision tree
dt_tree=treeexport_text(dtree)
print(dt_text)
