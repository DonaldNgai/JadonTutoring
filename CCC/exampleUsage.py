from checkAnswer import *

def answer(inputs):
    output = (inputs[0] * 50) - (inputs[1] * 10)
    if inputs[0] > inputs[1]:
        output += 50
    return output

checkAnswers("j1", answer)