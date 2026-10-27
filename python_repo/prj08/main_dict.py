# dictionary

x = {
    "name":None ,
    "atk":10 ,
    "hp":100
}

print(x)

x["hp"] = 200

print(x["name"])
print(x.get("dddddd"))
print(x["hp"])

print("atk" in x)

print(type(x))

for elem in x.items():
    print(elem)
    print(type(elem))
