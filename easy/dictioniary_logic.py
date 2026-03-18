# Problem 2: Dictionary Logic

students = [
    {"name": "Alice", "score": 85},
    {"name": "Bob", "score": 92},
    {"name": "Charlie", "score": 78},
    {"name": "Diana", "score": 92}
]

# Find the student(s) with the highest score
# Expected output: ["Bob", "Diana"]

max_score = max(s["score"] for s in students)
top_students = [s["name"] for s in students if s["score"] == max_score]

print(top_students)