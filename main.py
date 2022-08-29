from linear_programming_problem import LinProgProblem
from simplex_method import SimplexMethod
import numpy as np

def main():

	amount_of_vars, obj_func, obj_func_dir, amount_of_limits, lin_eq_sys = task_input()

	l = LinProgProblem(amount_of_vars, obj_func, lin_eq_sys, obj_func_dir)

	print(l, end="\n\n")
	l.simplex_method()


def info():
	print("This is Linear Programming Problems Solver.")


def task_input():
	print("Please, enter your linear programming problem.")

	amount_of_vars = int(input("Amount of variables: "))
	obj_func: list = int_list_input(amount_of_vars)
	obj_func_dir: str = input("Objective function direction (min/max): ")
	amount_of_limits = int(input("Amount of limits in linear system: "))
	lin_eq_sys: np.array = lin_system_input(amount_of_limits, amount_of_vars)

	return amount_of_vars, obj_func, obj_func_dir, amount_of_limits, lin_eq_sys


def int_list_input(amount_of_vars):
	print("Coefficients in the objective function: ", end=" ")
	result = []
	for i in range(amount_of_vars + 1):
		el = int(input())
		result.append(el)
	return result


def lin_system_input(amount_of_limits: int, amount_of_vars: int):
	print("Coefficients of linear system: ")
	lin_sys = np.zeros([amount_of_limits, amount_of_vars + 1], dtype=float)
	for i in range(amount_of_limits):
		print("\tEquation ", i+1)
		for v in range(amount_of_vars):
			print(f"x{v+1}= ", end="")
			value = int(input())
			lin_sys[i, v] = value
		print(f"b{i+1}= ", end="")
		b = int(input())
		lin_sys[i, v + 1] = b
	return lin_sys



main()