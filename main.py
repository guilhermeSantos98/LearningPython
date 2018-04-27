def pick(choice):
    if int(choice) == 1:
        import pi
    elif int(choice) == 2:
        import fibonacci
    elif int(choice) == 3:
        import changeCalculator

choice=0
while choice!=4:
    print "\nWhat do you want to do?\n1.Pi until nth \n2.Fibonacci number until nth\n3.Change calculator\n4.Quit"
    choice = input()
    pick(choice)
