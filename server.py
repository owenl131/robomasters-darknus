import redis
import cv2
import base64
import serialize
from flask import Flask

r = redis.Redis()

app = Flask(__name__)

@app.route('/<name>')
def get(name):
    img = r.get(name)
    if img is None:
        return ''
    img = serialize.unserialize(img)
    ret, buffer = cv2.imencode('.jpg', img)
    jpg_text = base64.b64encode(buffer)
    return jpg_text

@app.route('/')
def get_view():
    img = r.get('cap')
    if img is None:
        return ''
    img = serialize.unserialize(img)
    ret, buffer = cv2.imencode('.jpg', img)
    jpg_text = base64.b64encode(buffer).decode()
    return f'<img src="data:image/jpg;base64,{jpg_text}" />'

if __name__ == '__main__':
    try:
        app.run(host='0.0.0.0', port=5001)
    except Exception as e:
        print(e)

