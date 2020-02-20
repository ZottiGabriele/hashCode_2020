import sys
import helpers
import sortedcontainers

def main(file_path):
    #READ THE INPUT
    (dataGeneral, scores, libraries) = helpers.io_handler.read_input(file_path)
    #SOLVE THE PROBELM
    books_to_scan = [i for i in range(0, dataGeneral.B)]
    days_left = dataGeneral.D

    #sort libraries by signup delay
    sorted_libs = sorted(libraries, key=lambda library: library.signup)
    sorted_libs.reverse()
    #print sorted_libs
    signing_lib = helpers.Library(-1, -1, 0, -1, []); # dummy library
    active_libreries = []
    used_libraries = []
    for day in xrange(days_left, 0,-1):
        print("DAY " + str(day))
        #signup new library if the signup process done
        if(signing_lib.signup == 0):
            #dont add the dummy library
            if(signing_lib.index != -1):
                active_libreries.append(signing_lib)
                used_libraries.append(signing_lib)
            #add new lib to signup queue
            if(len(sorted_libs) > 0):
                signing_lib = sorted_libs.pop()
        #first day counts as signup day
        signing_lib.signup -= 1
        #push books in each active library
        for lib in active_libreries:
            books_to_push = lib.shipping
            #push as many books as possible from a single library
            
            for i in xrange(books_to_push):
                if(len(lib.books) > 0):
                    book = lib.books.pop()
                    lib.shipped_books.append(book)
                else:
                    active_libreries.remove(lib)
                    break
    
    #WRITE THE OUTPUT
    helpers.write_output(used_libraries, file_path)

    return NotImplemented

if __name__ == "__main__":
    if (len(sys.argv) < 2):
        print "ERROR"
        exit()

    main(sys.argv[1])