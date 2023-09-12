# importing  all the
# functions defined in test.py
from checkAnswer import *
relpath = "junior\j1\j1.01.in"
j1Input = getInputs(relpath)
# [P,C]/
# j1Input[0] = N = 5
# j1Input[1] = T = 2
# output =730

# //WRITE HERE
def answer(inputs):
    n = int(inputs[0])

    availability = ["", "", "", "", ""]

    for l in range(n):
        person_availability = inputs[l + 1]
        for i in range(5):
            availability[i] += person_availability[i]

    max_attendance = 0
    max_attendance_days = []

    for day, availability_data in enumerate(availability, start=1):
        attendance = availability_data.count("Y")
        if attendance > max_attendance:
            max_attendance = attendance
            max_attendance_days = [day]
        elif attendance == max_attendance:
            max_attendance_days.append(day)

    print(max_attendance_days)
    return max_attendance_days
checkAnswers("j3", answer)
