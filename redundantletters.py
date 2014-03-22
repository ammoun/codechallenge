#!/usr/bin/env python
import string

#return true if all characters are ponctuations.
def isPonctuation(str):
	return all(x in string.punctuation for x in str)


def omitredundant(str):
	if not isPonctuation(str):
		candidates = [""]
		i= 0
		while i < len(str):	
			#There is triple or more of the same character
			if (i<len(str)-2 and str[i] == str[i+1] == str[i+2]): 
					
					#go through the list of candidates and add that letter to every entry
					for j,x in enumerate(candidates):
						candidates[j] += str[i]
					
					#make new entries for the double letter version	
					for j,x in enumerate(list(candidates)):
						candidates.append(candidates[j] + str[i])
					
					#advance the pointer of the string until it finds a different letter of the end of the string
					while (i < len(str) -1 and str[i] == str[i+1]):
						i += 1
			else:
				#single occurence just append it to all the elements of the list.
				for j,x in enumerate(candidates):
					candidates[j] += str[i] 
			
			i +=1
		return candidates
	
	#all characters are ponctuation
	else:
		return [str]	
		
	
print omitredundant("??????!!!!!!")
print omitredundant("Helllllllloooooooo")
