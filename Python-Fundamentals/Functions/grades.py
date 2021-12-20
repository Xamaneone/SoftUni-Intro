def get_grade(grade):
    if 2.00 <= grade <= 6.00:
        if grade < 3.00:
            return "Fail"
        elif grade < 3.50:
            return "Poor"
        elif grade < 4.50:
            return "Good"
        elif grade < 5.50:
            return "Very Good"
        else:
            return "Excellent"

grade_data = float(input())

print(get_grade(grade_data))
