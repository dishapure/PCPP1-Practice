

import xml.etree.ElementTree as ET

# Create root element
library = ET.Element('library')

# Create a book element under library
book = ET.SubElement(library, 'book')

# Create child elements under book
title = ET.SubElement(book, 'title')
title.text = 'Python Basics'

author = ET.SubElement(book, 'author')
author.text = 'John Doe'

# Convert to string
xml_str = ET.tostring(library, encoding='unicode')
print(xml_str)
