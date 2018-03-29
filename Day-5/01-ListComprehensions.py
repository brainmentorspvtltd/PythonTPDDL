Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a = []
>>> for i in range(1,1001):
	a.append(i)

	
>>> len(a)
1000
>>> a = []
>>> for i in range(1,1001):
	if i % 2 == 0:
		a.append(i)

		
>>> len(a)
500
>>> a[0:10]
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
>>> a = [i for i in range(1,1001)]
>>> len(a)
1000
>>> a = [i for i in range(1,1001) if i % 2 == 0]
>>> a[0:10]
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
>>> d = {x : [x**2 for x in range(1,20)]}
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    d = {x : [x**2 for x in range(1,20)]}
NameError: name 'x' is not defined
>>> d = {'s' : [x**2 for x in range(1,20)]}
>>> d
{'s': [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361]}
>>> 
