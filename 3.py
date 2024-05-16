"""
Valid parantheses problem

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid. 
An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

"""

def isValid(s):
    stk = []
    pairs = {')':'(', '}':'{', ']':'['}
    
    for c in s:
        if c in pairs.values():
            if not stk or stk.pop() != pairs[c]:
                return False
        elif c in pairs.values():
            stk.append(c)
    
    return not stk

auto = input("Do you want to run the predefined test cases? (Y/n) : ")
if not auto or auto == 'Y' or auto == 'y':
    testCases = ["()", "()[]{}", "(]", "([)]", "{[]}", "([)]",]
    for tc in testCases:
        if isValid(tc):
            print(f"{tc} : Valid parantheses")
        else:
            print(f"{tc} : Invalid parantheses")
else:
    ip = input("Enter a string containing parantheses : ")
    if isValid(ip):
        print("Valid parantheses")
    else:
        print("Invalid parantheses")