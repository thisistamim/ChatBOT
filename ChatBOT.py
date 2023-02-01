"""***********************************************************************************
                              Run this code on Python IDLE
***********************************************************************************"""
#simple chat BOT v1.0.0

import random

#list for greetings
A = [
  "hi",
  "hey",
  "hello"
]

#list for questions
B = [
  "how are you?",
  "what's up?",
  "are you okay?",
  "are you fine?"
]

C = [
  "what is your name?",
  "who are you?",
  "your identity?"
]

#list for answers
D = [
  "I'm good 😊",
  "I'm fine 🙂",
  "I'm ill 🤒",
  "I'm happy 😌",
  "I'm great 😎"
]

E = [
  "My name is Bee.",
  "I'm Bee,",
  "My name is Bee. I'm your virtual assistant."
]

#random generator
X1 = A[random.randint(0, 2)]
X2 = B[random.randint(0, 3)]
X3 = D[random.randint(0, 4)]
X4 = E[random.randint(0, 2)]

def list_Ai():
	print ('BOT : '+X1+'!',X2)
def list_Bi():
	print ('BOT : '+X3,'BTW how about you?')
def list_Ci():
	print ('BOT : '+X4,'Nice to meet you.')
def list_Q(ext):
    print ('BOT : Why are you saying '+'\''+ext+'\''+'?')

while not False:
	try:
		text = input('\nUser : ').lower()
	except EOFError:
		break
	print()
	if not text:
		print ("BOT : Please ask me something. I'll answer your questions if possible ツ")
		continue
	else:
		if A[0] in text or A[1] in text or A[2] in text:
			list_Ai()
		elif B[0] in text or B[1] in text or B[2] in text or B[3] in text:
			list_Bi()
		elif C[0] in text or C[1] in text or C[2] in text:
			list_Ci()
		elif text.endswith("?"):
			print ("BOT : You are very chatty and inquisitive about everything ツ")
		else:
			list_Q(text)