def determine_grade_limits(max_points, passing_percentage):
    grade_limit = [0.0] * 5
    grade_limit[0] = max_points * passing_percentage / 100
    for i in range(1, 5):
        grade_limit[i] = grade_limit[i-1] + (max_points - grade_limit[0])/5

    return grade_limit


def grade_points(exam_points, grade_limits):
    grade = 0

    if exam_points < grade_limits[0]:
        grade = 0
        return grade

    for i in range(5):
        if exam_points >= grade_limits[i]:
            grade = i+1

    return grade

def main():
    max_points = float(input("Enter the maximum points of the exam.\n"))
    passing_percentage = int(input("Enter the passing percentage of the exam.\n"))
    print("Enter the exam points of the students. Stop with empty line.")
    grades = []

    while True:
        grade = input()

        if grade == "":
            break

        grades.append(float(grade))

    grade_limits = determine_grade_limits(max_points, passing_percentage)

    print("Points Grade")

    for point in grades:
        grade = grade_points(point, grade_limits)
        print("{:<7.1f} {:d}".format(point, grade))

main()

