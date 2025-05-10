import re

class UserProfile:
    def __init__(self, username, email, password):
        self.username = username  # Public attribute
        self._email = email       # Private attribute (Encapsulated)
        self.__password = password  # Private attribute (Encapsulated)

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, new_email):
        # Validate email format using regex
        if re.match(r"[^@]+@[^@]+\.[^@]+", new_email):
            self._email = new_email
        else:
            raise ValueError("Invalid email format!")

    @property
    def password(self):
        return "******"  # Hiding the password for security purposes

    @password.setter
    def password(self, new_password):
        # Password policy: at least 8 characters long
        if len(new_password) >= 8:
            self.__password = new_password
        else:
            raise ValueError("Password must be at least 8 characters long!")

    @password.deleter
    def password(self):
        print("Password is being deleted.")
        del self.__password  # Deletes the password from memory

    def __str__(self):
        return f"User Profile: {self.username}, Email: {self.email}"

# 🚀 Testing the Class
profile = UserProfile("john_doe", "john.doe@example.com", "securePassword123")
print(profile)  # Show basic profile

# Update email and password
profile.email = "john_new@example.com"
profile.password = "newSecurePassword456"
print(profile.email)  # Should print the updated email
print(profile.password)  # Should print '******' (hiding actual password)

# Deleting password
del profile.password  # Should print "Password is being deleted."
