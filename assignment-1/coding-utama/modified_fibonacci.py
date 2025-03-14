fibonacci_seq = []

user_input = input("Input a number for the Fibonacci Sequence:")
user_input = int(user_input)

def fibonacci(i):
    if i == 0:
        return 0
    elif i == 1:
        return 1
    elif i > 1:
        if i % 2 == 0:
            return fibonacci(i - 2) + fibonacci(i - 1)
        else: 
            return fibonacci(i - 1) - fibonacci(i - 2)
    
for x in range (user_input + 1):
    fibonacci_seq.append(fibonacci(x))

print(fibonacci_seq)
print(fibonacci_seq[user_input])
