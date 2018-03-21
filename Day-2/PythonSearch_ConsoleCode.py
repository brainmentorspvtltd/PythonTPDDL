Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> hello_intent = ['hello','hi','hey','good morning','hie']
>>> word = "hello"
>>> for w in hello_intent:
	if w == word:
		print("Match Found")
		print(w)

		
Match Found
hello
>>> for w in hello_intent:
	if w == word:
		print("Match Found")
		print(w)
	else:
		print("Not found")

		
Match Found
hello
Not found
Not found
Not found
Not found
>>> for w in hello_intent:
	if w == word:
		print("Match Found")
		print(w)
		break
	else:
		print("Not found")

		
Match Found
hello
>>> word in hello_intent
True
>>> word not in hello_intent
False
>>> 
