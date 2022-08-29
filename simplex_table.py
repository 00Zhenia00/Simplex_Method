import numpy as np

class SimplexTable:

	def __init__(self, table: np.array, basis: np.array):
		
		self._table = table
		self._basis = basis
		self._work_element = None


	@property
	def basis(self):
		return self._basis


	@property
	def work_element(self):
		return self._work_element


	def optimal_plan(self):
		plan = np.zeros(self._table.shape[1] - 1)
		for i, var in enumerate(self._basis):
			var_value = self._table[i, -1]
			plan[var-1] = var_value
		return plan


	def obj_func_value(self):
		return self._table[-1, -1]
	

	def is_optimal(self):
		z = self._table[-1][:]
		return not z[z < 0].size


	# Calculation by rectangle method
	def calculate(self):

		pivot_col = int(self._find_pivot_column())
		pivot_row = self._find_pivot_row(pivot_col)
		self._work_element = self._table[pivot_row][pivot_col]

		# Add new variable into basis
		self._basis[pivot_row] = pivot_col + 1

		rows, cols = self._table.shape[0], self._table.shape[1]

		for i in range(rows):
			for j in range(cols):
				if i == pivot_row:
					continue
				elif j == pivot_col:
					continue
				else:
					self._table[i][j] = self._table[i][j] - self._table[i][pivot_col] * self._table[pivot_row][j] / self._work_element


		# Fill pivot row
		for col in range(cols):
			self._table[pivot_row, col] /= self._work_element


		# Fill basis columns
		for i in self._basis:
			self._table[:,i-1].fill(0)
			row = np.where(self._basis == i)[0][0]
			self._table[row][i-1] = 1


	# Return index of the pivot column in simplex-table
	def _find_pivot_column(self):
		min_el_ind = np.argmin(self._table[-1])
		if self._table[-1][min_el_ind] < 0:
			return int(min_el_ind)
		return None


	# Return index of the pivot row in simplex-table
	def _find_pivot_row(self, pivot_col_ind: int):

		pivot_col_arr = self._table[:-1, pivot_col_ind]
		solution_col_arr = self._table[:-1, -1]

		div_arr = solution_col_arr / pivot_col_arr

		min_pos_el = np.min(div_arr[div_arr >= 0])

		min_pos_el_ind, = np.where(div_arr == min_pos_el)

		return min_pos_el_ind[0]


	def __str__(self):
		return f'{self._table}'


