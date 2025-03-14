def manipulate_string(s):
    result = ""
    counter = 1

    for i in range (1, len(s)):
        if s[i] == s[i - 1]:
            counter += 1
        else:
            result += s[i - 1] + str(counter)
            counter = 1
    result += s[-1] + str(counter)
    return result

input_string = input("Enter a string:")

print(manipulate_string(input_string))
