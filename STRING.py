#string methods in python
# captilized method

msg = 'welcome to python'
print(msg.capitalize)

msg2 = 'hello world'
print(msg2.capitalize())

#upper()

string = 'hi there how are you'
string2 = 'hello am fyn'
print(string.upper())
print(string2.upper())

#lower()

print('WELCOME'.lower())
print('PYTHON'.lower())

#swapcase()

print('Hi WelcOMe To Python'.swapcase())
print('PyTHon'.swapcase())

#count()

strin = 'welcom to python python'
print(strin.count('o'))
print(strin.count('python'))
print(strin.count('o'))
print(strin.count('p'))
print(strin.count(' '))
print(strin.count('java'))

#index

promt = 'welcom to python'
print(promt.index('t'))
print(promt.index('t',8))
print(promt.index('wel'))
print(promt.index('to'))

# find

promt2 = 'welcom to python'
print(promt2.find('T'))
print(promt2.upper().find('T'))
print(promt2.find('o',7,100))

#rindex

promt3 = 'python python'
print(promt3.rindex('n'))
print(promt3.rindex('python'))
print(promt3.rindex('o',3,6))
print(promt3.rindex('y'))

# replace

stri = 'welcom to python'
print(stri.upper().replace('O','*'))
print(stri.replace('o','*',2))
print(stri.replace('python','univers',1))

#startswith()

stri2= 'welcome to python world'
print(stri2.startswith('welcome'))
print(stri2.startswith('e',1))
print(stri2.startswith('p',6))
print(stri2.replace('w','W').startswith('W'))

#endswith()

stri3 = 'welcome to the world of magics'
print(stri3.endswith('magics'))
print(stri3.endswith('s',-1))
print(stri3.replace('s','S',-1).endswith('S'))

#split()

msag = 'welcome to the world of logics and creativity'
print(msag.split())
print(msag.split(' '))
print(msag.split('l'))

# strip()

msag2 = '   welcome to   '
print(msag2.strip().replace(' ',''))
print(msag2.strip().replace(' ','*').upper())
print(msag2.replace(' ','*'))

#rstrip()

msag3 = '  hi hello how are you    '
print(msag3.rstrip().replace(' ','*'))
print(msag3.rstrip())

# lstrip()

msag4 = '     welcome to python    '
print(msag4.lstrip().replace(' ','*'))

# join()

words = 'hello world i am python programmer'
result = '.'.join(words)
print(result.upper().replace('.','*',3))

words = ['hi','ji','how',]
result2= '*'.join(words)
print(result2)

#isalpha()

alpha = ('hii3')
print(alpha.isalpha())

alpha2 = ['lsjf']
print(alpha2[0].upper().isalpha())

alpha3 = 'hi allow'
print(alpha3.isalpha())
print(alpha3.replace(' ','A').isalpha())

#isalnum()

alnum = 'hi3432 '
print(alnum.isalnum())

alnum = 'hi8e34'
print(alnum.isalnum())

#islower()

lower = 'asigd'
print(lower.upper().islower())
print(lower.islower())

#isupper()

upper = 'slfjd hi'
print(upper.upper().isupper())
print(upper.isupper())

#isdigit()

dig = '23432 3'
print(dig.isdigit())

dig = '23948'
print(dig.isdigit())

#isidentifier()

print('ksdfj23_j'.isidentifier())
print('kdj1 jl'.upper().isidentifier())

# zfill()

print('4545'.zfill(5))
print(' kdd'.zfill(7).islower())

# print extention of the file

file = 'youtube.com'
result = file.split('.')
print(result[-1])

# print file name 

file = 'image.jpg'
result= file.split('.')
print(result[0])

