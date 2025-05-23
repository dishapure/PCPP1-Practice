import json

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# serialize: object to dict
def encode_person(obj):
    if isinstance(obj, Person):
        return {"__type__": "Person", "name": obj.name, "age": obj.age}
    raise TypeError("Not serializable")

# deserialize: dict to object
def decode_person(dct):
    if dct.get("__type__") == "Person":
        return Person(dct["name"], dct["age"])
    return dct

p = Person("BOB", 45)

# to JSON
json_str = json.dumps(p, default=encode_person, indent=2)
print("Serialized:\n", json_str)

# to object
p2 = json.loads(json_str, object_hook=decode_person)
print("Deserialized:", p2.name, p2.age)
