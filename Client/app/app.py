import requests
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def image_page():
    return render_template('index.html')
    
if __name__ == '__main__':
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(host='0.0.0.0', port=8000, debug=True)