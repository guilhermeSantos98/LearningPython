import math
def pi(n):
    i=0
    n+=2
    sPi = str(math.pi)
    result = ""
    while n>i:
        result+= sPi[i]
        i+=1
    return result

print "How many decimals do you want in pi (max:11)"
n=input()
print pi(int(n))