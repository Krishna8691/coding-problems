obj = {
  "stuff": 'foo',
  "data": {
    "val": {
      "thing": {
        "info": 'bar',
        "moreInfo": {
          "evenMoreInfo": {
            "weMadeIt": 'baz'
          }
        }
      }
    }
  }
}

def collectStrings(obj):
    result = []
    for k in obj:
        if type(obj[k]) is str:
            result.append(obj[k])
        elif type(obj[k]) is dict:
            result.extend(collectStrings(obj[k]))
        else:
            continue
    return result

print(collectStrings(obj))