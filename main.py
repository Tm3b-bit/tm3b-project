from tokenizer import tokenize
from convert_tokens import convert_token
from evaluate import evaluate

expression = input("enter your expression: ")
result = tokenize(expression)
result_convert = convert_token(result)
final_result = evaluate(result_convert)
print(final_result)


