"""
-Given an integer x, return true if x is palindrome integer.

-An integer is a palindrome when it reads the same backward as 
forward. For example, 121 is palindrome while 123 is not.
"""

def isPalindrome(x): 
	if -2**31 <= x <= 2**31 - 1: 
		if str(x) == str(x)[::-1]: 
			return True
	return False



#Follow up: 
#Can you do it without converting the number into a string?