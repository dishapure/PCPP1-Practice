import xml.etree.ElementTree as ET

xml_data = '''<library>
  <book>
    <title>Python Basics</title>
    <author>John Doe</author>
  </book>
  <book>
    <title>Advanced Python</title>
    <author>Jane Smith</author>
  </book>
    <book>
    <title>Way to Disha's heart</title>
    <author>Take her to kedarnath!</author>
  </book>
</library>'''

root = ET.fromstring(xml_data)
first_book = root.find('book')
print(first_book.find('title').text)  # Python Basics

all_books = root.findall('book')
for book in all_books:
    title = book.find('title').text
    author = book.find('author').text
    print(f'Title: {title}, Author: {author}')