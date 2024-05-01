import random 
import words
choosen_word=random.choice(words.word)
display=[]
for i in range(len(choosen_word)):
    display=display+'_'
print(display)

