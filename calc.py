import os
logo = """
 _____________________
|  _________________  |
| | Pyronista    0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""
def add(inp1,inp2):
    return inp1+inp2
def sub(inp1,inp2):
    return inp1-inp2
def mul(inp1,inp2):
    return inp1*inp2
def div(inp1,inp2):
    return inp1/inp2

def calc():
    print(logo)
    inp4='n'
    while inp4=='n':
        inp1=float(input("Enter the First Number: "))
        inp3="y"
        while inp3=='y':
            print("+")
            print("-")
            print("*")
            print("/")
            op=input("Pick an operator: ")
            if op not in "+-*/":
                print("Invalid Operator")
                inp3=input("Do you wish to continue - (Y - Yes| N - No)")
                inp3=inp3.lower()
                continue
            inp2=float(input("Enter the Second Number: "))
            operations={
                "+": add,
                "-": sub,
                "*": mul,
                "/": div
            } 
            f=operations[op]
            a=f(inp1,inp2)
            print(inp1 , op , inp2 , "=" , a)
            inp4=input(f"Type 'y' to continue calculating with {a}, or Type 'n' to start a new calculation, or Type 'e' to exit the calculator: ")
            inp4=inp4.lower()
            if inp4=='y': 
                inp1=a
                continue
            elif inp4=='n':
                os.system('cls')
                break
            elif inp4=='e':
                raise SystemExit
calc()
