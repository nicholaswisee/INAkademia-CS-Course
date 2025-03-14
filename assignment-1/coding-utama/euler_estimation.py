import random

def random_calc():
    i = 0
    times_calculated = 0
    while i < 1:
        i += random.random()
        times_calculated += 1
    return times_calculated  
    
def euler_estimation(n):
    total = 0
    for x in range(n):
        total += random_calc()
    return total / n    

print(euler_estimation(1000000))
# print(random_calc())

# 1. Estimasi nilai e yang aku peroleh adalah 2.71...
# 2. nilai n yang saya pilih adalah 1000000 atau sejuta, karena semakin banyak percobaan, semakin akurat estimasi yang dihasilkan dari percobaan
