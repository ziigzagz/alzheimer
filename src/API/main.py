from flask import *
from flask_cors import CORS
import urllib.request
import cv2
from json import JSONEncoder
import numpy
import ast
from sklearn import tree
import re
class NumpyArrayEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, numpy.ndarray):
            return obj.tolist()
        return JSONEncoder.default(self, obj)
# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

BOOKS=[]
# sanity check route
@app.route('/get', methods=['GET', 'POST'])
def rsv():
    response_object = {'status': 'success'}
    print(request)
    if request.method == 'POST':
        post_data = request.get_json()
        print("data",post_data)
        imgURL = post_data[0]
        print(type(post_data[1]))
        print(type(int(post_data[1])))

        # hw_h_w = int(post_data[1])
        urllib.request.urlretrieve(imgURL, "image.jpg")
        input = cv2.imread('image.jpg')
        height, width = input.shape[:2]
        w, h = (int(post_data[1]), int(post_data[1]))
        temp = cv2.resize(input, (w, h), interpolation=cv2.INTER_LINEAR)

        numpyData = temp
        encodedNumpyData = json.dumps(numpyData, cls=NumpyArrayEncoder)  # use dump() to write array into file
        print("Printing JSON serialized NumPy array")
        # print(encodedNumpyData)
        tmp = ast.literal_eval(encodedNumpyData)
        # print(tmp[9])
        output = cv2.resize(temp, (width, height), interpolation=cv2.INTER_NEAREST)
        cv2.waitKey(0)
        feature = [[0,0,0],[255,255,255]]
        labels = ["#000000","#ffffff"]
        f = open("demofile2.txt", "r")
        colorlst = []
        row = []
        col = []
        for x in f:
            tmp_color = x.split("/")[0]
            tmp_color = tmp_color[1:-1]  # ตัดวงเล็บออก
            r = tmp_color.split(",")[2]
            r = int(r)
            g = tmp_color.split(",")[1]
            g = int(g)
            b = tmp_color.split(",")[0]
            b = int(b)
            colorlst.append(r)
            colorlst.append(g)
            colorlst.append(b)
            feature.append(colorlst)
            tmp_labels = x.split("/")[1]
            tmp_labels = tmp_labels.replace("\n","")
            # print(tmp_labels)
            colorlst = []
            labels.append(tmp_labels)
        # print((feature))
        # print((labels))
        classifier = tree.DecisionTreeClassifier()
        # print(classifier)
        classifier = classifier.fit(feature, labels)
        # print(classifier.predict([j]))
        print(classifier.predict([tmp[0][3]]))
        # print(col)

        new_lst = []
        for i in tmp:
            for j in i:
                # print(classifier.predict([j])[0].replace("#",""))
                h = classifier.predict([j])[0].replace("#","")
                h = tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))
                col.append(h[2])
                col.append(h[1])
                col.append(h[0])
                row.append(col)
                col = []
                # print(j)
            new_lst.append(row)
            row = []
            # print("------------------------------")
        # print(new_lst)
    else:
        response_object['books'] = BOOKS
    # print(tmp)
    return jsonify(new_lst)

@app.route('/save', methods=['GET', 'POST'])
def test():
    txt = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        data = post_data
        print(data)
        f = open("demofile2.txt", "a")
        print(type(hex_to_rgb(data[0])))
        print(str(hex_to_rgb(data[0])))
        f.write(str(hex_to_rgb(data[0]))+"/"+data[1]+"\n")
        f.close()
        # data[0] is new color
        print(data[0],data[1],hex_to_rgb(data[0]))
    return jsonify('complete')

def hex_to_rgb(hx, hsl=False):
    if re.compile(r'#[a-fA-F0-9]{3}(?:[a-fA-F0-9]{3})?$').match(hx):
        div = 255.0 if hsl else 0
        if len(hx) <= 4:
            return tuple(int(hx[i] * 2, 16) / div if div else
                         int(hx[i] * 2, 16) for i in (1, 2, 3))
        return tuple(int(hx[i:i + 2], 16) / div if div else
                     int(hx[i:i + 2], 16) for i in (1, 3, 5))
    raise ValueError(f'"{hx}" is not a valid HEX code.')


if __name__ == '__main__':
    app.run()