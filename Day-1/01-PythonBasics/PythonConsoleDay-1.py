Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> print("Hello world")
Hello world
>>> a = 10
>>> b = 12
>>> c = a + b
>>> print(c)
22
>>> a = "Hello"
>>> type(a)
<class 'str'>
>>> type(b)
<class 'int'>
>>> id(a)
2573212903608
>>> id(b)
1759627280
>>> d = b
>>> d
12
>>> b
12
>>> id(d)
1759627280
>>> id(b)
1759627280
>>> b = None
>>> 
 RESTART: C:/Users/asus/Desktop/PythonTataPower/01-PythonBasics/PythonFirstProgram.py 
Sum is 22
>>> a = "Hello"
>>> a*10
'HelloHelloHelloHelloHelloHelloHelloHelloHelloHello'
>>> a = 10
>>> a**2
100
>>> a**3
1000
>>> a**4
10000
>>> a = 15
>>> b = 4
>>> a/b
3.75
>>> a//b
3
>>> a,b = 10,12
>>> a,b = b,a
>>> a
12
>>> b
10
>>> 
