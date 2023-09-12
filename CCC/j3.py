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
n = int(input())

availability = ["", "", "", "", ""]

for _ in range(n):
    person_availability = input()
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
