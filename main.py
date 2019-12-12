# two inputs, inputs checked for number,float format
# operation restricted to + - * / and %. message if other than these inputs.

user_input_number1 = input("Enter a number : ")
user_input_number2 = input("Enter another number : ")
uOperation = input("Enter the operation symbol : ")
result = ""
try:
    # TODO: write code...
    number1 = float(user_input_number1)
    number2 = float(user_input_number2)
except ValueError:
    print("Please enter valid input numbers")
else:
    
    if(uOperation == '+'):
        result = number1 + number2
    elif(uOperation == '-'):
        result = number1 - number2
    elif(uOperation == '*'):
        result = number1 * number2
    elif(uOperation == '/'):
        result = number1 / number2
    elif(uOperation == '%'):
        result = number2 / number1
    else :
        print("Enter valid operation : +, -, *, /, %")

print(result)

