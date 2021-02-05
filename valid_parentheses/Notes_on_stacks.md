 
 Will be valid if: 
 We find each instance of opening and closing brackets/parenth that 
 occur next to each other and remove them. Repeat until the string is 0. 
 If we cannot make the string 0, it will be invalid. 

 How to do this without getting into an endless loop? that is, how to stop
 the loop when we get to a point where we cant remove any more brackets?
 One way to do it is by employing the counting method after each loop. If 
 it is ever negative we know that it cant be valid. 

 Another way to do this is to use a stack data structure. 
 Stack is a linear data structure which follows a particular order in which the
 operations are performed. The order may be LIFO(Last In First Out) or 
 FILO(First In Last Out). 
 So, you add the opening brackets to the stack, and if a closing side is found, 
 you remove the opening side from the stack. If you ever see a closing bracket/
 parenth that doesnt have a left side in the stack, we will know that it is 
 an invalid expression. What about ([)]?

 Well, remember that a stack depends on following a particular order. 
 If we find a closing bracket, the bracket at the top/end of the stack HAS
 to be the opening bracket of that same type. Otherwise, it is invalid. This works
 because we are only putting the opening brackets in the stack. 

So, if we have something like (([{}])), We will get a stack looks like this 
 before we start popping things off: 
 "(([{"
The first closing bracket is "}", which matches the last bracket. So, 
we remove "{" from the stack. The next closing bracket is "]",
which matches the now last bracket in the stack "[". We remove that and continue. 
and so on. 

For a string like ([)], we would get to the closing bracket ")" first. Our stack
would at that point be: "([". 
Because ")" doesnt match the closing braket at the top of the stack ("[",), 
it would be an invalid string. 



A counting algorithm for simply counting the brackets would look like this: 
def counting(s): 
    parcount = 0
    curlcount = 0
    brackcount = 0
    for i in s: 
        if i == "(":
            parcount += 1
        if i == ")": 
            parcount -=1
        if i == "[": 
            brackcount += 1
        if i == "]": 
            brackcount -= 1
        if i == "{": 
            curlcount += 1
        if i == "}": 
            curlcount -= 1
        if parcount <0 or curlcount<0 or brackcount<0: 
            return False
    if parcount ==0 and curlcount ==0 and brackcount ==0:
        return True
    
    else: 
        return False

This is quite a bit of code, and we can see by the stack method that this is 
quite a bit easier (and more efficient) than running multiple loops and counting
after each loop to see if any of our variables are negative. 


