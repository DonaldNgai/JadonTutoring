import os

def getLines(filepath):
    testsite_array = []
    with open(filepath) as my_file:
        for line in my_file:
            testsite_array.append(int(line))
    return testsite_array

def getInputs(path):
    
    file_dir = os.path.dirname(os.path.realpath('__file__'))
    abs_file_path = os.path.join(file_dir, path)
    print (abs_file_path)
    input = getLines(abs_file_path)
    # for key, value in enumerate(input):
    #     print("value", value)
    #     print("key", key)
    return input

def checkAnswer(path, answer):
    file_dir = os.path.dirname(os.path.realpath('__file__'))
    abs_file_path = os.path.join(file_dir, path)
    output = getLines(abs_file_path)
    # for key, value in enumerate(output):
    #     print("value", value)
    #     print("key", key)
    if answer == output[0]:
        print("WOOOHOOOOOO")
    else:
        print ("Incorrect")
     

    # print(output[key])

