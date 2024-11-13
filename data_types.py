""" 1. Write a script, data_types.py, to:
○ Create variables of each primitive data type (int, float, str, bool).
○ Perform a few operations: arithmetic (on int and float), string concatenation, and
logical operations.
○ Create a dictionary to store and display these variables by their types as keys
(e.g., int: [10, 20]).
 """

# Creating Primitive data types
data_int: int = 20
data_float: float = 10.3
data_str: str = 'shristi'
data_bool: bool = True
# Operations on each primitive data type
int_result = data_int + 1  # Arithmetic operation on int
float_result = data_float + 0.3  # Arithmetic operation on float
str_result = data_str + ' Shrestha'  # String concatenation
bool_result = data_bool and False  # Logical operation
# Creating dictionary to store and display these variables by their types
data_dict = {
    'int': [data_int, int_result],
    'float': [data_float, float_result],
    'str': [data_str, str_result],
    'bool': [data_bool, bool_result]
}
# Displaying the dictionary
print("Data Types Dictionary:", data_dict)