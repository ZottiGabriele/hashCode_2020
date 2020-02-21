import os
import sys
import solve_optimized
from helpers import io_handler

def main():
    solve_optimized.main("inputs/a_example.txt")
    solve_optimized.main("inputs/b_read_on.txt")
    solve_optimized.main("inputs/c_incunabula.txt")
    solve_optimized.main("inputs/d_tough_choices.txt")
    solve_optimized.main("inputs/e_so_many_books.txt")
    solve_optimized.main("inputs/f_libraries_of_the_world.txt")

    io_handler.build_zip()

if __name__ == "__main__":
    main()