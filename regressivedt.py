import pandas as pd
from SKlearn import tree
from SKlearn.tree import decisiontreeregression
from SKlearn.tree import plot_tree
import matplotlib.pyplot as plt
df=pandas.read_CSV("example1.CSV")
features=['feature1','feature2']
X=df[features]
Y=df['target']
dtree=decisiontreeregression()
model=d.tree.fit(x.values,y.values)
p=dtree.predict([0.7,0.5])
print("predicted values using DTR is:",p)
plt.figure(fig_size=(10,10))
plot_tree{mode,feature_name=features,font_size=10}
plt.tree("decision tree structure")
plt.show
