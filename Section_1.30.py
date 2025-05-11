import shelve

def add_student(db):
    roll = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    marks = float(input("Enter Marks: "))
    db[roll] = {'name': name, 'marks': marks}
    print("Student added successfully.")

def display_all(db):
    print("\nAll Student Records:")
    for roll, record in db.items():
        print(f"Roll: {roll}, Name: {record['name']}, Marks: {record['marks']}")

def update_marks(db):
    roll = input("Enter Roll Number to update: ")
    if roll in db:
        new_marks = float(input("Enter new marks: "))
        db[roll]['marks'] = new_marks
        print("Marks updated.")
    else:
        print("Record not found.")

def delete_student(db):
    roll = input("Enter Roll Number to delete: ")
    if roll in db:
        del db[roll]
        print("Student deleted.")
    else:
        print("Record not found.")

def main():
    with shelve.open('students_db') as db:
        while True:
            print("\n1. Add Student\n2. Display All\n3. Update Marks\n4. Delete Student\n5. Exit")
            choice = input("Enter your choice: ")
            if choice == '1':
                add_student(db)
            elif choice == '2':
                display_all(db)
            elif choice == '3':
                update_marks(db)
            elif choice == '4':
                delete_student(db)
            elif choice == '5':
                print("Exiting program.")
                break
            else:
                print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
