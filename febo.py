

ntimes = int(input("enter the number"))

n1 = 0

n2 = 1

count = 0

if ntimes <= 0:

    print("enter positive number")

elif ntimes == 1:

    print(n1)
else:

    while count < ntimes:

        print(n1)

        n3 = n1 + n2

        n1 = n2

        n2 = n3

        count += 1


