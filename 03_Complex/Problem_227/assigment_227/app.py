from flask import Flask, Response, render_template
import cv2
import numpy as np
import io

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/display_image')
def display_image():
    # Read the image using OpenCV
    image = cv2.imread('path_to_your_image.jpg')
    
    # Convert the image to JPEG format
    (flag, encodedImage) = cv2.imencode(".jpg", image)
    if not flag:
        return ""

    # Convert to bytes and serve the image directly
    stream = io.BytesIO(encodedImage.tobytes())
    return Response(stream, mimetype="image/jpeg")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

