def tokenize(expression):
    current_number = ""
    tokens = []
    index = 0

    while index < len(expression):
        char = expression[index]
        if char.isdigit() or char == ".":
            while True:
                current_number += char
                index += 1
                if index == len(expression):
                    tokens.append(current_number)
                    current_number = ""
                    break
                char = expression[index]
                if not char.isdigit() and char != ".":
                    tokens.append(current_number)
                    current_number = ""
                    break
        else:
            tokens += char
            current_number = ""
            index += 1
            if index == len(expression):
                    break

    return tokens