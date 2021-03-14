import urllib.request
imgURL = "https://firebasestorage.googleapis.com/v0/b/alzeimer-4a47b.appspot.com/o/img%2Fflower.jpg?alt=media&token=b3d3fa6c-ee10-4973-afc8-fe34f9bf0307"

urllib.request.urlretrieve(imgURL, "flower.jpg")