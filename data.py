import json

data = {
    "name" : "rshvspsutlbr eaer",
    "adres" : "jsnhjdbnzyjdf 5r2 rs 66",
    "login" : "Login",
    "password" : "Password"
}
json_object = json.dumps(data,indent=4)
with open("data.json","w") as clients:
    clients.write(json_object)