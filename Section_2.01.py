import sys

# Check the default encoding
print("Default encoding:", sys.getdefaultencoding())

# Encode a string using default encoding (UTF-8)
text = "Hello, world! 🌍"
encoded = text.encode()  # same as text.encode('utf-8')
print("Encoded bytes:", encoded)

# Decode it back using default encoding
decoded = encoded.decode()  # same as encoded.decode('utf-8')
print("Decoded text:", decoded)
