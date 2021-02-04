"""Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string """

# test strings: 
string1= ["flower", "flo", "float", "flow rider", "flopple", "floximationsynth"]
string2= ["aa", "ab"]
string3 = ["aa", "apple", "ab"]
string4 = ["a", "b"]
string5 =[]
string6 = ["flower","flow","flight"]
string7 = ["car", "cur", "cur"]


"""
One way to do this is to take the shortest string and work backwards, removing the last 
item in the shortest string until we find a common prefix: 

*if empty string, return "". Otherwise: 
1. sort the list by length
2. check to see if the shortest string is a prefix for the rest 
   of the strings.
3. if yes, the shortest string is the answer
4. if no, take the last item off the shortest string
5. repeat until we get a result. 
6. if there are no common prefixes, return an empty string. 

"""
def longestCommonPrefix (strs): 
    answer = ""
    if len(strs) ==0: 
        return answer
    short = sorted(strs, key=len)[0]
    count = 0
    for i in range(len(short)):
        for j in range(len(strs)): 
            if strs[j][i] == short[i]:
                count+=1
            if count == len(strs): 
                answer += short[i]
            if strs[j][i]!= short[i]: 
                return answer
        count = 0
            

    return answer


print(longestCommonPrefix(string1))
print(longestCommonPrefix(string2))
print(longestCommonPrefix(string3))
print(longestCommonPrefix(string4))
print(longestCommonPrefix(string6))
print(longestCommonPrefix(string7))


"""
--The other way to do this would be to work forwards. 
1. sort to get the shortest string. 
2. set up empty answer string.
3. iterate through the nth letter of each string in the list to see
   if it matches the nth letter of the shortest string. 
4. if it matches for each string, add that letter to the answer string. 
5. to ensure that it does not continue running after getting to a letter that does not
   match the nth letter of each string, we need to add a rule to stop it. Otherwise, we 
   would get an answer of "cr" for the strings "car" and "cur"
"""

def longestCommonPrefix (strs): 
    answer = ""
    if len(strs) ==0: 
        return answer
    short = sorted(strs, key=len)[0]
    count = 0
    for i in range(len(short)):
        for j in range(len(strs)): 
            if strs[j][i] == short[i]:
                count+=1
            if count == len(strs): 
                answer += short[i]
            if strs[j][i]!= short[i]: 
                return answer
        count = 0
            

    return answer

print(longestCommonPrefix(string1))
print(longestCommonPrefix(string2))
print(longestCommonPrefix(string3))
print(longestCommonPrefix(string4))
print(longestCommonPrefix(string6))
print(longestCommonPrefix(string7))




