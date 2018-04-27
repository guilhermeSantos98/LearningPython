def fibonnaci(n):
    a,b,i =0,1,0    
    while n>i:
        print b,
        a, b = b, a+b
        i+=1

print "How many numbers do you which to see?"
n = input()
fibonnaci(n)