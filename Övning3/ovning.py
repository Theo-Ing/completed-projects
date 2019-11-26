def digitSum():
    sum = 0
    numbers = 0
    print("Write your numbers, press enter without a number when the last number has been given.")
    while True:
        x = input("Next number: ")
        if x == "":
            break
        sum += float(x)
        numbers += 1
    print("The sum of the given numbers were:", round(sum/numbers,2))

def factorial(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    return n*factorial(n-1)

def sin(x):
    sum = term = x
    lim = 1e-10
    k = 1
    sign = 1
    while abs(term) > lim:
        k += 2
        sign *= -1
        term = term*x*x/k/(k-1)
        sum += sign*term
    return round(sum,5)

def semiFac(n):
    if n <= 2:
        return n
    return n*semiFac(n-2)

def gender(psn):
    if len(psn) != 11:
        return "Invalid input, please use format YYMMDD-XXXX. Thank you."
    odd = "13579"
    if psn[9] in odd:
        return "Male"
    return "Female"

def reverseOrder(str):
    array = str.split()
    length = len(array)
    for i in range (0, length//2):
        temp = array[i]
        array[i] = array[length-1-i]
        array[length-1-i] = temp
    return " ".join(array)

def yearsSinceStart(start, year):
    length = len(start)
    y = int(start[length-2:length])
    if y > year%100:
        return year - (1900+y)
    return year - (2000+y)

def commonDenom(x, y):
    if x == y:
        return x
    a = max(x,y)
    b = min(x,y)
    if b == 0:
        return a
    else:
        return commonDenom(b, a%b)

print(sin(float(input("sin(x), x= "))))
#print(semiFac(int(input("n = "))))
#print(gender(input("Personal id (YYMMDD-XXXX): ")))
#print(reverseOrder(input("String that should be reversed: ")))
#print(yearsSinceStart(input("Class-code: "), int(input("Current year: "))))
#print("Highest common denominator:", commonDenom(int(input("First integer: ")), int(input("Second integer: "))))
