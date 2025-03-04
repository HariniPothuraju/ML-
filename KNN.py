import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier

# Training pattern
X = [0, 0.8, 1.1, 0.7, 1.1, 3, 3.7, 4.1, 3.7, 4.1, 3.7, 4.1, 4.3, 4.3, 3.1, 3.1]
Y = [0.7, 0.8, 0.7, 1.1, 1.1, 2, 2.7, 2.7, 3.1, 3.1, 2.7, 3.1, 2.7, 3.1, 0.3, 0.6]
classes = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3]

plt.scatter(X, Y, c=classes)
plt.text(2, 2.5, "Before classification")
plt.show()

data = list(zip(X, Y))
KNN = KNeighborsClassifier(n_neighbors=5)  # K=5
KNN.fit(data, classes)

# Testing pattern T
new_X = 2.1
new_Y = 0.7
new_point = [(new_X, new_Y)]
prediction = KNN.predict(new_point)
print("Testing pattern belongs to the class:", prediction[0])

# For plotting the graph
plt.scatter(X + [new_X], Y + [new_Y], c=classes + [prediction[0]])
plt.text(2, 2.5, "After classification")
plt.text(new_X - 0.5, new_Y - 0.4, "New pattern: " + str(prediction[0]))
plt.show()
