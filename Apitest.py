from __future__ import print_function
import requests
import json
import cv2



addr = 'http://10.80.12.79:5000'
test_url = addr + '/api/test'

content_type = 'image/jpeg'
headers = {'content_type':content_type}

img = cv2.imread('We.jpg')
_, img_encode = cv2.imencode('.jpg',img)
response = requests.post(test_url, data = img_encode.tostring(),headers = headers)
print(json.loads(response.text))