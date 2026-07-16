from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

students = [
    {"id": 1, "name": "Arsalan Khan", "course": "Artificial Intelligence", "email": "arsalan@example.com"},
    {"id": 2, "name": "Zainab Ahmed", "course": "Web Development", "email": "zainab@example.com"},
    {"id": 3, "name": "Bilal Siddiqui", "course": "Cyber Security", "email": "bilal@example.com"},
    {"id": 4, "name": "Ayesha Umar", "course": "Data science", "email": "ayesha@example.com"}
]

@app.route('/students-page/<int:student_id>', methods=['GET'])
def student_profile_page(student_id):
    selected_student = None
    for student in students:
        if student["id"] == student_id:
            selected_student = student
            break
            
    return render_template('student_profile.html', student=selected_student)


if __name__ == '__main__':
    app.run(debug=True)