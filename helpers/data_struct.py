# class DataStruct():
#     def __init__(self, M, N, data):
#         self.M = int(M)
#         self.N = int(N)
#         self.data = data

class Book():
    def __init__(self, index, score):
        self.index = int(index)
        self.score = int(score)

class Library():
    def __init__(self, no_books, signup, shipping, books):
        self.no_books = int(no_books)
        self.signup = int(signup)
        self.shipping = int(shipping)
        self.books = books

class DataGeneral():
    def __init__(self, B, L, D):
        self.B = B
        self.L = L
        self.D = D