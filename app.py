from flask import Flask, request, redirect, Response, jsonify

app = Flask(__name__)

@app.route('/health')
def health():
  return 'pass'

@app.route('/hello/<name>')
def hello(name):
  return 'Hello ' + name + '!'

@app.route('/')
def root():
  return 'python-hello'

if __name__ == '__main__':
  app.run(debug=True,host='0.0.0.0')
