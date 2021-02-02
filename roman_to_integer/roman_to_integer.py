"""Given a roman numeral, convert it to an integer."""

#One way to do this is to create special rules for instances where 
#subtraction is used after adding all of the individual numerals of 
#the string. 
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

#another way to do it is to add the subtraction numerals 
#to the dict, iterate through every pair of numerals in 
#the list, and subract if it finds a subtraction pair, like "IV". 
#Then iterate through the list again and add each 
#numeral up. Cleaner code, but a benifit to doing it 
#the first way is that if the numeral is written incorrectly, like
#"IIV," we would still get the number "3" as a result. 