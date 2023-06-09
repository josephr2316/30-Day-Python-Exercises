# 1.Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
string_a = "Thirty " + "Days " + "Of " + "Python"
print(string_a)

# 2.Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
string_b = "Coding " + "For " + "All"
print(string_b)

# 3.Declare a variable named company and assign it to an initial value "Coding For All".
company = "Coding For All"

# 4.Print the variable company using print().
print(company)

# 5.Print the length of the company string using len() method and print().
print(len(company))

# 6.Change all the characters to uppercase letters using upper() method.
print(company.upper())

# 7.Change all the characters to lowercase letters using lower() method.
print(company.lower())

# 8. Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
print(company.capitalize())
print(company.title())
print(company.swapcase())

# 9.Cut(slice) out the first word of Coding For All string.
print(company[7:])

# 10.Check if Coding For All string contains a word Coding using the method index, find or other methods.
if company.find("Coding") != -1:
    print("Found!!!")
else:
    print("No found")

# 11.Replace the word coding in the string 'Coding For All' to Python.
print(company.replace("Coding", "Python"))

# 12. Change Python for Everyone to Python for All using the replace method or other methods.
company_b = "Python for Everyone"
print(company_b)
print(company_b.replace("Everyone", "All"))

# 13.Split the string 'Coding For All' using space as the separator (split()) 
print(company.split(" "))

# 14."Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
string_c = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(string_c.split(","))

# 15.What is the character at index 0 in the string Coding For All.
print(company[0])

# 16.What is the last index of the string Coding For All.
print(company[len(company)-1])

# 17.What character is at index 10 in "Coding For All" string.
print(company[10])

# 18.Create an acronym or an abbreviation for the name 'Python For Everyone'.
split = 'Python For Everyone'.split(" ")
new_word = ""
for word in split:
    new_word += word[0]
print(new_word)

# 19.Create an acronym or an abbreviation for the name 'Coding For All'.
split = 'Coding For All'.split(" ")
new_word = ""
for word in split:
    new_word += word[0]
print(new_word)

# 20.Use index to determine the position of the first occurrence of C in Coding For All.
word = "Coding For All"
print(word.index('C'))

# 21.Use index to determine the position of the first occurrence of F in Coding For All.
print(word.index('F'))

# 22.Use rfind to determine the position of the last occurrence of l in Coding For All People.
word = 'Coding For All People'
print(word.rindex('l'))

# 23.Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
word = 'You cannot end a sentence with because because because is a conjunction'
print(word.index('because'))
print(word.find('because'))

# 24.Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print(word.rindex('because'))
print(word.rfind('because'))

# 25.Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print(word.replace(" because", ""))

# 26.Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print(word.find('because'))

# 27.Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print(word.replace(" because", ""))

# 28.Does ''Coding For All' start with a substring Coding?
word = 'Coding For All'
print(word.startswith('Coding'))

# 29.Does 'Coding For All' end with a substring coding?
print(word.endswith('coding'))

# 30.'   Coding For All      '  , remove the left and right trailing spaces in the given string.
word = '   Coding For All      '
word = word.removeprefix(" " * 3)
word = word.removesuffix(" " * 6)
print(word)
word = '   Coding For All      '
print(word.strip())
print(word.strip(" "))

# 31.Which one of the following variables return True when we use the method isidentifier():
# 30DaysOfPython
# thirty_days_of_python
print('30DaysOfPython'.isidentifier())
print('thirty_days_of_python'.isidentifier())

# 32.The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
libraries = "# ".join(libraries)
print(libraries)

# 33. Use the new line escape sequence to separate the following sentences.
# I am enjoying this challenge.
# I just wonder what is next.
print("I am enjoying this challenge.\nI just wonder what is next.")

# 34.Use a tab escape sequence to write the following lines.
# Name      Age     Country   City
# Asabeneh  250     Finland   Helsinki
print ("Name\t        Age\tCountry\t    City")
print("Asabeneh\t250\tFinland\t    Helsinki")

# 35.Use the string formatting method to display the following:
# radius = 10
# area = 3.14 * radius ** 2
# The area of a circle with radius 10 is 314 meters square.
radius = 10
area = 3.14 * radius ** 2
print("The area of a circle with radius {} is {} meters square.".format(radius,int(area)))

# 36.Make the following using string formatting methods:
# 8 + 6 = 14
# 8 - 6 = 2
# 8 * 6 = 48
# 8 / 6 = 1.33
# 8 % 6 = 2
# 8 // 6 = 1
# 8 ** 6 = 262144

a, b = 8, 6

print("{} + {} = {}".format(a, b, a + b))
print("{} - {} = {}".format(a, b, a - b))
print("{} * {} = {}".format(a, b, a * b))
print("{} / {} = {:0.2f}".format(a, b, a / b))
print("{} % {} = {}".format(a, b, a % b))
print("{} // {} = {}".format(a, b, a // b))
print("{} ** {} = {}".format(a, b, a ** b))
