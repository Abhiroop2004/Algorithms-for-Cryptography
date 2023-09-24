def extended_euclid(a,b): #function to calculate GCD
    (s0,t0,s1,t1)=(1,0,0,1)
    (r0,r1)=a,b
    while(r1!=0): #follows the original mathematical approach implemented with a while loop
        q=r0//r1
        (r0,r1)=(r1,r0-q*r1)
        (s0,s1)=(s1,s0-q*s1)
        (t0,t1)=(t1,t0-q*t1)
    return(s0,t0,r0)    #where s0 and t0 are the coefficients and r0 is the gcd
a=int(input("Enter 1st number for GCD:"))
b=int(input("Enter 2nd number for GCD:"))
s,t,r=extended_euclid(a,b)
print("Greatest Common Divisor: ",r)
print("({}) . {} + ({}) . {} = {}".format(s,a,t,b,r))
