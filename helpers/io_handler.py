import os.path
import re
import data_struct
from zipfile import ZipFile

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
    file_name = input_path.split(os.path.sep)[::-1][0][:-4] + ".txt"
    output_path = "outputs" + os.path.sep + file_name
    file = open(output_path, "w")
    file.write(str(len(output)) + "\n")
    
    for lib in output:
        file.write(str(lib.index) + " " + str(len(lib.shipped_books)) + "\n")
        for book in lib.shipped_books:
            file.write(str(book.index) + " ")
        file.write("\n")

    file.close()
    print "Output written at " + output_path

def build_zip():
    # create a ZipFile object
    zipObj = ZipFile('outputs/hashCode_2020.zip', 'w')
    
    abs_dirname = os.getcwd()
    for folder, subfolders, files in os.walk(abs_dirname):
        if ".vscode" in subfolders:
            subfolders.remove(".vscode")
        if ".git" in subfolders:
            subfolders.remove(".git")

        for filename in files:
            ext = filename.split(".")
            ext = ext[len(ext)-1]
            if (ext != "pyc" and ext != "zip" and ext != "pdf" and filename != ".gitignore"):
                rel_dirname = folder[len(abs_dirname)+1:]
                file_path = os.path.join(rel_dirname, filename)
                zipObj.write(file_path)

    zipObj.close()
    print("Zip File created at " + os.path.join(os.getcwd(), "outputs/hashCode_2020.zip"))
    