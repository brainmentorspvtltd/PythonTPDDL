Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a = (12,34,45,47)
>>> a[0]
12
>>> a[]-1
SyntaxError: invalid syntax
>>> a[-1]
47
>>> a[0:3]
(12, 34, 45)
>>> emp = 'Ram', 27, 'TCS'
>>> emp
('Ram', 27, 'TCS')
>>> emp = name,age,company = 'Ram', 27, 'TCS'
>>> emp
('Ram', 27, 'TCS')
>>> name
'Ram'
>>> age
27
>>> company
'TCS'
>>> emp = name,age,company = ['Ram','Shyam'], [27,28], ['TCS','Wipro']
>>> emp
(['Ram', 'Shyam'], [27, 28], ['TCS', 'Wipro'])
>>> name
['Ram', 'Shyam']
>>> age
[27, 28]
>>> company
['TCS', 'Wipro']
>>> name[0]
'Ram'
>>> emp
(['Ram', 'Shyam'], [27, 28], ['TCS', 'Wipro'])
>>> print(emp[0][0], emp[1][0], emp[2][0])
Ram 27 TCS
>>> print(emp[0][1], emp[1][1], emp[2][1])
Shyam 28 Wipro
>>> for i in range(5):
	print(i)

	
0
1
2
3
4
>>> 
>>> for i in range(5):
	print(i, end=" ")

	
0 1 2 3 4 
>>> for i in range(len(emp)):
	for j in range(len(emp)-1):
		print(emp[j][i], end = ' ')
	print()

	
Ram 27 
Shyam 28 
Traceback (most recent call last):
  File "<pyshell#31>", line 3, in <module>
    print(emp[j][i], end = ' ')
IndexError: list index out of range
>>> for i in range(len(emp)-1):
	for j in range(len(emp)):
		print(emp[j][i], end = ' ')
	print()

	
Ram 27 TCS 
Shyam 28 Wipro 
>>> for i in range(len(emp)-1):
	for j in range(len(emp)):
		print(emp[j][i], end = ',')
	print()

	
Ram,27,TCS,
Shyam,28,Wipro,
>>> 
