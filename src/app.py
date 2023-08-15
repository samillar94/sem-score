from flask import Flask, request, Response

import addition, json

app = Flask(__name__)

@app.route('/')

def main():

    #change as needed
    params = 5

    r = {
        "error": False,
        "data": {},
        "score": 0
    }

    # e = False
    # s = 400
    # reply = ''

    # rx = request.args.get('x')
    # ry = request.args.get('y')

    for id in range(1, params+1):
        item = request.args.get('item_'+str(id))
        attendance = request.args.get('attendance_'+str(id))
        r['data'][item] = int(attendance)

    print(r['data'])

    a_lec = 33
    a_lab = 22
    a_sup = 44
    a_can = 55
    w_lec = 0.3
    w_lab = 0.4
    w_sup = 0.15
    w_can = 0.15

    r['score'] = (
        r['data']['Lecture sessions'] * w_lec / a_lec +
        r['data']['Lab sessions'] * w_lab / a_lab +
        r['data']['Support sessions'] * w_sup / a_sup +
        r['data']['Canvas activities'] * w_can / a_can        
    )

    s = 200

    # try:
    #     try:
    #         x = int(rx)
    #     except TypeError:
    #         r = r+"X value is missing. "
    #         e = True
    #     except ValueError:
    #         r = r+"X must be an integer. " 
    #         e = True

    #     try:        
    #         y = int(ry)
    #     except TypeError:
    #         r = r+"Y value is missing. "
    #         e = True
    #     except ValueError:
    #         r = r+"Y must be an integer. "
    #         e = True

    #     if e:
    #         raise Exception(r)

    #     z = addition.add(x,y)
    #     r = {
    #         "string": rx+" + "+ry+" = "+str(z),
    #         "x": x,
    #         "y": y,
    #         "answer": z
    #     }
    #     s = 200

    # except Exception:
    #     r = {
    #         "message": r
    #     }

    # r["error"] = e

    reply = json.dumps(r)

    response = Response(response=reply, status=s, mimetype='application/json')
    response.headers["Content-Type"]="application/json"
    response.headers["Access-Control-Allow-Origin"]="*"

    return response

if __name__ == '__main__':

    app.run(host='0.0.0.0', port=80)
    # app.run(host='pwd.40103709.qpc.hal.davecutting.uk', port=80)
