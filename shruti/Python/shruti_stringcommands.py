#################### STRING METHODS ##############################
str = "Hello my name is Shruti 1001"
txt = "H\te\tl\tl\to"

#capitalize() - converts first character to uppercase
print("String with first letter capital:",str.capitalize())

#casefold() - converts string in lowercase
print("String in lower case:",str.casefold())

#center() - returns a centered string
print("centered string:",str.center(30,'*'))

#count() - returns the no of times a specified value occurs
print("Value of my in string:",str.count("my"))

#encode() - returns an encoded version of string
print("encoded string:",str.encode(encoding="ascii",errors="backslashreplace"))

#endswith() - returns true if string ends with a specified value
print("the answer is:",str.endswith("1"))

#expandtabs() - set tab size of string
x=txt.expandtabs(2)
print("using xpandtabs():",x)

#find - searches string for a specified value and returns position where it was found
print("found the string at:",txt.find("l"))

#format() - allows use of simple placeholders for formatting
print("Hello {}, your age is {}.".format("Shruti",20))


#format_map() - takes a single argument mapping(dictionary)
point = {'x':4,'y':-5}
print('{x} {y}'.format_map(point))

#index() - searches string for a specified value and returns its position
print("index of value:",str.index("n"))

#isalnum() - returns true if chars are alphanumeric
print("is string alnum:",str.isalnum())

#isalpha() - returns true if chars are in alphabet
print("is string alpha:",str.isalpha())

#isdecimal() - returns true if chars are in decimal
print("is string decimal",txt.isdecimal())

#isdigit() - returns true if chars are digits
print("is string in digits:",txt.isdigit())

#isidentifier() - returns true if string is identifier
print("is string identifier:",str.isidentifier())

#islower() - returns true if chars are lowercase
print("are chars lowercase:",txt.islower())

#isnumeric() - returns true if string is numeric
print("is string in numeric:",str.isnumeric())

#isprintable() - returns true if string is printable
print("is string printable:",str.isprintable())

#isspace() - true id all srings are whitespaces
print("are all whitespaces:",str.isspace())

#istitle() - returns true if string follows title rules
print("does string follow title rules:",str.istitle())


#isupper() - true if all chars are uppercase
print("are all chars uppercase:",str.isupper())

#join() - joins two strings
x=str.join(txt)
print("joined string:",x)

#ljust() - returns left justified version of string
text = "Mango"
y=text.ljust(20)
print(y,"is my fav fruit")

#lower() - converts string in lowercase
print(y.lower())


#lstrip() - removes leading characters
text1 = "    banana    "
c=text1.lstrip()
print("of all fruits",x,"is my fav")


#maketrans() - creates a unicode representation of each char
dict={"a":"123","b":"456","c":"789"}
string = "abc"
print(string.maketrans(dict))

#partition() - splits a string into three parts
a="I could eat bananas all day"
n=a.partition("bananas")
print("Partitioned string:",n)

#replace() - replace a specified value with another
print("replaced string:",a.replace("bananas","mango"))


#rfind() - finds last occurrence of specified value
print("last index of value:",str.rfind("i"))


#rindex() - finds last occurrence of specified value
print("last index of value,use of rindex():",str.rindex("i"))

#rpartition() - searches for last occurrence of string and splits into tuple containing three elements
b="I could eat bananas all day, bananas are my fav fruit."
print("text into parts:",b.rpartition("bananas"))


#rsplit() -  split a string into list starting from right
dic = "apple,banana,cherry"
print(dic.rsplit(" , "))


#rstrip() - removes spaces to the right of string
print("used rstrip():",text1.rstrip(),"here")


#split() - splits string in a list
foo = "welcome to jungle"
print(foo.split())


#splitlines() - split string into list, splitting is done at line breaks
text2 = "Thanks for music\nWelcome to jungle"
print(text2.splitlines())


#startswith() - true if string starts with the specified value
print("is it true:",str.startswith("e"))

#swapcase() - swap cases,lower case becomes upper and vice versa
print("HELOO i am Happy".swapcase())

#title() - converts first char of each word to uppercase
print(str.title())


#translate() - returns string where each char is mapped to corresponding char as per the translation table
firstString = "abc"
secondString = "ghi"
thirdString = "ab"
string1 = "abcdef"
print("Original string:", string1)
translation = string1.maketrans(firstString, secondString, thirdString)
print("Translated string:", string1.translate(translation))

#upper() - converts string in uppercase
print(string1.upper())

#zfill() - adds zeros at beginning of the string until it reaches specified length
print(txt.zfill(15))
