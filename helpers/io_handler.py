import os.path
import re
import data_struct

def read_input(file_path):
    
    if(not(os.path.exists(file_path) and os.path.isfile(file_path))):
        print("File error")
        exit()

    print "Reading Input..."
    file = open(file_path, "r")
    content = file.read()
    out = parse_input(content)
    file.close()
    return out

def parse_input(input):
    print "Parsing Input..."
    data = re.split(' |\n', input)
    M = data[0]
    N = data[1]
    
    return NotImplemented

def write_output(output, input_path):
    file_name = input_path.split(os.path.sep)[::-1][0][:-3] + ".out"
    output_path = "outputs" + os.path.sep + file_name
    file = open(output_path, "w")
    file.write(str(output.K) + "\n")
    file.write(output.data + "\n")
    file.close()
    print "Output written at " + output_path
    