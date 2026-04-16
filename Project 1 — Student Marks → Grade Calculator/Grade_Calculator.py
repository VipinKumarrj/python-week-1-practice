def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "B"
    elif percentage >= 70:
        return "C"
    elif percentage >= 60:
        return "D"
    elif percentage >= 50:
        return "E"
    else:
        return "Fail"


num_subjects = int(input("Enter number of subjects: "))

total_obtained = 0
total_max = 0

for i in range(num_subjects):

    subject = input(f"\nEnter subject {i+1} name: ")

    obtained = float(input("Enter obtained marks: "))
    maximum = float(input("Enter maximum marks: "))

    if obtained > maximum or obtained < 0:
        print("Invalid marks entered!")
        continue

    percentage = (obtained * 100) / maximum
    grade = calculate_grade(percentage)

    print("Percentage:", percentage)
    print("Grade:", grade)

    total_obtained += obtained
    total_max += maximum


overall_percentage = (total_obtained * 100) / total_max
overall_grade = calculate_grade(overall_percentage)

print("\n----- Overall Result -----")
print("Overall Percentage:", overall_percentage)
print("Overall Grade:", overall_grade)