import re
regex = re.compile('[^a-zA-Z]')


input_string = input("Please enter a string: ")

def clear_string(n):
    n = regex.sub('', n)
    n = n.lower()
    return n
    # print(n)
    
def check_palindrome(n):
    if n == n[::-1]:
        # print(n)
        return True
    else:
        # print(n)
        return False
    

def declare_palindrome(n):

    if n == True:
        print("This string is a Palindrome")
    else:
        print("This string is not a Palindrome")

modified_string = clear_string(input_string)
palindrome = check_palindrome(modified_string)
declare_palindrome(palindrome)

#clear_string() untuk membersihkan string dari karakter non alfabet, check_palindrome() untuk cek apakah string akan sama apabila dibalik urutannya, declare_palindrome() untuk print hasil cek dari fungsi sebelumnya

