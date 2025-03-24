from flask import Flask, jsonify
import cv2
import base64
from datetime import datetime
import time

app = Flask(__name__)

@app.route('/', methods=["GET"])
def get_img():
    current_time_seconds = time.time()
    readable_time = datetime.fromtimestamp(current_time_seconds)

    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open camera.")
        return jsonify({'timestamp': readable_time.isoformat(),'error': 'Could not open camera'}), 500

    ret, frame = cap.read()

    if not ret:
        print("Error: Could not read frame.")
        return jsonify({'timestamp': readable_time.isoformat(),'error': 'Could not read frame'}), 500

    _, buffer = cv2.imencode('.jpg', frame)
    img_base64 = base64.b64encode(buffer).decode('utf-8')

    cap.release()

    return jsonify({'timestamp': readable_time.isoformat(), 'img': img_base64})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
