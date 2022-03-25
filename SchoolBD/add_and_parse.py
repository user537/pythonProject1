import json

name = "Vasyan"
age = 15
gender = "M"
description = "Attaboy"



dictData = {}
jsonData = json.dumps(dictData)
print(jsonData)

with open("data.json", "w") as file:
    file.write(jsonData)