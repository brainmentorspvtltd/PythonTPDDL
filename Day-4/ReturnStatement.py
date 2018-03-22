Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def add():
	x = 10
	y = 12
	print(x+y)

	
>>> add()
22
>>> a = add()
22
>>> a
>>> print(a)
None
>>> print(add())
22
None
>>> def calc(x,y):
	return x + y, x - y, x * y, x / y

>>> c = calc(12,4)
>>> c
(16, 8, 48, 3.0)
>>> a,b,c,d = calc(12,4)
>>> a
16
>>> b
8
>>> c
48
>>> d
3.0
>>> a,b,*c = calc(12,4)
>>> a
16
>>> b
8
>>> c
[48, 3.0]
>>> *a,b,c = calc(12,4)
>>> a
[16, 8]
>>> b
48
>>> c
3.0
>>> *a,b = calc(12,4)
>>> a
[16, 8, 48]
>>> b
3.0
>>> 
