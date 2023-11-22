"""Simple interest formula is given by: Simple Interest = (P x T x R)/100 Where, P is the principal amount T is the time and R is the rate

Examples:

Input : P = 10000
        R = 5
        T = 5
Output :2500.0
We need to find simple interest on 
Rs. 10,000 at the rate of 5% for 5 
units of time."""

principle = 10000
rate= 5
T=5
SI = (principle*rate*T)/100
print(SI)

#Program for simple interest with Taking input from user:

principle=input("enter the priciple:")
rate=input("enter the rate of interest:")
time=input("enter the time:")
simpleInterest=(int(principle)*int(rate)*int(time))/100
print(simpleInterest)