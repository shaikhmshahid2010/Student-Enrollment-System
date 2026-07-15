from flask import Flask, jsonify, request

app = Flask(__name__)

students = [
    {"id": 1, "name": "Arsalan Khan", "course": "AI", "email": "arsalan@example.com"},
    {"id": 2, "name": "Zainab Ahmed", "course": "Web Dev", "email": "zainab@example.com"},
    {"id": 3, "name": "Bilal Siddiqui", "course": "Cyber Sec", "email": "bilal@example.com"},
    {"id": 4, "name": "Ayesha Umar", "course": "Data sci", "email": "ayesha@example.com"}
]

@app.route('/students', methods=['GET'])
def get_students():
    course_filter = request.args.get('course')
    
    if course_filter:
        filtered_students = [
     s for s in students 
    if s["course"].strip().lower() == course_filter.strip().lower()
        ]
    return jsonify(filtered_students), 200
        
    return jsonify(students), 200
if __name__ == '__main__':
    app.run(debug=True)