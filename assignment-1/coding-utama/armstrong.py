def check_armstrong(n):

    str_number = str(n)
    digits = len(str_number)
    total = sum(int(digit) ** digits for digit in str_number)
    return total == n

def armstrong_count(x):

    for i in range(x + 1):
        if check_armstrong(i):
            print(i)


input_number = int(input("Enter a number: "))


armstrong_count(input_number)

# check_armstrong() untuk cek apabila armstrong atau bukan, armstrong_count() untuk run function sebelumnya pada setiap angka dari 0 - angka batas yg dipilih