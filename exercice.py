"""
Chapitre 11.2
"""


import math
from inspect import *

from matrix import *


def main():
	foo = Matrix(3, 3, 42)
	bar = Matrix(3, 3, 69)
	print(str(foo - bar))
	print(foo.__repr__())

if __name__ == "__main__":
	main()

