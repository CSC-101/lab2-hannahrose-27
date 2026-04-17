def smallest(n:float, m:float) -> float:
    if n < m:
        return n #For which calls below is this statement evaluated? Neither are evaluated.
    else:
        return m

first = smallest(3, 2) #What is the value of first? first=2
second = smallest( 2, 2) #What is the value of second? second=2 Is this a reasonable result? No because 2 is not smaller than 2.
print (first, second)

def function2(a:int, b:int, c:int) -> int:
    if a > b and a > c:
        return a - b #In general, when will a call to this function evaluate this statement? A call will be evaluated when a is greater than b and c.
    elif b> c:
        return b + c #In general, when will a call to this function evaluate this statement? A call will evaluate this statement if b is greater than c.
    else:
        return 2 * c #In general, when will a call to this function evaluate this statement? A call will evaluate this statement when b is less than c.

answer1 = function2(3, 2, 1) #What is the value of answer1? answer1 = 1
answer2 = function2(2, 3, 1) #What is the value of answer2? answer2 = 4
answer3 = function2(2,1, 3) #What is the value of answer3? answer3 = 6
print(answer1, answer2, answer3)

