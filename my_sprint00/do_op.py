print("---- Simple calculator ----")
print("Let's add some numbers")
value = int(input("Input your first value:"))
op = input("Input your operator:")

if op != "*" and op != "+" and op != "-" and op != "/":
    print("usage: the operator must be '*' or '+' or '-' or '/'")
else:
    second_value = int(input("Input your second value:"))
    if op == "*":
        print("first value({}) * second_value({}) = {}".format(value, second_value, (value*second_value)))
    elif op == "+":
        print("first value({}) + second_value({}) = {}".format(value, second_value, (value+second_value)))

    elif op == "-":
        print("first value({}) - second_value({}) = {}".format(value, second_value, (value-second_value)))

    else:
        print("first value({}) / second_value({}) = {}".format(value, second_value, (value / second_value)))
print("---- Simple calculator ----")