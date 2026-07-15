from flask import Flask, jsonify, request

app = Flask(__name__)

students = [
    {"id": 1, "name": "Arsalan Khan", "course": "AI", "email": "arsalan@example.com"},
    {"id": 2, "name": "Zainab Ahmed", "course": "Web Dev", "email": "zainab@example.com"},
    {"id": 3, "name": "Bilal Siddiqui", "course": "Cyber Sec", "email": "bilal@example.com"},
    {"id": 4, "name": "Ayesha Umar", "course": "Data sci", "email": "ayesha@example.com"}
]

@app.route('/add-student-form', methods=['POST'])
def add_student_form():
    name = request.form.get('name')
    course = request.form.get('course')
    email = request.form.get('email')
    
    if not name or not course or not email:
        return jsonify({"error": "Missing required fields: name, course, and email are all required!"}), 400
        
    new_id = max([s["id"] for s in students]) + 1 if students else 1
    
    new_student = {
        "id": new_id,
        "name": name,
        "course": course,
        "email": email
    }
    
    students.append(new_student)
    
    return jsonify({
        "message": "Student added successfully via Form Data!",
        "student": new_student
    }), 201


if __name__ == '__main__':
    app.run(debug=True)