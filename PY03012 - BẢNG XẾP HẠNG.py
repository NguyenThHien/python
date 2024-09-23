
def sorted_studens(students):
    students_sorted = sorted(students, key=lambda student: (-student['correct'], student['submit'], student['name']))
    return students_sorted
n = int(input())
students = []
for _ in range(n):
    name = input()
    correct,  submit = map(int, input().split())
    students.append({'name': name, 'correct': correct, 'submit': submit})

    results = sorted_studens(students)
for student in results:
    print(f"{student['name']} {student['correct']} {student['submit']}")
