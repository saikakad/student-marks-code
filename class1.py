def get_marks():
    marks = []
    n = int(input("Enter number of students: "))
    print("Enter the marks for each student (use -1 for absent student):")
    for i in range(n):
        mark = int(input(f"Marks for student {i+1}: "))
        marks.append(mark)
    return marks

def average_score(marks):
    total = 0
    count = 0
    for mark in marks:
        if mark != -1:
            total += mark
            count += 1
    if count == 0:   # should be outside loop
        return 0
    return total / count

def highest_lowest_score(marks):
    present_marks = [mark for mark in marks if mark != -1]
    if not present_marks:
        return None, None
    highest = max(present_marks)
    lowest = min(present_marks)
    return highest, lowest

def count_absent_students(marks):
    count = 0
    for mark in marks:
        if mark == -1:
            count += 1
    return count   # should be outside loop

def mark_with_highest_frequency(marks):
    frequency = {}
    for mark in marks:
        if mark != -1:
            if mark in frequency:
                frequency[mark] += 1
            else:
                frequency[mark] = 1
    if not frequency:
        return None, 0
    max_freq = 0
    most_frequent_mark = None
    for mark in frequency:
        if frequency[mark] > max_freq:
            max_freq = frequency[mark]
            most_frequent_mark = mark
    return most_frequent_mark, max_freq


# main program
marks = get_marks()

print("\nResult:")
print("1. Average score of class:", average_score(marks))

high, low = highest_lowest_score(marks)
if high is None:
    print("2. No students are present")
else:
    print("2. Highest score:", high)
    print("   Lowest score:", low)

print("3. Number of absent students:", count_absent_students(marks))

freq_mark, freq_count = mark_with_highest_frequency(marks)
if freq_mark is not None:
    print(f"4. Marks with highest frequency: {freq_mark} (appeared {freq_count} times)")
else:
    print("4. No valid marks to calculate frequency.")
