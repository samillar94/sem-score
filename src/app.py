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
    except Exception as e:
        results['message'] =f"An exception was thrown in extractData: {e}"

    try:
        results = buildResults(extractedData)
    except Exception as e:
        results['message'] = f"An exception was thrown in buildResults: {e}"

    print(results)

    s = 200

    results = json.dumps(results)

    res = Response(response=results, status=s, mimetype='application/json')
    res.headers["Content-Type"]="application/json"
    res.headers["Access-Control-Allow-Origin"]="*"

    return res

if __name__ == '__main__':

    app.run(host='0.0.0.0', port=80)
