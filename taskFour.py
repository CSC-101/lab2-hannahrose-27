from typing import Optional #Gain access to the Optional[x] type hint

def checked_access(L:list[int], idx:int) -> Optional[int]:
    test = idx >= 0 and idx < len(L) # What is the value of test on each call?  False for the first call and True for second call
    if test: #What is this check preventing? It prevents returning an index value that is greater than the length of the list.
        return L[idx]
    else:
        return None

first = checked_access([1,0, 1], 9) #What is the value of first? first = None
second = checked_access([1, 0, 1], 2) #What is the value of second? second = 1
print(first, second)

def length_sum(L:list[str]) -> int:
    if len(L) > 2:
        result = len(L[0]) + len(L[1]) + len(L[2]) #For which call below is the statement evaluated? First call
    elif len(L) > 1: #And what are the values being added? 4 + 2 + 3
        result = len(L[0]) + len(L[1]) # For which call below is this statement being evaluated? Third call
    elif len(L) > 0: # And what are the values being added? 7 + 4
        result = len(L[0]) # For which call below is the statement evaluated? Second call
    else: # And what are the values being added? 11
        result = 0
    return result

first = length_sum(["this", "is", "the", "first", "call"])
second = length_sum(["second call"])
third = length_sum(["another", "call"])
print(first, second, third)

def surprising(L:list[str], other:str) -> list[str]:
    L.append(other.upper())
    return L

words = ["this", "is", "confusing", "code."]
first = surprising(words, "Avoid")
second = surprising(words, "such.")
         # What is the value of words at this point? words = ["this" , "is" , "confusing" , "code." , "AVOID" , "SUCH."]
         # What are the values of first and second at this point? first = ["this" , "is" , "confusing" , "code." , "AVOID" , "SUCH."] second = ["this" , "is" , "confusing" , "code." , "AVOID" , "SUCH."]
         # What happened? The surprising function added "Avoid" and "such." to the end of the list, and the upper function made them fully uppercase.
print(first, second)



