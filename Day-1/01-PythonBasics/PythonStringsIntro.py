Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
 RESTART: C:/Users/asus/Desktop/PythonTataPower/01-PythonBasics/PythonFirstProgram.py 
Sum is 22
Sum of 10 and 12 is 22
>>> 
 RESTART: C:/Users/asus/Desktop/PythonTataPower/01-PythonBasics/PythonFirstProgram.py 
Sum is 22
Sum of 10 and 12 is 22
Sum of 10 and 12 is 22
>>> 
 RESTART: C:/Users/asus/Desktop/PythonTataPower/01-PythonBasics/PythonFirstProgram.py 
Sum is 22
Sum of 10 and 12 is 22
Sum of 10 and 12 is 22
Sum of 10 and 12 is 22
>>> a = "HELLO"
>>> a.lower()
'hello'
>>> 
 RESTART: C:/Users/asus/Desktop/PythonTataPower/01-PythonBasics/PythonInput.py 
Enter first number : 12
Enter second number : 11
Sum is 1211
>>> 
 RESTART: C:/Users/asus/Desktop/PythonTataPower/01-PythonBasics/PythonInput.py 
Enter first number : 12
Enter second number : 11
Sum is 23
>>> str_1 = "Hello this is python programming"
>>> str_1[0]
'H'
>>> str_1[1]
'e'
>>> str_1[0:5]
'Hello'
>>> str_1[0:4]
'Hell'
>>> str_1[0:10:2]
'Hloti'
>>> str_1[0:]
'Hello this is python programming'
>>> str_1[:100]
'Hello this is python programming'
>>> str_1[:]
'Hello this is python programming'
>>> str_2 = "Hello"
>>> str_2[::-1]
'olleH'
>>> str_2[-1]
'o'
>>> str_2[-2]
'l'
>>> str_2[0:-1]
'Hell'
>>> str_1[-1:-4]
''
>>> str_2[::-2]
'olH'
>>> str_1
'Hello this is python programming'
>>> str_1[0:5] = 'Bye'
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    str_1[0:5] = 'Bye'
TypeError: 'str' object does not support item assignment
>>> str_1.replace('Hello','Bye')
'Bye this is python programming'
>>> str_1
'Hello this is python programming'
>>> str_1.find('p')
14
>>> str_1.rfind('p')
21
>>> str_1.find('i')
8
>>> str_1.find('i',9)
11
>>> str_1.find('z')
-1
>>> str_2.lower()
'hello'
>>> str_2.upper()
'HELLO'
>>> str_2.capitalize()
'Hello'
>>> 
