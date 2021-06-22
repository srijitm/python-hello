from flask import Flask, request, redirect, Response, jsonify
from gallery import gallery
import base64

PORT = 8080

app = Flask(__name__)

@app.route('/health')
def health():
  status = {'health': 'pass'}
  return status

@app.route('/hello/<name>')
def hello(name):
  return 'Hello ' + name + '!'

if __name__ == '__main__':
  app.run(debug=True,host='0.0.0.0', port=PORT)
