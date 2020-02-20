# class DataStruct():
#     def __init__(self, M, N, data):
#         self.M = int(M)
#         self.N = int(N)
#         self.data = data

class Book():
    def __init__(self, index, score):
        self.index = int(index)
        self.score = int(score)
    
    def __repr__(self):
        return "Book <index:" + str(self.index) + ", score:" + str(self.score) + ">"

class Library():
    def __init__(self, index, no_books, signup, shipping, books):
        self.index = int(index)
        self.no_books = int(no_books)
        self.signup = int(signup)
        self.shipping = int(shipping)
        self.books = books
        self.shipped_books = []
    
    def __repr__(self):
        return "Library <index:" + str(self.index) + ", no_books:" + str(self.no_books) + ", signup:" + str(self.signup) + ", shipping" + str(self.shipping) + ">"

class DataGeneral():
    def __init__(self, B, L, D):
        self.B = int(B)
        self.L = int(L)
        self.D = int(D)
    
    def __repr__(self):
        return "DataGeneral <B:" + str(self.B) + ", L:" + str(self.L) + ", D:" + str(self.D) + ">"

class OutputData:
    def __init__(self, A, data):
        self.A = A
        self.data = data
