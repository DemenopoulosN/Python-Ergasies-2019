a, b = map(int, input("Give two numbers for [a,b]: ").split())
diff = int(input("Give the difference of prime numbers: "))

firstPair = False;
for num in range(a,b-diff+1):
    if (firstPair):
        break
    #Check for first prime
    for i in range(2,num):
        isprime = True
        for a in range(2, num):
            if a % num == 0:
                isprime = False
                break
        else: # loop not exited via break
            isprime = True
        if (isprime):
            p = num
            q = p + diff
            #Check if (first prime + d) is prime
            for i in range(2,q):
                isprime2 = True
                for a in range(2, q):
                    if a % q == 0:
                        isprime2 = False
                        break
                else: # loop not exited via break
                    isprime2 = True
            if (isprime2):
                print("The first pair of primes in [",a,",",b,"] with difference",diff,"is (",p,",",q,")")
                firstPair = True;
                break
