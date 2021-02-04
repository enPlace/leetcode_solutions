"""Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string """

 # My first thought was to take the shortest string, and check each string 
 # in the list to see if the first x letters of each string matched the shortest string. 
 # If not, take one letter off the end of the shortest string, and repeat the process.
 # If there is a common prefix, we  will arrive at it at some point. Otherwise, return 
 # an empty string. This doesn't work, however, if the lengths of all the words are 
 # the same. 

def longestCommonPrefix(string): 
	answer = ""
	count = 0
	ind = string.index(min(string, key=len))
	while len(string[ind]) != 0:
		for i in string: 
			if i[0: len(string[ind])] == string[ind]: 
				count+=1
		if count==len(string):
			answer = string[ind]
			break
		else: 
			count = 0
			string[ind]= string[ind].replace(string[ind][-1], "")

	return answer

print(longestCommonPrefix(string))
