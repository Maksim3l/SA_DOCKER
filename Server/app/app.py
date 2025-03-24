from flask import Flask, jsonify
import cv2
import base64
from datetime import datetime
import time

app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
