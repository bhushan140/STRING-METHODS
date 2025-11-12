# case conversion
# conver 'hello world' to lowercase

string = 'Hello World'
print(string.lower())

# convert to uppercase

string2 = 'python is FUN'
print(string2.upper())

# capitalize the first letter

string3 = 'welcome to bengaluru'
print(string3.capitalize())

# searching and counting
#counting 'a'

print('banana'.count('a'))

# to check given string in string

cstr = 'data science is cool'
print(cstr.find('data'))

# to find index

fstr = 'hello'
print(fstr.index('o'))

# replacing and modifying

rstr = 'i love java'
print(rstr.replace('java','python'))

# to remove space using replace()

rstr2 = 'a b c d'
print(rstr2.replace(' ',''))

# to replace vowels with(*)

vstr = 'education'
vowels = 'aeiou'
for v in vowels:
    vstr =(vstr.replace(v,'*'))
print(vstr)

# splittin and join
# split
spstr = 'apple,banana,grape'
print(spstr.split(','))

#join

jstr = ['a','b','c']
print('-'.join(jstr))

# trimming and formatting
# remove spaces

sstr = ' hello '
print(sstr.rstrip())

# zfill()

print('43'.zfill(5))

# center the string

cnstr = 'python'
print(cnstr.center(20).replace(' ','*'))

# case and identity
#- Check if "Python" is in uppercase using .isupper()

pstr = 'Python'
print(pstr.isupper())

#- Convert "HELLO" to lowercase and check if it equals "hello"

hstr = 'HELLO'
lhstr = hstr.lower()
print (lhstr == 'hello')

#- Use .title() to convert "machine learning is fun" to "Machine Learning Is Fun".

tstr = 'machine learning is fum' 
print(tstr.title())

# validation and checks
#- Check if "12345" is all digits using .isdigit().

vdig = '1234'
print(vdig.isdigit())

#- Check if "hello123" is alphanumeric using .isalnum()

hdig = 'hello123'
print(hdig.isalnum())

#- Check if " " is a space using .isspace()

space = 'i am'
print(space.replace(space,'   ').isspace())

# slicing and indexing
#- Extract the first 3 characters of "Bengaluru"

bstr = 'bengaluru'
print(bstr[:3])

#- Get the last character of "Python" using negative indexing

pstri = 'python'
print(pstri[-1])

#- Print every second character of "abcdefg" using slicing.

astr = 'abcdefg'
print(astr[1::2])

# advanced replace and format
#- Replace all spaces in "data science rocks" with underscores.

dastr = 'data science rocks'
print(dastr.title().replace(' ','_'))

#- Format "My name is {}" with "Bhushan" using .format().

name = 'bhushan'
name2 = 'dhanush'
ftext = 'my name is {} and {} {}'.format(name,1,{8})
print(ftext)

#- Replace only the first occurrence of 'a' in "banana" using .replace() with count=1

rstr = 'banana'
print(rstr.replace('a','*',1))

# strip and pad
#- Strip "#" from both ends of "###hello###" using .strip().

hasstr = '##hello###'
print(hasstr.strip('#'))

#- Left-justify "Python" in 15 spaces using .ljust().

ptext = 'python'
print(ptext.ljust(12,'*'))

#- Right-justify "Python" in 15 spaces using .rjust().

ptext = 'python'
print(ptext.rjust(20,'-'))
print(ptext.center(20,'_'))

#- Extract the last 4 characters of "Cybersecurity".

ctext = 'cybersecurity'
print(ctext[-4:])

#- Slice "OperatingSystem" to get "System".

otext = 'operatingsystem'
inotext = otext.find('system')
print(otext[inotext:])

#- Print every third character of "PythonProgramming".

ppromt = 'PythonProgramming'
print(ppromt[::3])

#- Check if "hello" starts with 'h' using .startswith()

htext = 'hello'
print(htext.startswith('h'))
print(htext.endswith('o'))

#- Replace all vowels in "Copilot" with #

cpromt = 'Copliot'
for i in cpromt:
    if i.lower() in 'aeiou':
       cpromt=cpromt.replace(i,'#')
print(cpromt)        

#- Replace spaces in "OS and Security" with -.

os = 'os and security'
print(os.replace(' ','_'))

#- Replace "Security" with "Defense" in "Cyber Security".

cs = 'Cyber Security'
print(cs.replace('Security','defense'))

#- Split "OS,Python,Cybersecurity" into a list.

bstr = 'OS,Python,Cybersecurity'
print(bstr.split(','))

#- Join ['OS', 'Python', 'Cybersecurity'] into "OS | Python | Cybersecurity" using .join().

jostr =['OS', 'Python', 'Cybersecurity']
print('|'.join(jostr))

#- Count how many words are in "Python is powerful" using .split()

costr ='Python is powerful'
count = costr.split()
print(len(count))

#- Strip * from "***Python***" using .strip("*").

strip = '***Python***'
print(strip.strip('*'))

# - Pad "42" to "0042" using .zfill(4)

pad = '42'
print(pad.zfill(4))

#- Center "Cyber" in 30 spaces using .center() with = as fill character

centext = 'cyber'
print(centext.center(20,'='))

#- Find the position of "gram" in "Programming" using .find().

print('programming'.find('gram'))

#- Use .rfind() to locate the last occurrence of 'o' in "Copilot is cool".

print('copilot is cool'.rfind('o'))

#- Check if "Python" contains "th" using the in keyword.

print('th' in 'python')

#- Swap case of "PyThOn" using .swapcase().

print('PyThOn'.swapcase())

#- Count how many times 'o' appears in "Copilot is cool" using .count().

print('copilot is cool'.count('o'))

#- Count vowels in "Cybersecurity" using a loop and .count()

vtext = 'cybersecurity'
vowels= 'aeiou'
count =0

for v in vowels:
    count+=vtext.count(v)
print(count)

#- Count how many words are in "Python is fun and powerful" using .split().

pytext = 'python is fun and powerful'
print(pytext.split())

#- Format "Welcome, {}!" with "Bhushan" using .format().

fotext = 'welcome,{}!'
print(fotext.format('bhushan'))

#- Center "OS" in 10 spaces using .center() with * as fill

print('os'.center(20,'*'))

#- Pad "7" to "007" using .zfill(3).

print('7'.zfill(3))

#- Strip @ from "@@@hello@@@" using .strip("@").

print('@@@hello@@@'.strip('@'))

