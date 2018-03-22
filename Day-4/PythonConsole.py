Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> abs(-5)
5
>>> a = [2,3,4,5,'']
>>> all(a)
False
>>> a = [2,3,4,5]
>>> all(a)
True
>>> chr(65)
'A'
>>> chr(97)
'a'
>>> chr(32)
' '
>>> ord('a')
97
>>> 
= RESTART: C:/Users/asus/Desktop/PythonTataPower/Day-4/02-FunctionsIntro.py =
Sum is 22
>>> 
 RESTART: C:/Users/asus/Desktop/PythonTataPower/Day-4/03-FunctionsArguments.py 
Sum is 14
Diff is 8
>>> 
 RESTART: C:/Users/asus/Desktop/PythonTataPower/Day-4/03-FunctionsArguments.py 
Sum is 12
Diff is 8
>>> a
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    a
NameError: name 'a' is not defined
>>> x = 10
>>> y = 12
>>> x - y if x > y and x > 5 else y - x
2
>>> 
=== RESTART: C:/Users/asus/Desktop/PythonTataPower/Day-4/04-DynamicArgs.py ===
Traceback (most recent call last):
  File "C:/Users/asus/Desktop/PythonTataPower/Day-4/04-DynamicArgs.py", line 7, in <module>
    emp(101,'Ram',28,'NSP','Rohini')
TypeError: emp() takes 4 positional arguments but 5 were given
>>> 
=== RESTART: C:/Users/asus/Desktop/PythonTataPower/Day-4/04-DynamicArgs.py ===
ID : 101
Name : Ram
Age : 28
Address : ('NSP', 'Rohini', 'Rithala')
>>> 
=== RESTART: C:/Users/asus/Desktop/PythonTataPower/Day-4/04-DynamicArgs.py ===
Traceback (most recent call last):
  File "C:/Users/asus/Desktop/PythonTataPower/Day-4/04-DynamicArgs.py", line 13, in <module>
    emp(101,'Ram','NSP','Rohini','Rithala',28)
TypeError: emp() missing 1 required keyword-only argument: 'age'
>>> 
=== RESTART: C:/Users/asus/Desktop/PythonTataPower/Day-4/04-DynamicArgs.py ===
>>> 
=== RESTART: C:/Users/asus/Desktop/PythonTataPower/Day-4/04-DynamicArgs.py ===
ID : 101
Name : Ram
Age : 28
Address : ('NSP', 'Rohini', 'Rithala')
>>> 
=== RESTART: C:/Users/asus/Desktop/PythonTataPower/Day-4/04-DynamicArgs.py ===
ID : 101
Name : Ram
Age : 28
Address 0 : NSP
Address 1 : Rohini
Address 2 : Rithala
>>> 
=== RESTART: C:/Users/asus/Desktop/PythonTataPower/Day-4/04-DynamicArgs.py ===
ID : 101
Name : Ram
Age : 28
Address 1 : NSP
Address 2 : Rohini
Address 3 : Rithala
>>> x = ['hi','hello','hey','world']
>>> for i in x:
	print(i)

	
hi
hello
hey
world
>>> for i in enumerate(x):
	print(i)

	
(0, 'hi')
(1, 'hello')
(2, 'hey')
(3, 'world')
>>> for i,j in enumerate(x):
	print(i,j)

	
0 hi
1 hello
2 hey
3 world
>>> emp_name = ['Ram','Shyam','Gopal','Mohan']
>>> emp_id = [101,102,103,104]
>>> zip(emp_id,emp_name)
<zip object at 0x0000021CACB18908>
>>> list(zip(emp_id,emp_name))
[(101, 'Ram'), (102, 'Shyam'), (103, 'Gopal'), (104, 'Mohan')]
>>> for id,name in zip(emp_id, emp_name):
	print(id,name)

	
101 Ram
102 Shyam
103 Gopal
104 Mohan
>>> emp_id = [101,102,103,104,105]
>>> for id,name in zip(emp_id, emp_name):
	print(id,name)

	
101 Ram
102 Shyam
103 Gopal
104 Mohan
>>> emp_name = ['Ram','Shyam','Gopal','Mohan','Anuj']
>>> for id,name in zip(emp_id, emp_name):
	print(id,name)

	
101 Ram
102 Shyam
103 Gopal
104 Mohan
105 Anuj
>>> emp_id = [101,102,103,104,105,106]
>>> list(zip(emp_id,emp_name))
[(101, 'Ram'), (102, 'Shyam'), (103, 'Gopal'), (104, 'Mohan'), (105, 'Anuj')]
>>> 
=== RESTART: C:/Users/asus/Desktop/PythonTataPower/Day-4/04-DynamicArgs.py ===
{'name': 'Ram', 'age': 14, 'grade': 'A'}
{'name': 'Shyam', 'age': 13, 'hobby': 'Cricket,Football'}
>>> 
=== RESTART: C:/Users/asus/Desktop/PythonTataPower/Day-4/04-DynamicArgs.py ===
{'name': 'Ram', 'age': 14, 'grade': 'A'}
{'name': 'Shyam', 'age': 13, 'hobby': 'Cricket,Football'}
>>> s = 'Don\'t Use headphones'
>>> s
"Don't Use headphones"
>>> s = "Don't Use headphones"
>>> s
"Don't Use headphones"
>>> import os
>>> os.getcwd()
'C:\\Users\\asus\\Desktop\\PythonTataPower\\Day-4'
>>> os.chdir('C:\Python36\abc\new')
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    os.chdir('C:\Python36\abc\new')
OSError: [WinError 123] The filename, directory name, or volume label syntax is incorrect: 'C:\\Python36\x07bc\new'
>>> os.chdir(r'C:\Python36\abc\new')
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    os.chdir(r'C:\Python36\abc\new')
FileNotFoundError: [WinError 3] The system cannot find the path specified: 'C:\\Python36\\abc\\new'
>>> os.chdir(r'C:\Python36\')
	 
SyntaxError: EOL while scanning string literal
>>> os.chdir(r'C:\Python36')
>>> s = "Hello\nWorld"
>>> print(s)
Hello
World
>>> s = r"Hello\nWorld"
>>> print(s)
Hello\nWorld
>>> 
