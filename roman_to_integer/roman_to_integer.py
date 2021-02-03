"""Given a roman numeral, convert it to an integer."""



# A simple way to do this would be to add a dictionary with those special 2-letter numerals 
# (IV; IX; XL, etc), with a negative number for each value. After adding all the numeral values, 
# We can iterate through the numeral and subtract if our loop finds any instances of each 2-letter numeral. 
# This isassuming that the roman numeral is written correctly. If it is, any 2-letter numeral would
#  only occur once.
def romanToInt(s):
        numerals = {"I": 1, "V": 5, "X":10, "L":50, "C":100, "D": 500, "M": 1000}
        two_letter = {"IV": -2, "IX": -2, "XL": -20, "XC": -20, "CD": -200, "CM": -200}
        answer = 0
        if 1<= len(s) <=15:
            for i in s:
                answer += numerals[i]
            for key, value in two_letter.items(): 
                if key in s: 
                    answer += value 
            return answer



print(romanToInt("IV"))
print(romanToInt("IV"))
print(romanToInt("III"))
print(romanToInt("IX"))
print(romanToInt("LVIII"))
print(romanToInt("MCMXCIV"))



