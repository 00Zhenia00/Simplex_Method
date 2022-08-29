import numpy as np
from simplex_table import SimplexTable


class SimplexMethod:
	
	def __init__(self, amount_of_vars: int, obj_func: list, lin_eq_sys: np.array, obj_func_dir: str = 'max'):

		self._table = self._make_simplex_table(amount_of_vars, obj_func, lin_eq_sys, obj_func_dir)
		self._basis = self._find_basis()
		self._obj_func_value = None
		self._optimal_plan = np.zeros(amount_of_vars)


	def solve(self):
		simplexTable = SimplexTable(self._table, self._basis)

		step = 0
		print(f"Step {step}")
		print(simplexTable, end="\n\n")
		
		while not simplexTable.is_optimal():
			step += 1
			print(f"Step {step}")
			simplexTable.calculate()
			print(f"Pivot element = {simplexTable.work_element}")
			print(f"Basis = {simplexTable.basis}")
			print(simplexTable, end="\n\n")

		print("Solution is optimal.")
		print(f"Z = {simplexTable.obj_func_value()}")
		print(f"Optimal plan: {simplexTable.optimal_plan()}")


	@property
	def obj_func_value(self):
		return self._obj_func_value


	@property
	def optimal_plan(self):
		return self._optimal_plan


	def _make_simplex_table(self, amount_of_vars: int, obj_func: list, lin_eq_sys: np.array, obj_func_dir: str):
		
		if (obj_func_dir == 'max'):
			for i in range(0, len(obj_func)-1):
				obj_func[i] = -obj_func[i]
		else:
			pass

		# Make simplier
		table = np.array([row for row in lin_eq_sys] + [obj_func])

		return table


	def _find_basis(self):
		basis = np.zeros(self._table.shape[0]-1, int)
		columns = self._table.shape[1]
		var_cnt = 0
		for i in range(columns-1):
			if self._is_basis_vector(self._table[:, i]):
				basis[var_cnt] = i + 1
				var_cnt += 1
		return basis



	def _is_basis_vector(self, v: np.array):
		# Return True if vector is (0, ... , 0, 1, 0, ... , 0)

		ones_cnt = 0

		for el in v:
			if el == 0:
				continue
			elif el == 1:
				ones_cnt += 1
			else:
				return False

		return (ones_cnt == 1)

