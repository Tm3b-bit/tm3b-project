while True:
        
        first,op,second=input("enter your expression:")
        first, second = map(int, (first, second))

        if op == "+":
            print(first+second)
        elif op == "-":
            print(first-second)
        elif op == "*":
            print(first*second)
        elif op == "/":
            print(first/second)
        elif op == "//":
            print(first//second)
            """
            به همین ترتیب عملگرهای دیگر نیز اضافه میشن
            Other operators are added in the same way.
            """
        else:
            print("invalid character")


