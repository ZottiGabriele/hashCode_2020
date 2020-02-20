import sys
import helpers
import sortedcontainers

def main(file_path):
    #READ THE INPUT
    (dataGeneral, scores, libraries) = helpers.io_handler.read_input(file_path)
    print((dataGeneral, scores, libraries))
    #SOLVE THE PROBELM
    

    #WRITE THE OUTPUT
    return NotImplemented

if __name__ == "__main__":
    if (len(sys.argv) < 2):
        print "ERROR"
        exit()

    main(sys.argv[1])