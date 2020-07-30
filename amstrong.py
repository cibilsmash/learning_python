

num = int(input("enter number : "))

sum = 0

temp = num

while temp > 0:

    digit = temp % 10

    sum += digit ** 3

    temp //= 10


if sum == num:
    print("yes it is ")

else:
    print("no it is not")



