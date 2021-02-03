"""Given a roman numeral, convert it to an integer."""

# One way to do this is to create special rules for instances where 
# subtraction is used after adding all of the individual numerals of 
# the string. 
def romanToInt(s):
        numerals = {"I": 1, "V": 5, "X":10, "L":50, "C":100, "D": 500, "M": 1000}
        answer = 0
        if 1<= len(s) <=15:
            for i in s:
                answer += numerals[i]
            if "IV"  in s: 
                answer -=2
            if "IX"  in s: 
                answer -=2
            if "XL" in s: 
                answer-=20
            if "XC" in s: 
                answer-=20
            if "CD" in s: 
                answer-=200
            if "CM" in s: 
                answer-=200
        return answer

print(romanToInt("IV"))
print(romanToInt("III"))
print(romanToInt("IX"))
print(romanToInt("LVIII"))
print(romanToInt("MCMXCIV"))
print(romanToInt("IVIV"))

#A simpler, cleaner way to do it would be to add another dictionary with those special 
#2-letter numerals, with a negative number for each value. You could iterate 
#through the numeral and subtract if it finds any instances of the 2-letter numeral. This is
# assuming that the roman numeral is written correctly. If it is, any 2-letter numeral would
# only occur once. 
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
print(romanToInt("IVIV"))


