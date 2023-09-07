import os

def getInputs(filepath):
    testsite_array = []
    with open(filepath) as my_file:
        for line in my_file:
            testsite_array.append(line)
    return testsite_array

rel_path = "junior\j1\j1.01.in"
file_dir = os.path.dirname(os.path.realpath('__file__'))
abs_file_path = os.path.join(file_dir, rel_path)
print (abs_file_path)
firstLine = getInputs(abs_file_path)
for key, value in enumerate(firstLine):
    print(value)
