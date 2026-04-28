📚 Student Record Management Terminal System (SRMTS)

A simple terminal-based application written in Python for managing student records. This system allows users to add student details, calculate averages and grades, and view stored records — all from the command line.

🚀 Features
✅ Add new student records
🔍 Validate user input (name, ID, scores)
📊 Automatically calculate average score
🏆 Assign grades based on performance
📋 View all stored student records
🚫 Prevent duplicate student IDs
🛠️ Technologies Used
Python 3.x
No external libraries required (pure Python)
📂 Project Structure
SRMTS/
│── main.py # Main application file
│── README.md # Project documentation
▶️ How to Run
Make sure you have Python installed (Python 3 recommended)

Save the code in a file, e.g.:

main.py

Run the program:

python main.py
💡 How It Works

When you run the program, you’ll see a menu:

=== Student Record System ===

1. Add Student
2. View Students
3. Exit
   ➤ Add Student
   Enter student name (letters only)
   Enter unique student ID (numbers only)
   Input scores for:
   Math
   English
   Science
   The system calculates:
   Average score
   Grade (A–F)
   ➤ View Students

Displays all saved student records including:

Name
ID
Subject scores
Average
Grade
📊 Grading System
Average Score Grade
70 – 100 A
60 – 69 B
50 – 59 C
40 – 49 D
Below 40 F
⚠️ Input Validation
Names must contain only letters
IDs must be numeric and unique
Scores must be numbers between 0 and 100
🧠 Future Improvements
💾 Save records to a file (JSON/CSV/database)
✏️ Edit or delete student records
🔎 Search for a student by ID or name
🌐 Convert to a web-based system (React + Django/Flask)
📈 Add analytics (e.g., top students, average class score)
🤝 Contribution

Feel free to fork this project and improve it. Suggestions and enhancements are welcome!
