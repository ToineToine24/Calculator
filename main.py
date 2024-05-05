# selection de l'operateur
VAILDE_OPERATEURS = ("+", "-", "*", "/")
while True:
    operator = input(f"Entrer un operateur {VAILDE_OPERATEURS}: ")
    if operator not in VAILDE_OPERATEURS:
        # => ops invalide
        print(f"l'operateur: {operator} n'est pas valide, recommencez ...")
        continue  # retry
    # => selection valide
    break

def foo(askText:str)->float:
    while True:
        txt = input(askText)
        try: num = float(txt)
        except ValueError:
            print(f"selection invalide: {txt}, recomencez ...")
            continue # retry
        # => selection valide
        return num

# selection des nombres
num1 = foo("1er nombre: ")
num2 = foo("2eme nombre: ")

# => l'ops et les nombres sont valides
# calcule du resultat
calcule = f"{num1} {operator} {num2}"
print(f"{calcule} = {eval(calcule)}")
