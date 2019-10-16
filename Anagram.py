print ("TO FIND GIVEN STRING IS ANAGRAM OR NOT")
s1=str (input("enter a str1: "))
s2=str (input("enter a str2: "))
if sorted(s1)==sorted(s2):
	print("string is anagram")
else:
	print("string is not anagram")
print("bye")