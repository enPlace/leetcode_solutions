
"""Given a signed 32-bit integer x, return x with its digits reversed. If reversing 
x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then 
return 0. Assume the environment does not allow you to store 64-bit integers (signed or unsigned)."""


#Solution 1: turning int into reversed string. If negative number, I have to 
#remove the '-' sign from the string and make the integer of the reversed 
#string negative at the end. 
def reverse(num):
        x = str(num)[::-1]
        if num<0:
            if -int(x.replace('-', ''))>=(-2**31):
                return -int(x.replace('-', ''))
        elif int(x) <= 2**31 -1: 
            return int(x)
        return 0

print(reverse(-123450))
##Solution 2: Using % operator to reverse the string. 
def reverse(num): 
	pass