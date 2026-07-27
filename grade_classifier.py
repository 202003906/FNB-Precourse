learner_name = input("Enter learner's name: ")
subject1 = float(input("Enter mark for Subject 1: "))
subject2 = float(input("Enter mark for Subject 2: "))
subject3 = float(input("Enter mark for Subject 3: "))

average = (subject1 + subject2 + subject3) / 3
average = round(average, 2)

if average >= 80:
    grade = "A"
elif average >= 70:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 50:
    grade = "D"
else:
    grade = "F"

if average >= 50:
    status = "Pass"
else:
    status = "Fail"

intervention_flags = []

if subject1 < 40:
    intervention_flags.append("Subject 1")
if subject2 < 40:
    intervention_flags.append("Subject 2")
if subject3 < 40:
    intervention_flags.append("Subject 3")

print("========= REPORT CARD =========")
print(f"Learner Name: {learner_name}")
print(f"Subject 1 Mark: {subject1}")
print(f"Subject 2 Mark: {subject2}")
print(f"Subject 3 Mark: {subject3}")
print(f"Average: {average}")
print(f"Grade: {grade}")
print(f"Status: {status}")

if len(intervention_flags) > 0:
    print(f"Needs Intervention: {', '.join(intervention_flags)}")
else:
    print("Needs Intervention: None")

print("================================")