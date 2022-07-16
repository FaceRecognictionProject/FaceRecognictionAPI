from flask import Flask, request,Response
import jsonpickle
import numpy as np
import cv2

app = Flask(__name__)

@app.route('/api/test',methods = ['POST'])
def test():
    r = request

    nparr = np.fromstring(r.data, np.uitn8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    
    response ={'message': 'imge received. size = {}x{}'.format(img.shape[1],img.shape[0])
    }

    response_pickled = jsonpickle.encode(response)
    
    return Response(response = response_pickled, status=200,mimetype="aplication/json")

    app.run(host = "0.0.0.0", port=5000
    )