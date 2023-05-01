def calculator(a, b, operation):

    if (a.isnumeric() & b.isnumeric()):
        a = float(a);
        b = float(b);
        result = 0;

        if operation == "Addition":
            result = a + b
        elif operation == "Subtraction":
            result = a - b
        elif operation == "Division":
            result = a/b
        elif operation == "Multiplication":
            result = a * b
        else:
            result = "Invalid Operator"


    else:
        result = "Invalid Value"


    return result;

