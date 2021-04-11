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
        output = cv2.resize(temp, (width, height), interpolation=cv2.INTER_NEAREST)
        numpyData = temp
        encodedNumpyData = json.dumps(numpyData, cls=NumpyArrayEncoder)  # use dump() to write array into file
        print("Printing JSON serialized NumPy array")
        # print(temp)
        # cv2.imshow('Output :', temp)
        tmp = ast.literal_eval(encodedNumpyData)
        # print(tmp)
        # new_lst = []
        new_lst = []
        row = []
        col = []
        for i in tmp:
            print(i)
            for j in i:
                h,s,v = rgb_to_hsv(j[2], j[1], j[0])
                col = findcolor(h,s,v)
                row.append(col)
                # print(j[2],j[1],j[0],"HSV =",rgb_to_hsv(j[2], j[1], j[0]))
            new_lst.append(row)
            row = []

        print(new_lst)
                # print(rgb_to_hsv(j[2], j[1], j[0]))
        # for i in tmp:
        #     # print(i)
        #     for j in i:
        #         # print(classifier.predict([j])[0].replace("#",""))
        #         col.append(j[2])
        #         col.append(j[1])
        #         col.append(j[0])
        #         row.append(col)
        #         col = []
        #         # print(j)
        #     new_lst.append(row)
        #     row = []
        # output = cv2.resize(temp, (width, height), interpolation=cv2.INTER_NEAREST)
        # print(temp)
    else:
        response_object['books'] = BOOKS
    return jsonify(new_lst)

def hex_to_rgb(hx, hsl=False):
    if re.compile(r'#[a-fA-F0-9]{3}(?:[a-fA-F0-9]{3})?$').match(hx):
        div = 255.0 if hsl else 0
        if len(hx) <= 4:
            return tuple(int(hx[i] * 2, 16) / div if div else
                         int(hx[i] * 2, 16) for i in (1, 2, 3))
        return tuple(int(hx[i:i + 2], 16) / div if div else
                     int(hx[i:i + 2], 16) for i in (1, 3, 5))
    raise ValueError(f'"{hx}" is not a valid HEX code.')

def rgb_to_hsv(r, g, b):
    r, g, b = r/255.0, g/255.0, b/255.0
    mx = max(r, g, b)
    mn = min(r, g, b)
    df = mx-mn
    if mx == mn:
        h = 0
    elif mx == r:
        h = (60 * ((g-b)/df) + 360) % 360
    elif mx == g:
        h = (60 * ((b-r)/df) + 120) % 360
    elif mx == b:
        h = (60 * ((r-g)/df) + 240) % 360
    if mx == 0:
        s = 0
    else:
        s = (df/mx)*100
    v = mx*100
    h = int(h)
    s = int(s)
    v = int(v)
    return h, s, v

def findcolor(h, s, v):
    if (v >= 0 and v <= 24):
        return [0, 0, 0]
    if (v >= 25 and v <= 49):
        return [91, 91, 91]
    if (v >= 50 and v <= 69):
        if (s >= 50 and s <= 100):
            if (h >= 340 and h < 360):
                return [255, 0, 85]
            if (h >= 318 and h < 340):
                return [255, 0, 179]
            if (h >= 298 and h < 318):
                return [243, 0, 255]
            if (h >= 276 and h < 298):
                return [154, 0, 85]
            if (h >= 256 and h < 276):
                return [68, 0, 85]
            if (h >= 234 and h < 256):
                return [0, 26, 255]
            if (h >= 214 and h < 234):
                return [0, 111, 255]
            if (h >= 192 and h < 214):
                return [0, 205, 255]
            if (h >= 172 and h < 192):
                return [0, 255, 222]
            if (h >= 150 and h < 172):
                return [0, 255, 128]
            if (h >= 130 and h < 150):
                return [0, 255, 43]
            if (h >= 108 and h < 130):
                return [51, 255, 0]
            if (h >= 88 and h < 108):
                return [137, 255, 0]
            if (h >= 66 and h < 88):
                return [230, 255, 0]
            if (h >= 46 and h < 66):
                return [255, 192, 0]
            if (h >= 24 and h < 46):
                return [255, 102, 0]
            if (h >= 0 and h < 24):
                return [255, 0, 0]
    if (v >= 75 and v <= 100):
        if (s >= 0 and s <= 24):
            return [255, 255, 255]
        if (s >= 25 and s <= 49):
            return [191, 194, 195]
        if (s >= 50 and s <= 100):
            if (h >= 340 and h < 360):
                return [255, 0, 85]
            if (h >= 318 and h < 340):
                return [255, 0, 179]
            if (h >= 298 and h < 318):
                return [243, 0, 255]
            if (h >= 276 and h < 298):
                return [154, 0, 85]
            if (h >= 256 and h < 276):
                return [68, 0, 85]
            if (h >= 234 and h < 256):
                return [0, 26, 255]
            if (h >= 214 and h < 234):
                return [0, 111, 255]
            if (h >= 192 and h < 214):
                return [0, 205, 255]
            if (h >= 172 and h < 192):
                return [0, 255, 222]
            if (h >= 150 and h < 172):
                return [0, 255, 128]
            if (h >= 130 and h < 150):
                return [0, 255, 43]
            if (h >= 108 and h < 130):
                return [51, 255, 0]
            if (h >= 88 and h < 108):
                return [137, 255, 0]
            if (h >= 66 and h < 88):
                return [230, 255, 0]
            if (h >= 46 and h < 66):
                return [255, 192, 0]
            if (h >= 24 and h < 46):
                return [255, 102, 0]
            if (h >= 0 and h < 24):
                return [255, 0, 0]




if __name__ == '__main__':
    app.run()