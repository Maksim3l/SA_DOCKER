from flask import Flask, jsonify
import cv2
import base64
from datetime import datetime
import time

app = Flask(__name__)

@app.route('/', methods=["GET"])
def get_img():

    cap = cv2.VideoCapture(0)

    ret, frame = cap.read()

    _, buffer = cv2.imencode('.jpg', frame)
    img_base64 = base64.b64encode(buffer).decode('utf-8')

    cap.release()

    return jsonify({'img': img_base64})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
