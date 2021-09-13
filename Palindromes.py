# Andrew Perez-Napan
# ap16at
# Due Date: 1-20-21
# The program in this file is the individual work of Andrew Perez-Napan

def is_palindrome(p):
    return p == p[::-1]


if __name__ == "__main__":

    counter = 0

    arr_temp = []
    arr_holder = []
    d1 = dict()

    print("Enter the strings:")

    while True:

        str_input = input("")

        if str_input == "Done":
            break
        else:
            counter += 1

        arr_holder.append(str_input)
        str_temp = str_input.replace(" ", "")
        arr_temp.append(str_temp.lower())

    counter2 = 0
    c = 0

    while counter != 0:

        s = arr_temp[counter2]
        s2 = arr_holder[counter2]

        if is_palindrome(s):
            key = c + 1
            d1[key] = s2
            counter2 += 1
            c += 1
        else:
            counter2 += 1

        counter -= 1

    print("The palindromes are:")
    print(d1)
