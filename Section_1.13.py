def generate_report(name, roll_number, *scores, grade="Not Assigned", attendance=None, **extra_info):
    print("\n--- Student Report ---")
    print(f"Name: {name}")
    print(f"Roll Number: {roll_number}")
    print(f"Grade: {grade}")

    if attendance is not None:
        print(f"Attendance: {attendance}%")

    if scores:
        average = sum(scores) / len(scores)
        print(f"Average Score: {average:.2f}")
    else:
        print("No scores provided.")

    for key, value in extra_info.items():
        print(f"{key.replace('_', ' ').title()}: {value}")


# Test Case 1: Basic report with all types of parameters
generate_report("Aarav", 23, 89, 76, 92, grade="A", project_score=18, club_member=True)

# Test Case 2: Report with only required arguments and default grade
generate_report("Maya", 45, 90, 85)

# Test Case 3: Report with attendance and no scores
generate_report("Rahul", 12, grade="B", attendance=95, behavior="Excellent")
