from checkAnswer import *

def answer(inputs):
    output = (inputs[0] * 50) - (inputs[1] * 10)
    if inputs[0] > inputs[1]:
        output += 50
    return output

checkAnswers("j1", answer)



number  = 70
if number < 80:
    print("hello")
if number < 60 and number >= 0:
    print("F")
else:
    print("a")

