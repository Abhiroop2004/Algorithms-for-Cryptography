def fast_exponentiation(x,e,n):
    r=1 #initializing result to 1
    e=bin(e)[2:]    #converting the exponent from integer to binary
    for i in e:
        r=(r*r)%n   #executes for every bit scanned
        if i=='1':
            r=(r*x)%n   #executes when scanned bit is 1
    return r
x=int(input("Base:"))
e=int(input("Exponent:"))
n=int(input("Modulus:"))
print("{} ^ {} mod {} = {} ".format(x,e,n,fast_exponentiation(x,e,n)))
