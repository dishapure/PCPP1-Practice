import xml.etree.ElementTree as ET  # XML files handle karne ke liye module

# XML file ko read karte hain
tree = ET.parse('students.xml')     # 'students.xml' file ko parse karo (read + convert to tree)

# Root element (yaha: <students>) ko get karo
root = tree.getroot()               # Root node milega (students)

print(root.tag)                     # Root ka naam print karo ('students')

# Sab <student> elements loop se nikalo
for student in root.findall('student'):  # root ke andar jitne <student> tags hain, sab pe loop
    id_ = student.attrib['id']           # 'id' attribute nikalo (e.g., id="1")

    name = student.find('name').text     # <name> tag ka text (e.g., Alice)
    age = student.find('age').text       # <age> tag ka text (e.g., 22)

    # Final output
    print(f"ID: {id_}, Name: {name}, Age: {age}")  # student ka data print karo
