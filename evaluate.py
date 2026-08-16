def find_operator_index(tokens, operators):
    index = 0
    while index < len(tokens):
        if tokens[index] in operators:
            return index
        index += 1
    return -1


def apply_one_operation(tokens, op_index):
    left = tokens[op_index - 1]
    operator = tokens[op_index]
    right = tokens[op_index + 1]

    if operator == '*':
        result = left * right
    elif operator == '/':
        result = left / right
    elif operator == '+':
        result = left + right
    elif operator == '-':
        result = left - right

    tokens[op_index - 1 : op_index + 2] = [result]
    return tokens


def evaluate(tokens):
    op_index = find_operator_index(tokens, ['*', '/'])
    while op_index != -1:
        tokens = apply_one_operation(tokens, op_index)
        op_index = find_operator_index(tokens, ['*', '/'])

    op_index = find_operator_index(tokens, ['+', '-'])
    while op_index != -1:
        tokens = apply_one_operation(tokens, op_index)
        op_index = find_operator_index(tokens, ['+', '-'])

    return tokens[0]