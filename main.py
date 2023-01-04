#trying to ask for input from the user then have those values plugged in
#in the code below for it to be multiplied and solved
def calc_inflation(init_bal, interest_rate, years_to_go):
    if years_to_go == 0:
        return init_bal
    if init_bal == 0:
        return 0
    interest = init_bal*interest_rate
    return calc_inflation(init_bal+interest, interest, years_to_go-1)

def main():
    input1 = int(input("What is your initial balance?"))
    input2 = float(input("What is the interest rate? (Decimals only)"))
    input3 = int(input("How many years are left to go?"))
    big = calc_inflation(input1, input2, input3)
    print(big)


main()

