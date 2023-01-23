# Solution to problems using sympy and pytest 
import pytest 
from sympy.matrices import Matrix 

def test_problem_1(): 
    M = Matrix([[2, 1, -3], [-6, 0, -1], [4, 5, -2], [3, -8, 7]])
    N = Matrix([[-4, -1], [9, 0], [6, -5]])
    Solution = M*N
    My_Solution = Matrix([[-17, 13],[18, 11], [17, 6], [-42, -38]])
    assert Solution == My_Solution

def test_problem_2(): 
    M = Matrix([[1, 2, 3], [4, 0, -2]])
    N = Matrix([[3, 1], [2, 4], [-1, 5]])
    Solution = M*N
    My_Solution = Matrix([[4, 24], [14, -6]])
    assert Solution == My_Solution

def test_problem_3(): 
    M = Matrix([[6, 1], [2, -3], [-10, 8]])
    N = Matrix([[4, 0, 9], [-7, 2, -5]])
    Solution = M*N
    My_Solution = Matrix([[17, 2, 49], [29, -6, 33], [-96, 16, -130]])
    assert Solution == My_Solution

def test_problem_4(): 
    M = Matrix([[1, -2], [-6, 4], [5, -3]])
    N = Matrix([[1, 0, 2, 4], [3, -1, 8, 6]])
    Solution = M*N
    My_Solution = Matrix([[-5, 2, -14, -8], 
                            [6, -4, 20, 0], 
                            [-4, 3, -14, 2]])
    assert Solution == My_Solution


