Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> list_1 = [23,45,678,2,1,2,5,7,8,3,4,5,2]
>>> set(list_1)
{1, 2, 3, 4, 5, 678, 7, 8, 45, 23}
>>> list_1 = set(list_1)
>>> list_1
{1, 2, 3, 4, 5, 678, 7, 8, 45, 23}
>>> set_1 = {2,4,5,6,8,9,4,2,1}
>>> set_2 = {4,6,7,8,2,11,0,19,81}
>>> set_1.intersection(set_2)
{8, 2, 4, 6}
>>> set_1.union(set_2)
{0, 1, 2, 4, 5, 6, 7, 8, 9, 11, 81, 19}
>>> set_1 & set_2
{8, 2, 4, 6}
>>> set_1 | set_2
{0, 1, 2, 4, 5, 6, 7, 8, 9, 11, 81, 19}
>>> 
