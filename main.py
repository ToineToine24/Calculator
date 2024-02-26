operator = input("Entrer un signe d'opération (+,-,*,/):")
num1=float(input("Entrer le premier nombre:"))
num2=float(input("Entrer le second nombre:"))

if operator in["+","-","*","/",]:
    result = eval(f"{num1} {operator} {num2}")
    print(round(result, 3))
else:
    print(f"{operator} is not a valid operator try again")
