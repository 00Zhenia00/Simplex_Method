import numpy as np
from simplex_method import SimplexMethod


class LinProgProblem():
	""" Class of Linear Programming Problem task."""
	
	def __init__(self, amount_of_vars: int, obj_func: list, lin_eq_sys: np.array, obj_func_dir: str = 'max'):
		"""
			param: obj_func - set the array of the coeffs of the objective function
			param: obj_func_dir - set the direction of the objective function (min/max). Set on 'max' by defolt.
			param: lin_eq_sys - set the array of the system equations

		"""
		# TODO check of the variables
		self._amount_of_vars = amount_of_vars
		self._obj_func = obj_func
		self._obj_func_dir = obj_func_dir
		self._lin_eq_sys = lin_eq_sys


	def simplex_method(self):
		simplexMethod = SimplexMethod(self._amount_of_vars, self._obj_func, self._lin_eq_sys, self._obj_func_dir)
		simplexMethod.solve()


	def _print_obj_func(self):

		obj_func = ''

		n = 1

		for k in self._obj_func:

			if n != 1:
				obj_func += ' + '

			if n <= self._amount_of_vars:
				obj_func += '(' + str(k) + ')' + '*x' + str(n)
			else:
				obj_func += '(' + str(k) + ')'
			n += 1

		return obj_func


	def _print_lin_system(self):

		lin_sys = ''

		for row in self._lin_eq_sys:
			n = 1
			for el in row[:-1]:

				if n != 1:
					lin_sys += ' + '

				lin_sys += '(' + str(el) + ')' + '*x' + str(n)
				n += 1

			lin_sys += ' = ' + str(row[-1]) + '\n\t'

		return lin_sys


	def __str__(self):

		return f'Z: {self._print_obj_func()} -> {self._obj_func_dir}\n\n\t{self._print_lin_system()}'


	

	