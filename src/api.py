from flask import Flask
from gparser import FstMap
import os
from gparser import TFST
from Geez2Sera import Geez2Sera
from GeezScore import GeezScore

app = Flask(__name__)

counter = {}
os.environ["SCORE_FILE"] = "ti_score.txt"


def consumer(src, x):
    geez = Geez2Sera.sera2geez(x)
    score = GeezScore.exists(geez)
    if (score > 0):
        if (not geez in counter):
            counter[geez] = 0
        counter[geez] = counter[geez] + score
    return [geez, str(score)]


@app.route('/<verb>/<src>')
def past_tense(verb, src):
    fst = FstMap.FstMap()
    result = fst.generate_all3([verb.upper()], Geez2Sera.geez2sera(src), consumer)
    return app.response_class(
        response={"map": result, "count_unique": len(counter), "count_all": sum([i for i in counter.values()])},
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
    app.run(port=5050)
