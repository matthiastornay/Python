# Q1 :

def divisor(n):
    divisor = []
    for i in range(1, n):
        if n%i == 0:
            divisor.append(i)
    print(divisor)
    print(len(divisor))

# Q2 :

divisor(60)
# => 11

divisor(100)
# => 8

# Q3 :

def sumdivision(n):
    sum=0
    for i in range(1, n):
        if n%i == 0:
            sum += i
    return sum


# Q4 :

nbperfect=[]
for n in range(1, 1000):
##    sum = 0
##    for i in range(1, n):
##        if n%i == 0:
##            sum += i   OR -> (below)
    sum = sumdivision(n)
    if n == sum:
        nbperfect.append(n)
print(nbperfect)
