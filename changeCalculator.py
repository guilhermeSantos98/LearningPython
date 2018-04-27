#The user enters a cost and then the amount of money given.
#The program will figure out the change and the number of coins in Euro
#needed for the change.
def findChange(costEuro,paidEuro):
    paidCents = int(paidEuro*100)
    costCents = int(costEuro*100)
    print paidCents
    print costCents
    c1,c2,c5,c10,c20,c50,c100,c200,c500,c1000,c2000,c5000,c10000,c20000,c50000=0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
    
    if paidCents>costCents:
        leftToRecieve= paidCents-costCents
        while leftToRecieve!=0:
            print leftToRecieve
            if leftToRecieve>=50000:
                c50000+=1
                leftToRecieve-=50000
            elif leftToRecieve>=20000:
                c20000+=1
                leftToRecieve-=20000
            elif leftToRecieve>=10000:
                c10000+=1
                leftToRecieve-=10000
            elif leftToRecieve>=5000:
                c5000+=1
                leftToRecieve-=5000
            elif leftToRecieve>=2000:
                c2000+=1
                leftToRecieve-=2000
            elif leftToRecieve>=1000:
                c1000+=1
                leftToRecieve-=1000
            elif leftToRecieve>=500:
                c500+=1
                leftToRecieve-=500
            elif leftToRecieve>=200:
                c200+=1
                leftToRecieve-=200
            elif leftToRecieve>=100:
                c100+=1
                leftToRecieve-=100
            elif leftToRecieve>=50:
                c50+=1
                leftToRecieve-=50
            elif leftToRecieve>=20:
                c20+=1
                leftToRecieve-=20
            elif leftToRecieve>=10:
                c10+=1   
                leftToRecieve-=10 
            elif leftToRecieve>=5:
                c5+=1
                leftToRecieve-=5
            elif leftToRecieve>=2:
                c2+=1
                leftToRecieve-=2
            elif leftToRecieve>=1:
                c1+=1
                leftToRecieve-=1
    
        print "The change is:\n"
        if(c50000>0):
            print "{} - 500 euro bill\n".format(c50000)
        if(c20000>0):
            print "{} - 200 euro bill\n".format(c20000)
        if(c10000>0):
            print "{} - 100 euro bill\n".format(c10000)
        if(c5000>0):
            print "{} - 50 euro bill\n".format(c5000)
        if(c2000>0):
            print "{} - 20 euro bill\n".format(c2000)
        if(c1000>0):
            print "{} - 10 euro bill\n".format(c1000)
        if(c500>0):
            print "{} - 5 euro bill\n".format(c500)
        if(c200>0):
            print "{} - 2 euro coin\n".format(c200)
        if(c100>0):
            print "{} - 1 euro coin\n".format(c100)
        if(c50>0):
            print "{} - 50 cents coin\n".format(c50)
        if(c20>0):
            print "{} - 20 cents coin\n".format(c20)
        if(c10>0):
            print "{} - 10 cents coin\n".format(c10)
        elif(c5>0):
            print "{} - 5 cents coin\n".format(c5)
        if(c2>0):
            print "{} - 2 cents coin\n".format(c2)
        if(c1>0):
            print "{} - 1 cents coin\n".format(c1)
    elif(paidCents==costCents):
        print "There is no change"
    elif(paidCents<costCents):
        print "You did not pay enough"

print "How much does the product cost in Euro (Accepts floats with .)?"
cost = input()
print "How much did you paid in Euro (Accepts floats with .)?"
paid = input()
findChange(cost,paid)