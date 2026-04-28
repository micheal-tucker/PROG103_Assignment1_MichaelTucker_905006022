# Student Record Management Terminal System (SRMTS)

students = []  # stores all student records


# Function to validate name (must be string)
def get_valid_name():
    while True:
        name = input("Enter student name: ").strip()
        if name.isalpha():
            return name
        else:
            print("❌ Name must contain only letters.")


# Function to validate ID (must be integer)
def get_valid_id():
    while True:
        student_id = input("Enter student ID (numbers only): ").strip()
        if student_id.isdigit():
            return student_id
        else:
            print("❌ ID must be a number.")


# Function to validate score (float allowed)
def get_valid_score(subject):
    while True:
        try:
            score = float(input(f"Enter {subject} score: "))
            if 0 <= score <= 100:
                return score
            else:
                print("❌ Score must be between 0 and 100.")
        except ValueError:
            print("❌ Invalid input! Enter a number.")


# Check duplicate ID
def id_exists(student_id):
    for student in students:
        if student["id"] == student_id:
            return True
    return False


# Add student
def add_student():
    print("\n--- Add Student ---")

    name = get_valid_name()
    student_id = get_valid_id()

    if id_exists(student_id):
        print("❌ ID already exists.")
        return

    math = get_valid_score("Math")
    english = get_valid_score("English")
    science = get_valid_score("Science")

    average = (math + english + science) / 3

    if average >= 70:
        grade = "A"
    elif average >= 60:
        grade = "B"
    elif average >= 50:
        grade = "C"
    elif average >= 40:
        grade = "D"
    else:
        grade = "F"

    student = {
        "name": name,
        "id": student_id,
        "math": math,
        "english": english,
        "science": science,
        "average": average,
        "grade": grade,
    }

    students.append(student)
    print("✅ Student added successfully!")


# Display students
def display_students():
    print("\n--- Student Records ---")

    if not students:
        print("No records found.")
        return

    for student in students:
        print("\n----------------------")
        print(f"Name: {student['name']}")
        print(f"ID: {student['id']}")
        print(f"Math: {student['math']}")
        print(f"English: {student['english']}")
        print(f"Science: {student['science']}")
        print(f"Average: {student['average']:.2f}")
        print(f"Grade: {student['grade']}")



def main():
    while True:
        print("\n=== Student Record System ===")
        print("1. Add Student")
        print("2. View Students")
        print("3. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            display_students()
        elif choice == "3":
            print("Exiting system...")
            break
        else:
            print("❌ Invalid choice.")


main()
