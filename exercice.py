"""
Chapitre 11.2
"""


import math
from inspect import *

from matrix import *


def main():
	foo = Matrix(3, 3, 3)
	bar = Matrix(3, 3, 69)
	print(str(foo - bar))
	print(str(3 * foo))
	print(foo.__repr__())
	print(Matrix(3, 3, 9) != 3 * foo)
	qux = (Matrix.identity(3) * 11.12)
	print(qux.__format__(">5.2f"))
	print(f"{qux :>5.2f}")

if __name__ == "__main__":
	main()

