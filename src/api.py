from cgi import parse_qs, escape
from Geez2Sera import Geez2Sera
from GeezFst import GeezFst
import json

def application(environ, start_response):
    status = '200 OK'
    response_header = [('Content-type', 'text/json')]
    parameters = parse_qs(environ['QUERY_STRING'])
    if('word' in parameters):
        word = parameters['word']
        word_active = Geez2Sera.geez2sera(word)
        geezFst = GeezFst()
        generated_words, score = geezFst.generate_all(word_active)
        body = {'word': score,'derivatives':generated_words}

        main = json.dumps(body ).encode("utf-8")

        start_response(status, response_header)
        return [main]
    else:
        start_response(status, response_header)
        return [json.dumps({"error","provide a Tigrinya verb to generate derivatives"}).encode("utf-8")]
