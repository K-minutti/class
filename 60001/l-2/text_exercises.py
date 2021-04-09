#Chapter 2.2

#finger exercise
#assuming input numbers are positive odd numbers 
def largest_odd(arr):
    largest = 0
    for num in arr:
        if num % 2 != 0 and largest < num:
            largest = num
    if largest == 0:
        print("You submitted no odd numbers")
    else:
        return largest

#print(largestOdd(19,11,23))



def ask_user_numbers(x):
    print("Hi! Lets find the largest odd number")
    numbersInput = input(f"Insert {x} numbers comma seperated: ")
    nums = numbersInput.split(",")
    numbers = [int(num.strip()) for num in nums]
    return numbers


# numbers = ask_user_numbers(9)
# print(largest_odd(numbers))

#####################
### second exercise
#####################
#TODO: FIX 
# user_int = int(input("Hey gimmie an integer: "))
# ans = 0
# root = 1
# power = 0


# for num in range(1,6):
#     root = 1
#     power = num
#     while root < user_int:
#         ans = root**power
#         if ans == user_int:
#             break
#         root += 1

# if ans == user_int:
#     print("These two ints a root {one} and power {two}".format(one=root, two=power))
# else: 
#     print(f"Sorry there is no root and power than are equal to your input number {user_int}")


#####################
### third exercise
#####################

def sum_of_string(s):
    arr = s.split(",")
    total = 0.0
    for num in arr:
        total += float(num)
    return total

print(sum_of_string("1.23,2.4,3.123"))