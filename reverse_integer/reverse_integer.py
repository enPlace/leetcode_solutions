
"""Given a signed 32-bit integer x, return x with its digits reversed. If reversing 
x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then 
return 0. Assume the environment does not allow you to store 64-bit integers (signed or unsigned)."""


#Solution 1: turning int into reversed string. If it is a negative number, I have to 
#remove the '-' sign from the string and make the integer  of the string negative again
#after reversing it. 
def reverse(num):
	x = str(num)[::-1]
	if num<0:
		if -int(x.replace('-', ''))>=(-2**31):
			return -int(x.replace('-', ''))
	elif int(x) <= 2**31 -1: 
		return int(x)
	return 0

print(reverse(-123450))


#Soluiton 2: Using the % operand to get the last digit of the number. The code is a bit longer 
#here as I have to do the reversing by hand (instead of using [::-1]). 
#We still have to write an extra case for negative numbers, and make the result negative
#after reversing the digits. 

def reverse1(num):
	x = num
	reverse = 0
	while num !=0:
		if num <0: 
			num = num*-1
		reverse += num%10
		num = num//10
		reverse = reverse*10
	reverse = int(reverse/10)
	if x <0: 
		if -2**31 <= reverse*1:
			return reverse*-1
		return 0

	if reverse<= 2**31 - 1: 
		return reverse

	return 0

print(reverse1(-12))

