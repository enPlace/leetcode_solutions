"""Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string """

# test strings: 
string1= ["flower", "flo", "float", "flow rider", "flopple", "floximationsynth"]
string2= ["aa", "ab"]
string3 = ["aa", "apple", "ab"]
string4 = ["a", "b"]
string5 =[]


"""
One way to do this is to take the shortest string and work backwards, removing the last 
item in the string until we find a common prefix: 

*if empty string, return "". Otherwise: 
1. sort the list by length
2. check to see if the shortest string is a prefix for the rest 
   of the strings.
3. if yes, the shortest string is the answer
4. if no, take the last item off the shortest string
5. repeat until we get a result. 
6. if there are no common prefixes, return an empty string. 

"""
def longestCommonPrefix(strs): 
    answer =""
    if len(strs)==0: 
        return answer
    count = 0
    short = sorted(strs, key=len)[0]
    while len(short) != 0: 
        for i in strs: 
            if i[0:len(short)] == short: 
                count +=1
        if count == len(strs): 
            answer = short
            break
        else: 
            count = 0
            short = short[:-1]
    return answer


print(longestCommonPrefix(string1))
print(longestCommonPrefix(string2))
print(longestCommonPrefix(string3))
print(longestCommonPrefix(string4))
print(longestCommonPrefix(string5))


