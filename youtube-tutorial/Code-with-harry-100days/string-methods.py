# String Concatination
a = 'Raj'
b = 'Rishu'
c = a+b     # both are in string so we can concatinate with + symbol
d = a + ' ' + b
print(c)
print(d)

# String Repetation
print(d*3)

# Accessing Character 
    # it is through indexing and each will represents one character
print(a[1])

# String Slicing
    # this is also done through indexing 
text = "Python Programming"
print(text[0:6])   # Output: Python
print(text[7:])    # Output: Programming
print(text[:6])    # Output: Python

# String Length
    # it returns the length of the string i.e counting character by character here 
print(len(c))

# String Case Conversion
text1 = "hello world"
print(text1.upper())      # Output: HELLO WORLD
print(text1.lower())      # Output: hello world
print(text1.capitalize()) # Output: Hello world
print(text1.title())      # Output: Hello World

# Strip whitespace or any other character
    # if it is any other character then it will be like something ::::::::> strip("!"), whitespace is default
text2 = "   Hello World   "
print(text2.strip())  # Output: Hello World                      # removes from both side
print(text2.lstrip(), 'hi') # Output: Hello World    hi          # removes left side only
print(text2.rstrip()) # Output:    Hello World                   # removes from right side only

# Sting Spliting
    # character which we specify within split we need to mention with " " or ''
    # and it will return a list as a output.
text3 = "apple,banana,cherry"
print(text3.split(","))  # Output: ['apple', 'banana', 'cherry']
# Sting Joining
# format delimiter.joins(literals)
# here delimiter refers to a string or 
fruits = ['apple', 'banana', 'cherry']
result = ", ".join(fruits)
print(result)  # Output: apple, banana, cherry
animal = ['cow', 'goat', 'dog']
result = animal[0].join(fruits)
print(result)
print(type(result))

mixed = ['apple', 42, 'cherry']
result = ", ".join(map(str, mixed))
print(result)  # Output: apple, 42, cherry

# Finding substring
    # find(): Returns the index of the first occurrence. and if dosen't find this will return -1
    # index(): Same as find() but raises an exception if not found.
    # it will return the first index where it finds 
text = "Hello World"
print(text.find("!"))  # Output: 6
print(text.index("World")) # Output: 6

# Replacing sub string
    # first literal will be which we want to replace and 2nd literal will be what we want to keep
text = "I love apples"
result = text.replace("apples", "bananas")
print(result)  # Output: I love bananas

# Checking String Content mean checking beg or end with specific str or character
text = "Hello World"
print(text.startswith("Hello")) # Output: True
print(text.endswith("World"))   # Output: True

# Counting Substrings
    # it checks for str or character
text = "banana"
print(text.count("a"))  # Output: 3

# String Alignment
    # if we specify n for alignment then that will include character of that string and it will be like alignment-len(str) / 2 then it will divide those spaces on each side.
text = "Hello"
print(text.center(10))  # Output: '  Hello   '
print(text.ljust(10))   # Output: 'Hello     '
print(text.rjust(10))   # Output: '     Hello'

# Checking String Properties
    # it return True/False
text = "Python"
print(text.isalpha())  # Output: True
print("123".isdigit()) # Output: True
print("123abc".isalnum()) # Output: True
print("   ".isspace())   # Output: True

# String Formatting
    # uses %
name = "Alice"
age = 25
print("My name is %s and I am %d years old" % (name, age))
print("My name is {} and I am {} years old".format(name, age))
print(f"My name is {name} and I am {age} years old")

# Reverse a String
text = "Python"
print(text[::-1])  # Output: nohtyP

# Case Folding
    # Symbols (@, #, !) and emojis remain unchanged.
    # casefold() is a robust tool for normalizing strings for case-insensitive comparisons, especially when working with international text or complex Unicode strings. If your application needs to handle text in multiple languages, always prefer casefold() over lower() for accurate comparisons.
str1 = "Straße"
str2 = "strasse"
print(str1.casefold() == str2.casefold())  # Output: True

# Checking for Substrings
    # in: Checks if a substring exists in a string.
text = "Hello World"
print("World" in text)  # Output: True
print("Python" in text) # Output: False

# Encoding and Decoding
    # encode(): Encodes the string into bytes.
    # decode(): Decodes bytes back into a string.
text = "Hello"
encoded = text.encode("utf-8")
print(encoded)  # Output: b'Hello'
decoded = encoded.decode("utf-8")
print(decoded)  # Output: Hello

# Checking String Patterns
    # isdecimal(): Checks if all characters are decimal.
    # isnumeric(): Checks if all characters are numeric.
text = "12345"
print(text.isdecimal())  # Output: True
print(text.isnumeric())  # Output: True

# Expanding Tabs
    # Replaces tabs (\t) with spaces.
text = "Hello\tWorld"
print(text.expandtabs(4))  # Output: Hello   World

# Partitioning
    # partition(): Splits the string at the first occurrence of the separator into a tuple.
    # rpartition(): Splits from the rightmost occurrence. this also do the samething but from right side
    # splits the string into tuple of 3 parts 1. one before that part of string 2. that part of string 3. rest part of the string 
    # it will always consider the last occurance for splitting
text = "I love Python and I love coding"
result = text.rpartition("love")
print(result)  # Output: ('I love Python and I ', 'love', ' coding') 


# Splitting by Lines
    # Splits the string by line breaks.
text = "Hello\nWorld"
print(text.splitlines())  # Output: ['Hello', 'World']

# Checking Identifier Validity
    # Checks if the string is a valid Python identifier.
text = "variable_name"
print(text.isidentifier())  # Output: True
print("123name".isidentifier()) # Output: False

# Formatting Strings
    # Pads the string with zeros on the left. (this is also character based i.e if we specify 5 it will add upto 5 zero depending upon the size of the string and if the size of the string is more it won't make any changes )
text = "42"
print(text.zfill(5))  # Output: 00042

# Removing Specific Characters
text = "unbelievable"
print(text.removeprefix("un"))  # Output: believable
print(text.removesuffix("able")) # Output: unbeliev

# Checking Printable Characters
    # Checks if all characters are printable.
text = "Hello\nWorld"
print(text.isprintable())  # Output: False

# Swapping Case
    #swapcase(): Converts uppercase to lowercase and vice versa.
text = "Hello World"
print(text.swapcase())  # Output: hELLO wORLD   

# Formatting Tabs
    #expandtabs(): Replaces tabs (\t) with spaces.
text = "Hello\tWorld"
print(text.expandtabs(4))  # Output: Hello   World

# Check Unicode Type
text = "Hello"
print(text.isascii())  # Output: True

# Complex Matching
import re
text = "The rain in Spain"
result = re.findall(r"\bS\w+", text)
print(result)  # Output: ['Spain']