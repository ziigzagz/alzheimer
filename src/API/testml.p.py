from sklearn import tree

feature = [[1,2],[10,13],[30,25],[0.2,0.6],[7,8],[100,20]]
labels = ["A","B","C","D","E","F"]
print(len(feature))
print(len(labels))
classifier = tree.DecisionTreeClassifier()
classifier = classifier.fit(feature,labels)
print(classifier.predict([[185,18]]))



