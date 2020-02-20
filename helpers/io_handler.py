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
    rows = re.split('\n', input)
    dataGeneral = 0
    scores = []
    libraries = []
    i = 0
    lib_index = 0
    while i < len(rows)-2:
        data = re.split(' ', rows[i])
        if(i == 0):
            dataGeneral = data_struct.DataGeneral(data[0], data[1], data[2])
        elif(i == 1):
            scores = data
        else:
            print(i)
            books_raw = re.split(' ', rows[i+1])
            books = []
            for book in books_raw:
                books.append(data_struct.Book(int(book), int(scores[int(book)])))
            libraries.append(data_struct.Library(lib_index, int(data[0]), int(data[1]), int(data[2]), books))
            lib_index += 1
            i += 1
        i += 1
    return (dataGeneral, scores, libraries)

def write_output(output, input_path):
    file_name = input_path.split(os.path.sep)[::-1][0][:-3] + ".out"
    output_path = "outputs" + os.path.sep + file_name
    file = open(output_path, "w")
    file.write(str(output.A) + "\n")
    file.write(output.data + "\n")
    file.close()
    print "Output written at " + output_path
    