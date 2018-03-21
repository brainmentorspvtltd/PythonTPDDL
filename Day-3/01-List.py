Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a = [12,34,56,'Hi','hello',10.5,True]
>>> a[0]
12
>>> a[2]
56
>>> a[4]
'hello'
>>> a[0:4]
[12, 34, 56, 'Hi']
>>> a = [[1,2,3],[4,5,6],[7,8,9]]
>>> a
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
>>> a[0]
[1, 2, 3]
>>> a[0][0]
1
>>> a[0][1]
2
>>> emp = []
>>> emp.append('Ram')
>>> emp
['Ram']
>>> emp.append('Shyam')
>>> emp
['Ram', 'Shyam']
>>> emp[0]
'Ram'
>>> emp.append('Anuj')
>>> emp
['Ram', 'Shyam', 'Anuj']
>>> emp.append('Pune','Delhi','Agra')
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    emp.append('Pune','Delhi','Agra')
TypeError: append() takes exactly one argument (3 given)
>>> emp.append(['Pune','Delhi','Agra'])
>>> emp
['Ram', 'Shyam', 'Anuj', ['Pune', 'Delhi', 'Agra']]
>>> emp[-1]
['Pune', 'Delhi', 'Agra']
>>> compnay_name = ['TCS','Wipro','HCL']
>>> emp.extend(compnay_name)
>>> emp
['Ram', 'Shyam', 'Anuj', ['Pune', 'Delhi', 'Agra'], 'TCS', 'Wipro', 'HCL']
>>> emp.pop()
'HCL'
>>> emp
['Ram', 'Shyam', 'Anuj', ['Pune', 'Delhi', 'Agra'], 'TCS', 'Wipro']
>>> emp.pop()
'Wipro'
>>> emp
['Ram', 'Shyam', 'Anuj', ['Pune', 'Delhi', 'Agra'], 'TCS']
>>> emp.pop(1)
'Shyam'
>>> emp
['Ram', 'Anuj', ['Pune', 'Delhi', 'Agra'], 'TCS']
>>> emp.insert(1,'John')
>>> emp
['Ram', 'John', 'Anuj', ['Pune', 'Delhi', 'Agra'], 'TCS']
>>> emp.remove('TCS')
>>> emp
['Ram', 'John', 'Anuj', ['Pune', 'Delhi', 'Agra']]
>>> emp.index('Anuj')
2
>>> len(emp)
4
>>> emp[-1].remove('Agra')
>>> emp
['Ram', 'John', 'Anuj', ['Pune', 'Delhi']]
>>> emp[-1].append('Agra')
>>> emp
['Ram', 'John', 'Anuj', ['Pune', 'Delhi', 'Agra']]
>>> emp[-1].insert(1,'Mumbai')
>>> emp
['Ram', 'John', 'Anuj', ['Pune', 'Mumbai', 'Delhi', 'Agra']]
>>> emp[0] = 'Shyam'
>>> emp
['Shyam', 'John', 'Anuj', ['Pune', 'Mumbai', 'Delhi', 'Agra']]
>>> emp.insert(12,'xyz')
>>> emp
['Shyam', 'John', 'Anuj', ['Pune', 'Mumbai', 'Delhi', 'Agra'], 'xyz']
>>> emp.remove('xyz')
>>> emp
['Shyam', 'John', 'Anuj', ['Pune', 'Mumbai', 'Delhi', 'Agra']]
>>> x = [12,23,55,1,2,5,78,56,45]
>>> sorted(x)
[1, 2, 5, 12, 23, 45, 55, 56, 78]
>>> x
[12, 23, 55, 1, 2, 5, 78, 56, 45]
>>> sorted(x, reverse = True)
[78, 56, 55, 45, 23, 12, 5, 2, 1]
>>> x.sort()
>>> x
[1, 2, 5, 12, 23, 45, 55, 56, 78]
>>> for i in x:
	print(i)

	
1
2
5
12
23
45
55
56
78
>>> a = ['hi','hello','python',12,34,55]
>>> b = a
>>> a[0] = 'bye'
>>> a
['bye', 'hello', 'python', 12, 34, 55]
>>> b
['bye', 'hello', 'python', 12, 34, 55]
>>> id(a)
2383878388040
>>> id(b)
2383878388040
>>> c = a[:]
>>> c
['bye', 'hello', 'python', 12, 34, 55]
>>> id(c)
2383877505224
>>> c[0] = 'hi'
>>> a
['bye', 'hello', 'python', 12, 34, 55]
>>> c
['hi', 'hello', 'python', 12, 34, 55]
>>> a = ['hi','hello',['python',12,34],55]
>>> a
['hi', 'hello', ['python', 12, 34], 55]
>>> b
['bye', 'hello', 'python', 12, 34, 55]
>>> d = a[:]
>>> d
['hi', 'hello', ['python', 12, 34], 55]
>>> a
['hi', 'hello', ['python', 12, 34], 55]
>>> a[2][0] = 'bye'
>>> a
['hi', 'hello', ['bye', 12, 34], 55]
>>> d
['hi', 'hello', ['bye', 12, 34], 55]
>>> import deepcopy
Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    import deepcopy
ModuleNotFoundError: No module named 'deepcopy'
>>> import copy
>>> e = copy.deepcopy(a)
>>> e
['hi', 'hello', ['bye', 12, 34], 55]
>>> a[2][0] = 'hi'
>>> a
['hi', 'hello', ['hi', 12, 34], 55]
>>> d
['hi', 'hello', ['hi', 12, 34], 55]
>>> e
['hi', 'hello', ['bye', 12, 34], 55]
>>> 
