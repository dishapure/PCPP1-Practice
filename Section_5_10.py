import configparser

#initialzie
config =configparser.ConfigParser()

# Step 1: Create a new config
config['General']={
    'username' : "disha",
    'theme' : "dark"
}

config['Database'] = {
    'host': 'localhost',
    'port': '5432'
}

# Write to file
with open('example_config.ini', 'w') as configfile:
    config.write(configfile)

# -------------------------------
# Step 2: Read the config file
config.read('example_config.ini')

# acess values

user = config['General']['username']
host = config['Database'].get('host')
port = config.getint('Database', 'port')

print("Before modification:")
print("Username:", user)
print("Host:", host)
print("Port:", port)

# Step 3: Modify a value
config.set('General', 'theme', 'light')

# Write changes back to file
with open('example_config.ini', 'w') as configfile:
    config.write(configfile)

# Confirm change
print("\nAfter modification:")
print("Theme:", config['General']['theme'])