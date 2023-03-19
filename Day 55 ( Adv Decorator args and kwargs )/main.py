from flask import Flask

app = Flask(__name__)

def make_bold(function):
    def wrapper_make_bold():
        return f"<b>{function}</b>"
    return wrapper_make_bold

def make_emphasis(function):
    def wrapper_make_emphasis():
        return f"<em>{function}</em>"
    return wrapper_make_emphasis

def make_underlined(function):
    def wrapper_make_underlined():
        return f"<u>{function}</u>"
    return wrapper_make_underlined


@app.route('/')
def hello_world():
    return 'Hello World'


@app.route('/bye')
def bye():
    return 'Bye!'


@app.route('/username/<name>/1')
def greet(name):
    return f'Hello {name} !'


@app.route('/username/<path:name>')
def greet2(name):
    return f'Hello {name} two!'


@app.route('/username/<name>/<int:number>')
def greet3(name, number):
    return f'<h1 style="text-align: center"> Hello {name}, you are number {number}</h1>' \
           f'<p>THis is a paragraph.</p>' \
           f'<img src="https://www.humanesociety.org/sites/default/files/styles/1240x698/public/2020-07/kitten-510651' \
           f'.jpg?h=f54c7448&itok=ZhplzyJ9" width=200> ' \
           f'<img src="https://media1.giphy.com/media/ozrZTb6qiC4hy/giphy.gif?cid=ecf05e47orppnvmqq82ny3iaznnxm29awy9apfwybm1yivp9&rid=giphy.gif&ct=g">'


if __name__ == "__main__":
    app.run(debug=True)
