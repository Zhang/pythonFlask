from flask import Flask
import newsAgg as N
import threading
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

def set_interval(func, sec):
    def func_wrapper():
        set_interval(func, sec)
        func()
    t = threading.Timer(sec, func_wrapper)
    t.start()
    return t

if __name__ == '__main__':
    N.init()
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
    newsInterval()