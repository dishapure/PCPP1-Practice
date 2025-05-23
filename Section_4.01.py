import json
json_data = '''
{
  "name": "Alice",
  "age": 25,
  "is_student": false,
  "skills": ["Python", "Data Analysis"],
  "address": {"city": "Mumbai", "zip": "400001"},
  "graduation": null
}
'''

python_obj = json.loads(json_data)
print(python_obj["address"]["city"])  # Output: Mumbai
