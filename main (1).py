# Program description: This Python script calculates and prints values for various mathematical series, including the Harmonic Series,
#Two Series, Zero Series, and Partial Riemann Zeta, based on user input. The results are provided in both fractional
#form and as approximate decimal values.
# Name = Niyam Acharya User Name = nka42(14510667)
#Date = October 12, 2023

from fraction import Fraction

def H(n):
    result = Fraction(1, n)
    for k in range(1, n ):
        result += Fraction(1, k)
    return result
    
def T(n):
    result = Fraction(0,1)
    for k in range(n+1):
        result += Fraction(1, 2**k)
    return result
    
def Z(n):
    result = Fraction(0,1)
    for k in range(n + 1):
        result += Fraction(1, 2**k)
    finalResult = Fraction(2,1) - result
    return finalResult
    
def R(n,b):
    result = Fraction(0, 1)
    for k in range(1, n + 1):
        result += Fraction(1, k**b)
    return result

def get_valid_input():
    while True:
        try:
            n = int(input("Enter Number of iterations (integer>0): "))
            if n > 0:
                return n
            else:
                print("Bad Input")
        except ValueError:
            print("Bad Input")

    
def main():
    print("Welcome to Fun with Fractions!")
    n = get_valid_input()

    
    print(f"H({n})={H(n)}")
    print(f"H({n})~={H(n).approximate()}")
    print(f"T({n})={T(n)}")
    print(f"T({n})~={T(n).approximate()}")
    print(f"Z({n})={Z(n)}")
    print(f"Z({n})~={Z(n).approximate()}")
    print(f"R({n},{n})={R(n,n)}")
    print(f"R({n},{n})~={R(n,n).approximate()}")


if __name__ == "__main__":
    #TODO
    main()