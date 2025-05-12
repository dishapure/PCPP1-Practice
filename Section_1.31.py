class LoggerMeta(type):
    def __new__(cls, name, bases, dct):
        print(f"Creating class: {name}")
        # Add a new method dynamically
        def log(self):
            print(f"Log from {self.__class__.__name__}")
        dct['log'] = log
        return super().__new__(cls, name, bases, dct)

class User(metaclass=LoggerMeta):
    def __init__(self, name):
        self.name = name

# Test
u = User("John")
u.log()  # Output: Log from User
