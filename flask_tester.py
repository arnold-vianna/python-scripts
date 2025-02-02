from flask import Flask

# this script is made to host a  simple Flask app with hello world message on port 45811

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World! This is a Flask app running in a dev container.'

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=45811)
