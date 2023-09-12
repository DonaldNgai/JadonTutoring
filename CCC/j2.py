# importing  all the
# functions defined in test.py
from checkAnswer import *
relpath = "junior\j1\j1.01.in"
j2Input = getInputs(relpath)
# [P,C]/
# j1Input[0] = N = 5
# j1Input[1] = T = 2
# output =730

# //WRITE HERE

def answer(inputs):
    n = int(inputs[0])
    
    total_spiciness = 0
    for i in range(n):
        pepper_name = inputs[i + 1].strip()
        if pepper_name == "Poblano":
            total_spiciness += 1500
        elif pepper_name == "Mirasol":
            total_spiciness += 6000
        elif pepper_name == "Serrano":
            total_spiciness += 15500
        elif pepper_name == "Cayenne":
            total_spiciness += 40000
        elif pepper_name == "Thai":
            total_spiciness += 75000
        elif pepper_name == "Habanero":
            total_spiciness += 125000

    print("Total Spiceness: ", total_spiciness)
    return total_spiciness
checkAnswers("j2", answer)
