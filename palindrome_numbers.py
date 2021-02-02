"""
-Given an integer x, return true if x is palindrome integer.

-An integer is a palindrome when it reads the same backward as 
forward. For example, 121 is palindrome while 123 is not.
"""

def isPalindrome(x): 
	if 0 <= x <= 2**31 - 1: 
		if str(x) == str(x)[::-1]: 
			return True
	return False



#Follow up: 
#Can you do it without converting the number into a string?
#Well first, any negative number cannot be a palindrome, as -121 -->121-
#We can use the % operand. 

def isPalindrome2(x):
	backwards = 0 
	original = x
	if 0 <= x <= 2**31 - 1: 
		while x !=0: 
			backwards += x%10
			x = x//10
			backwards *=10
		if original == backwards/10: 
			return True
	return False

print(isPalindrome2(-121))
