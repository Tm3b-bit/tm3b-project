class CalculatorError(Exception):
    pass
 
 
def find_operator_index(tokens, operators):

    index = 0
    while index < len(tokens):
        if tokens[index] in operators:
            return index
        index += 1
    return -1
 
 
def apply_one_operation(tokens, op_index):
    if op_index == 0 or op_index == len(tokens) - 1:
        raise CalculatorError("Invalid!")
 
    left = tokens[op_index - 1]
    operator = tokens[op_index]
    right = tokens[op_index + 1]
 

    if not isinstance(left, (int, float)) or not isinstance(right, (int, float)):
        raise CalculatorError("Invalid!")
 
    if operator == '*':
        result = left * right
    elif operator == '/':
        if right == 0:
            raise CalculatorError("	Division by zero is not allowed")
        result = left / right
    elif operator == '+':
        result = left + right
    elif operator == '-':
        result = left - right
    else:
        raise CalculatorError("Unknown operator")
 
    tokens[op_index - 1: op_index + 2] = [result]
    return tokens
 
 
def evaluate(tokens):

    if not tokens:
        raise CalculatorError("No expression entered")
 
    if len(tokens) == 1:
        if isinstance(tokens[0], (int, float)):
            return tokens[0]
        raise CalculatorError("Invalid!")
 
    tokens = list(tokens)
 
    op_index = find_operator_index(tokens, ['*', '/'])
    while op_index != -1:
        tokens = apply_one_operation(tokens, op_index)
        op_index = find_operator_index(tokens, ['*', '/'])
 
    op_index = find_operator_index(tokens, ['+', '-'])
    while op_index != -1:
        tokens = apply_one_operation(tokens, op_index)
        op_index = find_operator_index(tokens, ['+', '-'])
 
    if len(tokens) != 1 or not isinstance(tokens[0], (int, float)):
        raise CalculatorError("Invalid!")
 
    return tokens[0]