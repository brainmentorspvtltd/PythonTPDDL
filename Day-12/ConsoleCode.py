Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> class Person():
	p_id = None
	name = None
	age = None

	
>>> Person
<class '__main__.Person'>
>>> __name__ == '__main__'
True
>>> Person.name
>>> Person.name = "Ram"
>>> Person.id = 101
>>> Person.age = 28
>>> Person()
<__main__.Person object at 0x000001CDF057B630>
>>> x = 'ram'
>>> x == 'ram'
True
>>> Person.p_id = 1
>>> Person.name
'Ram'
>>> Person.age
28
>>> Person.id
101
>>> Person.p_id
1
>>> class Person():
	_p_id = None
	_name = None
	_age = None

	
>>> Person._name
>>> Person._name = 'Ram'
>>> Person.name
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    Person.name
AttributeError: type object 'Person' has no attribute 'name'
>>> Person._name = 'Ram'
>>> class Person():
	__p_id = None
	__name = None
	__age = None

	
>>> Person.name
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    Person.name
AttributeError: type object 'Person' has no attribute 'name'
>>> Person._name
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    Person._name
AttributeError: type object 'Person' has no attribute '_name'
>>> Person.__name
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    Person.__name
AttributeError: type object 'Person' has no attribute '__name'
>>> a = 10
>>> type(a)
<class 'int'>
>>> type(int)
<class 'type'>
>>> type(Person)
<class 'type'>
>>> type(type)
<class 'type'>
>>> isinstance(a,int)
True
>>> isinstance(int, type)
True
>>> isinstance(a,type)
False
>>> a = "hello"
>>> isinstance(a,int)
False
>>> isinstance(a,str)
True
>>> 
