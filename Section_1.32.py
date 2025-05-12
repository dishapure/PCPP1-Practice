class EnforceToJSONMeta(type):
    def __new__(cls, name, bases, dct):
        if 'to_json' not in dct:
            raise TypeError(f"Class '{name}' must implement 'to_json()' method.")
        return super().__new__(cls,name,bases,dct)

class ValidModel(metaclass=EnforceToJSONMeta):
    def to_json(self):
        return {"message": "This works"}

# Uncommenting the following will raise an error
# class InvalidModel(metaclass=EnforceToJSONMeta):
#     pass  # Missing to_json()

# Test
vm = ValidModel()
print(vm.to_json())  # Output: {'message': 'This works'}
