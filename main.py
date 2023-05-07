# -*- coding: windows-1251 -*-

from flask import Flask
from _2kr import load_to_json as ltj

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Hello, World</h1>'


@app.route('/kr2')
def kr2():
    KR2test("_2KR/test_front_json.json")
    return '<h1>KR2 example</h1>'

def KR2test(json):
    ## Receieving the front json with A, B, FIO, Group and Answers. Then, call load_to_json, where 1st parameter -
    ## json that we need to fill, 2nd parameter - front json ##

    ltj.clear_json("_2KR/KR2_json.json")
    right_answers, check_user_answers = ltj._2KR_load_to_json("_2KR/KR2_json.json", json)
    print(right_answers)
    print(check_user_answers)

    ## Giving back to front for print ##
    #--------------------------------------------# put your code here

if __name__ == '__main__':
    app.run(debug=True)
