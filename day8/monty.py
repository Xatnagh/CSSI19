l=list(range(0,100))
print l[5:20]





factors= []

def factor(one):
    i=1
    while i<=one:
        if one%i==0:
            factors.append(i)
        i=i+1
factor(50)
"print factors"

def countToN(number):
    i=1
    while(i<=number):
        print(i)
        i=i+1

"countToN(30)"


