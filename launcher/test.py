from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'hello world!'

@app.route('/info/tx/', methods=['GET'])
def test ():
    return "test"

if __name__ == '__main__':
    app.debug = True
    app.run()