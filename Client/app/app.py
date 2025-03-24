import requests
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def image_page():
    return render_template('index.html')

@app.route('/fetch')
def get_image():
    try:
        response = requests.get("http://server:5000")
        if response.status_code == 200:

            info = response.json()
            imgSrc = f"data:image/jpeg;base64,{info['img']}"

            if "img" in info:
                return {
                    "img": imgSrc,
                    "timestamp": info["timestamp"],
                    "success": True
                }     
        else:
            return {
                "msg": f"Failed to fetch camera picture from server. Status: {response.status_code}",
                "success": False
            }
    
    except Exception as e:
        print("Error fetching camera picture:", e)
        return {
            "msg": str(e),
            "success": False
        }
    
if __name__ == '__main__':
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(host='0.0.0.0', port=8000, debug=True)