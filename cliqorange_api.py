import json
import requests

# Define or load your own images list
images_list = [
    "http://r-ec.bstatic.com/images/hotel/840x460/166/16637972.jpg",
    "http://q-fa.bstatic.com/images/hotel/840x460/506/50695030.jpg"
]

images = []
for image in images_list:
    images.append({"image": image})


# Body of the request
body = {}
# It's required to specify Content-type
headers = {'Content-type': 'application/json'}
url = "http://api.cliqorange.com/api/v1/classify/traveling/"
# Entr your user key
body["user_key"] = "xxxxxxxxxxxxxxxxxxxxxxxxxxxx"

n = len(images)
# Batch size
batch_size = min(50, n)
# Amount of batches
reps = n / batch_size + (1 if n % batch_size != 0 else 0)
results = []
for batch in range(reps):
    # Bounds
    left = batch * batch_size
    right = batch * batch_size + batch_size
    body["images"] = images[left:right]
    # As JSON string
    body_json = json.dumps(body)
    r = requests.post(url, data=body_json, headers=headers)
    result_json = r.json()
    results += result_json

# We return list of results always saving order of images
for i in range(len(results)):
    print images[i], results[i]
