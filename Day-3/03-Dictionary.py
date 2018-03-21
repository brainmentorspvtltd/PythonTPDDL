Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> emp = {'name':'Ram', 'age':27,'company':'TCS'}
>>> emp[0]
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    emp[0]
KeyError: 0
>>> emp['name']
'Ram'
>>> emp['age']
27
>>> emp.keys()
dict_keys(['name', 'age', 'company'])
>>> emp.values()
dict_values(['Ram', 27, 'TCS'])
>>> emp.items()
dict_items([('name', 'Ram'), ('age', 27), ('company', 'TCS')])
>>> for data in emp:
	print(emp)

	
{'name': 'Ram', 'age': 27, 'company': 'TCS'}
{'name': 'Ram', 'age': 27, 'company': 'TCS'}
{'name': 'Ram', 'age': 27, 'company': 'TCS'}
>>> for data in emp:
	print(data)

	
name
age
company
>>> for data in emp.values():
	print(data)

	
Ram
27
TCS
>>> 
>>> for data in emp.items():
	print(data)

	
('name', 'Ram')
('age', 27)
('company', 'TCS')
>>> emp['salary'] = 45000
>>> emp
{'name': 'Ram', 'age': 27, 'company': 'TCS', 'salary': 45000}
>>> del emp['salary']
>>> emp
{'name': 'Ram', 'age': 27, 'company': 'TCS'}
>>> emp = {'name':['Ram','Shyam','Anuj'], 'age':[27,28,32],'company':['TCS','Wipro','HCL']}
>>> emp
{'name': ['Ram', 'Shyam', 'Anuj'], 'age': [27, 28, 32], 'company': ['TCS', 'Wipro', 'HCL']}
>>> [{'name':'Ram','age':''}]
[{'name': 'Ram', 'age': ''}]
>>> emp = [{'name':'Ram','age':27},{'name':'Shyam','age':28},{'name':'Gopal', 'age':30}]
>>> emp
[{'name': 'Ram', 'age': 27}, {'name': 'Shyam', 'age': 28}, {'name': 'Gopal', 'age': 30}]
>>> emp[0]
{'name': 'Ram', 'age': 27}
>>> emp[1]
{'name': 'Shyam', 'age': 28}
>>> emp[0]['name']
'Ram'
>>> emp[0].get('name')
'Ram'
>>> 
