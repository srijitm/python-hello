from flask import Flask, request, redirect, Response, jsonify

PORT = 8080

app = Flask(__name__)

@app.route('/health')
def health():
  return 'Healthy!'

@app.route('/hello/<name>')
def hello(name):
  return 'Hello ' + name + '!'

if __name__ == '__main__':
  app.run(debug=True,host='0.0.0.0', port=PORT)
