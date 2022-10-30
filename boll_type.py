# 1) Fix the error in comparison 3! 5, don't delete anything
print('Examples of the 1st task')

comparison_result: bool = 3 != 5
print(comparison_result)  # True

# 2) List all combinations of arithmetic comparisons for 5 _ 5 in which the result will be True
print('Examples of the 2nd task')

comparison_result: bool = 5 == 5
print(comparison_result)  # True

comparison_result: bool = 5 <= 5
print(comparison_result)  # True

comparison_result: bool = 5 >= 5
print(comparison_result)  # True

# 3) List 5 combinations of logical operators (or, and, not)
# and parentheses so that the result of the expression True _ True _ False is True'''
print('Examples of the 3rd task')

is_true = 3 == 2 or 3 == 3
print(is_true)  # True
is_true = 3 == 3 and 2 < 3
print(is_true)  # True

age = 35
is_he_old = False  # :)
print(not age < 35)  # True
print(not is_he_old)  # True

# Subtract boolean values for the pair of arguments (bool()) and match (==) between them.
print('Examples of the 4rd task')

print(bool(None)) == (bool(7))  # bool(None) - False, because None is an empty value, bool(7) - True

print(bool("")) == (bool(10 - 1))  # bool(None) - False, because an empty string is an empty value, bool(10-1) - True

print(bool(True or False)) == (bool(print(1)))  # In both cases, the results of the functions are the value

print(bool(type(None))) == bool(id(None))  # In both cases, the results of the functions are the value.
