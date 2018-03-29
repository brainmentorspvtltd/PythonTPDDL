Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> from datetime import datetim
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    from datetime import datetim
ImportError: cannot import name 'datetim'
>>> from datetime import datetime
>>> today = datetime.now()
>>> print(today)
2018-03-26 10:44:12.415168
>>> today.date()
datetime.date(2018, 3, 26)
>>> today.time()
datetime.time(10, 44, 12, 415168)
>>> time = today.time()
>>> print(time)
10:44:12.415168
>>> time.strftime("%H : %M : %S")
'10 : 44 : 12'
>>> time.strftime("%H:%M:%S")
'10:44:12'
>>> time.isoformat()
'10:44:12.415168'
>>> time.strftime("%H:%M:%S")
'10:44:12'
>>> 
