 
 A straightforward way to do this is to use a stack data structure. 
 A stack is a linear data structure which follows a particular order in which the
 operations are performed. The order may be LIFO(Last In First Out) or 
 FILO(First In Last Out). 
 Here we can use LIFO. We add the opening brackets to the stack (in this case a list), and if a closing side is found,  we remove the opening side from the stack. If you ever see a closing bracket/ parenth that doesnt have a left side in the stack, we will know that it is an invalid expression. What about ([)]? It is invalid, but each closing bracket
 has a corresponding bracket in the stack. 

 Well, remember that a stack depends on following a particular order. 
 If we find a closing bracket, the bracket at the top/end of the stack HAS
 to be the opening bracket of that same type. Otherwise, it is invalid. 

 For example, if we have a string like (([{}])), we will get a stack looks like 
 this before we start removing the items from the stack: 

 "(([{"


The first closing bracket is "}", which matches the last bracket. So, 
we remove "{" from the stack. The next closing bracket is "]",
which matches the now last bracket in the stack "[". We remove that and continue 
this process until we get to the end of the string.  

For a string like ([)], we would get to the closing bracket ")" first. Our stack
would at that point be: "([". 
Because ")" doesnt match the closing braket at the top of the stack ("[",), 
it would be an invalid string. 

The other instance that the string would be invalid would be in the case where
there were more opening brackets than closing brackets. After iterating through 
the string and adding to the stack, if the stack is anything but empty, we have 
an invalid use of parentheses/brackets. 





