import random

operations = ["+", "-", "x", "/"]

def question_generator():
    global solution
    question = None
    
    num1 = random.randint(1,9)
    num2 = random.randint(1,9)
    operator = random.choice(operations)
    
    if operator == "+":
        solution = num1 + num2
        question = f"{num1} + {num2} =?"
    elif operator == "-":
        solution = num1 - num2
        question = f"{num1} - {num2} =?"
    elif operator == "x":
        solution = num1 * num2
        question = f"{num1} x {num2} =?"
    elif operator == "/":
        solution = round(num1 / num2, 2)
        question = f"{num1} / {num2} =?"
    
    return question

def checker():
    answer = float(input("Enter your answer:"))
    if answer == solution:
        return True
    else:
        return False

count = 0
while count < 5:
    print(question_generator())
    if checker() == True:
        count += 1
        print(f"Total correct answers: {count}")
    else:
        count = 0
        print("Start again!")