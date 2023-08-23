import math

def extractData(query):

    extractedData = {
        "attendances": [],
        "availabilities": [],
        "weights": []
    }

    argCount = len(query)

    hasNext = True

    att = query['attendance_1']
    av = query['availability_1']
    w = query['weight_1']

    if att is None or av is None or w is None:
        raise AttributeError("Component attribute missing") 
    
    nextID = 2

    while nextID <= argCount // 3 + 1 and hasNext is True:

        attFloat = float(att) if att is not None else None
        avFloat = float(av) if av is not None else None
        wFloat = float(w) if w is not None else None

        if attFloat is None or math.isnan(attFloat):
            raise ValueError("Non-numerical/blank attendance")
        if avFloat is None or math.isnan(avFloat):
            raise ValueError("Non-numerical/blank availability")

        if attFloat < 0:
            raise ValueError("Negative attendance")
        if avFloat < 0:
            raise ValueError("Negative availability")
        
        if wFloat < 0:
            raise ValueError("Negative weight")
        if wFloat > 1:
            raise ValueError("Weight cannot be greater than 1")

        if attFloat > avFloat:
            raise ValueError("Attendance larger than available")

        extractedData["attendances"].append(attFloat)
        extractedData["availabilities"].append(avFloat)
        extractedData["weights"].append(wFloat)

        att = query.get(f"attendance_{nextID}")
        av = query.get(f"availability_{nextID}")
        w = query.get(f"weight_{nextID}")

        if att is None and av is None and w is None:
            hasNext = False
        elif att is None or av is None or w is None:
            hasNext = False
            raise ValueError(f"Inconsistent counts of component attributes. Next attendance {att}, next availability {av}, next weight {w}")
        
        nextID += 1

    if sum(extractedData["weights"]) != 1:
        raise ValueError("Weights do not add to 1")

    return extractedData


def buildResults(extractedData):

    results = {
        "error": False,
        "data": {
            "score": 0
        },
        "lines": []
    }

    for id in range(1, len(extractedData['weights'])+1):
        results['data']['score'] += extractedData['attendances'][id] * extractedData['weights'][id] / extractedData['availabilities'][id]

    results['lines'] = f"Engagement Score: {round(results['data']['score'])}"

    return results