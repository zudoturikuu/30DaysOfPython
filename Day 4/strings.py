greeting = 'I hope you are having a great day'
print(greeting)
print(len(greeting))

longest_word = 'pneumonoultramicroscopicsilicovolcanoconiosis'
print(len(longest_word))

multiline_string = '''I like cats. Cats are cute
Cats are not dogs. Dogs are cute too
Everyone is cute. Everyone should stop fighting each other and being divided
We should all want peace. The world is a mess. Dogs are cute'''
print(multiline_string)

first_name = 'John'
last_name = 'Doe'
space = ' '

full_name = first_name + space + last_name
print(full_name)

print(len(full_name) >= len(first_name))

print('I know who you are. \nI know what you look like')
print('I am coming \tfor you')
print('And I am going to say \"Hello World\"')

formatted_string = 'I am %s %s and I lov u.' %(first_name, last_name)
print(formatted_string)

radius = 11.2345
pi = 3.14
area = pi * radius ** 2
format_string = 'The area of a circle with radius %d is %.2f' %(radius, area)

print(format_string)

format_string_new = 'I am {} {} and i am an AI.'.format(first_name, last_name)
print(format_string_new)

a = 3
b = 4

print('{} + {} = {}'.format(a,b,a+b))
print('{} ** {} = {}'.format(a,b,a**b))

print('The area of a circle with radius {} is {:.2f}.'.format(radius,area))

print(f'{a} + {b} = {a+b}')
print(f'{a} ** {b} = {a**b}')

language = "Python"
a,b,c,d,e,f = language
print(a)
first_letter = language[0]
print(first_letter)
last_index = len(language) -1
print(last_index)
last_letter = language[last_index]
print(last_letter)
lastLetter = language[-1]
print(lastLetter)

first_three = language[0:3]
print(first_three)
last_three = language[3:6]
lastThree = language[-3:]
last_Three = language[3:]
print(last_three)
print(lastThree)
print(last_Three)

greeting = 'Hello World'
greeting2 = 'Hello\tWorld'
print(greeting[::-1])
print(greeting[0:6:2])
print(greeting.capitalize())
print(greeting.count('H'))
print(greeting.endswith('Z'))
print(greeting2.expandtabs(200))
print(greeting2.find('W'))
print(greeting.rfind('He'))
print("".join(greeting))
print(greeting.strip('H'))

area_of_circle = 100

sentence = 'The area of circle is {}'.format(str(area_of_circle))
print(sentence)
substring = "Wo"
print(greeting.index(substring))
print(greeting.rindex(substring))
print(greeting.isalnum())
print(greeting.isalpha())
print(greeting.isidentifier())
print(greeting.isupper())
print(greeting.islower())
print(greeting.replace('World', "Friend"))
print(greeting.title())
print(greeting.swapcase())
print(greeting.startswith("hello"))


num = '123'
print(num.isdecimal())
print(num.isdigit())
print(num.isnumeric())

string = ['Thirty', 'Days', 'of']
join = ''.join(string)
print(join)














