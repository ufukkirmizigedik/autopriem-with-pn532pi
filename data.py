import json

data = {
    "name" : "rshvspsutlbr eaer",
    "adres" : "jsnhjdbnzyjdf 5r2 rs 66",
    "login" : "89251771507",
    "password" : "Ufuk1478963"
}
json_object = json.dumps(data,indent=4)
with open("data.json","w") as clients:
    clients.write(json_object)