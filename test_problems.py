# Solution to problems using sympy and pytest 
import pytest 
from sympy.matrices import Matrix 

def test_problem_1(): 
    M = Matrix([[2, 1, -3], [-6, 0, -1], [4, 5, -2], [3, -8, 7]])
    N = Matrix([[-4, -1], [9, 0], [6, -5]])
    Solution = M*N
    My_Solution = Matrix([[-17, 13],[18, 11], [17, 6], [-42, -38]])
    assert Solution == My_Solution
