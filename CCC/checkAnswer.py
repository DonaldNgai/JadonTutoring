import os
from pathlib import Path


def getLines(filepath):
    testsite_array = []
    with open(filepath) as my_file:
        for line in my_file:
            testsite_array.append(line)
    return testsite_array

def getInputs(path):
    
    file_dir = os.path.dirname(os.path.realpath('__file__'))
    abs_file_path = os.path.join(file_dir, path)
    print (abs_file_path)
    input = getLines(abs_file_path)
    for key, value in enumerate(input):
        print("key:", key, " value:", value.strip())
    return input

def checkAnswer(path, answer):
    file_dir = os.path.dirname(os.path.realpath('__file__'))
    abs_file_path = os.path.join(file_dir, path)
    output = getLines(abs_file_path)
    print("Provided Answer:", answer)
    for key, value in enumerate(output):
        print("Correct Answer: ", value)

    # if int(answer) == int(output[0]):
    #     print("Correct")
    # else:
    #     print ("!!!! Incorrect !!!!")
        print ("Correct answer is: ", value, " Answer function returned: ", answer)
     
def checkAnswers(question, answerFunc):
    file_dir = os.path.dirname(os.path.realpath('__file__'))
    rel_path = "junior/" + question 
    questionDir = os.path.join(file_dir, rel_path)
    testCases = []


    for file in os.listdir(questionDir):
        if file.endswith(".in"):   
          testCases.append(os.path.join(questionDir, file))

    for file in testCases:
        inputs = getInputs(file)
        answer = answerFunc(inputs)
        checkAnswer(os.path.join(questionDir, Path(file).stem + ".out"), answer)
        print()      
    #    
    # print(output[key])

