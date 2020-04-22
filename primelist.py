# I want to find all of the prime numbers I can get. Let's do that with a couple of loops.

# our base list that we'll be pulling numbers from
baseList = [2, 3]
# the list of prime numbers that we're building. We know 2 belongs there already.
primeList = [2]

# let's start by checking every number up to 1000
while baseList[-1] <= 1000:
    i = baseList[0]  # this is the numerator. we start at the beginning of the list, which is 2
    b = baseList[-1]  # the number we're testing, which will be at the end of the list
    prime = True  # the prime flag
    # and here's where we actually do the math
    while i < b:  # as long as the numerator is less than the denominator, we'll do this loop
        if b % i == 0:  # if the test number is divisible evenly by the numerator, it's not a prime
            prime = False  # change the flag
            break  # and break the loop
        else:  # otherwise,
            i += 1  # add one to the numerator, and loop again
    if prime:  # if it's made it all the way through, it's a prime number
        primeList.append(b)  # add it to the list of primes
    # now we add the next number to be tested to the end of the list
    baseList.append(b+1)

# we now have a long list of prime numbers. let's print them out.
print(primeList)

