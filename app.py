#!env python
import os
from flask import Flask
from flask import request

port = int(os.getenv("PORT", 8003))

Flask.get = lambda self, path: self.route(path, methods=['get'])

app = Flask(__name__)

@app.get('/')
def hello(): 
    return "Hello " + request.args.get('name') + "!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=port)
