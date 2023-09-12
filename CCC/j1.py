# importing  all the
# functions defined in test.py
from checkAnswer import *
relpath = "junior\j1\j1.01.in"
j1Input = getInputs(relpath)
# [P,C]/
# j1Input[0] = P = 5
# j1Input[1] = C = 2
# output =730

# //WRITE HERE
output = 50*(j1Input[0]) - 10*(j1Input[1]) 
if j1Input[0] > j1Input[1]:
    output += 500
print ("Output: ", output)

relpath = "junior\j1\j1.01.out"
checkAnswer(relpath, output)
