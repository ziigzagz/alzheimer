from sklearn import tree

feature = []
labels = []
f = open("demofile2.txt", "r")
colorlst = []
for x in f:
    tmp_color = x.split("/")[0]
    tmp_color = tmp_color[1:-1] #ตัดวงเล็บออก
    r = tmp_color.split(",")[0]
    r = int(r)

    g = tmp_color.split(", ")[1]
    g = int(g)

    b = tmp_color.split(", ")[2]
    b = int(b)
    colorlst.append(r)
    colorlst.append(g)
    colorlst.append(b)
    feature.append(colorlst)
    tmp_labels = x.split("/")[1]
    colorlst = []
    labels.append(tmp_labels)
print(len(feature))
print(len(labels))
classifier = tree.DecisionTreeClassifier()
# print(classifier)
classifier = classifier.fit(feature,labels)

print(classifier.predict([[185,18,18]]))



