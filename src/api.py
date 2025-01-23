
from gparser import FstMap
import os
import json
from gparser import TFST
from Geez2Sera import Geez2Sera
from flask import Flask, render_template

app = Flask(__name__  )
counter = {}
os.environ["SCORE_FILE"] = "resources/ti_score.txt"


def consumer(maps):
    unique= set()
    count = 0
    total = 0
    for x in maps:
        for y in maps[x]:
            total = total+1
            if(maps[x][y][1]):
               count= count+1
               unique.add(maps[x][y][0])
    return total, count,len(unique)


@app.route('/')
def root():
    return render_template('index.html')
@app.route('/<verb>/<src>')
def past_tense(verb, src):
    fst = FstMap.FstMap()
    result = fst.generate_all2(verb.upper(), Geez2Sera.geez2sera(src))
    total, counter,unique = consumer(result)
    data = {"map": result, "count_unique":  unique, "count_all": counter, "total": total}
    return app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    )


@app.route('/generate/<feature>/<src>')
def generate(feature, src):
    tfst = TFST.TFST(feature)
    sera = Geez2Sera.geez2sera(src)
    generator = tfst.generate(sera)
    return Geez2Sera.sera2geez(list(generator)[0])


# main driver function
if __name__ == '__main__':
    app.run( port=5050)
