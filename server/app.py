#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Python Operations with Flask Routing and Views</h1>"

@app.route('/print/<string:parameter>')
def print_string(parameter):
    print (parameter)
    return parameter

@app.route('/count/<int:number>')
def count(number):
    numlst = []
    i = 0
    for i in range (number):
        print(i)
        numlst.append(i)
        # i += 1
    return numlst

    # return number
    # i = 0
    # for i in range(len(parameter)):
    #     print(i)
    #     i += 1


if __name__ == '__main__':
    app.run(port=5555, debug=True)
