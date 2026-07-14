from flask import Flask, jsonify

app = Flask(__name__)

students = [
    {
        "id": 1,
        "name": "Arsalan Khan",
        "course": "Artificial Intelligence",
        "email": "arsalan@example.com"
    },
    {
        "id": 2,
        "name": "Zainab Ahmed",
        "course": "Web Development",
        "email": "zainab@example.com"
    },
    {
        "id": 3,
        "name": "Bilal Siddiqui",
        "course": "Cyber Security",
        "email": "bilal@example.com"
    },
    {
        "id": 4,
        "name": "Ayesha Umar",
        "course": "Data Science",
        "email": "ayesha@example.com"
    }
]

@app.route('/')
def home():
    return "Welcome to Student Enrollment System"

@app.route('/test-data')
def get_all_students():
    return jsonify(students)

if __name__ == '__main__':
    app.run(debug=True)