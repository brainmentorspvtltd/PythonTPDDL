Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> str_1 = '
SyntaxError: EOL while scanning string literal
>>> str_1 = 'this is python programming and python is used in machine learning'
>>> str_2 = 'machine learning is used a lot now a days and so python is'
>>> str_1 = str_1.split()
>>> str_1
['this', 'is', 'python', 'programming', 'and', 'python', 'is', 'used', 'in', 'machine', 'learning']
>>> str_2 = str_2.split()
>>> str_2
['machine', 'learning', 'is', 'used', 'a', 'lot', 'now', 'a', 'days', 'and', 'so', 'python', 'is']
>>> stopwords = ['a','am','and','are','the','is','in','so','this','that']
>>> token_1 = []
>>> token_2 = []
>>> for word in str_1:
	if word not in stopwords:
		token_1.append(word)

		
>>> token_1
['python', 'programming', 'python', 'used', 'machine', 'learning']
>>> for word in str_2:
	if word not in stopwords:
		token_2.append(word)

		
>>> token_2
['machine', 'learning', 'used', 'lot', 'now', 'days', 'python']
>>> set_1 = set(token_1)
>>> set_2 = set(token_2)
>>> set_1
{'learning', 'programming', 'used', 'machine', 'python'}
>>> set_2
{'learning', 'now', 'used', 'machine', 'days', 'python', 'lot'}
>>> x = len(set_1.intersection(set_2))
>>> x
4
>>> y = len(set_1.union(set_2))
>>> y
8
>>> x/y
0.5
>>> 
