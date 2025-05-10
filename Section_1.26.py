class SecureString(str):
    def __str__(self):
        return "*" * len(self)

    def reveal(self):
        return super().__str__()

# Test
s = SecureString("my_secret_password")
print(s)           # ***************
print(s.reveal())  # my_secret_password