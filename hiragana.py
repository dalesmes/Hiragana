import random

def Fun_hiraganas():
	hiraganas = ['a', 'i', 'u', 'e', 'o', 'ka', 'ki', 'ku', 'ke', 'ko', 'sa', 'shi', 'su', 'se', 
	'so', 'ta', 'chi', 'tsu', 'te', 'to', 'na', 'ni', 'nu', 'ne', 'no', 'ha', 'hi', 'fu', 'he', 'ho']
	print("escriba el hiragana", hiraganas[random.randint(0, len(hiraganas)-1)])

print("Hello, type exit if you want to leave")
answer = ""
while answer.lower() != 'exit':
	Fun_hiraganas() 
	answer = input("Type exit if you want to leave")
print("bye")
