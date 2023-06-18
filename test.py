from boilerplate import get_boilerplate_code
from description import get_problem_description
import time

url = 'https://leetcode.com/problems/invert-binary-tree/'

problem_description = get_problem_description(url)
boilerplate_code = get_boilerplate_code(url)

print(problem_description)
print(boilerplate_code)
