from lxml import etree

xml_data  = '''
<library>
<book>
<title> Python XML </title>
<author> John </author>
</book>
</library>
            '''

root = etree.fromstring(xml_data)

for book in root.findall('book'):
    title = book.find('title').text
    author = book.find('author').text
    print(f'Title: {title}, Author : {author}')

