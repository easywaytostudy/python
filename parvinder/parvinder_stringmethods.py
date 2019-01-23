str='  parvinder singh  '
str1='parvinder'
print(str1.capitalize())     	 #first letter will be capital 
print('---------------------------------------------------------------------')
print(str1.center(10))       	 #it will add 10 spaces at first and last to the string like= '          parvinder          '
print('---------------------------------------------------------------------')
str2='past is past cant be future'
print(str2.count("past"))      	 #it will count that how many times 'ka' is repeated in the string
print('---------------------------------------------------------------------')
print(str2.endswith('.'))	 #it checks that the string is ends with '.' if yes it give true otherwise false
print('---------------------------------------------------------------------')
str3='h\te\tl\tl\to'
print(str3.expandtabs(2))	 #it will generate tabs instead of \t and gives 2 spaces at every tab as assigned in its parameter
print('---------------------------------------------------------------------')
print(str2.find("past"))	     	 #it finds the positi of 'ka' in string
print('---------------------------------------------------------------------')
print(str2.index("past"))		 #it will finds th position of 'ka' in the string
print('---------------------------------------------------------------------')
print(str2.isalnum())		 #it returns true if string contains alphanumeric items like 0-9 and a-z and false if string contains !@#$%^& type of symbols
print('---------------------------------------------------------------------')
str4='parvinder singh'
print(str4.isalpha())		 #it returns true if string contains only alphabets otherwise it returns false
print('---------------------------------------------------------------------')
str5='7'
print(str4.isdigit())		 #return true if all characters in string are digits else it returns false
print('---------------------------------------------------------------------')
print(str4.islower())		 #return true if all characters in string in lower case else returns false
print('---------------------------------------------------------------------')
print(str4.isupper())		 #return true if all characters in string in upper case else returns false

print('---------------------------------------------------------------------')
print(str2.isspace())		 #return true if string contains only space else return false
print('---------------------------------------------------------------------')
print(str2.istitle())		 #return true if first character of every word in string is in upper case else return false
print('---------------------------------------------------------------------')
str6=('a','b','c','d','e')
print("_".join(str6))		 #it joins all items into single string by underscores
print('---------------------------------------------------------------------')
print(str1.ljust(10))		 #it add number of spaces at the last of the string
print('---------------------------------------------------------------------')
print(str1.lower())			 #it return string in lower case
print('---------------------------------------------------------------------')
print(str1.lstrip())		 #it remove all spaces present at starting of string
print('---------------------------------------------------------------------')
print(str1.rstrip())		 #it remove all spaces present at last of the string
print('---------------------------------------------------------------------')
print(str2.partition("past"))	 #it divide string into 3 parts main selected part,part before selected part , and part after selected part
print(str4.replace('p','P')) 	 #it replace the particular part of string with desired part
print(str2.rfind('p'))		 #if finds position of particular part of string from right side
print(str2.rpartition('past')) 	 #it parts the string from right side
print(str2.split(" "))		 #it spits the string when space arises
str7='parvinder\nsingh'
print(str7.splitlines())	 #it splits the string into different stings when \n is used
print(str7.startswith("p"))  	 #return true if string started with assigned characted else return false
print(str7.swapcase())		 #it swaps lower case into upper case and upper case to lower case
print(str2.title())  		 #Converts the first character of each word to upper case
print(str2.upper())			 #converts the whole srting into upper case
print(str5.zfill(10))		 #it adds zeros in the biinning of string and make length of string as assigned

	
