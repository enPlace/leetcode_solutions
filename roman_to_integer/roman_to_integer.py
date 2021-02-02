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