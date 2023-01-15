import string


obj = {
  "num": 1,
  "test": [],
  "data": {
    "val": 4,
    "info": {
      "isRight": True,
      "random": 66
    }
  }
}

def stringifyNumbers(obj):
    result = {}
    for key in obj:
        if type(obj[key]) is int:
            result[key] = str(obj[key])
        elif type(obj[key]) is dict:
            result[key] = stringifyNumbers(obj[key])
        else:
            result[key] = obj[key]
    return result

print(stringifyNumbers(obj))
