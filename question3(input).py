'''3. Write a multiplication game program for kids. The program should give the player
ten randomly generated multiplication questions to do. After each, the program
should tell them whether they got it right or wrong and what the correct answer is.
Question 1: 3 x 4 = 12
Right!
Question 2: 8 x 6 = 44
Wrong. The answer is 48.
...
...
Question 10: 7 x 7 = 49
Right.'''
import random

n = 0
while n < 11:
    a = random.randint(1,9)
    b = random.randint(1,9)
    guess = int(input("Question:" + str(a)+"x"+ str(b)+"="))
    answer = a*b
    n +=1
    if guess == answer:
        print("Right!")
    else:
        print("Wrong, the answer is ",answer)
    
