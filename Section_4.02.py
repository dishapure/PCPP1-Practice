import json

person = {
    "name": "Alice",
    "age": 25,
    "is_student": False,
    "skills": ["Python", "Data Analysis"],
    "address": {"city": "Mumbai", "zip": "400001"},
    "graduation": None
}

json_str = json.dumps(person, indent=2)
print(json_str)
