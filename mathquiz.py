import random 
import time
operations = ["+", "*", "/", "-"]
min_num = 0
max_num = 99
num_problems = 10

def generate_problem():
    A = random.randint(min_num, max_num)
    B = random.randint(min_num, max_num)
    operation = random.choice(operations)

    expression = str(A) + " " + operation + " " + str(B)
    answer = eval(expression)
    return expression, answer

def take_quiz():
    start = input("Press Enetr to Start")
    start_time = time.time()
    for i in range(num_problems):
        expression, correct_answer = generate_problem()
        wrong = 0
        while True:
            guess = input("Problem " + str(i + 1) + ": " + expression + " = ")
            if guess == str(correct_answer):
                print("Correct")
                break
            wrong += 1
    end_time = time.time()
    total = end_time - start_time
    
    print("Nice Work you finished in "+total+" !")
            

take_quiz()

