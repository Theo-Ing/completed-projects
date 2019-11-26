fibonacci_cache = {}

def fib(n):
    if n in fibonacci_cache:
        return fibonacci_cache[n]
    elif n <= 2:
        return 1
    else:
        value = fib(n-1)+fib(n-2)
        fibonacci_cache[n] = value
        return value

def traingle_base_down(dist, width):
    if width <= 1:
        print(dist*" " + width*"*")
    else:
        print(dist*" " + width*"*")
        traingle_base_down(dist+1, width-2)

def traingle_base_up(dist, width):
    if width <= 1:
        print(dist*" " + width*"*")
    else:
        traingle_base_up(dist+1, width-2)
        print(dist*" " + width*"*")

def diamond(n):
    traingle_base_up(1,n-2)
    traingle_base_down(0,n)

def digit_sum(n):
    if n//10==0:
        return n
    return n%10 + digit_sum(n//10)

def sort_check(list):
    if len(list)<=1:
        return True
    return list[0]<=list[1] and sort_check(list[1:])

#print(fib(int(input("Fib n: "))))
#diamond(int(input("n: ")))
#print(digit_sum(int(input("n: "))))
#print(sort_check([1,2,2,4]))
