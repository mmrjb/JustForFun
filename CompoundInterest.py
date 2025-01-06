#How to find Compound Interest
"""

    A = P(1 + R/100) ^ t 

    Compound Interest = A – P 

    Where, 


        A is amount 

        P is the principal amount 

        R is the rate in a year and 

        T is the time span

"""

P = float(input("Please enter the original investment amount :"))
R = float(input("Please enter the annual growth rate :"))
T = float(input("Please enter the investment timeframe in years :"))

#Result Of the Formula

A = P * ((1 + R/100)**T)
Result = (A-P)

print(f"The Compound Interest is {Result}")