
from gparser import FstMap
import os
import json
from gparser import TFST
from gparser.Geez2Sera import Geez2Sera
from flask import Flask
from persist.DbPersist import DbPersistor

app = Flask(__name__  )
counter = {}


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
    f = open(os.path.join(os.path.dirname(__file__), 'static/index.html'), mode="r", encoding='utf-8')
    return app.response_class(response=str(f.read()),status=200, mimetype="text/html")

@app.route('/generated')
def generated():
    f = open(os.path.join(os.path.dirname(__file__), 'static/generated.html'), mode="r", encoding='utf-8')
    return app.response_class(response=str(f.read()),status=200, mimetype="text/html")
@app.route('/<verb>/<src>')
def past_tense(verb, src):
    fst = FstMap.FstMap()
    result = fst.generate_all2(verb.upper(), Geez2Sera.geez2sera(src),False)
    total, counter,unique = consumer(result)
    data = {"map": result, "count_unique":  unique, "count_all": counter, "total": total}
    return app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    )

@app.route('/parents/<limit>')
def parents(limit):
    dbDao = DbPersistor()
    data = {"V":dbDao.getParents('V',limit),"N":dbDao.getParents('N',limit)}
    return app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    )

@app.route('/germinate/<pos>/<word>')
def germinate(pos,word):
    dbDao = DbPersistor()
    data =  dbDao.getGermination(pos,word)
    return app.response_class(
        response=json.dumps([json.loads(x.to_json()) for x in data]),
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
