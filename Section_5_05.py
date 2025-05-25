import csv

# Sample data for demonstration
data_rows = [['Name', 'Age'], ['Alice', 23], ['Bob', 30]]
dict_data = [{'Name': 'Alice', 'Age': 23}, {'Name': 'Bob', 'Age': 30}]

# 1. Write CSV using csv.writer
with open('example_writer.csv', 'w', newline='') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerows(data_rows)
print("Written using csv.writer")

# 2. Read CSV using csv.reader
with open('example_writer.csv', 'r') as file:
    csv_reader = csv.reader(file)
    print("\nRead using csv.reader:")
    for row in csv_reader:
        print(row)

# 3. Write CSV using csv.DictWriter
with open('example_dictwriter.csv', 'w', newline='') as file:
    fieldnames = ['Name', 'Age']
    csv_writer = csv.DictWriter(file, fieldnames=fieldnames)
    csv_writer.writeheader()
    csv_writer.writerows(dict_data)
print("\nWritten using csv.DictWriter")

# 4. Read CSV using csv.DictReader
with open('example_dictwriter.csv', 'r') as file:
    csv_reader = csv.DictReader(file)
    print("\nRead using csv.DictReader:")
    for row in csv_reader:
        print(f"{row['Name']} is {row['Age']} years old")
