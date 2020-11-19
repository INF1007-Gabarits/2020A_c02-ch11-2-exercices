"""
Chapitre 11.2
"""


import numbers
import copy
import collections
import collections.abc


class Matrix:
	"""
	Matrice numérique stockée en tableau 1D en format rangée-major.

	Par exemple, soit la matrice :
	11 12 13 14
	21 22 23 24
	31 32 33 34
	On construirait un tableau de cette façon.
	tab = [11, 12, 13, 14, 21, 22, 23, 24, 31, 32, 33, 34]
	Pour accéder à la deuxième rangée, quatrième colonne (élément de valeur 24), on ferait mat[1*4 + 3]

	:param height: La hauteur (nb de rangées)
	:param width: La largeur (nb de colonnes)
	:param data: Si une liste, alors les données elles-mêmes (affectées, pas copiées). Si un nombre, alors la valeur de remplissage
	"""

	def __init__(self, height, width, data = 0.0):
		if not isinstance(height, numbers.Integral) or not isinstance(width, numbers.Integral):
			raise TypeError()
		if height == 0 or width == 0:
			raise ValueError(numbers.Integral)
		self.__height = height
		self.__width = width
		if isinstance(data, list):
			if len(data) != len(self):
				raise ValueError(list)
			self.__data = data
		elif isinstance(data, numbers.Number):
			self.__data = [data for i in range(len(self))]
		else:
			raise TypeError()

	@property
	def height(self):
		return self.__height

	@property
	def width(self):
		return self.__width

	@property
	def data(self):
		return self.__data

	def __getitem__(self, indexes):
		"""
		Indexation rangée-major

		:param indexes: Les index en `tuple` (rangée, colonne)
		"""

		if not isinstance(indexes, tuple):
			raise IndexError()
		if indexes[0] >= self.height or indexes[1] >= self.width:
			raise IndexError()
		return self.data[indexes[0] * self.width + indexes[1]]

	def __setitem__(self, indexes, value):
		"""
		Indexation rangée-major

		:param indexes: Les index en `tuple` (rangée, colonne)
		"""
		
		if not isinstance(indexes, tuple):
			raise IndexError()
		if indexes[0] >= self.height or indexes[1] >= self.width:
			raise IndexError()
		self.data[indexes[0] * self.width + indexes[1]] = value

	def __len__(self):
		"""
		Nombre total d'éléments
		"""
		return self.height * self.width

	def __str__(self):
		lines = []
		for i in range(self.height):
			lines.append(" ".join([str(self[i, j]) for j in range(self.width)]))
		return "\n".join(lines)

	def __format__(self, format_spec):
		fmt_template = f"{{:{format_spec}}}"
		lines = []
		for i in range(self.height):
			lines.append(" ".join([fmt_template.format(self[i, j]) for j in range(self.width)]))
		return "\n".join(lines)


	def __repr__(self):
		return f"Matrix({self.height.__repr__()}, {self.width.__repr__()}, {self.data.__repr__()})"

	def clone(self):
		return Matrix(self.height, self.width, self.data)

	def copy(self):
		return Matrix(self.height, self.width, copy.deepcopy(self.data))

	def has_same_dimensions(self, other):
		return (self.height, self.width) == (other.height, other.width)

	def __pos__(self):
		return self.copy()

	def __neg__(self):
		return Matrix(self.height, self.width, [-e for e in self.data])

	def __add__(self, other):
		if not self.has_same_dimensions(other):
			raise ValueError(Matrix)
		return Matrix(self.height, self.width, [e1 + e2 for e1, e2 in zip(self.data, other.data)])

	def __sub__(self, other):
		return self + -other

	def __mul__(self, other):
		if isinstance(other, Matrix):
			if self.height != other.width:
				raise ValueError(Matrix)
			# Rappel de l'algorithme simple pour C = A * B, où A, B sont matrices compatibles (hauteur_A = largeur_B)
			# C = Matrice(hauteur_A, largeur_B)
			# Pour i dans [0, hauteur_C[
				# Pour j dans [0, largeur_C[
					# Pour k dans [0, largeur_A[
						# C(i, j) = A(i, k) * B(k, j)
			result = Matrix(self.height, other.width)
			for i in range(result.height):
				for j in range(result.width):
					for k in range(self.width):
						result[i, j] += self[i, k] * other[k, j]
			return result
		elif isinstance(other, numbers.Number):
			return Matrix(self.height, self.width, [e * other for e in self.data])
		else:
			raise TypeError()

	def __rmul__(self, other):
		if isinstance(other, numbers.Number):
			return self * other
		else:
			raise TypeError()

	def __abs__(self):
		return Matrix(self.height, self.width, [abs(e) for e in self.data])

	def __eq__(self, other):
		return self is other or (self.height, self.width, self.data) == (other.height, other.width, other.data)

	@classmethod
	def identity(cls, width):
		result = cls(width, width)
		for i in range(width):
			result[i, i] = 1.0
		return result

