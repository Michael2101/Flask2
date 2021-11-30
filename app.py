from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/hello')
def hello_world():
    return "hello world"

@app.route('/hello/<name>')
def hello_with_name(name):
    return f"hello {name}"

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()