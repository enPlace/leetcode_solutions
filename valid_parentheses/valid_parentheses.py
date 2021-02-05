"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
determine if the input string is valid.

"""



def isValid(s): 
    """uses a stack to check the validity of a string of brackets"""
    pardict = {"}":"{", "]":"[", ")":"("}
    stack = []
    for i in s: 
        if i == "(" or i=="[" or i =="{": #adds opening bracket to stack
            stack.append(i)
        if i == ")" or i =="]" or i =="}": 
            if len(stack) == 0 or stack[-1] != pardict[i]: #for closing bracket, checks if last item is matching opening bracket.
                return False
            else: 
                stack.pop() #removes last item in stack if closing bracket matches
    if len(stack)!=0: #if we have more opening than closing brackets, this will be the case.
        return False
    return True


s1= "()"
s2= "()[]{}"
s3= "(]"
s4= "([)]"
s5 ="{[]}"
s6 = "["

print(isValid(s1))
print(isValid(s2))
print(isValid(s3))
print(isValid(s4))
print(isValid(s5))
print(isValid(s6))