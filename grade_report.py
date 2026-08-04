students = [
    {"name": "Amanda Dlamini", "maths": 85, "english": 78, "science": 92},
    {"name": "Bongani Nkosi",  "maths": 62, "english": 55, "science": 70},
    {"name": "Cebo Simelane",  "maths": 45, "english": 50, "science": 40},
    {"name": "Duduzile Mabuza","maths": 90, "english": 88, "science": 95},
    {"name": "Emmanuel Vilakati","maths": 72, "english": 68, "science": 75},
    {"name": "Fikile Shongwe", "maths": 58, "english": 62, "science": 60},
]


def get_grade(average):
    """Return a letter grade based on the average mark."""
    if average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"


def get_status(average):
    """Return Pass/Fail status based on the average mark."""
    if average >= 50:
        return "Pass"
    else:
        return "Fail"


results = []          
all_marks = []         

for student in students:
    name = student["name"]
    subjects = ["maths", "english", "science"]

    marks = []
    for subject in subjects:
        mark = student[subject]
        marks.append(mark)
        all_marks.append(mark)   

    average = sum(marks) / len(marks)
    grade = get_grade(average)
    status = get_status(average)

    results.append({
        "name": name,
        "average": average,
        "grade": grade,
        "status": status,
    })


class_average = sum(r["average"] for r in results) / len(results)
highest_mark = max(all_marks)
lowest_mark = min(all_marks)

print("=" * 55)
print(f"{'CLASS GRADE REPORT':^55}")
print("=" * 55)
print(f"{'Name':<20}{'Average':>10}{'Grade':>10}{'Status':>12}")
print("-" * 55)

for r in results:
    print(f"{r['name']:<20}{r['average']:>10.2f}{r['grade']:>10}{r['status']:>12}")

print("-" * 55)
print(f"Class Average : {class_average:.2f}")
print(f"Highest Mark  : {highest_mark}")
print(f"Lowest Mark   : {lowest_mark}")
print("=" * 55)


print("\nStudent Search (type 'quit' to exit)")

while True:
    search_name = input("Enter a student's name to search: ").strip()

    if search_name.lower() == "quit":
        print("Exiting search. Goodbye!")
        break   

    if search_name == "":
        
        continue

    found = False
    for r in results:
        if r["name"].lower() == search_name.lower():
            print(f"\n--- {r['name']} ---")
            print(f"Average : {r['average']:.2f}")
            print(f"Grade   : {r['grade']}")
            print(f"Status  : {r['status']}\n")
            found = True
            break   

    if not found:
        print(f"No student named '{search_name}' was found. Try again.\n")