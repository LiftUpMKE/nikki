from flask import Flask
app = Flask(__name__)

Filey = open(file="NOres1.html")
webstring = Filey.read()

@app.route('/')
def hello_world():
    return webstring

if __name__ == '__main__':
    app.run()