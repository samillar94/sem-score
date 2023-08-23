from flask import Flask, request, Response

import json

from functions import extractData, buildResults

app = Flask(__name__)

@app.route('/')

def main():

    results = {
        "error": True
    }

    try:
        extractedData = extractData(request.args)
        results = buildResults(extractedData)
    except Exception:
        results.message = "An exception was thrown in the Python functions"

    print(results)

    s = 200

    results = json.dumps(results)

    res = Response(response=results, status=s, mimetype='application/json')
    res.headers["Content-Type"]="application/json"
    res.headers["Access-Control-Allow-Origin"]="*"

    return res

if __name__ == '__main__':

    app.run(host='0.0.0.0', port=80)
    # app.run(host='pwd.40103709.qpc.hal.davecutting.uk', port=80)
