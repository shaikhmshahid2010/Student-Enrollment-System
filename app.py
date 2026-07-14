from flask import Flask, jsonify

app = Flask(__name__)

# Task 3 waali list (isay top par hi rehne dein)
students = [
    {"id": 1, "name": "Arsalan Khan", "course": "Artificial Intelligence", "email": "arsalan@example.com"},
    {"id": 2, "name": "Zainab Ahmed", "course": "Web Development", "email": "zainab@example.com"},
    {"id": 3, "name": "Bilal Siddiqui", "course": "Cyber Security", "email": "bilal@example.com"},
    {"id": 4, "name": "Ayesha Umar", "course": "Data Science", "email": "ayesha@example.com"}
]

# Task 4: Path Parameter Route
# '<int:student_id>' ka matlab hai ke URL mein sirf integer (number) accept hoga
@app.route('/student/<int:student_id>', methods=['GET'])
def get_student_by_id(student_id):
    # List mein se matching ID wala student dhoondna
    for student in students:
        if student["id"] == student_id:
            # Agar student mil jaye, toh data aur 200 OK status return karein
            return jsonify(student), 200
            
    # Agar student nahi milta (Loop khatam hone ke baad), toh error aur 404 status return karein
    return jsonify({"error": f"Student with ID {student_id} not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)